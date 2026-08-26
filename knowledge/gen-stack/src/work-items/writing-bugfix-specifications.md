---
type: Guide
title: Writing bugfix specifications
description: Use when investigation has identified a Bug and an authorized corrective change needs a separate delivery-driving Specification; link its Defect reports, bound the correction, develop the Change Design, and define verification without losing Provenance.
tags: [bugfix, bugfix-specification, corrective-change, bug, defect-report, change-design, requirements-impact, verification, delivery, work-item-template]
status: draft
sources:
  - id: bugfix-explainer
    resource: bugs-and-bugfix-specifications.md
    title: Bugs and bugfix specifications
  - id: change-specification-guide
    resource: writing-change-specifications.md
    title: Writing change specifications
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
  at: 2026-08-26T16:11:30Z
---

# Writing bugfix specifications

Use this guide when investigation has identified concrete defective behavior
or a defective condition in the realized system and an authorized decision has
selected corrective change. Create a Bugfix Specification as a separate work
item or other explicit Specification container; never retitle the originating
Defect report.

For the conceptual boundary and relationship cardinalities, read
[Bugs and bugfix specifications](bugs-and-bugfix-specifications.md). If the
observation or cause is still uncertain, continue with
[Recording defect reports](recording-defect-reports.md) or a bounded
investigation instead.

A Bugfix Specification specializes a [Change
Specification](writing-change-specifications.md). Apply the general source,
authority, Requirements, Architecture, Change Design, verification, delivery,
and relationship guidance here, then add the Bug-specific provenance,
corrective-decision, unchanged-expectation, and regression requirements below.

## Goal

Implementers and reviewers can recover which Bug is being corrected, which
evidence and authority justify the change, which Requirements and Architecture
constrain it, how the response is designed and delivered, and what evidence
will verify it—without turning the Bugfix into a second Defect report or
rewriting the originating Signal.

## Preconditions

- At least one linked Defect report preserves the originating Signal,
  evidence, and investigation.
- Investigation has identified a concrete Bug rather than only a suspected
  discrepancy or an unlocalized Failure.
- The applicable authority has selected corrective change rather than only
  further investigation, deferment, compensation, or accepted risk.
- Restricted evidence remains in an approved location and can be referenced
  safely.

## 1. Create a separate Bugfix identity

Create a new work item or other explicit Specification container. Link every
material Defect report and preserve the host's relationship to incidents,
occurrences, regressions, and related Bugs.

Do not copy the reports wholesale. Include a concise synopsis sufficient to
orient the corrective work, then point to the reports for source evidence,
chronology, reporter context, and investigation history. Never close, retitle,
or replace a report merely because the Bugfix exists.

## 2. State the identified Bug

Describe the smallest concrete defective behavior or system condition that the
investigation established:

> Invoice export excludes zero-value lines when tax detail is present because
> the export filter treats zero as absent.

Name the affected behavior, triggering conditions, and established scope.
Distinguish confirmed findings from remaining hypotheses. Link the evidence
and diagnosis in the Defect report rather than restating their full history.

If the work concerns only a defective Requirement, Architecture representation,
test, or document and no concrete system Bug has been identified, use the
applicable [Change Specification](writing-change-specifications.md) instead of
calling it a Bugfix Specification.

## 3. Record the corrective decision and authority

State which decision selected corrective change, who or what had authority,
and which outcomes remain possible. Record priority, target, ownership, or
delivery timing only when already decided by the applicable authority.

Identifying a Bug does not itself authorize implementation. Keep the decision
to correct separate from the diagnosis and from the later evidence that the
correction worked.

## 4. Establish the expectation and intended correction

Link the accepted Requirement, specification, invariant, contract, or other
authority that the realized system should satisfy. State current defective
behavior and intended corrected behavior separately.

Do not silently create desired state inside the Bugfix Specification. When no
accepted expectation can determine the corrected behavior, preserve the gap
and obtain the applicable Requirement or Architecture decision before treating
the response as authorized.

## 5. Analyze Requirement and Architecture impact

Apply [Analyzing Requirement impact](../control-loop/analyzing-requirement-impact.md)
proportionately. Classify whether the Bugfix:

- restores Implementation satisfaction of unchanged Requirements and
  Architecture;
- exposes a defective or missing Requirement;
- proposes a Requirement or Architecture change that needs separate
  acceptance;
- requires an Evaluation correction or reinterpretation; or
- remains unresolved because the relevant authority is missing or disputed.

Link canonical Requirements and Architecture subjects. Do not copy a binding
obligation into the Bugfix as a second normative authority.

## 6. Bound scope, constraints, and non-goals

State affected behavior, actors, data, interfaces, components, environments,
and versions only as far as they shape the correction. Preserve unchanged
constraints and invariants that the Bugfix must conserve. Name explicit
non-goals when they prevent the correction from becoming an opportunistic
feature or unrelated refactor.

