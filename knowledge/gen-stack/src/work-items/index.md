# Software work items

Tool-neutral concepts and authoring guides for work items that preserve an
operational event, an observed discrepancy, or a bounded system or
Architecture change. Use the explainers to choose and understand the artifact;
use the guides to write one and preserve existing context in a tracker such as
Linear, GitHub, Jira, or Azure Boards.

For the standing model of work that can coordinate several items and item
types, see [Process](../processes/process.md) and [Defining a
Process](../processes/defining-a-process.md). A work item preserves one case; it does not
become the Process merely because a tracker supplies states or automation.

## Titles and summaries

Applies to every type below.

- [Work item titles and summaries](work-item-titles-and-summaries.md) - Why a work item's title and summary form a derived brief that serves the reading surfaces where items are scanned rather than opened, and why restating that brief changes nothing else about the item.
- [Titling and summarizing work items](titling-and-summarizing-work-items.md) - Use when a work item must be recognizable in lists and search or its meaning has changed; write or re-derive its title and short summary without changing anything else.

## Existing design and delivery context

Applies when source material already contains technical investigation, design,
planning, or testing detail.

- [Preserving design and delivery context in software work items](preserving-design-and-delivery-context.md) - Use when supplied design or delivery context must survive transfer into a software work item; retain findings, constraints, decisions, sketches, plans, testing strategies, tradeoffs, and open questions without inventing or approving missing work.

When the technical response still needs to be developed rather than merely
preserved, use [Developing a Change
Design](../design/developing-a-change-design.md). The conversation may lead
directly to implementation or to a proportional work-item section; it does not
require a standalone Design document.

A work item may act as a Change Specification or, for an authorized correction
of an identified Bug, a Bugfix Specification when it composes the
representations needed for that bounded change. A Defect report never becomes
the Bugfix by retitling or maturation. The
[Specification vocabulary](../glossary.md#specifications) defines this as a
composition role: Requirements, Architecture, Change Design, verification
context, and delivery state retain their distinct meanings and authorities.

Every material item also receives a proportional
[Requirement-impact analysis](../control-loop/analyzing-requirement-impact.md). That
cross-cutting guide owns the desired-state, Architecture, and Evaluation
classifications rather than repeating them in each work-item type.

## Operational incidents

- [Operational incident records](operational-incident-records.md) - How operational impact, service state, response state, and understanding evolve independently; how one incident identity coordinates several response surfaces; and why impact end, restoration, recovery, closure, and follow-up remain distinct.
- [Recording operational incidents](recording-operational-incidents.md) - Use when a live operational disruption needs coordinated, attributable recording; maintain impact evidence, command roles, objectives, actions, communication, chronology, handoffs, exit criteria, closure validation, and independently owned follow-up.

## Software defects and bugfixes

- [Failures, defects, and defect reports](failures-defects-and-defect-reports.md) - How observations and anomalies become classified defect reports; how failures, defects, incidents, corrections, verification, and closure differ; and why tracker labels do not prove diagnosis.
- [Recording defect reports](recording-defect-reports.md) - Use when a suspected discrepancy needs an attributable, evidence-bearing record; preserve its source and expectation, add proportional evidence, and maintain classification, resolution, relationships, and verification without inventing diagnosis or priority.
- [Bugs and bugfix specifications](bugs-and-bugfix-specifications.md) - How investigation can identify a concrete Bug from one or more Defect reports, why the reports remain separate provenance, and how a Bugfix Specification drives an authorized corrective change.
- [Writing bugfix specifications](writing-bugfix-specifications.md) - Use when investigation has identified a Bug and an authorized corrective change needs a separate delivery-driving Specification; link its Defect reports, bound the correction, develop the Change Design, and define verification without losing Provenance.

## System and Architecture changes

- [Change specifications and delivery work](change-specifications-and-delivery-work.md) - How bounded Change Specifications compose source context, authority, Requirements, Architecture, Change Design, verification, and delivery without taking over their meanings or lifecycles.
- [Writing change specifications](writing-change-specifications.md) - Use when a proposed or authorized system or Architecture change is bounded enough to coordinate; preserve its sources and authority, analyze Requirements and Architecture impact, develop proportional Change Design, and define verification and delivery without inventing acceptance.
