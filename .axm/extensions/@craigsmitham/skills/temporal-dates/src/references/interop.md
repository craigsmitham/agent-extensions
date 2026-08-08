# Temporal at the boundaries

Temporal is not yet what drivers, ORMs, and third-party SDKs speak. The working pattern is a **thin shell**: convert on the way in, convert on the way out, keep `Temporal` everywhere in between. Don't scatter conversions through business logic.

## Date ↔ Temporal

```js
const instant = legacyDate.toTemporalInstant();          // Date → Instant
const zdt = instant.toZonedDateTimeISO('America/Chicago');
const legacyDate = new Date(instant.epochMilliseconds);  // Temporal → Date
```

**Polyfill caveat:** `Date.prototype.toTemporalInstant` only exists if the polyfill patches globals. With the modular import you get it as a standalone function:

```js
import { Temporal, toTemporalInstant } from 'temporal-polyfill';
const instant = toTemporalInstant.call(legacyDate);
```

Or import the global build (`temporal-polyfill/global`) once at your entry point and use the method form everywhere. Pick one and be consistent — mixed styles across a codebase are a reliable source of "works in tests, throws in prod".

## JSON

`JSON.stringify` works: every Temporal type has `toJSON()` producing RFC 9557.

`JSON.parse` does **not** work — you get strings back. There is no automatic revival, and there shouldn't be, since a string like `"2026-03-14"` doesn't say which type it wants. Revive explicitly at your schema boundary.

```js
// Zod
const PlainDate = z.string().transform((s, ctx) => {
  try { return Temporal.PlainDate.from(s, { overflow: 'reject' }); }
  catch { ctx.addIssue({ code: 'custom', message: 'Invalid date' }); return z.NEVER; }
});
```

Do the same for `Instant` and `ZonedDateTime`. Once the schema owns parsing, everything downstream is typed and no `from()` calls leak into handlers.

## SQL type mapping

| Column type | Temporal type |
|---|---|
| `date` | `PlainDate` |
| `time` | `PlainTime` |
| `timestamptz` / `TIMESTAMP WITH TIME ZONE` | `Instant` |
| `timestamp` (no zone) | `PlainDateTime` — naive, and usually a schema bug |
| `interval` | `Duration` |
| future scheduled event | `timestamp` + separate `text` IANA zone column, or the full `ZonedDateTime` string |

That last row matters: storing a future appointment as `timestamptz` bakes in today's DST rules. If a government changes the rules before the date arrives, the appointment moves. Store wall time plus zone id.

### node-postgres

`pg` returns JS `Date` for date/timestamp columns. Override the parsers once, globally:

```js
import pg from 'pg';
pg.types.setTypeParser(1082, (v) => Temporal.PlainDate.from(v));       // DATE
pg.types.setTypeParser(1184, (v) => Temporal.Instant.from(v));         // TIMESTAMPTZ
pg.types.setTypeParser(1114, (v) => Temporal.PlainDateTime.from(v));   // TIMESTAMP
```

`1184` values arrive as `'2026-03-14 21:00:00+00'`, with a space instead of `T`. Temporal accepts that form — its grammar allows a space separator, per the RFC 3339 readability note (strict ISO 8601 requires `T`) — so no normalization is needed.

### Prisma

`DateTime` fields are always JS `Date` in the client. Convert in a client extension so the rest of the app never sees a `Date`:

```js
prisma.$extends({
  result: {
    booking: {
      startsAt: {
        needs: { startsAt: true },
        compute: (b) => b.startsAt.toTemporalInstant(),
      },
    },
  },
});
```

Writes still take `Date` — convert back with `new Date(instant.epochMilliseconds)` in your repository layer.

### Drizzle

Prefer `mode: 'string'` over `mode: 'date'` — it hands you the raw SQL string, which is exactly what `Temporal.X.from()` wants, and skips a lossy `Date` round-trip:

```js
startsAt: timestamp('starts_at', { withTimezone: true, mode: 'string' }),
```

Then parse in the repository, or wrap with a Drizzle custom type.

## Intl

`Intl.DateTimeFormat` accepts Temporal objects directly — **on native implementations**.

**Polyfill caveat:** the built-in `Intl.DateTimeFormat` doesn't know polyfilled Temporal objects — `.format(plainDate)` throws `TypeError`. On a polyfill, either use `.toLocaleString()` (patched, works) or import the polyfill's formatter:

```js
import { Intl } from 'temporal-polyfill';   // @js-temporal/polyfill exports one too
```

Two rules either way:

- Format options must not request fields the type lacks (`timeStyle` on a `PlainDate` throws).
- For an `Instant`, pass `timeZone` in the options — otherwise you render in the system zone, which on a server means UTC or whatever the container was configured with.

```js
new Intl.DateTimeFormat('en-US', {
  dateStyle: 'medium', timeStyle: 'short', timeZone: user.timeZone,
}).format(instant);
```

Reuse formatter instances — constructing `Intl.DateTimeFormat` is expensive and shows up in render loops. (On a polyfill, the reused instance must be the polyfill's `Intl`, not the global one.)

`Intl.DurationFormat` handles `Duration` where available; check support before relying on it.

## Workers, postMessage, structuredClone

Temporal objects are **not** structured-cloneable, and the two implementations fail differently:

- **Native** throws `DataCloneError`.
- **`temporal-polyfill` fails silently.** `structuredClone(plainDate)` returns a prototype-less object — `instanceof Temporal.PlainDate` is `false`, `.year` is `undefined`, `.toString()` gives `'[object Object]'`. No error at the boundary; the breakage surfaces somewhere else entirely.

So this is not a bug you can rely on catching in a polyfilled test run. Always serialize to a string at the boundary:

```js
worker.postMessage({ date: plainDate.toString() });
// worker side
const date = Temporal.PlainDate.from(e.data.date);
```

## React and state

Immutability makes Temporal a good fit for state, with one wrinkle: every operation returns a new object, so referential equality checks always miss.

```js
useMemo(() => expensive(date), [date.toString()]);   // ✅ stable key
useMemo(() => expensive(date), [date]);              // ❌ recomputes every render
```

Same for `key` props, `useEffect` deps, and memo comparators — key on `.toString()`.

## Testing and fake clocks

`vi.useFakeTimers()` / `jest.useFakeTimers()` patch `Date` and `Date.now`. Whether they reach `Temporal.Now` depends on the version and on whether you're on native or polyfill — **don't assume they do**. The durable fix is to not call `Temporal.Now` in business logic at all:

```js
// inject a clock
function isExpired(token, now = Temporal.Now.instant()) {
  return Temporal.Instant.compare(now, token.expiresAt) >= 0;
}
```

Tests pass an explicit instant; production uses the default. This is worth doing regardless of the fake-timer question — it makes DST edge cases directly testable instead of requiring you to mock the system zone.

## Third-party SDKs

Most still take and return `Date`. Convert at the call site and immediately back:

```js
const res = await sdk.query({ after: new Date(since.epochMilliseconds) });
return res.items.map((i) => ({ ...i, at: i.timestamp.toTemporalInstant() }));
```

Resist the urge to hold `Date` values "just until the next call" — that's how they spread.