If an adjacent tidy makes the correction safer or more legible, apply the
[Tidy First pattern](../patterns/tidy-first.md) deliberately and keep the
behavior-preserving tidy distinguishable from the Bugfix behavior change.

## 7. Develop the proportional Change Design

Use [Developing a Change Design](../design/developing-a-change-design.md) for
the technical response. Capture only the choices needed to resolve present
ambiguity, such as:

- affected responsibilities, interactions, and boundaries;
- state, data, interface, and failure behavior;
- compatibility, migration, rollout, and rollback;
- alternatives and consequential tradeoffs;
- operational and security risks; and
- unresolved questions that can still change implementation.

The Change Design may live in the Bugfix work item or in a linked authoritative
design discussion. Accepted durable architecture choices retain an independent
Architecture Decision Record when their lifecycle requires one.

## 8. Define verification conditions

State observable conditions that would show the correction satisfies the
applicable expectation. Include the original failing or static case and
material adjacent, negative, boundary, and regression cases.

Do not define success as “the proposed code was merged.” Verification should
remain valid if another implementation satisfies the same obligations and
constraints.

## 9. Describe the Evaluation or testing strategy

Explain how evidence will be gathered across the necessary levels,
environments, fixtures, data, integration boundaries, and operational checks.
Link existing Evaluation Definitions and identify any that need creation,
correction, rerun, or reinterpretation.

Keep verification conditions distinct from the strategy used to gather
evidence. Keep expected future evidence distinct from Evaluation Results that
actually exist.

## 10. Plan delivery and recovery proportionately

Record the authorized implementation sequence, dependencies, decomposition,
rollout, observability, rollback, and ownership needed for the current planning
horizon. Link child delivery tasks rather than forcing every execution detail
into the Specification.

One Bugfix Specification may address several Bugs, and one Bug may require
several Bugfixes with independent delivery or rollback. Preserve these links
instead of assuming a one-to-one parent-child shape.

## 11. Derive the title and summary last

Title the corrected behavior and discriminating condition rather than the
reporter's wording, a presumed file, or the implementation mechanism:

> Preserve zero-value invoice lines when tax detail is exported

A linked Defect report may remain titled `Invoice export omits zero-value lines
when tax details are included`. These titles coexist: the report names the
observed discrepancy, while the Bugfix names the authorized corrected outcome.
Never obtain the Bugfix title by retitling the report.

Avoid `Fix defect report #482`, the report's title copied unchanged, a presumed
code location, or an implementation mechanism that does not define the
accepted boundary. Put Defect-report identifiers and relationships in links or
structured fields, and omit a `Bugfix` prefix when the surrounding surface
already shows the type.

The summary should name the established Bug, the bounded authorized
correction, and why the response matters. Do not put evidence, scope, or
authority only in the brief; see
[Titling and summarizing work items](titling-and-summarizing-work-items.md).

## Tracker-ready template

Use the smallest sections that make the authorized correction implementable
and reviewable. Omit unsupported sections rather than inventing content.

```markdown
# <Corrected behavior> when <condition>

## Summary

What Bug is being corrected, what bounded outcome should change, and why does
that matter?

## Bug and provenance

- Identified Bug:
- Defect reports:
- Related incidents, occurrences, or regressions:
- Confirmed scope and remaining uncertainty:

## Corrective decision

- Decision and authority:
- Rationale:
- Priority, target, or owner when already decided:

## Expected and corrected behavior

- Applicable Requirements or other expectation:
- Current defective behavior or condition:
- Intended corrected behavior:

## Requirement and Architecture impact

- Impact classification:
- Applicable Requirements:
- Affected Architecture and decisions:
- Candidate authority changes requiring acceptance:

## Scope and constraints

- Affected scope:
- Unchanged constraints and invariants:
- Non-goals:

## Change Design

Material choices, responsibilities, interactions, state and data behavior,
failure handling, alternatives, tradeoffs, risks, and open questions.

## Verification

### Verification conditions

Observable conditions that establish the correction and material regressions.

### Evaluation or testing strategy

How, where, and with which identified Evaluation Definitions the evidence will
be gathered.

## Delivery and recovery

- Implementation sequence and dependencies:
- Child delivery work:
- Rollout and observability:
- Rollback or recovery:
- Residual risk:
```

## Final check

- The Bugfix has a separate identity; no Defect report was retitled or
  replaced.
- Every material Defect report remains linked as Provenance.
- A concrete Bug and an authorized corrective decision are both present.
- Diagnosis, correction authority, and verification evidence remain distinct.
- Current and corrected behavior have an accepted basis or a visible authority
  gap.
- Requirement and Architecture impact is explicit without creating a second
  normative authority.
- Scope, unchanged constraints, and non-goals prevent accidental feature work.
- Change Design is proportional and consequential unknowns remain open.
- Verification conditions are behavioral; the Evaluation or testing strategy
  explains how evidence will be gathered.
- Delivery, rollout, rollback, and residual risk are proportional to the
  change.
- Relationship cardinalities are preserved rather than forced into one report,
  one Bug, and one Bugfix.
