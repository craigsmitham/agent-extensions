---
type: Pattern
title: Checklist for recurring omissions
description: When familiar work has recurring omissions, a checklist gives people observable prompts where they act and a way to respond when an item is unmet.
tags: [docs, documentation-pattern, checklist, checklist-design, verification, coordination, human-factors, validation, authoring]
status: draft
sources:
- id: checklist-design-origin
  resource: https://github.com/craigsmitham/agent-extensions/tree/156c3d4346bee6874ab3d356c19446cf6425713b/skills/checklist-design/src
  title: Craig Smitham — Checklist design skill and references, version 0.1.10
- id: nasa-checklists
  resource: https://www.faa.gov/sites/faa.gov/files/2022-11/NASA%20Ames%20Rpt%20CR%20177549%20.pdf
  title: Degani and Wiener — Human Factors of Flight-Deck Checklists
- id: aapm-checklists
  resource: https://aapm.onlinelibrary.wiley.com/doi/10.1002/acm2.13895
  title: Conroy et al. — Development, implementation, use and maintenance of safety checklists
- id: mrc-process
  resource: https://www.bmj.com/content/350/bmj.h1258
  title: Moore et al. — Process evaluation of complex interventions
generated:
  by: codex/gpt-6
  at: '2026-11-21T22:50:25Z'
---

# Checklist for recurring omissions

When known actions, states, or communications are easily missed, **place
concise, observable prompts at the point of work with an explicit use protocol
and response to unmet items**.

A checklist couples its items to how people use them. A checked box records a
response; it does not by itself establish correct execution, sound judgment,
learning, or an effective intervention. The purpose-specific patterns below describe different uses of this design.

## Problem and applicability

People who know how to do the work can still omit an action, overlook a
condition, or fail to communicate it. A bounded prompt can make that omission
visible at a useful moment. The user must be able to recognize the situation,
interpret the item, and act on the result.

Establish the outcome, relevant failure, users and expertise, trigger and
completion condition, environment, medium, available resources, and authority.
Consider interruption, time pressure, and the consequences of delay or false
completion. Scale this brief to the decisions it changes.

Choose a different primary aid when another problem dominates:

| Reader's need | Alternative and possible checklist role |
| --- | --- |
| Complete procedural detail | [Runbook](runbook.md); checklist at entry, pause, or completion points |
| Diagnosis and response selection | [Playbook](playbook.md) or decision tree; branch-local checks |
| Judgment across quality dimensions | Rubric; checklist for evidence or coverage |
| Structured data capture | Form; prompts for omissions or follow-up |
| Deterministic prevention | Automation or an interface constraint; checks for exceptions |
| Substantial instruction and practice | [Tutorial](tutorial.md), worked examples, coaching, or simulation; temporary learning prompts |

An ordinary personal to-do list needs little of this machinery. A maintained
checklist is justified by a recurring omission or coordination problem, not by
the availability of checkbox formatting.

## Choose a design for the likely omission

Select the primary outcome before choosing how users encounter the items:

| Purpose | Pattern |
| --- | --- |
| Carry out known actions without omission | [Execution checklist](execution-checklist.md) |
| Detect incorrect or missing completed work | [Verification checklist](verification-checklist.md) |
| Decide whether conditions permit proceeding | [Readiness checklist](readiness-checklist.md) |
| Make reporting coverage or inspection findings explicit | [Reporting and review checklist](reporting-review-checklist.md) |
| Support practice toward later independence | [Learning checklist](learning-checklist.md) |

For an account of how a prompt changes a handoff, read
[What a checklist changes at the point of work](../explainers/checklist.md).
For item design, interaction, adaptation, and validation, use
[How to design a checklist](../guides/designing-a-checklist.md).
Where purposes conflict, separate the checks so that the person using
each can recognize the decision and the evidence it requires.

## Tradeoffs and failure modes

Prompts can make omissions and handoffs visible, while adding attention and
maintenance costs. Excessive coverage creates irrelevant work; excessive
compression makes interpretation depend on memory. Independence of verification
costs time and coordination. Familiarity can encourage ritual responses.

Challenge a candidate with wrong-aid selection, a missing critical item,
ambiguous wording, impossible actions, interruption, urgent competing work,
and completion without the required state. Consider language and access needs,
hierarchy, incentives, and missing resources. These are design-review scenarios;
imagining them does not establish usability or effectiveness.

## Evidence and maintenance

Degani and Wiener observed how flight crews used normal checklists, including
the method of performing or confirming an action and reporting completion.[^nasa-checklists]
Process evaluation examines implementation and context, both of which matter
when interpreting an intervention’s results.[^mrc-process] The [checklist explainer](../explainers/checklist.md)
examines this distinction using evidence from a field trial. Costs include
maintaining the aid when tools,
roles, or criteria change. Conroy and colleagues treat maintenance and
retirement as part of the lifecycle in their practice setting.[^aapm-checklists]

## Examples and evidence boundary

A publication checklist might prompt an editor to inspect the final rendered
file. A handoff checklist might ask participants to state an unresolved issue
and acknowledge its owner. Both need a trigger and observable response, but
their order, medium, and evidence differ. Neither replaces a full procedure or
establishes the quality of the entire publication or handoff. These are
illustrative designs, not evaluated interventions.

This draft reorganizes the repository's earlier checklist guidance into a
documentation pattern and purpose-specific companions.[^checklist-design-origin]
Its synthesis and examples have not been independently field-validated. The
sources support particular distinctions and concerns, not a universal template.

[^checklist-design-origin]: Craig Smitham — Checklist design skill and references, version 0.1.10.
[^nasa-checklists]: Degani and Wiener — Human Factors of Flight-Deck Checklists.
[^aapm-checklists]: Conroy et al. — Development, implementation, use and maintenance of safety checklists.
[^mrc-process]: Moore et al. — Process evaluation of complex interventions.
