# Assess Codebase Change Readiness

Determine whether an accepted codebase change is sufficiently evidenced,
constrained, planned, and verifiable to begin implementation without hidden
product or architecture decisions, unverified technical paths, or unresolved
feasibility prerequisites.

The skill applies risk-proportional scrutiny, distinguishes a resolvable
`Not Ready` finding from an evidence-blocked assessment, and routes each gap to
acceptance, research, design, specification, or planning. It audits supplied
artifacts without repairing them.

Use it before implementation when an accepted change contract, current-state
evidence, and an implementation path need an independent readiness decision. Do
not use it to discover requirements, choose a design, write an implementation
plan, implement the change, or verify completed code.

Install it with:

```sh
axm install @craigsmitham/skills/assess-codebase-change-readiness
```

For example:

> Assess this accepted webhook-replay contract, current repository snapshot,
> and implementation plan for readiness. Preserve unaffected scope and route
> any blocker without resolving it.
