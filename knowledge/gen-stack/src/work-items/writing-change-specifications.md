---
type: Guide
title: Writing change specifications
description: Use when a proposed or authorized system or Architecture change is bounded enough to coordinate; preserve its sources and authority, analyze Requirements and Architecture impact, develop proportional Change Design, and define verification and delivery without inventing acceptance.
tags: [change-specification, system-change, architecture-change, change-design, requirement-impact, verification, delivery, work-item-template]
status: draft
sources:
  - id: change-specification-explainer
    resource: change-specifications-and-delivery-work.md
    title: Change specifications and delivery work
  - id: gen-stack-vocabulary
    resource: ../glossary.md
    title: Gen Stack vocabulary and relationship model
  - id: change-design-guide
    resource: ../design/developing-a-change-design.md
    title: Developing a Change Design
  - id: requirement-impact
    resource: ../control-loop/analyzing-requirement-impact.md
    title: Analyzing Requirement impact
  - id: preserving-context
    resource: preserving-design-and-delivery-context.md
    title: Preserving design and delivery context in software work items
generated:
  by: codex/gpt-5.6
  at: 2026-08-26T16:30:00Z
---

# Writing change specifications

Use this guide when a proposed or authorized change to the System or its
Architecture has a recognizable boundary and needs a durable composition for
decision, design, delivery, or verification. For the semantic boundary, read
[Change specifications and delivery work](change-specifications-and-delivery-work.md).

## Goal

Implementers and reviewers can recover why the change exists, its current
authority, which Requirements and Architecture constrain it, how the response
is designed, how evidence will be gathered, and what remains unresolved—without
turning the work item into a second authority for those constituents.

## Preconditions

- The candidate change is bounded enough to state an affected context, intended
  outcome, current decision state, and material exclusions.
- Originating Signals, source records, or authority links can be preserved or
  explicitly marked unavailable.
- The work item will not be mistaken for automatic acceptance of a Requirement,
  Architecture change, Design, priority, or delivery commitment.

If only an unbounded desire is known, retain the Signal or source record and
continue Orientation. If only uncertainty reduction has been authorized, use
an investigation. If a Bug has been identified and correction authorized, use
[Writing bugfix specifications](writing-bugfix-specifications.md).

## 1. Create one bounded change identity

Create a work item or other explicit Specification container whose identity
names the intended change outcome rather than a presumed file, implementation
mechanism, or source record.

One Change Specification may coordinate several tasks, and one broad change
may require several Specifications with independent delivery, rollback, or
verification. Choose the smallest identity that can move through decision and
delivery coherently.

Do not retitle an Incident Record, Defect Report, source request, or
investigation into the Change Specification. Link those artifacts so each
retains its own evidence and lifecycle.

## 2. Preserve source context and Provenance

Inventory every material initiating source before synthesis. Record its source
type, stable identifier and authoritative link, observation or request time,
relevant context, and a direct statement or faithful synopsis when available.
Mark whether supplied claims are observed, reported, inferred, hypothesized,
proposed, recommended, accepted, or rejected.

Keep source wording separate from normalized analysis. Do not attribute an
inferred need, generalized demand, or selected response to someone who only
suggested one mechanism.

For a public work item, never copy personal information, private customer
content, credentials, confidential commercial data, or restricted evidence.
Use a safe synopsis and an access-controlled source link when the provenance
itself is not public.

## 3. State the current condition and intended change

Describe:

- the affected System, Architecture subject, workflow, actor, or operating
  context;
- what exists or is difficult today, with evidence and uncertainty;
- the bounded outcome or condition intended to change;
- why the change matters; and
- what is deliberately outside the change.

Use outcome language that survives alternative implementations. Retain a
requested mechanism as source context or a proposed solution unless it is an
accepted constraint or Design choice.

## 4. Record decision state and authority

State the current decision explicitly:

- proposed and awaiting a named decision;
- authorized for Design, delivery, or another bounded next action;
- deferred or declined;
- implemented but not yet verified;
- verified within stated evidence limits; or
- superseded by a linked change.

Identify who or what has authority for the recorded decision. Priority,
ownership, target release, and delivery timing are separate decisions; record
them only when the applicable authority has made them.

A detailed Specification does not authorize itself. If authority is missing or
disputed, preserve that gap and the exact decision needed rather than advancing
the item silently.

## 5. Analyze Requirement impact

Apply [Analyzing Requirement impact](../control-loop/analyzing-requirement-impact.md)
proportionately. Classify whether the change:

- is constrained by unchanged accepted Requirements;
- proposes a candidate new obligation;
- proposes revision or retirement of an accepted Requirement;
- changes only Implementation while desired state remains unchanged;
- exposes an evidence or interpretation gap; or
- remains unresolved because the relevant authority is missing or disputed.

Link canonical Requirement IDs. Do not copy an accepted `shall` statement into
the work item as another normative authority. A proposed verification condition
or test may repeat the predicate as a distinct witness without becoming the
Requirement.

## 6. Analyze Architecture impact

Identify affected responsibilities, boundaries, relationships, decisions, and
eligible Requirement subjects from accepted Architecture. Distinguish:

- working within unchanged Architecture;
- a proposed Architecture change awaiting acceptance;
- an accepted Architecture or ADR change that constrains this work; and
- an unresolved Architecture gap whose owner must decide.

Do not select an Architecture subject from current code location or invent a
durable boundary merely to make the work item look complete. Link the canonical
Architecture concepts and ADRs when they exist.

## 7. Bound constraints, invariants, and non-goals

