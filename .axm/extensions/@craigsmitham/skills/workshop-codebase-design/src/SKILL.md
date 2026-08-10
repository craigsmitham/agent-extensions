---
name: workshop-codebase-design
description: Workshops an evidence-grounded functional and technical codebase design from change intent and current-state evidence, revalidates material evidence as the codebase drifts, surfaces consequential decisions, and records explicit human choices in a Codebase Design Record. Use when asked to workshop, discuss, explore, align on, or decide the behavior, design, or architecture of a codebase change after relevant current behavior is understood through a research report or directly supplied evidence. Not for codebase research, unilateral design generation, specification drafting, implementation planning, coding, code review, or merely documenting a decision already made.
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

Accept either a snapshot-bound research report or direct evidence supplied by
the caller or inspected for this workshop. Bind evidence to the strongest
available identity: a repository and commit or revision when available,
otherwise a named source and observation time. Capture branch, worktree state,
configuration, dependencies, deployment, or runtime versions only when they
could constrain a decision. Never invent unavailable provenance; mark it
`Unknown` only when its absence is material.

At workshop entry, distinguish the evidence snapshot from the design snapshot
when possible. If a live repository or revision history is available, compare
them with a scoped check of affected boundaries. If it is not, state the
evidence limit and proceed when the supplied evidence is sufficient. Record the
basis for classifying encountered drift as irrelevant. If drift or missing
provenance may invalidate material evidence, state the precise current-state
question, mark only dependent decisions `Needs research`, and pause them. Do not
broaden into general codebase research or guess. If the change has no
consequential design choice, explain why a formal workshop is unnecessary.

## Working agreement

- Discuss one consequential decision at a time and wait for an explicit human
  choice before treating it as accepted.
- Present two or three materially distinct, viable options when alternatives
  exist. Include an explicit recommendation, its rationale, tradeoffs,
  consequences, and reversibility.
- Maintain a decision ledger. Use `Proposed`, `Accepted`, `Deferred`,
  `Needs research`, or `Superseded`; a recommendation is never `Accepted` by
  default.
- Give material in-scope outcomes, observable behaviors, accepted decisions, and
  contracts stable identifiers when later artifacts must trace them. Preserve
  identifiers supplied by the caller. Assign an identifier as soon as an
  unresolved behavior or contract blocks specification; do not wait for it to
  be accepted. Record whether each unresolved or deferred item blocks
  specification of the accepted scope.
- Before resolving each consequential decision, confirm that its constraining
  evidence still applies to the current design-time evidence identity. Recheck
  only affected evidence when that identity changes during the workshop.
- Stay at design level. Do not produce code, commands, tasks, file-by-file steps,
  estimates, or an implementation plan. If the caller also requests those
  outputs, defer them to a separate workflow after design acceptance; do not
  promise to produce them as part of this workshop.
- If the caller supplies an output path or an explicit repository convention,
  update one living record after each accepted decision. Otherwise maintain the
  ledger in the conversation and return the complete record at the end. Do not
  invent a durable documentation location or commit anything.

## Workshop

### 1. Confirm the frame

Summarize the evidence timeline, relevant drift, current state, desired outcomes,
constraints, non-goals, known decisions, assumptions, and material unknowns. Ask
the developer to confirm or correct this frame before resolving design choices.

### 2. Build the decision agenda

Identify only decisions that materially affect responsibilities, behavior,
contracts, state, boundaries, failure handling, compatibility, operations, or
the cost of later change. Order them by dependency and label each `Decide now`,
`Constrained`, `Defer`, or `Needs research`.

### 3. Resolve one decision at a time

For each `Decide now` item:

1. State the decision as a concrete question and cite the current-state evidence
   and source or snapshot identity that constrain it.
2. Present viable options with their fit, tradeoffs, consequences, and
   reversibility. Exclude an option only for a stated constraint or invariant.
3. Classify the affected elements using the change model below.
4. Recommend one option and explain why it best fits the agreed outcomes and
   constraints.
5. Ask for an explicit choice or revision. Record the response and its rationale
   before moving to a dependent decision.

### 4. Model structure and behavior

Use `O<n>` for material outcomes, `B<n>` for observable behaviors, `D<n>` for
accepted decisions, and `C<n>` for material contracts or invariants that must
trace into later artifacts.

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

For each behavioral or mixed element, record the observer, preconditions and
trigger, externally visible result and state transition, behavior preserved, and
material boundary or failure scenarios. Tie each scenario to design-level
verification. Treat a missing product policy as a decision, not an assumption.

Record ordering only when order itself changes observable behavior, migration
safety, compatibility, or recoverability. Express it as a design constraint for
later specification and planning; do not create increments, review boundaries,
tasks, or implementation sequencing.

### 5. Synthesize and pressure-test

After the dependent decisions are accepted, describe the proposed end state:
responsibilities and boundaries, control and data flow, interfaces and
contracts, state and invariants, failure behavior, compatibility and migration,
security, performance, operations, and design-level verification.

Pressure-test it against the original intent and revalidated current-state
evidence. Look for contradictory decisions, externally visible structural
changes, partial failure, concurrency and lifecycle gaps, migration hazards,
snapshot drift, uncovered acceptance scenarios, and speculative structure with
no present purpose. Trace every in-scope outcome and behavior to accepted
decisions, contracts, and design-level verification. Reopen any decision
invalidated by the test.

### 6. Obtain design acceptance

Before acceptance, record the current design-time evidence identity and repeat
the scoped drift check if it changed since the last validation. Present the
completed record and ask the developer to accept it or name the remaining
decisions. Keep the record `Discussing` until acceptance is explicit; use
`Blocked` when unresolved evidence prevents progress and `Accepted` only after
approval. Do not accept an in-scope design while a consequential behavior,
contract, or technical choice remains unresolved; explicitly exclude genuinely
deferred scope. Acceptance requires the material snapshot or source identity
against which the design was validated; if it is unavailable, keep the record
`Blocked` rather than inferring provenance from reported prior acceptance.
Record that exact identity so later work can detect drift.

## Codebase Design Record

When first creating or finalizing the living record, read
`references/codebase-design-record.md` and adapt its shape to the change; omit
inapplicable sections rather than leaving boilerplate.

Before handoff, confirm that no accepted decision depends on stale evidence;
material in-scope outcomes, behaviors, decisions, and contracts have stable
identifiers and design-level verification; deferred scope and specification
impact are explicit; paused decisions are `Needs research`; and the acceptance
snapshot or evidence identity is sufficient to detect later material change.
