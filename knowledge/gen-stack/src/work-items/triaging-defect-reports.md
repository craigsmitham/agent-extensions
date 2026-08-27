---
type: Guide
title: Triaging defect reports
description: Use when one or more Defect Reports need an evidence-backed disposition and next route; preserve occurrences and uncertainty while relating, consolidating, splitting, escalating, or routing cases without inventing diagnosis, priority, or corrective authority.
tags: [defect-report, triage, duplicate, overlap, merge, split, classification, routing, severity, priority, investigation, reproduction]
status: draft
sources:
  - id: defect-explainer
    resource: failures-defects-and-defect-reports.md
    title: Failures, defects, and defect reports
  - id: recording-defects
    resource: recording-defect-reports.md
    title: Recording defect reports
  - id: investigating-defects
    resource: investigating-possible-defects.md
    title: Investigating possible defects
  - id: work-item-identity
    resource: maintaining-work-item-identity-relationships-and-lifecycle.md
    title: Maintaining work-item identity, relationships, and lifecycle
  - id: evidence-authority
    resource: preserving-work-item-evidence-and-authority.md
    title: Preserving evidence and authority in software work items
  - id: metadata-labels
    resource: managing-work-item-metadata-and-labels.md
    title: Managing work-item metadata and labels
  - id: process
    resource: ../processes/process.md
    title: Process
generated:
  by: codex/gpt-5.6
  at: 2026-08-27T02:30:57Z
---

# Triaging defect reports

> **Authority:** This Guide applies the canonical meaning in the [Gen Stack
> vocabulary and relationship model](/glossary.md). When it authors a
> profile-governed corpus concept, the [Gen Stack application
> profile](/profile/gen-stack-application-profile.md) owns its required
> representation. This Guide supports action and adds neither semantic authority
> nor profile-conformance rules.

Use this guide when one or more Defect Reports need a current disposition and
an authorized next route. Triage orients the available Signals and evidence; it
does not require the triager to diagnose a Bug, choose a correction, or promise
delivery.

For safe intake before triage, use [Recording defect
reports](recording-defect-reports.md). For the distinction among a failure,
Defect Report, Defect, Bug, Bugfix Specification, and incident, read [Failures,
defects, and defect reports](failures-defects-and-defect-reports.md).

## Goal

Each report leaves triage with a recoverable, evidence-backed disposition and
next route. Material occurrences remain traceable; urgent or restricted cases
reach the right channel; relationship decisions preserve uncertainty; and
classification and impact remain distinct from diagnosis, priority, and
corrective authority. The result names its owner, blocker, and review trigger
so new evidence can revise it without reconstructing lost provenance.

The desired outcome is not an empty queue. It is a queue whose cases are safely
preserved, related, understood to the degree evidence permits, and routed to the
right decision or investigation.

## Representation and shared guidance

Triage results belong in the native systems that own the affected Defect
Reports, occurrences, relationships, evidence references, metadata, and next
routes. Use native fields and relationship types when their semantics match;
add only residual disposition, uncertainty, authority, and provenance. Keep one
canonical owner for each fact and link peer systems; summaries and generated
views are projections, not additional authorities.

This guide owns comparison, disposition, and next-route decisions. Use:

- [evidence and authority](preserving-work-item-evidence-and-authority.md) for
  occurrences, claim states, safe channels, and attribution;
- [identity, relationships, and
  lifecycle](maintaining-work-item-identity-relationships-and-lifecycle.md) for
  duplicate, merge, split, regression, closure, and reopening semantics;
- [metadata and labels](managing-work-item-metadata-and-labels.md) for governed
  workflow state, severity, priority, assignment, and mutation; and
- [titles and summaries](titling-and-summarizing-work-items.md) for clearer
  discriminators.

## Guardrails

- **Preserve before consolidating.** Capture every material occurrence and its
  provenance first.
- **Similarity is orientation evidence, not identity proof.** Shared symptoms,
  components, traces, reporters, or time windows may suggest a relationship;
  they do not by themselves prove a duplicate or common cause.
- **Triage is not diagnosis.** Keep observations, hypotheses, Defects, and Bugs
  distinguishable; relate overlap or suspected common cause without forcing a
  duplicate decision.
- **Reproduction is selective evidence, not a gate.** Attempt it only when a
  bounded result could materially change the disposition and the attempt is
  safe, authorized, and proportionate.
- **Impact is not priority; routing is not corrective authorization.** Mutate
  priority, assignment, timing, or corrective scope only through their
  applicable authority.
- **Unknown is a valid disposition component.** Record the evidence or decision
  needed instead of manufacturing confidence.
- **Respect evidence boundaries.** Keep restricted evidence in an approved
  channel and leave only a safe synopsis and controlled reference elsewhere.

## Triage the reports

### 1. Bind scope, authority, and urgent routes

