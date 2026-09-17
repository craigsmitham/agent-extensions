# Business Requirements template

Use for the business case of the system: the problem or opportunity it
addresses, the outcomes it must bring about, and its scope.

## Type contract

- **BIZ-1** The title MUST be "<System> business requirements".
- **BIZ-2** A Business Requirements document MUST include these sections:
  - **Problem or opportunity**: whose need is unmet and the current gap, with
    any known evidence for it, without selecting a solution.
  - **Business objectives**: the business outcomes the system must bring
    about, stated as outcomes rather than outputs, each under its own heading
    `Objective <n>`.
  - **Success indicators** *(optional)*: how the achievement of each
    objective will be recognized, with its target and timeframe.
  - **Stakeholders** *(optional)*: the stakeholders, what they value, and any
    authority they hold over the system.
  - **Scope**: what is in scope and what is explicitly out of scope.
- **BIZ-3** Each success indicator MUST name, with a link, the objective it
  indicates.

## Suggested document

```markdown
---
type: Business Requirements
title: <System> business requirements
description: <The opportunity, objectives, and scope that justify the system, in one sentence>
---

# <System> business requirements

## Problem or opportunity
## Business objectives
### Objective 1
## Success indicators
## Stakeholders
## Scope
### In scope
### Out of scope
## Open questions
## Related
```

## Writing guidance

### Problem or opportunity

Give the background and why now, the audience and the need that is unmet,
the current gap, and any evidence of demand that is known. Link each
[job to be done](job-to-be-done.md) that is unmet rather than restating it. This is the need that the
system addresses now; why the business exists is its [mission](mission.md),
as the profile's
[ownership tests](../references/profile.md#direction-job-or-business-requirements)
decide.

### Business objectives

Head each objective with its number alone, so that its anchor stays stable
when the wording changes, and state the outcome below the heading. Other
documents link to it by anchor, such as `business.md#objective-1`, so its
number stays with the objective, and a number that other documents link to is
never reused for a different objective.

```markdown
### Objective 1

Contractor customers reserve equipment without calling a depot.
```

### Success indicators

For each objective, state the success indicator, its target, and timeframe,
and link to indicator or KPI definitions where they exist. Outcomes of use,
such as user effectiveness or satisfaction, are success indicators too. A
target that is not decided is an open question, not a plausible number:

```markdown
- [Objective 1](#objective-1): at least 60% of reservations are made online
  within 12 months of launch.
- [Objective 2](#objective-2): the share of rentals returned late; the target
  is an open question.
```

### Scope and stakeholders

- **Scope** links the major capabilities and names exclusions a reader might
  otherwise assume are included. It links the concepts it includes, such as
  features and user classes, rather than describing them.
- **Stakeholders** names sponsors, insurers, regulators, and others with an
  interest in the system, as
  [users and stakeholders](user-class.md#users-and-stakeholders) tells them
  apart from user classes.
- **Related** links records such as business strategy, roadmaps, and
  research when readers need them, and the records that hold
  initiative priorities and constraints, assumptions and dependencies, and
  risks, which this version does not define.
