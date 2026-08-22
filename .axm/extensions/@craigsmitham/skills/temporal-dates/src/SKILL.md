---
name: temporal-dates
description: Write date, time, timezone, duration, and calendar code with the JavaScript Temporal API instead of the legacy Date object. Use when authoring or reviewing any code that creates, parses, formats, compares, stores, or does arithmetic on dates and times, when choosing a date library (moment, dayjs, date-fns, luxon), or when deciding which Temporal type a value should be. Triggers on Temporal, PlainDate, ZonedDateTime, Instant, Duration, new Date(), timezone, DST, epoch, timestamp.
---

# Temporal instead of Date

`Temporal` replaces `Date`. Write new date/time code with it. `Date` is mutable, month-indexes from 0, parses inconsistently, and collapses every distinct concept — a birthday, a meeting, a log entry, a duration — into one timestamp that silently shifts when the timezone changes.

The single highest-value thing this skill does is **stop you reaching for one type for everything**. Pick the type first; the API follows.

If a request demands one Temporal type for values with different meanings,
correct that requirement explicitly. Do not provide a uniform-type compromise
as the implementation: show each value with its semantically correct type and
explain that consistent JSON strings do not require identical in-memory types.

## Step 0 — establish the runtime (do this once per project)

Native support is mid-rollout, so never assume. Check, then write code that matches:

```bash
# Node / Bun / Deno — is it a global here?
node -e "console.log(typeof Temporal)"

# Is a polyfill already a dependency?
rg -n "temporal-polyfill|@js-temporal/polyfill" package.json

# Does this ship to browsers, and which?
rg -n "browserslist|\"engines\"" package.json
```

- **`"object"` and no browser target** → use the `Temporal` global, no import.
- **`"undefined"`, or a browserslist that includes anything not yet shipping Temporal** → the project needs a polyfill. Prefer `temporal-polyfill` (smaller, actively maintained); `@js-temporal/polyfill` is the champions' reference implementation. Add the import at the top of files that use it:
  ```js
  import { Temporal } from 'temporal-polyfill';
  ```
- If a polyfill is already present, **match the existing import style** rather than introducing the global.

Every example below uses bare `Temporal.*`. Add the import line if the project needs it.

## Pick the type

Ask: **what would be wrong if this value moved when the timezone changed?**

| The value is… | Use | Why |
|---|---|---|
| Birthday, contract date, holiday, due date | `Temporal.PlainDate` | A date with no time and no zone. Never shifts. |
| "3pm on Mar 14 in Chicago" — a real scheduled event | `Temporal.ZonedDateTime` | The only type that is both wall-clock *and* an exact instant. |
| Log line, audit trail, `createdAt`, "when did this happen" | `Temporal.Instant` | An exact point on the timeline. No zone, no calendar. |
| Store opening hours, a 7am alarm | `Temporal.PlainTime` | Time of day, recurring, zone-independent. |
| Billing month, card expiry, "Q3 2026" | `Temporal.PlainYearMonth` | Month granularity without a fake day-of-month. |
| Anniversary, annual holiday, Feb 29 handling | `Temporal.PlainMonthDay` | Recurs yearly; no year to get wrong. |
| Elapsed time, timeout, "2h30m" | `Temporal.Duration` | A length of time, not a point. |
| `"2026-03-14T15:00"` from a legacy system, zone unknown | `Temporal.PlainDateTime` | Naive wall time. **Resolve to a zone before doing anything real with it.** |

**The most common bug this prevents:** storing a birthday as an `Instant` or `Date`. A user born `1990-06-15` becomes `1990-06-14` for anyone east of the storage timezone. Birthdays are `PlainDate`. So are due dates, holidays, and anything a human would write on a paper calendar.

**Corollary:** a `PlainDateTime` is not a moment in time. It is a moment in time *missing its most important field*. Don't let one linger in a data model — either it has a zone (`ZonedDateTime`) or it doesn't need one (`PlainDate` / `PlainTime`).

## Now

```js
Temporal.Now.instant()                            // exact moment — for timestamps
Temporal.Now.zonedDateTimeISO()                   // system zone
Temporal.Now.zonedDateTimeISO('America/Chicago')  // explicit zone — prefer this
Temporal.Now.plainDateISO()                       // today, system zone
Temporal.Now.timeZoneId()                         // 'America/Chicago'
```

Pass the zone explicitly wherever the answer depends on it. `Temporal.Now.plainDateISO()` means "today *where this process happens to run*", which is a server-config dependency hiding in your business logic.

## The five rules

**1. Everything is immutable.** `.add()`, `.with()`, `.round()` return new objects. `d.add({days: 1})` alone does nothing — assign the result.

