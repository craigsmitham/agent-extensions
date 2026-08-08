# Temporal pitfalls

Temporal removes most `Date` footguns. These are the ones it deliberately keeps — because the underlying problem is real, and the API makes you choose rather than guessing for you.

## DST: the two ambiguities

Local time is not a function. Twice a year it is either undefined or two-valued.

**Spring forward — the time doesn't exist.** In `America/Chicago`, 2026-03-08 jumps 02:00 → 03:00. There is no 02:30.

**Fall back — the time happens twice.** 2026-11-01 repeats 01:00 → 02:00. There are two 01:30s, an hour apart.

`disambiguation` decides:

| Value | Nonexistent time | Ambiguous time |
|---|---|---|
| `'compatible'` (default) | shift **later** (03:30) | pick the **first** (earlier offset) |
| `'earlier'` | shift **earlier** (01:30) | pick the first |
| `'later'` | shift later | pick the second |
| `'reject'` | **throws** | **throws** |

```js
// user picked a time in a scheduling UI — don't silently move their meeting
Temporal.ZonedDateTime.from(
  { year: 2026, month: 3, day: 8, hour: 2, minute: 30, timeZone: 'America/Chicago' },
  { disambiguation: 'reject' },
);   // RangeError → show the user a real error
```

Rule of thumb: `'reject'` for anything a human typed, `'compatible'` for machine-generated or recurring times where "just pick something sane" is genuinely fine.

## Calendar days are not 24 hours

The single most common DST bug, and Temporal makes both behaviors expressible — so pick on purpose:

```js
const z = Temporal.ZonedDateTime.from('2026-03-07T12:00[America/Chicago]');
z.add({ days: 1 });    // 2026-03-08T12:00 — same wall time, 23 real hours later
z.add({ hours: 24 });  // 2026-03-08T13:00 — 24 real hours, different wall time
```

- "Same time tomorrow" (a recurring meeting) → `{ days: 1 }`.
- "24 hours from now" (a token expiry, a rate-limit window) → `{ hours: 24 }`.

Mixed durations resolve **largest unit first**: `{ days: 1, hours: 2 }` adds the calendar day, then two exact hours.

## Midnight doesn't always exist

Some zones have transitioned at 00:00 (Brazil historically, parts of Chile, Cuba, Iran). `.with({ hour: 0, minute: 0 })` on those dates lands on a nonexistent time.

```js
z.startOfDay();                    // ✅ always correct
z.with({ hour: 0, minute: 0 });    // ❌ shifts or throws on transition days
```

Same reasoning for day-length math — use `.hoursInDay` (usually 24, but 23, 25, or even fractional like 24.5 in half-hour-DST zones) rather than assuming 24.

## Offset vs. zone conflicts

A stored string can carry both an offset and a zone id. When the tzdata database updates — governments change DST rules with weeks of notice — the offset you stored may no longer match what the zone says.

```js
'2026-11-01T01:30:00-05:00[America/Chicago]'
```

The `offset` option decides who wins:

| Value | Behavior |
|---|---|
| `'reject'` (default for `from`) | Throws on mismatch. Loud, safe. |
| `'use'` | Trust the offset; the instant is preserved, wall time may shift. |
| `'prefer'` | Use the offset if it's valid for that zone, else re-resolve. |
| `'ignore'` | Discard the offset; re-resolve wall time in the zone. |

For stored past events, `offset: 'use'` preserves what actually happened. For future scheduled events, `'ignore'` or `'prefer'` keeps the appointment at the intended wall-clock time even if the rules changed. **These are genuinely different answers — decide which one your feature needs.**

Corollary: store future scheduled events as wall time + zone id (`ZonedDateTime` string, or `PlainDateTime` + IANA id), not as a bare epoch timestamp. An epoch timestamp bakes in a DST rule that may not survive to the event date.

## Arithmetic is not commutative

```js
const d = Temporal.PlainDate.from('2026-01-31');
d.add({ months: 1 }).add({ days: 1 });   // 2026-02-28 → 2026-03-01
d.add({ days: 1 }).add({ months: 1 });   // 2026-02-01 → 2026-03-01
```

They agree here; near other month boundaries they don't. Adding a month to Jan 31 constrains to Feb 28 and **the lost day never comes back** — `d.add({months:1}).subtract({months:1})` is not `d`. Where round-tripping matters, store the original and recompute rather than reversing.

## `until` / `since` default to days

