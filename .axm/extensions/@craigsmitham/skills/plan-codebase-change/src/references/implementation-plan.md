# Implementation Plan shape

Use this shape selectively. Omit sections and fields that do not apply; never
leave empty boilerplate.

```markdown
# Implementation Plan: <change>

Status: Draft | Ready | Blocked
Blocker type: Needs acceptance | Needs research | Needs redesign <only when Blocked; list all that apply>

## Inputs, Snapshots, and Drift
- Accepted specification: <source, acceptance, scope, snapshot, and time>
- Planning snapshot: <strongest available identity and time; add only material branch, worktree, configuration, dependency, deployment, and runtime details>
- Relevant drift: <evidence and effect; unknowns remain explicit>

## Delivery Strategy
<Slice order, structural/behavioral sequencing, safe stopping points, and why.>

## Work Graph
| ID | Slice/result | Depends on | Safe parallel work | Checkpoint |
| --- | --- | --- | --- | --- |

## Work Items
### P1 — <independently reviewable result>
- Covers: <O/B/D/C/S IDs>
- Observable result: ...
- Change surfaces: <verified paths, symbols, contracts, tests, and operations>
- Implementation actions: ...
- Behavior preserved: ...
- Verification and completion evidence: ...
- Migration, rollout, recovery, or rollback: ...
- Depends on / enables: ...

## Cross-Cutting and Final Verification
...

## Traceability
| Specification ID or repository obligation | Work items | Completion evidence |
| --- | --- | --- |

## Handoff Notes
<Execution boundaries, optional work, blockers, and safe restart points.>
```
