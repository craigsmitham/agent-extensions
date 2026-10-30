# Changelog

## 0.2.0 — 2026-10-30

- Align with the canonical `GoogleCloudPlatform/open-knowledge-format` spec and
  README at `ad30107c31c06aec8a7d5636e0d1058118604e6f` (checked 2026-10-30).
  OKF remains v0.2; the spec now requires explicit UTC offsets on timestamps.
- Update provenance and lifecycle guidance and templates. Compare staleness as
  `now >= stale_after`; keep reserved log headings as `YYYY-MM-DD`.
- Match §4.1's SHOULD-preserve / MUST-NOT-reject distinction for unknown keys,
  allow actual machine verification events, and use §10.3's fenced inline
  computation form in the template.
- Warn on date-only or offset-free timestamps, including verification events,
  shared and per-source usage windows, and source modification times. Preserve
  base-conformance versus optional-family severity; `--strict` fails on these
  warnings. Invalid unquoted YAML timestamps now produce diagnostics instead
  of crashing. Invalid verification timestamps no longer elevate trust.
- Add `--now` for deterministic instant comparisons; retain `--today` with an
  explicit midnight-UTC meaning. The Python helper's internal `validate` clock
  argument now takes an offset-aware datetime instead of a date.
- Migration: establish intended instants from evidence or a documented producer
  policy before replacing old dates. Do not infer midnight UTC or new trust
  events. Existing bundles may gain warnings; no corpus migration is performed.
  Retain the earlier skill version to recover the previous date-based checks.
- Keep application profiles provisional; update canonical source attribution,
  include the vendored Apache-2.0 license, and ignore Python test bytecode in
  consumer worktrees. No new runtime dependency or execution authority.

## 0.1.10

- Rename the skill from `author-okf` to `okf`
  (`@craigsmitham/skills/okf`). Behavior is unchanged.

## 0.1.9 — 2026-09-08

- Default citation definitions to short titles while preserving source IDs,
  useful qualifications, and linked titles for rendered-Markdown readers.
- Apply the convention across creation, conversion, and maintenance; align
  the concept template and add two citation-maintenance regression cases.
- Move frontmatter details and representation-review procedure into linked
  references. Citation brevity remains authoring guidance; OKF conformance,
  activation scope, and execution authority are unchanged.
