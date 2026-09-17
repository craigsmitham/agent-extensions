# Objectives template

Use for the results that the system must bring about, and the indicators by
which each is recognized.

## Type contract

- **OBJ-1** The title MUST be "<System> objectives".
- **OBJ-2** An Objectives document MUST include these sections:
  - **Objectives**: one entry for each objective, headed `Objective <n>`.
- **OBJ-3** An entry's objective MUST be the first paragraph below its
  heading, stated as a change outside the system, in the progress of those the
  business serves or in the business's own results, rather than as an output,
  and the rest of the entry MUST be entry lines.
- **OBJ-4** Each **Indicator** line MUST state one indicator, with its target
  and timeframe when it is quantitative or the evidence observed when it is
  qualitative, and is binding content.
- **OBJ-5** An objective's number MUST NOT be given to a different objective,
  including after the objective is deleted.
- **OBJ-6** An objective MUST NOT state features, requirements, release
  timing, or the steps of a plan.

## Suggested document

```markdown
---
type: Objectives
title: <System> objectives
description: The results <system> must bring about, and how each is recognized
---

# <System> objectives

## Objectives

### Objective 1

<The outcome the system must bring about.>

- **Indicator:** <what will be observed, with its target and timeframe, or the evidence>

## Open questions
## Related
```

## Writing guidance

### Results, not outputs

Results exist only outside the system; inside it there is only work. An
objective is a change that the system's work brings about there: in the
progress of the people the business serves, as "contractor customers reserve
equipment without calling a depot" is, or in the business's own results, as
"fewer rentals are returned late" is. It is not an output, such as "launch
online reservations". When the change is in the progress a
[job to be done](job-to-be-done.md) describes, link the job in the
objective. Keep the objectives few, so that
each one steers decisions. What the [vision](vision.md) pursues without a
target, and what the [opportunity](opportunity.md) says is possible, become
objectives here once someone commits to recognizing them.

Head each objective with its number alone, so that its anchor stays stable
when the wording changes. Other documents link it by anchor, such as
`business/objectives.md#objective-1`, and state **serves** for it.

### Indicators

An indicator is how the business will know that an objective is being
achieved: a measure of the system's effectiveness in use, seen from outside
it.

- A quantitative indicator states what is counted, its target, and its
  timeframe. A qualitative indicator names the evidence to be observed, such
  as what customers report in interviews. An objective often needs both.
- A target that is not decided is an open question, not a plausible number.
- An indicator can be a leading sign of a result that takes longer to show.
- An indicator need not be a change in how people behave; a business result,
  such as the share of rentals returned late, is observed directly.
- How well the system itself performs, such as response time, is a measure of
  a [quality characteristic](quality-characteristic.md), not an indicator.
- A key result committed for a planning period belongs to planning records,
  and links the objective it advances.

~~~markdown
### Objective 1

Contractor customers reserve equipment without calling a depot.

- **Indicator:** At least 60% of reservations are made online within 12
  months of launch.

### Objective 2

Fewer rentals are returned late.

- **Indicator:** The share of rentals returned late, with a target that is
  not yet agreed.
~~~