Identify the reports, time window, product or service boundary, and triage
authority. Determine which decisions the triager may make directly and which
require a product owner, incident commander, security role, domain authority,
maintainer, or other named decision-maker.

Before comparing reports, route current or imminent qualifying operational
impact to an [operational incident record](recording-operational-incidents.md),
possible vulnerabilities to the private security path, restricted evidence to
an approved channel, and material legal, safety, compliance, or data-integrity
concerns to their designated authority.

Keep the Defect Report as provenance when another record coordinates the live
response. Escalation changes the handling route; it does not erase the report
or prove a Bug.

Do not infer that tracker access grants authority to change priority, close a
report, disclose restricted evidence, accept a Requirement, identify a Bug, or
authorize a correction. Apply any standing [Process](../processes/process.md)
without transferring semantic authority to its workflow.

### 2. Preserve occurrences and form candidate groups

Before relating or consolidating anything, preserve every material occurrence,
its source, stable identifier, safe evidence, and provenance. Then recover the
smallest discriminators needed to compare reports:

- the accepted, disputed, inferred, or missing expectation;
- the smallest observable discrepancy;
- affected Surface, behavior, work product, or quality characteristic;
- relevant environment, version or revision, configuration, data shape,
  permissions, timing, workload, and locale;
- occurrence or discovery time, frequency, and known regression window;
- safely retained evidence and stable occurrence identifiers;
- known impact, workaround, and affected or tested-unaffected scope; and
- current claim state: observed, reported, measured, inferred, hypothesized,
  confirmed, or unknown.

Group reports that may describe the same or related observable discrepancy.
Compare symptoms and conditions before presumed cause. A candidate group or
similarity score is an orientation aid, not a duplicate or relationship
decision.

Request missing information only when it can materially change identity,
classification, impact, urgency, or route. Preserve useful incomplete reports;
ideal reproduction steps are not an intake requirement.

### 3. Decide whether selective reproduction would matter

After forming candidate groups, but before final duplicate or relationship
decisions, ask whether one bounded attempt to reproduce the observable
discrepancy could materially change identity or relationship, classification,
affected scope or impact, urgency, or the next route.

Skip reproduction when existing evidence is sufficient, no plausible result
would change the disposition, or the cost, delay, or risk is disproportionate.
Attempt it only within authorized systems, data, revisions, and actions, with
safeguards and a stopping condition. Production mutation, restricted-data
access, security testing, and destructive experiments require separate
authority.

Record whether reproduction was selected and why. When attempting it, apply the
evidence-planning and incremental gathering guidance in [Investigating possible
defects](investigating-possible-defects.md), then record:

- exact revision, conditions, inputs, and environment;
- result: reproduced, not reproduced, inconclusive, or blocked;
- material limitations and untested scope; and
- how the result changed—or did not change—the disposition.

Failure to reproduce is bounded negative evidence. It may weaken a hypothesis
for the tested revision and conditions, but it does not prove that no Defect
exists, that an occurrence did not happen, or that reports are unrelated.
Triage may complete without reproduction when the available evidence supports
a disposition and next route; otherwise defer the identity decision or route a
specific investigation question.

### 4. Decide identity and relationships

Use the narrowest relationship supported by the preserved evidence and any
selective reproduction result.

| Finding | Disposition | Required preservation |
| --- | --- | --- |
| Same observable discrepancy under materially equivalent conditions | Consolidate as a duplicate when the identity decision is authorized | Preserve the occurrence, source, evidence, and bidirectional canonical relationship |
| Related symptoms or context, but identity remains uncertain | Relate the reports; do not mark duplicate | State the suspected relationship, evidence, and uncertainty |
| Partly shared behavior with independently actionable differences | Keep separate and record overlap | Name the shared and distinct scope and any coordination needed |
| One report contains multiple independently triageable discrepancies | Split into distinct reports | Preserve the source report and lineage from each new report |
| A previously corrected behavior recurs | Relate as a possible regression or recurrence | Preserve the new occurrence, affected version, and prior verification boundary |
| Reports may share a cause but describe different observable cases | Relate as suspected common cause | Keep each Defect Report; link a later identified Bug or diagnostic finding |
| Evidence is insufficient to choose | Defer the identity decision | Record the discriminator, evidence, or authority needed to resume |

When consolidating, choose a canonical report for durable reasons such as the
clearest expectation and discrepancy, strongest evidence, safest and most
accessible provenance, established discussion, or required external identity.
Age or identifier order alone is not a sufficient rule. Move no claim or
evidence across confidentiality boundaries merely to make one report complete.

### 5. Classify understanding and assess impact

Record what the evidence supports now, without turning the workflow label into
the conclusion:

