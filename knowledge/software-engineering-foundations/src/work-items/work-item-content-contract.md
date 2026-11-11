---
type: Reference
title: Work-item content contract
description: Defines the semantic content, title and summary conventions, technical context, and bounded verification claims of portable work items.
tags: [work-item, content-contract, template, scope, evidence, completion, verification, next-action, software-engineering-foundations]
generated: { by: codex/gpt-6, at: 2026-11-11T19:45:59Z }
sources:
- id: prior-titling-and-summarizing-work-items
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/software-engineering-foundations/src/work-items/titling-and-summarizing-work-items.md
  title: Titling and summarizing work items
- id: prior-preserving-technical-context
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/software-engineering-foundations/src/work-items/preserving-technical-context.md
  title: Preserving technical context
- id: prior-defining-verification
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/software-engineering-foundations/src/work-items/defining-verification.md
  title: Defining work-item verification
---

# Work-item content contract

Every portable work item composes four layers over the roles defined in the
[Software work-item taxonomy](software-work-item-taxonomy.md).

```text
common contract → role-specific contract → repository considerations
                → native host representation
```

The layers govern meaning, not mandatory Markdown. Use an exact native field
when it carries the same semantics; use body content only for residual meaning.

## Common semantic slots

| Slot | Include when | Content |
| --- | --- | --- |
| Identity and role | Always | Stable host identity when persisted; Operational Incident Record, Defect Report, or Change role |
| Classification | Established and decision-relevant | Such as Bugfix, maintenance, migration, or another local classification; never infer from a label alone |
| Title and summary | Always for a persisted item | A derived brief consistent with the current body |
| Sources and evidence | Material input exists | Originating occurrences, requests, observations, findings, links, conditions, availability, and limitations |
| Context or motivation | Always | Why the item exists and which situation it concerns |
| Scope and exclusions | A bounded response or case is needed | Included and intentionally excluded outcomes, systems, users, or conditions |
| Constraints and risks | Material | Binding limits, invariants, compatibility conditions, uncertainty, consequences, and residual risk |
| Relationships | Material peers exist | Explicit direction and meaning for dependencies, duplicates, remediation, follow-up, or source evidence |
| Decisions and open questions | A choice has been made or remains | Decision, authority, rationale, state, and the exact unresolved question |
| Completion conditions | A next boundary is being defined | Observable conditions for handoff, disposition, delivery, or closure |
| Verification | A claim needs evidence | Conditions, strategy, bounded result, revision, environment, and observation window |
| Ownership and next action | Active coordination is needed | Who acts, who decides when different, the next authorized action, and any blocker |

## Application rules

- Omit an inapplicable slot instead of printing an empty heading or `N/A`.
- Write **unknown** when a material value is not established and **unavailable**
  when expected evidence cannot be accessed or recovered.
- Keep observations, reports, hypotheses, decisions, plans, and results
  distinguishable.
- Link peer specifications, designs, decisions, tests, and runbooks rather than
  copying them into competing authorities.
- Preserve supplied technical context proportionately, even when it is not yet
  accepted or selected.
- Do not infer priority, assignment, approval, verification, or closure from a
  host status, label, implementation, or absence of objections.
- Put the current reader's most time-sensitive information first. Operational
  Incident Records therefore lead with current state; other roles usually lead
  with the derived brief and case meaning.

Role templates are complete fallbacks for hosts without suitable structured
fields. They apply this contract directly and add only role-specific meaning.

## Title and summary

The title identifies the affected behavior, artifact, service, or bounded
outcome and its distinguishing condition or result. Useful prompts are:

- Defect Report: `<subject> <observed result> when <condition>`
- Change: `<verb> <bounded outcome>`
- Operational Incident Record: `<affected service or capability> <current impact>`

These are prompts, not mandatory grammar. Avoid leading with a tracker label,
priority, team, or mechanism unless it is the enduring subject. The summary
uses one or two sentences to explain the case and current boundary before a
proposed response. Neither brief adds cause, priority, decisions, or results
absent from the record; both remain consistent when the case changes.

## Technical context and verification

Preserve material constraints, findings, alternatives, decisions, test strategy,
risks, and open questions with their source and applicable revision or
conditions. Proposed, recommended, selected, rejected, and superseded are
meaningfully different states. A polished proposal does not authorize work.

Short case-specific context belongs in the record. Stable peer artifacts retain
their detail; transient or restricted sources need a compact attributed synopsis
through an appropriate evidence channel.

Completion conditions state what must be observably true. An evidence strategy
states how to assess it, including limitations. A result records what a bounded
execution or observation established: method, target revision, environment,
inputs, observation window, outcome, and uncertainty. Planned testing is not a
result, and a pass does not generalize to another revision or context. Unknown
or unavailable evidence is not a pass. Local authority determines sufficiency
for closure, with residual risk and follow-up visible; see
[Work-item lifecycle and completion](managing-lifecycle-and-completion.md).

## Local representation

[Local policy and host representation](../local-policy-and-host-representation.md)
owns the shared rules for local obligations, native fields, and derived views.
This contract supplies the work-item semantics that representation must retain.

## Relation to the requirement contract

This contract governs work items. The obligation a Change carries or a Defect
Report cites has its own slots in the requirement content
contract (optional companion reading: `@craigsmitham/knowledge/requirements-engineering#authoring/requirement-content-contract`).
Link the requirement rather than copying its text into a slot here, and read
[Requirements and neighboring
artifacts](../requirements/requirements-and-neighboring-artifacts.md)
when it is unclear which of the two owns a fact.
