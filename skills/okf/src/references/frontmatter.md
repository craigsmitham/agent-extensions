# OKF frontmatter reference

`type` is the only always-required key. A concept carrying just `type` is fully conformant.

| Field | Req | Form | Notes |
|---|---|---|---|
| `type` | **yes** | string | Kind of concept. Uncontrolled vocabulary — see [Type discipline](../SKILL.md#type-discipline). |
| `title` | rec | string | Canonical display name. Use exact wording in index links. Consumers may fall back to the filename. |
| `description` | rec | string | One sentence distinguishing this concept from its neighbors. For action concepts, include the selection condition and supported outcome; for Processes, include the trigger and closing outcome. Reuse it exactly in index entries and search snippets. |
| `resource` | rec | URI/path | Canonical URI of the underlying asset. Omit for abstract concepts. |
| `tags` | rec | list | Stable domain terms, aliases, and query vocabulary; do not merely repeat the title. |
| `sources` | opt | list | Provenance. Each entry needs `resource`; `id`, `title`, `author`, `usage_count`, `last_modified`, `usage_window` optional. `last_modified` is an offset datetime. |
| `usage_window` | opt | `{from, to}` | Sibling of `sources`; frames every `usage_count`. Offset datetimes; an entry's own window overrides the shared one. |
| `generated` | opt | `{by, at}` | `by` required within it; an actor. `at` = last meaningful content change, offset datetime. |
| `verified` | opt | list of `{by, at}` | Verification events. A bare mapping is a one-element list. |
| `status` | opt | enum | `draft` \| `stable` \| `deprecated`. Absent means `stable`. |
| `stale_after` | opt | offset datetime | Absolute instant, not a TTL. Stale when `now >= stale_after`. |

## Timestamps and migration

Every timestamp-valued key uses an ISO 8601 datetime with an explicit UTC offset
(§5), for example `2026-06-30T14:00:00Z` or `2026-06-30T09:00:00-05:00`. This
applies to `generated.at`, every `verified[].at`, `sources[].last_modified`,
both endpoints of shared and per-source `usage_window`, and `stale_after`.
Compare staleness as instants, preserving offsets and time of day. Quoted and
unquoted YAML timestamps have the same meaning. Reserved log headings remain
date-only `YYYY-MM-DD` (§9).

Earlier v0.2 snapshots used dates for `last_modified`, `usage_window`, and
`stale_after`. Recover actual times and offsets from evidence where possible.
A producer may define a documented conversion policy for date boundaries, but
do not silently append midnight UTC or present assumed precision as observed
provenance. If the intended instant is unknown, surface that uncertainty and
leave migration unresolved or omit the optional field when authorized. Changing
representation is not a new generation or verification event.

The bundled validator warns on invalid, date-only, or offset-free timestamps.
These remain optional-family findings under §11, separate from base conformance.
It does not infer staleness or elevate trust from malformed timestamps.

## Extensions and trust

Producers may add any other keys; consumers should preserve them when round-tripping
and must not reject documents for unrecognized fields (§4.1). Use that freedom sparingly — a
custom key no consumer reads is dead weight.

**Trust tiers** are derived, never stored: no `verified` key → unverified; `verified` by non-`human:`
actors only → machine-confirmed; at least one `human:<id>` → human-reviewed.

## Actor convention

Identity fields (`generated.by`, `verified[].by`) use exactly one of:

- `<producer>/<version>` — agents and tools, e.g. `reference_agent/gemini-2.5-pro`
- `human:<id>` — people, e.g. `human:ahormati`
- `process:<id>` — automated processes, e.g. `process:finance-nightly`

The `human:` prefix is load-bearing: it is what raises a concept to the human-reviewed tier. Use it
for hand-authored and human-confirmed content, and never for agent output.

`sources[].author` nominally uses the same convention, but the spec's own examples use a team form
(`team:finance-fpa`). Both are accepted; the validator only flags freeform values here.