| Classification | Evidence boundary |
| --- | --- |
| Awaiting investigation | A discrepancy is preserved; whether or where a Defect exists is unresolved. |
| Confirmed Defect | An accepted expectation and nonconforming work product or behavior are established; cause may remain unknown. |
| Bug hypothesis | Evidence suggests a concrete software cause but does not yet identify it. |
| Identified Bug | A concrete software problem explains one or more reports; link rather than replace their provenance. |
| Expectation disputed or indeterminate | Authority, clarity, completeness, or agreement is insufficient. |
| Expected behavior or candidate change | Behavior conforms to accepted meaning, or different desired state is requested; preserve the Signal and route the change separately. |
| Insufficient safe evidence | Record what is needed and who may provide or decide it. |

If classification depends on reducing uncertainty, create or link a bounded
investigation with an explicit question and completion condition. An
investigation result may update the disposition; it does not silently rewrite
what was originally observed.

For a material Requirement, Surface, C4 structure, Evaluation, or operational
meaning gap, apply [Analyzing Requirement
impact](../control-loop/analyzing-requirement-impact.md) and, when needed, the
[candidate Architecture and Requirements
guide](../architecture/developing-candidate-architecture-and-requirements.md).
Record its evidence, impact, options or candidate correction, recommendation,
authority, and blocking status; do not invent missing meaning to finish triage.
Route an actual candidate Requirement change through a separately authorized
Specification using [Specifying Requirement
changes](specifying-requirement-changes.md).

Summarize who or what is affected, consequence, extent, frequency, duration,
recoverability, workaround, and evidence confidence. Include the scope tested
and known not to be affected when it changes interpretation.

Use this evidence for the local severity model, while keeping priority,
assignment, target date, service commitment, and delivery sequence with their
applicable authorities.

### 6. Select the next authorized route

Choose the smallest next route that can resolve the material uncertainty or
advance an authorized correction:

- gather a specific missing discriminator or safe evidence;
- run a bounded investigation into identity, expectation, cause, scope, or
  impact;
- ask the applicable authority to clarify or accept an expectation;
- coordinate with an active operational incident or security response;
- link one or more Defect Reports to an identified Bug;
- write a [Bugfix Specification](writing-bugfix-specifications.md) when a Bug
  is identified and corrective change is authorized;
- write a [Change Specification](writing-change-specifications.md) for an
  authorized desired-state change that is not a correction of an identified
  Bug;
- retain the report in a named waiting state with a review trigger; or
- close or reject it only when the applicable lifecycle authority and evidence
  support that decision.

Record the next action or decision, responsible owner or authority, blocking
condition, and completion or review trigger. Avoid vague outcomes such as
“needs investigation” when the actual question can be named.

### 7. Record and verify the triage decision

Update each affected report with:

- triage date and attributable decision-maker or role;
- disposition and supporting evidence;
- canonical, duplicate, overlap, split, regression, incident response,
  diagnostic activity,
  Bug, or Specification relationships;
- preserved occurrence and provenance references;
- current classification and material uncertainty;
- selective reproduction decision and, when attempted, its conditions,
  revision, result, limitations, and disposition impact;
- impact assessment and any separately governed metadata decision;
- next route, owner or authority, blocker, and review trigger; and
- decision history when the disposition supersedes an earlier conclusion.

Verify that relationships are reciprocal where the host requires both sides,
restricted evidence remains restricted, canonical reports retain access to the
distinct occurrences, and no automation silently changed priority, assignment,
closure, or corrective scope.

## Triage batches without losing item-local decisions

For a large intake, use automation to normalize discriminators, form candidate
groups, find existing relationships, and surface missing evidence. Treat each
group as a candidate, then apply the selective-reproduction decision only where
its result could matter; do not reproduce every report.

Apply urgent-channel checks before bulk consolidation. Then record a distinct
disposition on every report, including those in the same cluster. Preserve
partial success: one unsafe, ambiguous, or blocked item must not invalidate
valid decisions on other reports, and one successful relationship must not be
presented as evidence that the whole batch is resolved.

Measure decision quality and recoverability, not merely queue reduction.
Useful signals include time to urgent routing or an actionable next route,
reversals caused by premature consolidation, unowned cases, and the age of
unresolved identity or authority decisions.

## Completion check

Triage is complete for a report when:

- the report and every material occurrence remain recoverable;
- urgent and restricted handling has been applied where needed;
- the selective-reproduction decision and any bounded result are recoverable
  when they could affect disposition;
- its identity or relationship disposition and evidence basis are explicit;
- its current classification and unknowns are distinguishable;
- material impact and cross-stack gaps are visible;
- the next authorized route, owner or authority, and trigger are recorded; and
- the decision can be revisited without reconstructing lost provenance.

Triage need not wait for reproduction, root cause, a chosen correction,
implementation, verification, closure, or every related report to reach the
same lifecycle state.

## Standing Process considerations

If triage recurs, a standing [Process](../processes/process.md) may own durable
entry criteria, roles, decision authorities, states, escalation channels,
review triggers, and outputs. Keep Defect Report meaning, relationship
semantics, Requirement authority, and corrective authorization in their
canonical owners.
