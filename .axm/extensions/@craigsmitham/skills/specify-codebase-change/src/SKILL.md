---
name: specify-codebase-change
description: Converts an accepted codebase design and supporting current-state evidence into a snapshot-bound functional and technical Change Specification with traceable behaviors, interfaces, invariants, scenarios, and vertical slices. Use when asked to specify, formalize, structure, outline, or make an approved codebase design implementation-ready before planning. Not for discovering requirements, researching current state, choosing a design, writing tasks or estimates, planning implementation, or changing code.
---

# Specify a codebase change

Turn approved design choices into a precise contract that constrains planning.
Elaborate what was accepted; do not make another consequential design decision.

## Inputs and readiness

Require:

- an explicitly accepted design or equivalent record of approved outcomes,
  behavioral choices, technical decisions, constraints, and exclusions; and
- snapshot-bound current-state evidence sufficient to verify the affected
  behavior, ownership, contracts, and implementation boundaries.

Accept these inputs in any caller-supplied format. Do not require another skill
or a particular artifact name. Preserve existing identifiers; assign stable
identifiers when the inputs lack them.

Bind each input and the specification-time evidence to the strongest available
identity: a repository and commit or revision when available, otherwise a named
source, version, and observation time. Never invent unavailable Git provenance.
Capture branch, worktree state, configuration, dependencies, deployment, and
runtime versions only when they materially constrain the specification. Compare
the specification-time identity with the accepted design and supporting evidence
identities only across affected boundaries. Missing provenance blocks only when
it prevents a material claim from being established or drift from being judged.

Set the specification to `Blocked` when:

- the design is not explicitly accepted for the requested scope;
- an unresolved choice would materially affect observable behavior, interfaces,
  state, failure handling, compatibility, operations, or verification;
- relevant drift may invalidate supporting evidence or an accepted decision; or
- the available evidence cannot anchor a material specification claim.

Name the precise missing decision or current-state question. Route a design gap
back to decision-making and an evidence gap back to research; do not fill either
with an assumption. Classify each blocker as `Needs design` or `Needs research`.
Record harmless assumptions only when they are reversible, non-consequential,
and clearly labeled.

## Specification workflow

### 1. Normalize scope and traceability

Identify accepted outcomes (`O<n>`), observable behaviors (`B<n>`), design
decisions (`D<n>`), and contracts or invariants (`C<n>`). Retain caller IDs where
present. Distinguish accepted scope, explicit exclusions, non-goals, and deferred
work. A deferred decision that changes the specification is a blocker, not a
planning note. Give every material implementation-constraining technical rule a
stable `C<n>` identifier, including responsibilities, interfaces, state rules,
failure semantics, and operational constraints. For a behavior-preserving
structural change, keep the preservation rule in a `C<n>` contract and mark
functional coverage `N/A — no observable behavior change`; do not invent a
`B<n>` that merely restates equivalence.

### 2. Specify functional behavior

Create a `B<n>` only for an intentionally changed observable behavior. Describe
preserved behavior within the applicable contract, slice, and verification
obligation rather than presenting preservation as a new behavior.

For every behavior, identify:

- the actor or observer;
- preconditions and triggering event;
- externally observable result and state transition;
- boundary, empty, duplicate, timing, authorization, and failure cases that are
  material to the change;
- compatibility expectations and behavior intentionally left unchanged;
- the accepted source or rationale that authorizes the behavior; and
- the future verification obligation or acceptance criterion that would show
  the implemented behavior satisfies the contract.

Use concrete scenarios when prose could conceal ambiguity. Do not invent product
policy to complete a scenario. Make non-functional outcomes measurable when the
accepted design supplies a threshold or authoritative objective; otherwise keep
the unresolved threshold visible.

### 3. Specify the technical contract

Describe only implementation-constraining structure:

- responsibilities, ownership, and component boundaries;
- end-to-end control and data flow;
- interfaces, signatures, types, schemas, events, and versioning rules;
- state transitions, persistence, invariants, and consistency boundaries;
- validation, authorization, errors, partial failure, retries, idempotency,
  concurrency, cancellation, and resource lifetime where relevant;
- compatibility, data migration, rollout, recovery, and rollback constraints;
  and
- security, privacy, performance, availability, and observability obligations.

Use signature or schema sketches only to define a contract. Do not write
implementation bodies, commands, file-by-file edits, tasks, or estimates.

### 4. Outline vertical slices

Partition the specified change into the smallest coherent slices that produce an
independently observable and reviewable result across the necessary boundaries.
For a behavior-preserving structural change, use an independently reviewable
structural result, mark its observable result `N/A — behavior preserved`, and
make equivalence evidence the checkpoint. For each slice, identify the applicable
behavior and contract IDs it advances, required enabling structure, preserved
behavior, and its verification checkpoint.

Do not force a vertical slice when a migration, compatibility bridge, or other
prerequisite must safely precede observable behavior. State that dependency and
the evidence available at its checkpoint. Avoid horizontal layer outlines that
defer all integration and meaningful verification until the end.

### 5. Pressure-test and obtain acceptance

Trace every accepted outcome and decision through each applicable behavior,
technical contract, slice, and verification obligation. Use `N/A — <reason>`
when a coverage category does not apply; never invent behavior or structure to
fill the matrix. Require every source ID to have sufficient applicable downstream
coverage and every slice to have a verification obligation. Look for
contradictions, unhandled observers, partial failure, concurrency or lifecycle
gaps, migration hazards, untestable requirements, and speculative structure.
Block rather than paper over a gap.

Present the complete specification for explicit acceptance. Use `Draft` until
reviewed, `Accepted` only after approval, and `Blocked` when a material gap
prevents an implementation-constraining specification. Returning a `Draft` for
review or a precise `Blocked` result completes specification authoring; neither
may be handed to planning. Only an explicitly approved `Accepted` specification
may proceed.

## Change Specification

Read `references/change-specification.md` and adapt its shape rather than leaving
empty boilerplate.

Before returning the artifact, confirm that every in-scope accepted decision is
represented, every material claim is supported at the specification-time
identity, the traceability matrix has no unexplained gaps, and no consequential
choice was made implicitly. Before handing it to planning, additionally confirm
that the specification has been explicitly accepted against a recorded identity.
