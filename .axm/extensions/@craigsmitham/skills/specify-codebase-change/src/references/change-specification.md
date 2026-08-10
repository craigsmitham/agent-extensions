# Codebase Change Specification shape

Use this shape selectively. Omit sections and fields that do not apply; never
leave empty boilerplate.

```markdown
# Codebase Change Specification: <change>

Status: Draft | Accepted | Blocked
Blocker type: Needs design | Needs research <only when Blocked>

## Inputs, Snapshots, and Drift
- Accepted design: <source, accepted scope, approver, strongest available identity, and time>
- Current-state evidence: <source, strongest available identity, material versions, and limitations>
- Specification-time evidence: <repository and revision, or named source, version, and observation time; add other material environment identity>
- Relevant drift: <evidence and effect; unknowns remain explicit>

## Scope and Identifiers
| ID | Kind | Accepted statement | Source |
| --- | --- | --- | --- |
| O1 | Outcome | ... | ... |

## Functional Contract
### B1 — <observable behavior>
- Observer: ...
- Preconditions and trigger: ...
- Result and state transition: ...
- Boundary and failure scenarios: ...
- Behavior preserved: ...
- Accepted source or rationale: ...
- Verification obligation: ...

## Technical Contract
### C1 — <responsibility or flow contract>
...
### Interfaces and Data
| ID | Interface, type, schema, or event | Contract | Compatibility |
| --- | --- | --- | --- |
### State and Invariants
| ID | State or invariant | Rule | Enforcement boundary |
| --- | --- | --- | --- |
### Failure, Concurrency, and Lifecycle
...
### Migration, Operations, and Quality Attributes
...

## Vertical Slice Outline
### S1 — <independently reviewable result>
- Covers: <O/B/D/C IDs>
- Observable result: <result, or N/A — behavior preserved>
- Enabling structure: ...
- Preserved behavior: ...
- Verification checkpoint: ...
- Depends on: ...

## Traceability
| Source ID | Functional coverage | Technical coverage | Slice | Verification obligation |
| --- | --- | --- | --- | --- |
| ... | <IDs or N/A — reason> | <IDs or N/A — reason> | <IDs or N/A — reason> | ... |

## Risks, Assumptions, and Blockers
...

## Specification Review and Acceptance
<For Draft: review requested and unresolved review questions. For Accepted: approver, accepted scope, accepted-against identity and time, and exclusions. For Blocked: blocker type, exact missing decision or evidence, and responsible next workflow.>
```
