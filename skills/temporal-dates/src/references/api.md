# Temporal API sharp edges

Not a full API reference — MDN has that, and most of the surface is guessable
(`Type.from()`, `Type.compare()`, `.with()`, `.add()/.subtract()`,
`.until()/.since()`, `.equals()`, `.toString()`, `.toLocaleString()`). This file
is only the places where a reasonable guess is wrong.

## Instant

- `.epochNanoseconds` is a **BigInt**; `.epochMilliseconds` is a Number (the `Date` interop hinge).
- `fromEpochSeconds` and `fromEpochMicroseconds` do **not** exist. Multiply into milliseconds, or use `fromEpochNanoseconds` with a BigInt.
- `.add()/.subtract()` accept **time units only** (hours and below). Calendar units throw — convert to `ZonedDateTime` first via `.toZonedDateTimeISO(tz)`.
- `.toString()` defaults to `Z`; pass `{ timeZone }` to render an offset.

## ZonedDateTime

- `from()` takes two decision options besides `overflow`: `disambiguation` (`'compatible'` default | `'earlier'` | `'later'` | `'reject'`) and `offset` (`'reject'` default | `'use'` | `'prefer'` | `'ignore'`). These are where DST bugs live — see `pitfalls.md`.
- Use `.startOfDay()`, never `.with({ hour: 0 })` — midnight doesn't exist in every zone on every day.
- `.hoursInDay` is usually 24, but can be 23, 25, or fractional — 23.5/24.5 in half-hour-DST zones like `Australia/Lord_Howe`. Never assume an integer.
- `.withTimeZone(tz)` keeps the same instant and changes the wall clock.
- `.equals()` compares instant **and** zone **and** calendar. For "same moment?", compare `.epochNanoseconds` or the `.toInstant()` values.
- `.timeZoneId` / `.calendarId` are strings, not objects.

## PlainDate

- `.dayOfWeek`: 1 = Monday … 7 = Sunday.
- `.monthCode` is `'M03'`; leap months are `'M05L'`. Use it instead of `.month` whenever the calendar may not be ISO.
- `.weekOfYear` / `.yearOfWeek` can be `undefined` in calendars without week numbering.
- `.toZonedDateTime({ timeZone, plainTime })` takes an **object argument** — unlike `PlainDateTime.prototype.toZonedDateTime(tz, options?)`, which takes the zone positionally.

## PlainTime

Arithmetic wraps around midnight with no day carry: `23:30` + 1 hour = `00:30`,
and the lost day is simply gone. If you needed it, you wanted `PlainDateTime`.

## PlainMonthDay

- Has `.monthCode` and `.day` but **no `.month` getter** — month numbers aren't stable across calendars without a year.
- No arithmetic; project into a year first with `.toPlainDate({ year })`.
- `toPlainDate()` takes **no options bag** — it always constrains. `02-29` projected into 2027 silently yields `2027-02-28`, with no `overflow: 'reject'` to opt out. If Feb 29 needs distinct handling, check `.monthCode === 'M02' && .day === 29` before projecting.

## Duration

- Fields are stored as given — `PT90M` reports `minutes: 90, hours: 0` until you `.round({ largestUnit: 'hour' })`. Never read `.hours` expecting normalization.
- Test emptiness with `.sign === 0` or `.blank` — every Duration object is truthy.
- `relativeTo` is mandatory once years, months, or weeks are involved (`.round()`, `.total()`, and `Duration.compare()` all take it) — those units have no fixed length without an anchor date.

## Rounding

`.round()` accepts `smallestUnit`, `roundingIncrement`, and `roundingMode`
(default `'halfExpand'`, not truncation). `largestUnit` is a `Duration.round()`
option only — the datetime types silently ignore it:

```js
// snap to the next 15-minute slot
zdt.round({ smallestUnit: 'minute', roundingIncrement: 15, roundingMode: 'ceil' });
```

## Formatting

- `Intl.DateTimeFormat` accepts Temporal objects directly — no conversion to `Date`. **Native only:** the built-in formatter throws `TypeError` on polyfilled objects; on a polyfill use `.toLocaleString()` or the polyfill's own `Intl` export (see `interop.md`).
- Option fields must match the type's fields: `timeStyle` on a `PlainDate` throws, as does formatting a non-ISO-calendar object with a formatter pinned to a different calendar.
- For an `Instant`, supply `timeZone` in the options or you get the system zone.
- `.toString()` produces RFC 9557 — ISO 8601 extended with a bracketed zone annotation: `2026-03-14T15:00:00-05:00[America/Chicago]`. The calendar annotation (`[u-ca=hebrew]`) appears only for non-ISO calendars or with `calendarName: 'always'`; the default `calendarName: 'auto'` omits `[u-ca=iso8601]`.

**Polyfill note:** `temporal-polyfill`'s default entry point ships **ISO
calendars only** — `withCalendar('hebrew')` throws `RangeError: Unknown
calendar`. Non-ISO calendars require the larger `temporal-polyfill/full` build.
Native `Temporal` has them all.
