# Vision template

Use for the future that the business or product that the system serves
pursues, beyond the horizon of its business objectives.

## Type contract

- **VIS-1** The title MUST be "<Business or product> vision".
- **VIS-2** A Vision document MUST include these sections:
  - **Vision**: the future that the business or product pursues, for whom,
    and what will be different for them, in one short paragraph.
- **VIS-3** A Vision MUST NOT state measures, targets, release timing,
  features, or the design of an experience.

## Suggested document

```markdown
---
type: Vision
title: <Business or product> vision
description: <The future pursued, in one sentence>
status: draft
---

# <Business or product> vision

## Vision

<For whom>, <what is true in the future pursued>.

## Illustrations
## Open questions
## Related
```

## Writing guidance

### Vision and business objectives

A vision describes where the business or product is going; business
objectives are the outcomes one system must bring about on the way, with
success indicators that recognize them. A statement that gains a measure or
target is an objective, as the profile's
[ownership tests](../references/profile.md#direction-job-or-business-requirements)
decide. Objective 1 of the rental system, that contractor customers reserve
equipment without calling a depot, is a step toward this vision:

```markdown
Contractors have the equipment their work needs on site when the work needs
it, and never lose a working day to finding, collecting, or returning
equipment.
```

### Statement

- Describe the world as it will be for those the business serves, not what
  the business will build. The vision is not a specification.
- State an approximate horizon, such as five years, when the business has
  agreed one; release timing belongs to work-management records.
- Give the narrative, storyboard, or prototype that conveys the vision in
  `sources`, when the statement comes from it, or under **Illustrations**. A
  positioning statement, such as "For <customer> who <need>, …", is a prompt
  for writing a vision, not the vision.
- Record only a vision that the business has agreed. A vision that is not
  agreed is an open question, as
  [record gaps instead of inventing](../references/profile.md#record-gaps-instead-of-inventing)
  requires.

### Shared visions

When several systems serve one business or product, one corpus holds the
vision and the others link it, as the profile's
[Structure](../references/profile.md#structure) requires.
