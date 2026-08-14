---
name: workshop-codebase-design
description: Workshops an evidence-grounded functional and technical codebase design, evaluates alternatives for technical feasibility and architectural fit, revalidates material evidence as the codebase drifts, and records explicit human choices in a Codebase Design Record. Use when asked to workshop, discuss, explore, compare alternatives, align on, or decide the behavior, design, or architecture of a codebase change after relevant current behavior is understood through a research report or directly supplied evidence. Not for codebase research, unilateral design generation, specification drafting, implementation planning, coding, code review, or merely documenting a decision already made.
---

# Workshop codebase design

Lead an interactive design session. Help the developer make informed choices;
do not make consequential choices on their behalf.

## Inputs

Require:

- the change intent, including the bug report or feature idea; and
- current-state evidence sufficient to explain the relevant behavior, ownership,
  flows, contracts, constraints, architectural and technical capabilities, and
  uncertainty.

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
question and respond as `Design-time inquiry` directs. When drift pauses design
acceptance, state that later acceptance must record both the exact revalidated
identity and its validation time. If the change has no consequential design
choice, explain why a formal workshop is unnecessary.

## Working agreement

- Discuss one consequential decision at a time and wait for an explicit human
  choice before treating it as accepted.
- Present two or three materially distinct options only when the feasibility
  gate below establishes that they are viable. Use the decision presentation
  contract below for the comparison, recommendation, and choice request.
- Maintain a decision ledger. Use `Proposed`, `Accepted`, `Deferred`,
  `Needs research`, or `Superseded`; a recommendation is never `Accepted` by
  default.
- Give material in-scope outcomes, observable behaviors, consequential
  decisions, and contracts stable identifiers when later artifacts must trace
  them. Preserve identifiers supplied by the caller. Assign an identifier as
  soon as an unresolved decision, behavior, or contract blocks specification;
  do not wait for acceptance. Record whether each unresolved or deferred item
  blocks specification of the accepted scope.
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

## Design-time inquiry

Design generates new current-state questions; answering them is part of the
workshop, not a detour. Three responses exist, and guessing is not one:

- **Look now** when the question is answerable at a boundary the supplied
  evidence already covers, including version-matched primary sources for an
  in-scope dependency, and its answer settles a pending item. Inspect only that
  boundary, stop when the item resolves, and record the evidence on the decision
  it constrains.
- **Mark `Needs research`** when the answer requires tracing a boundary the
  evidence does not cover, a prototype or spike, evaluation of a new dependency,
  or would reframe the agenda rather than resolve one item. State the precise
  question, pause only dependent decisions, and continue with independent items.
- Never infer an unverified current-state fact to keep a decision moving.

Design-time findings inherit the design snapshot identity. Do not open a
research brief, produce a report, restate what the supplied evidence already
answers, or inspect areas no pending decision touches.

## Workshop

### 1. Orient to the design challenge

Design often passes to someone who did not write the issue or do the research,
and a neutral research report deliberately omits intent. Reconstruct the whole
picture before any decision work. Open with one short paragraph carrying the
situation, the problem it causes, and the intended outcome, then expand it:

- **Situation:** what exists today and what is wrong or missing, in the domain's
  terms rather than file names.
- **Aim:** what should become true, for whom, and why it matters now.
- **Outcomes and boundaries:** desired outcomes and how they are observed;
  constraints, non-goals, and already-binding decisions.
- **Crux:** what makes this a design problem rather than a task — the competing
  forces, the boundaries under tension, and the shape of the choices ahead.
- **Evidence and unknowns:** evidence identity, relevant drift, assumptions,
  decision-relevant architecture and capability baseline, and material unknowns.

Make the orientation self-contained, so it stands without the issue or the
research report. Attribute each claim to evidence, stated intent, or a labeled
assumption; never carry a reported cause as fact. Do not name a preferred
mechanism, recommend, or start the agenda here. Scale it to how much the
participants already hold; a confirmed frame needs only a brief restatement.

Ask the developer to confirm or correct the aim, outcomes, and boundaries.
Correcting the issue is expected. Do not build the agenda until the frame holds.

### 2. Build the decision agenda

Derive the agenda from the confirmed outcomes and affected current-state flows:

- **Functional:** identify unresolved observer-visible behavior, policy, state
  transitions, and failure or boundary semantics.
