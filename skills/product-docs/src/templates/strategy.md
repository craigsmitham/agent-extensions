# Strategy template

Use for the stand taken to overcome the challenge that most limits progress
toward the system's objectives now: where effort concentrates, what is set
aside, and when the strategy is revisited.

## Type contract

- **STG-1** The title MUST be "<System> strategy".
- **STG-2** A Strategy document MUST include these sections:
  - **Challenge**: what most limits progress toward the objectives now, and
    the evidence or insight behind that judgment.
  - **Approach**: the few areas where effort concentrates to overcome the
    challenge, and why each.
  - **Not now**: what is deliberately set aside that a reader might expect to
    be pursued.
  - **Revisit**: the date or event at which the strategy is reconsidered.
- **STG-3** **Challenge** MUST link each objective, job to be done, or the
  opportunity whose progress the challenge limits.
- **STG-4** A Strategy MUST NOT state actions, initiatives, features, key
  results, targets, estimates, budgets, or release timing.
- **STG-5** **Approach** SHOULD NOT name more than three areas.

## Suggested document

```markdown
---
type: Strategy
title: <System> strategy
description: <Where effort concentrates now, and why, in one sentence>
---

# <System> strategy

## Challenge
## Approach
## Not now
## Revisit
## Open questions
## Related
```

## Writing guidance

### Strategy, direction, and objectives

The [objectives](objectives.md) say which results matter, and direction says
why the business exists and how it decides, whatever it is working on now.
The strategy says what stands most in the way of those results at present and
where to concentrate to get past it, so it changes when the challenge does. A
stand that would hold whatever the challenge is a
[principle](principles.md); the profile's
[ownership tests](../references/profile.md#direction-job-opportunity-objectives-strategy-or-scope)
decide.

### Challenge

Name the obstacle, not the goal. "Grow online reservations" restates
Objective 1 and decides nothing; a challenge says why that result is not yet
happening. Give the evidence or insight behind the judgment, such as call
logs, research, or what a new technology makes possible, and record where it
came from in `sources`. A challenge that no one has evidence for yet is an
open question, not a statement.

### Approach and Not now

- Concentrate. Each area in **Approach** takes effort from others, and a list
  of everything worth doing decides nothing.
- State each area as a problem to overcome for those served or for the
  business, not as a solution to build. Features, and the actions,
  initiatives, and key results that carry out the approach, belong to the
  rest of the specification and to work-management records, as the profile's
  [P-CON-7](../references/profile.md#work-management-and-design) requires.
- **Not now** makes each exclusion a decision rather than an omission. What
  the system will not take on, whatever it is working on, is
  [scope](scope.md); what it sets aside only while this challenge lasts is
  here.

~~~markdown
## Challenge

Contractor customers who reserve online still call a depot to confirm that
the equipment will be ready, because they do not trust an online
confirmation enough to plan a crew around it. Depot call logs show that most
calls about online reservations ask for this. This limits
[Objective 1](<link>) and progress on
[Get equipment on site when the work needs it](<link>).

## Approach

Make a confirmed reservation dependable enough that a contractor plans a crew
around it without calling a depot.

## Not now

Getting equipment to sites near depots that do not offer delivery.

## Revisit

When Objective 1's indicator is first reported, or sooner if the share of
reservations made online falls.
~~~

### Revisit

Agree when to look again before relying on the strategy: a date, or an event
such as an objective's indicator being reported, the challenge being overcome,
or an unexpected success or failure. A strategy whose challenge has been
overcome is no longer current, as the profile's
[Change](../references/profile.md#change) section states.

### Writing a strategy

Write only a strategy that a person or a source states. Do not compose one
from what the system does or from a list of planned work; when none is stated,
leave the strategy unwritten. The strategy of an enclosing business, such as
which markets it enters, belongs to that business's records and is linked
under **Related**.
