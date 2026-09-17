# Vision template

Use for the future that the system's business pursues, beyond the horizon of
the system's objectives, whether that business is a whole enterprise or
product or sits within an enclosing business.

## Type contract

- **VIS-1** The title MUST be "<Business> vision".
- **VIS-2** A Vision document MUST include these sections:
  - **Vision**: the future that the business pursues, for whom,
    and what will be different for them, in one short paragraph.
- **VIS-3** A Vision MUST NOT state indicators, targets, release timing,
  features, or the design of an experience.

## Suggested document

```markdown
---
type: Vision
title: <Business> vision
description: <The future pursued, in one sentence>
---

# <Business> vision

## Vision

<For whom>, <what is true in the future pursued>.

## Open questions
## Related
```

## Writing guidance

### Vision and objectives

A vision describes where the business is going;
[objectives](objectives.md) are the results one system must bring about on the
way, with indicators that recognize them. A statement that gains an indicator
or target is an objective, as the profile's
[ownership tests](../references/profile.md#direction-job-opportunity-objectives-or-scope)
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
- State an approximate horizon, such as five years, when one is stated; release timing belongs to work-management records.
- Give the narrative, storyboard, or prototype that conveys the vision in
  `sources`, when the statement comes from it. A
  positioning statement, such as "For <customer> who <need>, …", is a prompt
  for writing a vision, not the vision.
- Write only a vision that a person or a source states. Do not compose one
  from what the system does; when none is stated, leave the vision
  unwritten.

### Shared and enclosing visions

When several systems serve one business, one corpus holds the vision and the
others link it. A business within an enclosing business links the enclosing
vision and can state its own: the future it pursues for those it serves,
without restating or contradicting the enclosing vision, as the profile's
[Structure](../references/profile.md#structure) requires.