- **Technical:** at each affected boundary, identify choices about responsibility
  and authority, state and invariant enforcement, coordination and failure
  recovery, interfaces and compatibility, or quality and operational constraints.
  Trace each new responsibility from trigger through completion; do not let a
  component's current participation or a candidate mechanism silently assign
  ownership.

Before presenting the first option, establish the decision-relevant architecture
and capability baseline: binding constraints and their authority; established
capabilities, patterns, and extension points; relevant dependency, runtime,
platform, and deployment versions; and material unknowns. Distinguish a binding
rule from a preference or merely available dependency. Capability availability
does not create an obligation, and an established pattern is not bypassed without
an evidenced reason.

Promote a candidate only when viable alternatives have materially different
consequences, risks, reversibility, or cost of later change. If evidence or an
accepted constraint permits only one choice, record the conclusion as an
evidenced `C<n>` contract or invariant with `Constrained` agenda status; do not
manufacture options or present it as a human decision. Use `D<n>` for actual
decision candidates. Order the agenda by dependency. Give each item a
functional, technical, or coupled type and a `Decide now`, `Constrained`,
`Defer`, or `Needs research` status, and record the evidence or forces that
justify that status.

Place every new responsibility explicitly: extend, generalize, or compose an
existing capability, or add a new one. When the evidence identifies a capability
that plausibly carries it, adding a new one is itself a `D<n>` requiring
options, never a silent default. When no candidate exists, record that as a
`Constrained` `C<n>` citing the evidence searched.

### Option feasibility gate

Evaluate every presented or materially considered candidate, not every
imaginable alternative:

- trace a design-level path from trigger through completion and name the
  capabilities it uses, extends, bypasses, replaces, or adds;
- test that path against accepted outcomes and contracts, binding architecture,
  and relevant versioned dependency, runtime, platform, and deployment semantics;
- examine only applicable cross-cutting concerns, such as validation and errors,
  state and consistency, concurrency and cancellation, resource lifetime,
  security, compatibility, observability, and operations; and
- record the evidence, assumptions, prerequisites, and material failure modes.

Classify technical feasibility as `Established`, `Conditional`, `Unverified`,
or `Infeasible`. `Conditional` means named prerequisites are already accepted
and traceable; missing evidence is `Unverified`, not a condition. Separately
classify architectural disposition as `Conforms`, `Exception required`, or
`Violates`. An option can be technically feasible yet architecturally
inadmissible, and a framework-shaped option is not feasible merely because it
sounds idiomatic.

Only `Established` or properly `Conditional` candidates that `Conform`, or whose
exception is explicitly accepted in a dependent decision, are viable. Apply
`Design-time inquiry` to `Unverified` candidates. Record `Infeasible`,
`Violates`, and unresolved `Exception required` candidates as excluded rather
than padding the option set. If alternatives have no material technical
difference, state that with evidence instead of manufacturing analysis.

### 3. Resolve one decision at a time

Use this exact relative order for every `Decide now` interaction. Adapt detail,
but do not move, duplicate, or merge the recommendation into an option:

```markdown
### D<n> — <decision question>
Status: Proposed

Evidence and forces: <current identity, criteria, constraints, affected boundaries>

#### Option A — <neutral name>
- Capability path: ...
- Feasibility: Established | Conditional — conditions
- Architecture: Conforms | Exception required — accepted by D<n>
- Evidence: ...
- Benefits: ...
- Tradeoffs and consequences: ...
- Conditions: ...
- Reversibility: ...

<Repeat the same fields in the same order for every viable option.>

Excluded candidates: <candidate and evidence-based reason; omit when none>
Affected elements: <change classification, observers, behaviors, contracts>

Recommendation: <one option and rationale tied to the stated evidence and forces>

Choose Option A, B, or C; revise the options; defer; or request named evidence.
```

The recommendation appears exactly once, after the complete neutral comparison
and affected-elements analysis. Never mark an option as recommended in its
heading or body, reveal a preference before all viable options appear, or repeat
the recommendation in the choice request. Keep option labels, field order, and
detail parallel enough for fair comparison. Omit a field only when it is
genuinely inapplicable and say why when omission could affect the choice.
For a purely functional decision with no differentiating technical path, state
the shared evidenced technical constraint once under `Evidence and forces`, use
`Shared — no differentiating technical path` for the capability, feasibility,
and architecture fields, and do not manufacture option-specific analysis.

For each `Decide now` item:

