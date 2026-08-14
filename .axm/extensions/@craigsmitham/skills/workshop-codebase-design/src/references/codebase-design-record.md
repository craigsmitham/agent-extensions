# Codebase Design Record shape

Use this shape selectively. Omit sections and fields that do not apply; never
leave empty boilerplate.

```markdown
# Codebase Design Record: <change>

Status: Discussing | Accepted | Blocked

## Design Brief
<Self-contained orientation for a reader who did not write the issue or do the
research. Omit nothing material; add nothing that belongs below.>

<One short paragraph, two to four sentences: the situation, the problem it
causes, and the intended outcome. Summarize only what this brief and the
outcomes below establish; name no preferred mechanism.>

- Situation: <what exists today and what is wrong or missing>
- Aim: <what should become true, for whom, and why it matters now>
- Crux: <competing forces, boundaries under tension, and the shape of the
  choices ahead; no preferred mechanism>

## Inputs, Evidence, and Drift
- Change intent: <source and relevant times when known>
- Evidence mode: Snapshot-bound research report | Direct current-state evidence
- Current-state evidence: <sources, observation or research time, and strongest
  available repository revision or source identity>
- Design snapshot: <validation time and material repository, configuration,
  dependency, deployment, or runtime identity available at design time>
- Evidence limits: <material unavailable provenance; omit if none>
- Relevant drift: <encountered changes, scoped basis, and impact>

## Current State
<Relevant behavior, structure, flows, contracts, and uncertainty.>

## Architecture and Capability Baseline
<Include only decision-relevant entries. Distinguish binding constraints,
established patterns, and available capabilities.>

| Kind | Capability or constraint | Evidence and authority | Version or environment | Design implication |
| --- | --- | --- | --- | --- |

## Desired Outcomes
| ID | Outcome, constraint, or non-goal | Observer | Verification |
| --- | --- | --- | --- |

## Decision Agenda
| ID | Decision question or constraint | Type | Status | Depends on | Basis or why consequential |
| --- | --- | --- | --- | --- | --- |

Use `D<n>` for decision candidates. Use `C<n>` for evidence-determined
`Constrained` items and carry the same identifier into Interfaces and
Invariants; do not log those items as accepted human decisions.

## Functional Behavior and Acceptance Scenarios
### B1 — <observable behavior>
- Observer: ...
- Preconditions and trigger: ...
- Result and state transition: ...
- Boundary and failure scenarios: ...
- Behavior preserved: ...
- Design-level verification: ...

## Change Model
### Behavioral Changes
| ID | Element | Current behavior | Desired behavior | Observer | Verification |
| --- | --- | --- | --- | --- | --- |

### Behavior-Preserving Structural Changes
| ID | Element | Structural change | Behavior preserved | Purpose | Equivalence evidence |
| --- | --- | --- | --- | --- | --- |

### Mixed or Boundary Changes
| ID | Element | Structural aspect | Observable effect | Affected observer |
| --- | --- | --- | --- | --- |

### Delivery Constraints
<Only ordering or rollout constraints that affect behavior, migration safety,
compatibility, or recoverability.>

## Proposed End State
<Responsibilities, flows, interfaces, state, and failure behavior. Trace each
material rule to an accepted decision, evidenced preserved `C<n>` constraint, or
unresolved agenda item.>

## Decision Log
### D1 — <decision>
- Status: Proposed | Accepted | Deferred | Needs research | Superseded
- Decision type: Functional | Technical | Coupled
- Change kind: Behavioral | Structural | Mixed
- Context, evidence, and supporting identity: ...
- Forces and constraints: ...
- Affected boundaries or contracts: ...

| Option or excluded candidate | Capability path | Feasibility | Architecture | Evidence | Conditions, consequences, or exclusion reason |
| --- | --- | --- | --- | --- | --- |
| ... | Uses, extends, bypasses, replaces, or adds ... | Established, Conditional, Unverified, or Infeasible | Conforms, Exception required, or Violates | ... | ... |

- Recommendation: <one proposed option and rationale; omit after acceptance only when it adds no historical value>
- Decision: ...
- Rationale and consequences: ...
- Revisit when: ...
- Specification impact: Non-blocking | Blocks specification — reason

## Interfaces and Invariants
| ID | Interface, invariant, or rule | Preserve or establish | Verification |
| --- | --- | --- | --- |

## Compatibility, Migration, and Operations
<Rollout, persisted data, version interaction, observability, and recovery.>

## Risks and Open Questions
<Unresolved evidence, deferred decisions, and explicit risks.>

## Design Acceptance
<Approver, accepted scope, accepted-against snapshot or evidence identity,
validation time, confirmation that accepted technical paths remain viable,
traceable feasibility conditions or architecture exceptions, and unresolved
exclusions.>

Specification readiness: Ready | Blocked — unresolved decisions or evidence
```