`largestUnit` defaults to `'auto'`, which for date types means days. "1 year, 2 months" requires asking:

```js
a.until(b);                              // { days: 428 }
a.until(b, { largestUnit: 'year' });     // { years: 1, months: 2, days: 3 }
```

`since` is `until` with the arguments reversed, not a negation shortcut — `a.since(b)` equals `b.until(a)`.

## Durations have no intrinsic length

`Temporal.Duration.from({ months: 1 })` is not a number of days, and cannot be converted to one without an anchor:

```js
dur.total({ unit: 'day' });                                  // throws
dur.total({ unit: 'day', relativeTo: Temporal.Now.plainDateISO() });   // ok
```

Also: `Duration` fields are stored as written. `PT90M` reports `minutes: 90, hours: 0` until you `.round({ largestUnit: 'hour' })`. Never read `.hours` expecting normalization.

And every `Duration` is truthy — `if (dur)` is always true. Use `dur.sign === 0` or `dur.blank`.

## Comparison and equality

- Relational operators don't work. `a < b` coerces to strings and is nonsense.
- `ZonedDateTime.equals()` also compares zone and calendar — `2026-03-14T15:00[America/Chicago]` and the same instant in `[America/New_York]` are **not** equal. For "same moment", compare `.epochNanoseconds`.
- Objects are never reference-equal after any operation. Deduplicating with a `Set` requires keying on `.toString()`.

```js
const unique = [...new Map(dates.map(d => [d.toString(), d])).values()];
```

**`.equals()` does not type-check — it coerces the argument.** This is the sharp edge:

```js
const d = Temporal.PlainDate.from('2026-03-14');
d.equals(Temporal.PlainDateTime.from('2026-03-14T23:59'));  // true  — time discarded
d.equals(Temporal.ZonedDateTime.from('2026-03-14T23:59[America/Chicago]')); // true
d.equals('2026-03-14');                                     // true  — string parsed
Temporal.PlainDate.compare(d, someDateTime);                // 0     — same coercion
```

The receiver decides. `plainDate.equals(x)` converts `x` to a `PlainDate` and compares dates; the reverse direction, `plainDateTime.equals(plainDate)`, converts the `PlainDate` to midnight and returns `false` for any nonzero time. So the same pair compares equal or unequal depending on which side you call it from. It only throws when the argument genuinely lacks the needed fields (`plainDate.equals(plainTime)` throws a `TypeError`).

Compare like with like. Narrow explicitly first — `a.toPlainDate().equals(b.toPlainDate())` — so the intent is on the page rather than in the coercion.

## `.map(Temporal.PlainDate.from)` throws

`from()` takes `(input, options)`, and `Array.prototype.map` passes `(element, index, array)`. The index arrives as the options bag:

```js
strings.map(Temporal.PlainDate.from);        // ❌ TypeError: Invalid object
strings.map(s => Temporal.PlainDate.from(s)); // ✅
```

Same hazard for `flatMap` and anything else passing extra arguments. The static comparators are safe point-free, because they take exactly `(a, b)`:

```js
dates.sort(Temporal.PlainDate.compare);   // ✅ fine
```

## Non-ISO calendars

```js
const hebrew = plainDate.withCalendar('hebrew');
hebrew.monthCode;   // 'M05L' in a leap year — L suffix marks a leap month
```

- Use `monthCode`, not `month`, when the calendar may not be ISO — month *numbers* shift when a leap month is inserted.
- `.equals()` is false across different `calendarId`s even for the same day.
- Formatting a non-ISO object with a formatter pinned to another calendar throws.
- `weekOfYear` / `yearOfWeek` can be `undefined` where the calendar has no week numbering.

## Range limits

All Temporal values sit within ±10⁸ days of the epoch: roughly `-271821-04-20` to `+275760-09-13`. Same bounds as `Date`. Arithmetic that escapes the range throws `RangeError` rather than producing `Invalid Date` — which is the improvement, but it does mean sentinel values like "year 9999999" now fail loudly.

## Precision loss at the `Date` boundary

`Instant` carries nanoseconds; `Date` carries milliseconds. `new Date(instant.epochMilliseconds)` truncates. Databases vary too — Postgres `timestamptz` is microsecond-precision, so a nanosecond value round-trips lossily. If sub-millisecond precision matters (distributed tracing, event ordering), store `epochNanoseconds` as a string or BigInt column rather than a timestamp type.