1. State the decision as a concrete question and cite the current-state evidence
   and source or snapshot identity that constrain it. When that evidence is
   missing, apply `Design-time inquiry` before presenting options.
2. State the forces that make a technical or coupled choice consequential, its
   affected boundaries or contracts, and the criteria the options must satisfy.
3. Apply the option feasibility gate. Present only viable options with their
   capability path, feasibility and architecture dispositions, supporting
   evidence, tradeoffs, consequences, conditions, and reversibility. Summarize
   materially considered excluded candidates and the evidence-based reason.
4. Classify the affected elements using the change model below.
5. Recommend one option exactly once and explain why it best fits the agreed
   outcomes and constraints.
6. End with an explicit choice or revision request that does not restate the
   recommendation. Record the response and its rationale
   before moving to a dependent decision.

### 4. Model structure and behavior

Use `O<n>` for material outcomes, `B<n>` for observable behaviors, `D<n>` for
consequential decisions, and `C<n>` for material contracts or invariants that
must trace into later artifacts. A `D<n>` status determines whether later
artifacts may rely on it. When an unresolved decision governs a material
observer-visible behavior, assign both the decision and the behavior stable
identifiers; do not let its `D<n>` substitute for the corresponding `B<n>`.

Classify every affected element as:

- **Behavioral:** intentionally changes something an observer can detect.
- **Behavior-preserving structural:** changes organization while preserving all
  relevant observable behavior.
- **Mixed or boundary:** looks structural internally but changes a published
  interface, persisted data, timing, resource use, deployment behavior, or
  another externally meaningful property.

Ask “observable to whom?” Consider users, API or event consumers, stored data
and older versions, operators, security boundaries, and performance or
availability objectives. Extending a shared capability makes its existing
consumers observers; treat that as mixed or boundary unless evidence shows
otherwise. Require evidence for claimed behavioral equivalence;
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

Derive every material end-state rule from an accepted decision, an evidenced
preserved `C<n>` contract or invariant, or a visibly unresolved agenda item. If
a technical choice first appears during synthesis, give it a `D<n>` identifier,
promote it to the agenda with explicit specification impact, and resolve or
defer it rather than silently adding it to the design.

Pressure-test it against the original intent and revalidated current-state
evidence. Look for contradictory decisions, externally visible structural
changes, partial failure, concurrency and lifecycle gaps, migration hazards,
snapshot drift, uncovered acceptance scenarios, re-implementation of capability
the evidence already provides, invalidated feasibility evidence or prerequisites,
unaccepted architecture exceptions, and speculative structure with no present
purpose. Trace every in-scope outcome, behavior, and material
end-state rule to accepted decisions, contracts, preserved constraints, and
design-level verification. Reopen any decision invalidated by the test.

### 6. Obtain design acceptance

Before acceptance, record the current design-time evidence identity and repeat
the scoped drift check if it changed since the last validation. Present the
completed record and ask the developer to accept it or name the remaining
decisions. Keep the record `Discussing` until acceptance is explicit; use
`Blocked` when unresolved evidence prevents progress and `Accepted` only after
approval. Do not accept an in-scope design while a consequential behavior,
contract, technical choice, feasibility condition, or architectural exception
remains unresolved; explicitly exclude genuinely deferred scope. Every accepted
technical path must remain viable against the acceptance snapshot. Name each
unresolved item and state its specification impact explicitly. Acceptance
requires the material snapshot or source identity against
which the design was validated; if it is unavailable, keep the record `Blocked`
rather than inferring provenance from reported prior acceptance. Record that
exact identity and its validation time so later work can detect drift.

## Codebase Design Record

When first creating or finalizing the living record, read
`references/codebase-design-record.md` and adapt its shape to the change; omit
inapplicable sections rather than leaving boilerplate.

Before handoff, confirm that the design brief stands without the issue or the
research report; no accepted decision depends on stale evidence;
material in-scope outcomes, behaviors, decisions, and contracts have stable
identifiers and design-level verification; no material technical rule first
appears in synthesis; every new responsibility has an explicit placement;
design-time findings are recorded on the decisions they constrain;
deferred scope and specification impact are explicit;
each `Constrained` agenda item traces to an evidenced `C<n>` contract or
invariant; paused decisions are `Needs research`; and the acceptance snapshot or
evidence identity is sufficient to detect later material change; every materially
considered option has a feasibility and architecture disposition; and every
accepted path is viable with its conditions and exceptions traceable.