Record only material legal, policy, compatibility, accessibility, performance,
security, privacy, safety, operational, data, and integration constraints.
Preserve invariants and conservation obligations that the change must not
violate. Label unverified constraints as reported or assumed.

State non-goals when they prevent predictable scope expansion. Do not add every
conceivable edge case or speculative future capability.

## 8. Develop proportional Change Design

Use [Developing a Change Design](../design/developing-a-change-design.md) when
the response contains consequential ambiguity. Capture the smallest material
set of:

- affected responsibilities and interactions;
- state, data, interfaces, and failure behavior;
- quality, security, compatibility, migration, rollout, and rollback concerns;
- alternatives and tradeoffs;
- selected response and its maturity; and
- unresolved questions that can still change implementation.

The Change Design may live in the work item or in a linked authoritative
discussion. Accepted durable choices that need an independent lifecycle remain
ADRs. Preserve supplied sketches, sequences, and tradeoffs without upgrading
their authority; see [Preserving design and delivery context in software work
items](preserving-design-and-delivery-context.md).

## 9. Define verification conditions

State observable conditions that would show the realized change satisfies the
applicable Requirements, Architecture, constraints, and intended outcome. Add
representative positive, negative, boundary, compatibility, migration, and
operational conditions only when they are material.

Keep these distinct:

- an **outcome signal** indicates whether the motivating condition improved;
- a **verification condition** states what the realized change must
  demonstrate; and
- a **testing or Evaluation strategy** states how evidence will be gathered.

Do not define success only as completing tasks, merging code, or deploying.

## 10. Describe the Evaluation or testing strategy

Identify the evidence needed across applicable unit, integration, contract,
system, migration, operational, security, or human review levels. Link existing
Evaluation Definitions and name any that need creation, correction, rerun, or
reinterpretation.

Keep expected future evidence separate from Evaluation Results that already
exist. A proposed test is not proof, and a passing bounded execution does not
establish broader fitness than its inputs, environment, and oracle support.

## 11. Plan delivery and recovery proportionately

Record the implementation sequence, dependencies, decomposition, rollout,
observability, rollback, ownership, and handoffs needed for the current
planning horizon. Link child tasks instead of copying their volatile status
into the Specification.

Preserve recovery conditions for destructive, stateful, compatibility-sensitive,
or difficult-to-reverse work. Do not manufacture estimates, assignments,
priority, or release commitments.

## 12. Preserve risks, unknowns, and relationships

List consequential unknowns, what could resolve each one, and who or what owns
the needed decision or evidence. Record residual risks and accepted exceptions
only when an applicable authority has done so.

Link related Signals, Incidents, Defect Reports, Specifications, Requirements,
Architecture, ADRs, tasks, Implementation revisions, and Evaluation evidence.
Preserve many-to-many relationships rather than forcing a parent-child shape.

## 13. Derive the title and summary last

Title the bounded change outcome and discriminating context, for example:

> Preserve policy ownership while replacing generic contribution markers

Avoid `Implement request #482`, a presumed code location, or a mechanism that
does not define the accepted boundary. Put source identifiers and relationships
in structured fields or links.

The summary should state the current condition, intended change, decision
state, and why the response matters. Do not put material scope or authority
only in the brief; see [Titling and summarizing work
items](titling-and-summarizing-work-items.md).

## Tracker-ready template

Use only the sections supported by the change. Omit empty headings rather than
inventing content.

```markdown
# <Bounded change outcome> <discriminating context>

## Summary

What condition should change, what bounded outcome is proposed or authorized,
what is its current decision state, and why does it matter?

## Source context and Provenance

- Signals or source records:
- Stable identifiers and authoritative links:
- Faithful source synopsis:
- Evidence, confidence, and material unavailable context:

## Change decision

- Current decision and maturity:
- Decision authority or unresolved authority:
- Priority, ownership, and timing only when separately established:

## Scope

- Affected context and current condition:
- Intended change outcome:
- Constraints and invariants:
- Non-goals:

## Requirement impact

- Applicable Requirement IDs:
- Classification: unchanged constraint | candidate obligation | proposed
  revision or retirement | implementation-only | evidence or interpretation
  gap | unresolved
- Required authority or follow-up:

## Architecture impact

- Affected Architecture and ADRs:
- Unchanged, proposed, accepted, or unresolved impact:

## Change Design

- Status and authority:
- Selected response:
- Material alternatives and tradeoffs:
- State, data, interfaces, failure behavior, migration, and recovery as needed:
- Open design questions:

## Verification

- Outcome signals:
- Verification conditions:
- Evaluation or testing strategy:
- Existing evidence and limitations:

## Delivery and recovery

- Implementation sequence and dependencies:
- Linked tasks:
- Rollout, observability, rollback, and handoffs:

## Risks and unresolved questions

- Risk or question:
- Owner or decision authority:
- Evidence or action needed:

## Relationships and lifecycle

- Related work items and authorities:
- Current host state:
- Next authorized action or review:
```

## Final check

- The item represents one bounded system or Architecture change.
- Source evidence remains attributable and distinct from normalized analysis.
- Decision, Requirements, Architecture, Design, delivery, and evidence states
  are visible rather than conflated.
- Canonical authorities are linked instead of copied into competing normative
  statements.
- Verification conditions and evidence strategy remain distinct.
- Existing technical and delivery context has not been lost or silently
  approved.
- Unknowns, non-goals, recovery, and the next authorized action are explicit
  where material.
- The title and summary are derived from the authoritative body.
