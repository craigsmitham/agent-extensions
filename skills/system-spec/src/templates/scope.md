# Scope template

Use for the business area under consideration, and what the system includes
and excludes within it.

## Type contract

- **SCP-1** The title MUST be "<System> scope".
- **SCP-2** A Scope document MUST include these sections:
  - **Business area** *(optional)*: the business activities and parties under
    consideration, and nearby ones that are not, whatever system supports
    them.
  - **In scope**: what the system takes on, linking the subsystems and major
    features that carry it.
  - **Out of scope**: what the system does not take on that a reader might
    assume it does, and who or what handles each exclusion when that is
    known.
- **SCP-3** **Business area** MUST NOT name the system, its features, or any
  technology.
- **SCP-4** **In scope** SHOULD NOT list or describe what the linked
  documents and folder indexes already state.

## Suggested document

```markdown
---
type: Scope
title: <System> scope
description: <What the system takes on, and what it leaves out, in one sentence>
---

# <System> scope

## Business area
## In scope
## Out of scope
## Open questions
## Related
```

## Writing guidance

### Business area and system scope

Scope has two layers. The **Business area** is the part of the business the
specification is concerned with, described as activities and parties, as it
would be if no system existed. **In scope** and **Out of scope** then say which
of that work the system takes on. Separating them shows what the system
leaves to people, other systems, or the business's policy, and makes each
exclusion a decision rather than an omission.

~~~markdown
## Business area

Renting construction equipment from depots to contractors: finding,
reserving, handing over, returning, and charging for equipment, and
maintaining the fleet. Buying and selling equipment are outside it.

## In scope

The rental system takes on finding, reserving, handing over, returning, and
charging for equipment through its features, and maintaining the fleet
through the [Fleet maintenance](<link>) subsystem.

## Out of scope

- Processing card payments, which the [Payment service](<link>) handles.
~~~

### Scope, boundary, and coverage

- The System's **Boundary and context** names the parties the system interacts
  with; scope says what work the system does for the business.
- A feature's **Coverage** says what one capability covers; scope says what
  the system as a whole takes on.
- An exclusion that the system must enforce, such as refusing a kind of
  rental, is a Requirement, not scope.
- What a release will include is work management and belongs to planning
  records, as the profile's
  [work management rule](../references/profile.md#work-management-and-design)
  states.
