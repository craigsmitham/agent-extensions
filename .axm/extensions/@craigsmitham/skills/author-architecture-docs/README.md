# Author architecture docs

Creates and revises human-readable software architecture docs that preserve
the smallest accepted semantic delta over repository and runtime authorities.

Use it for architecture overviews, responsibility and boundary documents,
product quality requirements, corpus organization, offering and
value models, capability/feature/surface models, DDD context views, C4 model
views, Wardley-informed strategic views, and focused document reviews. Do not
use it for initial setup or whole-set maintenance, to choose among architecture
alternatives, to turn a proposal into accepted design, or to mirror the
implementation in prose. Product research, roadmaps, pricing, sales, and
marketing content remain outside the skill unless architecture documentation
is the requested artifact.

When a repository has explicitly adopted the software architecture docs
application profile, the skill routes each named profile type to a concise
one-artifact guide and creates only the requested semantic artifact and required
navigation. Otherwise it applies the semantic guidance while preserving the
repository's established architecture-document form and paths. Adjacent
additions, reductions, or reorganizations remain grounded recommendations until
the user authorizes them.

The bundled knowledge currently declares Candidate maturity; its concept
documents are draft and not human-verified. Repository-local accepted authority
and formats take precedence, and the application profile remains opt-in.

Within the pack, initial adoption and system-to-corpus mapping belong to
`setup-architecture-docs`; a bounded new, revised, organized, or reviewed
artifact belongs here; established-corpus health and repair belong to
`reconcile-architecture-docs`.

This skill is a non-standalone member of the software-architecture pack because
it loads that pack's software-architecture knowledge.

## Revision 1.1.4

- Preserves established local formats and paths unless the application profile
  is explicitly adopted.
- Makes setup, bounded authoring, and established-corpus reconciliation
  ownership explicit.
- Adds same-pack routing regressions and a fixture-backed artifact-producing
  execution case.

This is a patch correction within the existing authority envelope. No migration
is required; rollback is to `1.1.3`. Behavioral regression and closure audit
evidence must remain bound to the exact `1.1.4` package and suite identities.

## Install

```bash
axm install @craigsmitham/packs/software-architecture
```

## Example

> Revise `docs/architecture/reservations.md` so it preserves the accepted
> reservation responsibility, recovery invariant, and evidence routes without
> duplicating the state-machine tests.

## License

MIT. The software-architecture knowledge bundle retains its separately declared
license.
