# Software architecture

> **Superseded:** this pack is retained for reproducibility and will be
> deprecated in the registry after version `0.7.0` is published. For active
> development, install `@craigsmitham/packs/gen-stack`.

Software architecture knowledge and focused workflows for setting up,
authoring, and reconciling architecture docs that preserve accepted, durable
functional meaning, subject-colocated requirements, and structural meaning
without duplicating obligations across architecture views or copying facts that
executable or live sources own better.

## Included extensions

| Extension | Role |
| --- | --- |
| `@craigsmitham/knowledge/software-architecture` | Human-first architecture and requirements meaning; the mandatory System and context kernel; subject-colocated requirements; named decisions; selected views; and the Just Enough Architecture Docs pattern |
| `@craigsmitham/skills/setup-architecture-docs` | Establish the system boundary, root, required context kernel, local adoption, authority routes, maintenance triggers, and agent discovery without inferred architecture |
| `@craigsmitham/skills/author-architecture-docs` | Create or revise an explicitly requested System, Requirement, ADR, or other architecture concept while routing exact current facts to their authorities |
| `@craigsmitham/skills/reconcile-architecture-docs` | Reconcile established docs and profile migrations through bounded repair, making semantic changes only with explicit user authority |

The three skills are non-standalone: they load the bundled knowledge through
its canonical AXM path and are distributed through this pack. The knowledge
bundle remains useful on its own. It currently declares Candidate maturity,
with draft, not human-verified concept documents. Just Enough Architecture Docs
defines the philosophy; every corpus managed by the pack must represent it as
OKF v0.2 and conform to the bundled software-architecture-docs profile.
Repository-local accepted authority governs meaning, while the profile governs
representation and permitted variance.

## Final revision 0.7.0

This is a migration-only final release. It brings the architecture workflows
onto profile `0.10.2`, the single Requirement authority semantics, and the
shared Gen Stack knowledge those workflows require. It does not alias or
transitively install the complete Gen Stack pack. Future cross-cutting
development is distributed through `@craigsmitham/packs/gen-stack`. Published
versions and source remain available so older installations can still be
reproduced.

## Install

```bash
axm install @craigsmitham/packs/software-architecture
```

For active repositories, migrate explicitly:

```bash
axm uninstall @craigsmitham/packs/software-architecture
axm install @craigsmitham/packs/gen-stack
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
  boundaries, dependency direction, invariants, requirement classification,
  functional, quality, process, human-factors, and usability obligations,
  offerings, audiences, needs,
  jobs to be done, value propositions, use cases, capabilities, features,
  surfaces, subject-colocated requirements, DDD contexts, C4 structures, or
  Wardley mapping.
- Keep undecided alternatives in proposals and precise current facts in their
  executable or live authorities.

## Evaluation cases

Each skill includes a behavioral suite. Together they check minimal adoption,
workflow routing boundaries, accepted desired-state handling, authority
reconciliation, demand-and-value separation, product-quality authority, C4
containment, strategic freshness, maintenance lifecycle decisions, and
resistance to empty scaffolding or exhaustive prose mirrors. Focused execution
cases cover system-context, requirement, and decision concepts.

## License

The pack's own metadata and README are licensed under MIT. Each member retains
the license declared in its manifest. See the repository for source attribution
and provenance.
