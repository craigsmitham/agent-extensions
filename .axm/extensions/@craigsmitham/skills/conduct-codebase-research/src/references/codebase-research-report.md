# Codebase Research Report shape

Use this shape selectively. Omit sections and fields that do not apply; never
leave empty boilerplate.

```markdown
# Codebase Research Report: <topic>

## Snapshot
- Repository: ...
- Branch and commit: ...
- Worktree state: ...
- Researched at: ...
- Relevant configuration, dependencies, deployment, or runtime: ...

## Chronology and Drift
| Stage | Time | Snapshot or environment | Evidence status |
| --- | --- | --- | --- |
| Observation or incident | ... | ... | Known, Partial, or Unknown |
| Source report | ... | ... | Known, Partial, or Unknown |
| Brief and anchor verification | ... | ... | Known, Partial, or Unknown |
| Research | ... | ... | Verified |

<Relevant intervening changes, their impact on questions or findings, and any drift that could not be assessed.>

## Current-State Technical Map
<Concise end-to-end explanation of relevant components and boundaries.>

## Existing Capabilities
<What already carries responsibility of this kind, without assessing fit. State explicitly when a search found none.>

| Capability | Location | What it does today | Extension points | Constraints and coupling | Consumers |
| --- | --- | --- | --- | --- | --- |

## Question Status
| Question | Status | Evidence |
| --- | --- | --- |
| Q1 | Answered, Partial, Unanswered, or Blocked | <key references> |

## Findings by Question

### Q1 — <label>
**Answer:** ...
**Evidence:** ...
**Inference:** ... <!-- only when needed -->

## Contracts and Invariants
<Relevant interfaces, schemas, state rules, compatibility constraints, and ownership.>

## Tests and Observability
<Existing tests, logs, metrics, traces, and what they establish.>

## Historical Context
<Only history needed to explain current state.>

## Contradictions and Open Questions
<Conflicting sources, missing evidence, and remaining uncertainty.>

## Evidence Index
<Paths, symbols, permalinks, commands, and primary external sources.>
```
