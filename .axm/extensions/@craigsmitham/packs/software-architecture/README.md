# Software architecture

Software architecture knowledge and focused workflows for setting up,
authoring, and reconciling architecture docs that preserve accepted, durable
functional meaning, product quality requirements, and structural meaning
without copying facts that executable or live sources own better.

## Included extensions

| Extension | Role |
| --- | --- |
| `@craigsmitham/knowledge/software-architecture` | Human-first, risk-driven architecture meaning, product quality requirements, lifecycle, stewardship, stable concept identity, selected views, and the Just Enough Architecture Docs pattern |
| `@craigsmitham/skills/setup-architecture-docs` | Establish the system boundary, root, local adoption, authority routes, maintenance triggers, and agent discovery without empty or inferred scaffolding |
| `@craigsmitham/skills/author-architecture-docs` | Create or revise the explicitly requested semantic delta while routing exact current facts to their authorities |
| `@craigsmitham/skills/reconcile-architecture-docs` | Reconcile established docs through bounded repair and classify semantic lifecycle issues, making changes only with explicit user authority |

The three skills are non-standalone: they load the bundled knowledge through
its canonical AXM path and are distributed through this pack. The knowledge
bundle remains useful on its own. It currently declares Candidate maturity,
with draft, not human-verified concept documents. Just Enough Architecture Docs
defines the philosophy; every corpus managed by the pack must represent it as
OKF v0.2 and conform to the bundled software-architecture-docs profile.
Repository-local accepted authority governs meaning, while the profile governs
representation and permitted variance.

## Revision 0.4.0

This release updates the pack floors to knowledge `2.0.0`, authoring `2.0.0`,
setup `0.4.0`, and reconciliation `0.2.0`. It replaces optional profile adoption
with required OKF v0.2 and software-architecture-docs profile conformance.
Existing unprofiled corpora require setup and migration; rollback is to pack
`0.3.1` and its prior member versions.

## Install

```bash
axm install @craigsmitham/packs/software-architecture
```

## Workflow

- Ask to set up architecture docs when adopting the method or connecting an
  existing documentation root.
- Ask to author architecture docs when accepted meaning needs a bounded new or
  revised, organized, or individually reviewed home.
- Ask to reconcile architecture docs when established docs
  need review, repair, reconciliation, consolidation, pruning, or lifecycle
  attention.
- Use the knowledge bundle directly to reason about responsibilities,
  boundaries, dependency direction, invariants, offerings, audiences, needs,
  jobs to be done, value propositions, use cases, capabilities, features,
  surfaces, product quality requirements, DDD contexts, C4 structures, or
  Wardley mapping.
- Keep undecided alternatives in proposals and precise current facts in their
  executable or live authorities.

## Evaluation cases

Each skill includes a behavioral suite. Together they check minimal adoption,
workflow routing boundaries, accepted desired-state handling, authority
reconciliation, demand-and-value separation, product-quality authority, C4
containment, strategic freshness, maintenance lifecycle decisions, and
resistance to empty scaffolding or exhaustive prose mirrors.

## License

The pack's own metadata and README are licensed under MIT. Each member retains
the license declared in its manifest. See the repository for source attribution
and provenance.
