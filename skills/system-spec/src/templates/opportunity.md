# Opportunity template

Use for what the system is built or changed to make possible: the need that
is unmet, how it is met today, and why the system is worth building or
changing now.

## Type contract

- **OPP-1** The title MUST be "<System> opportunity".
- **OPP-2** An Opportunity document MUST include these sections:
  - **Opportunity**: what becomes possible, and for whom, in a short
    paragraph.
  - **Current situation**: how the need is met today and where that falls
    short, with any known evidence.
  - **Why now** *(optional)*: what makes the system worth building or
    changing now.
- **OPP-3** **Current situation** MUST link each Job to Be Done whose progress
  is unmet, rather than restating it.
- **OPP-4** An Opportunity MUST NOT select a solution, name features, or state
  indicators or targets.

## Suggested document

```markdown
---
type: Opportunity
title: <System> opportunity
description: <What becomes possible, and for whom, in one sentence>
---

# <System> opportunity

## Opportunity
## Current situation
## Why now
## Open questions
## Related
```

## Writing guidance

### Opportunity and problem

Write a problem as the opportunity it opens. "Customers must phone a depot to
reserve equipment" describes a gap; the opportunity is what closing it makes
possible for contractors. Stating the opportunity keeps the document on the
results the system is for, rather than on a list of faults to fix, and leaves
the choice of solution to the rest of the specification.

The [mission](mission.md) says why the business exists whatever system serves
it; the opportunity says why this system is built or changed now. A statement
that gains a target is an [objective](objectives.md), as the profile's
[ownership tests](../references/profile.md#direction-job-opportunity-objectives-or-scope)
decide.

### Current situation

- Describe what the people served do today, including workarounds, and where
  it falls short for them and for the business.
- Link the unmet [jobs to be done](job-to-be-done.md) instead of describing
  the progress people seek.
- Summarize evidence of the need, such as call logs, research, or lost
  business, and record where it came from in `sources`. A need that no one
  has evidence for yet is an open question, not a statement.

~~~markdown
## Opportunity

Contractors can reserve equipment when their work is planned, at any hour,
without waiting for a depot to answer.

## Current situation

Customers reserve by calling a depot during opening hours, because the
previous system is used only by depot staff. Depot call logs show that most
reservations are made by phone, and contractors report working days lost
waiting for a depot to confirm equipment for
[Get equipment on site when the work needs it](<link>).

## Why now

The previous system is being replaced.
~~~
