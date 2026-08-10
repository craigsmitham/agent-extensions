---
name: workshop-codebase-design
description: Workshops an evidence-grounded software design from change intent and current-state evidence, surfaces consequential decisions, presents viable options and tradeoffs, records explicit human choices, and produces a Codebase Design Record. Use when asked to workshop, discuss, explore, align on, or decide the design or architecture of a codebase change after relevant current behavior is understood. Not for codebase research, unilateral design generation, implementation planning, coding, code review, or merely documenting a decision already made.
---

# Workshop codebase design

Lead an interactive design session. Help the developer make informed choices;
do not make consequential choices on their behalf.

## Inputs

Require:

- the change intent, including the bug report or feature idea; and
- current-state evidence sufficient to explain the relevant behavior, ownership,
  flows, contracts, constraints, and uncertainty.

Also use any supplied outcomes, non-goals, constraints, candidate ideas, prior
decisions, decision participants, or output path. Keep facts, intent,
assumptions, and candidate solutions distinct.

If a critical fact is missing, state the precise research question and pause the
affected decision. Do not broaden into general codebase research or guess. If
the change has no consequential design choice, explain why a formal workshop is
unnecessary.

## Working agreement

- Discuss one consequential decision at a time and wait for an explicit human
  choice before treating it as accepted.
- Present two or three materially distinct, viable options when alternatives
  exist. Include an explicit recommendation, its rationale, tradeoffs,
  consequences, and reversibility.
- Maintain a decision ledger. Use `Proposed`, `Accepted`, `Deferred`,
  `Needs research`, or `Superseded`; a recommendation is never `Accepted` by
  default.
- Stay at design level. Do not produce code, commands, tasks, file-by-file steps,
  estimates, or an implementation plan.
- If the caller supplies an output path or an explicit repository convention,
  update one living record after each accepted decision. Otherwise maintain the
  ledger in the conversation and return the complete record at the end. Do not
  invent a durable documentation location or commit anything.

## Workshop

### 1. Confirm the frame

Summarize the current state, desired outcomes, constraints, non-goals, known
decisions, assumptions, and material unknowns. Ask the developer to confirm or
correct this frame before resolving design choices.

### 2. Build the decision agenda

Identify only decisions that materially affect responsibilities, behavior,
contracts, state, boundaries, failure handling, compatibility, operations, or
the cost of later change. Order them by dependency and label each `Decide now`,
`Constrained`, `Defer`, or `Needs research`.

### 3. Resolve one decision at a time

For each `Decide now` item:

1. State the decision as a concrete question and cite the current-state evidence
   that constrains it.
2. Present viable options with their fit, tradeoffs, consequences, and
   reversibility. Exclude an option only for a stated constraint or invariant.
3. Classify the affected elements using the change model below.
4. Recommend one option and explain why it best fits the agreed outcomes and
   constraints.
5. Ask for an explicit choice or revision. Record the response and its rationale
   before moving to a dependent decision.

### 4. Model structure and behavior

Classify every affected element as:

- **Behavioral:** intentionally changes something an observer can detect.
- **Behavior-preserving structural:** changes organization while preserving all
  relevant observable behavior.
- **Mixed or boundary:** looks structural internally but changes a published
  interface, persisted data, timing, resource use, deployment behavior, or
  another externally meaningful property.

Ask “observable to whom?” Consider users, API or event consumers, stored data
and older versions, operators, security boundaries, and performance or
availability objectives. Require evidence for claimed behavioral equivalence;
do not assume a refactor is harmless or reversible.

For each affected element, explicitly choose `Structure first`, `Behavior
first`, `Alternate pure increments`, `Structure after`, or `No structural
work`. Prefer reviewable increments that keep structural and behavioral changes
distinguishable, but do not assume tidying first is always safest.

### 5. Synthesize and pressure-test

After the dependent decisions are accepted, describe the proposed end state:
responsibilities and boundaries, control and data flow, interfaces and
contracts, state and invariants, failure behavior, compatibility and migration,
security, performance, operations, and design-level verification.

Pressure-test it against the original intent and current-state evidence. Look
for contradictory decisions, externally visible structural changes, partial
failure, concurrency and lifecycle gaps, migration hazards, and speculative
structure with no present purpose. Reopen any decision invalidated by the test.

### 6. Obtain design acceptance

Present the completed record and ask the developer to accept it or name the
remaining decisions. Keep the record `Discussing` until acceptance is explicit;
use `Blocked` when unresolved evidence prevents progress and `Accepted` only
after approval.

## Codebase Design Record

Use this shape, adapting it rather than leaving empty boilerplate:

```markdown
# Codebase Design Record: <change>

Status: Discussing | Accepted | Blocked

## Inputs and Snapshot
<Change intent, evidence sources, repository snapshot, and freshness caveats.>

## Current State
<Relevant behavior, structure, flows, contracts, and uncertainty.>

## Desired Outcomes
<Outcomes, constraints, and non-goals.>

## Change Model
### Behavioral Changes
| Element | Current behavior | Desired behavior | Observer | Verification |
### Behavior-Preserving Structural Changes
| Element | Structural change | Behavior preserved | Purpose | Equivalence evidence |
### Mixed or Boundary Changes
| Element | Structural aspect | Observable effect | Affected observer |
### Sequencing
<Chosen sequence per element and review boundaries.>

## Proposed End State
<Responsibilities, flows, interfaces, state, and failure behavior.>

## Decision Log
### D1 — <decision>
- Status: Proposed | Accepted | Deferred | Needs research | Superseded
- Change kind: Behavioral | Structural | Mixed
- Context and evidence: ...
- Options considered: ...
- Decision: ...
- Rationale and consequences: ...
- Revisit when: ...

## Interfaces and Invariants
<Contracts and rules the design must preserve or establish.>

## Compatibility, Migration, and Operations
<Rollout, persisted data, version interaction, observability, and recovery.>

## Risks and Open Questions
<Unresolved evidence, deferred decisions, and explicit risks.>

## Design Acceptance
<Approver, accepted scope, and unresolved exclusions.>
```