```js
const due = start.add({ days: 30 });        // ✅
start.add({ days: 30 });                    // ❌ discarded
```

**2. Months are 1-based.** `month: 1` is January. (`Date` used 0.) Use `monthCode: 'M01'` when working across non-Gregorian calendars.

**3. Calendar days ≠ 24 hours.** On a `ZonedDateTime`, `.add({days: 1})` keeps the wall-clock time and may cross 23 or 25 real hours; `.add({hours: 24})` adds exactly 24 hours and may land on a different wall time. Choose deliberately — this is the DST bug.

```js
const z = Temporal.ZonedDateTime.from('2026-03-07T12:00[America/Chicago]');
z.add({ days: 1 }).toString();   // 2026-03-08T12:00 — same wall time, 23h later
z.add({ hours: 24 }).toString(); // 2026-03-08T13:00 — exactly 24h later
```

**4. Reject bad input instead of silently fixing it.** `from()` and `.with()` default to `overflow: 'constrain'`, which turns Feb 30 into Feb 28. For anything user- or API-supplied, pass `{ overflow: 'reject' }`.

```js
Temporal.PlainDate.from({ year: 2026, month: 2, day: 30 });                        // 2026-02-28 😬
Temporal.PlainDate.from({ year: 2026, month: 2, day: 30 }, { overflow: 'reject' }); // throws ✅
```

**5. Compare with the right tool.** Ordering uses the static: `Temporal.PlainDate.compare(a, b)` → `-1 | 0 | 1`, which drops straight into `.sort()`. Relational operators (`<`, `>`) do **not** work on Temporal objects.

`.equals()` tests equality but **coerces its argument rather than type-checking it** — `plainDate.equals(someZonedDateTime)` is `true` whenever the dates match, silently discarding the time. Narrow both sides explicitly before comparing across types. See `references/pitfalls.md`.

```js
dates.sort(Temporal.PlainDate.compare);
if (Temporal.Instant.compare(now, expiry) >= 0) { /* expired */ }
```

## Arithmetic

```js
d.add({ months: 1, days: 5 })          // larger units first, then smaller
d.subtract({ weeks: 2 })
d.with({ day: 1 })                      // set fields — start of month
d.until(other, { largestUnit: 'year' }) // → Duration
```

Two traps:

- **Not commutative.** `d.add({months: 1}).add({days: 1})` ≠ `d.add({days: 1}).add({months: 1})` near month ends. Adding a month to Jan 31 constrains to Feb 28.
- **`until`/`since` default to days.** `largestUnit` defaults to `'auto'`, which yields days for date types. Pass `largestUnit: 'year'` explicitly if you want "2 years, 3 months".

`Duration.total()` needs a `relativeTo` for calendar units — weeks, months, and years:

```js
dur.total({ unit: 'minute' });                       // fine — hours and below are exact
dur.total({ unit: 'day', relativeTo: someDate });     // required once weeks/months/years are involved
```

Check for zero with `dur.sign === 0`, not truthiness — every `Duration` object is truthy.

## Formatting and serialization

```js
d.toString()                          // RFC 9557 — the wire/storage format
d.toJSON()                            // same; JSON.stringify uses it automatically
d.toLocaleString('en-US', { dateStyle: 'long' })   // human-facing
```

`JSON.stringify` serializes correctly, but **parsing is not automatic** — `JSON.parse` gives you back a string. Revive explicitly with `Temporal.PlainDate.from(str)` at your schema boundary.

Match `toLocaleString` options to the fields the type actually has. Asking a `PlainDate` for `timeStyle` throws.

## Reference files

Load these only when the task calls for them:

- **`references/api.md`** — per-type sharp edges where the API differs from a reasonable guess: missing methods, argument-shape inconsistencies, BigInt fields, option defaults.
- **`references/pitfalls.md`** — DST disambiguation, nonexistent midnights, `hoursInDay`, offset conflicts, non-ISO calendars, range limits.
- **`references/interop.md`** — crossing boundaries: `Date`, Postgres/MySQL/SQLite drivers, ORMs (Prisma, Drizzle, TypeORM), Zod/schema validation, `Intl`, and third-party APIs that still hand you a `Date`.

## When `Date` is still correct

Don't convert reflexively at the boundary. Keep `Date` where an external API demands it — pass it in, convert on receipt:

```js
const instant = legacyDate.toTemporalInstant();      // Date → Temporal
const legacy = new Date(instant.epochMilliseconds);  // Temporal → Date
```

Convert at the edges; keep `Temporal` everywhere inside.
