# Initial public migration — 2026-08-08

This repository was created with fresh Git history. The packages below were
copied from `agent-extensions-private`, reviewed against the public-readiness
gate in `AGENTS.md`, normalized for public metadata and licensing, versioned,
and published from this repository. The private repository now consumes these
releases from the AXM registry rather than authoring parallel copies.

## Migrated packages

| Package | Public version |
| --- | --- |
| `@craigsmitham/packs/effect-v4` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-async-coordination` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-branded-types` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-config` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-error-modeling` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-observability` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-optics` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-request-batching-and-cache` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-resource-safety` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-schema-boundaries` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-services-and-layers` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-streams` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-structured-concurrency` | `0.0.2` |
| `@craigsmitham/skills/effect-v4-testing` | `0.0.2` |
| `@craigsmitham/packs/docs` | `0.1.1` |
| `@craigsmitham/knowledge/docs` | `0.4.1` |
| `@craigsmitham/skills/author-guide` | `0.1.1` |
| `@craigsmitham/skills/review-docs` | `0.1.1` |
| `@craigsmitham/skills/temporal-dates` | `0.0.3` |
| `@craigsmitham/skills/okf-author` | `0.0.2` |
| `@craigsmitham/skills/eval-whatever` | `0.0.3` |

## Subsequent package rename

`@craigsmitham/skills/okf-author` was superseded by
`@craigsmitham/skills/author-okf` on 2026-08-08 to align with the repository's
verb-first skill naming. The old package remains available but deprecated so
existing installations continue to resolve and receive a migration notice.

## Subsequent documentation skill consolidation

`@craigsmitham/skills/author-guide` and
`@craigsmitham/skills/review-docs` were superseded on 2026-08-08 by
`@craigsmitham/packs/docs` 0.2.0. The pack pairs the documentation knowledge
bundle with the consolidated `@craigsmitham/skills/author-docs` routing skill.
The old packages remain available but deprecated so existing installations
continue to resolve and receive a migration notice.

## Review performed

- Scanned package content and metadata for credentials, personal identifiers,
  private paths, private hosts, private repository references, and real data.
- Verified that packages have public-repository metadata, descriptions,
  keywords, and explicit license declarations.
- Preserved upstream attribution for Diátaxis-derived documentation and the
  vendored Open Knowledge Format specification.
- Ran strict AXM lint, package inventory checks, sensitive-pattern checks, and
  symlink-boundary checks before publishing.
- Verified the published package archives and changed the private repository's
  AXM trust authority from `workspace` to `registry` for every migrated item.

## Deferred scope

- `workstation` and its skills remain withheld candidates. They contain real
  machine and authentication topology and require a separate generalization
  and remediation project before public consideration.
- `personal-os` and its skills remain private-only because their behavior is
  identity-specific and includes personal operational context.
- No attempt was made to generalize either family during this migration.
