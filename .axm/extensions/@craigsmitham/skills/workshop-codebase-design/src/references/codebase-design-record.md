# Codebase Design Record shape

Use this shape selectively. Omit sections and fields that do not apply; never
leave empty boilerplate.

```markdown
# Codebase Design Record: <change>

Status: Discussing | Accepted | Blocked

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

## Desired Outcomes
| ID | Outcome, constraint, or non-goal | Observer | Verification |
| --- | --- | --- | --- |

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
<Responsibilities, flows, interfaces, state, and failure behavior.>

## Decision Log
### D1 — <decision>
- Status: Proposed | Accepted | Deferred | Needs research | Superseded
- Change kind: Behavioral | Structural | Mixed
- Context, evidence, and supporting identity: ...
- Options considered: ...
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
validation time, and unresolved exclusions.>

Specification readiness: Ready | Blocked — unresolved decisions or evidence
```
