---
name: assess-codebase-change-readiness
description: Assesses whether a proposed codebase change has sufficient accepted behavior, current-state evidence, technical contracts, implementation planning, and verification obligations to begin implementation. Use when asked whether a change request, case, design, specification, or plan is ready to implement, implementation-ready, or needs a readiness review. Not for discovering requirements, choosing a design, planning, implementing, or verifying completed code.
---

# Assess codebase change readiness

Determine whether implementation can start without making hidden product,
architecture, safety, or operational decisions. Audit the supplied change case;
do not repair it.

## Assessment boundary

Use the accepted change contract as the authority for intended behavior and the
current codebase snapshot as the authority for implementation facts. Treat a
plan as supporting evidence, never as permission to fill a contract gap. Accept
equivalent caller-supplied artifacts; do not require particular document names
or another skill.

Readiness is contextual, not a universal checklist. Apply scrutiny in proportion
to failure impact, irreversibility, exposure, novelty, and uncertainty. Do not
block a small internal change for irrelevant deployment ceremony, and do not
wave through a high-risk migration because every template field is populated.

Never invent a missing outcome, interface semantic, state transition,
compatibility rule, failure policy, security boundary, migration behavior,
rollback boundary, or verification method. Route the gap to the kind of work
that must resolve it.

## Inputs and disposition

Establish:

- the proposed scope, exclusions, stakeholders, and accepted authority;
- the governing outcomes, behaviors, decisions, contracts, and constraints;
- current-state evidence and its repository or named snapshot identity;
- the intended implementation path and objective completion evidence; and
- applicable repository, security, privacy, migration, and operational duties.

Use one overall disposition:

- `Ready` — implementation can proceed without a consequential unresolved
  choice; material risks are controlled or explicitly accepted by an identified
  authority; and every material obligation has a defined, executable verification
  method and an objective description of the evidence implementation must produce.
- `Not Ready` — the assessment boundary is known and a material gap,
  contradiction, unaccepted risk, or invented plan decision is established well
  enough to route for resolution. Use this when a required acceptance,
  current-state fact, contract, or implementation obligation is identifiably
  absent.
- `Blocked` — unavailable authority, provenance, access, or governing evidence
  prevents a defensible judgment of the proposed change's material readiness.
  Name exactly what would establish the assessment boundary or permit judgment.

Do not use `Blocked` merely because a required input is absent when that absence
itself supports a specific `Not Ready` finding. For example, an accessible
contract that omits a material behavior is `Not Ready`; an inaccessible or
unidentifiable governing contract that prevents determining whether the behavior
is defined is `Blocked`.

Classify findings as `Blocker`, `Accepted risk`, or `Advisory`. An accepted risk
must name the accepting authority, rationale, and affected scope. Do not use
“ready with caveats” to hide a blocker.

## Workflow

### 1. Bind scope, authority, and snapshots

Identify what is proposed, what is accepted, and which artifacts govern when
they disagree. Bind current-state claims to the strongest supplied identity and
observation time. Check relevant drift across code, configuration, dependencies,
schemas, deployment, and runtime evidence. Never invent Git provenance.

### 2. Test whether the right change is defined

Check that outcomes and success measures are explicit, scope and exclusions are
coherent, affected people and systems are represented, and requirements are
correct, complete, consistent, feasible, unambiguous, traceable, and verifiable.
Cover nominal, off-nominal, and adverse scenarios in proportion to risk.

### 3. Test whether the change is technically constrained

Check relevant ownership, interfaces, state and data transitions, failure and
concurrency semantics, authorization and trust boundaries, compatibility,
migration, observability, rollout, recovery, and rollback. Verify material
implementation anchors against the current snapshot. Surface contradictions
between accepted artifacts instead of choosing one silently.

### 4. Test whether implementation and verification are executable

Confirm that work can proceed in coherent increments with known dependencies,
safe stopping points, preserved behavior, and objective completion evidence.
Trace every material obligation to planned work and a verification method.
Require both requirement-conformance checks and vulnerability or failure-mode
discovery where risk warrants them. A test name alone is not evidence that the
required behavior is testable.

Classify coverage as `Covered`, `Gap`, `Accepted risk`, or `Not applicable`.
An `Accepted risk` must retain its named authority, rationale, and scope; it does
not convert a missing contract or verification method into coverage.

### 5. Route gaps without resolving them

For each blocker, name the affected scope, evidence, consequence, and smallest
next action using one or more routes:

- `Needs acceptance` — authority or risk acceptance is absent;
- `Needs research` — a material current-state fact is unknown;
- `Needs design` — intended behavior or a consequential technical choice is
  unsettled;
- `Needs specification` — an accepted choice is not expressed as a precise,
  traceable, verifiable contract; or
- `Needs planning` — accepted scope lacks an executable path, dependency, safe
  transition, or completion evidence.

Do not rewrite the source artifacts, produce missing designs or tasks, estimate
delivery, or implement fixes.

## Readiness Assessment

Read `references/readiness-assessment.md` and adapt its shape. Preserve stable
source identifiers. Cite evidence precisely enough that another reviewer can
reproduce each finding, and distinguish observed facts from declarations and
inferences.

Set `Ready` only when all material scope is accepted, current evidence supports
the intended path, traceability is complete, required verification is
executable, and no implementation step must decide consequential behavior.
