---
type: Reference
title: Requirements and neighboring artifacts
description: Distinguishes requirements from goals, designs, plans, tests, evidence, and work items.
tags: [requirement, goal, design, use-case, test, evidence, work-item, software-engineering-foundations]
generated: { by: codex/gpt-6, at: 2026-11-11T19:45:59Z }
sources:
- id: prior-composing-with-work-management
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/requirements-engineering/src/adaptation/composing-with-work-management.md
  title: Composing with work management
---

# Requirements and neighboring artifacts

A requirement states an obligation on an obligated subject under identified
conditions. It should not silently absorb the jobs of neighboring artifacts.

| Artifact | Primary question |
| --- | --- |
| Goal or outcome | Why is change valuable? |
| Use case | How can an actor pursue a goal at the boundary, through success and failure paths? |
| Scenario | What happens along one path through that interaction? |
| Requirement | What obligation must hold, for whom or what, and when? |
| Design or decision record | How will the obligation be realized, and why this approach? |
| Work item or plan | What coordinated activity will be performed? |
| Test or assessment | How will a claim be exercised or assessed in a context? |
| Evidence record | What was observed, for which target and revision? |

A requirement may constrain design when a genuine constraint exists, but an
implementation preference is not automatically a requirement. A test may
witness a requirement but does not become its authoritative wording. A work
item may change a requirement but does not own its durable identity unless the
project explicitly designates that host as authoritative.

A [use case](../behavior/use-cases.md) connects product meaning to
observable behavior through an actor's goal and the success and failure paths
at a chosen system boundary. It can expose candidate requirements or express
accepted behavioral requirements. It does not by itself establish the
underlying job, supply a complete set of requirements, determine internal
implementation, or provide evidence that the behavior creates value.

Normative obligations belong in the project's accepted requirements form.
That is an authority policy, not a requirement to translate every use case
into a separate set of sentences: the accepted form may be a use case whose
obligations satisfy the requirement content
contract (optional companion reading: `@craigsmitham/knowledge/requirements-engineering#authoring/requirement-content-contract`). Its identity, authority,
and supporting detail can be maintained through linked records. If project
policy instead requires separate requirement records, those records remain
authoritative and the use case links to them. Keep one normative authority
rather than two independently maintained copies. Cockburn's account explicitly
allows use cases to serve as behavioral requirements; the
[use-case explanation](../behavior/use-cases.md#connections-to-neighboring-concepts)
develops that relationship and its source basis.

## Requirements and work items

A requirement keeps its authority, identity, and decision history independently
of the record coordinating work around it. A work item keeps its lifecycle
independently of the obligation it cites.

- A Defect Report may cite the requirement or intended use against which a
  suspected deficiency was observed.
- A Change may propose, authorize, or coordinate a requirement revision and its
  downstream realization.
- An Operational Incident Record may provide evidence that a requirement,
  assumption, realization, or verification strategy needs review.
- A requirement may link to these records as provenance or change context while
  retaining its own authoritative identity and decision history.

Do not copy the requirement into a work item as a competing authority. Do not
infer that reported behavior is a defect, that a proposed change is approved,
or that delivery changes normative requirement text. A project that coordinates
work through its own native records rather than these portable roles applies
the same semantic boundary to whatever records it has.

The [work-item content contract](../work-items/work-item-content-contract.md)
and requirement content contract (optional companion reading:
`@craigsmitham/knowledge/requirements-engineering#authoring/requirement-content-contract`)
define the respective records. Their shared adaptation rules live in
[Local policy and host representation](../local-policy-and-host-representation.md).

## Continue exploring

- Domain-driven design (optional companion reading: `@craigsmitham/knowledge/architecture-and-design#domain-driven-design`) develops
  the language and models through which domain behavior is understood; the
  model does not confer requirement authority by itself.
- Executable specifications (optional companion reading: `@craigsmitham/knowledge/software-testing#patterns/executable-specifications`)
  explains how selected obligations gain readable examples and executable evidence.
- The [behavior and commitment route](../reading-software-engineering.md#behavior-and-commitment)
  connects these distinctions to actor goals, construction, and validation.
