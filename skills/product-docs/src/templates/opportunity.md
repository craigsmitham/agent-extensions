# Opportunity template

Use for what the system is built or changed to make possible: the need that
is unmet, how it is met today, why the system is worth building or changing
now, and what must hold for it to stay worth pursuing.

## Type contract

- **OPP-1** The title MUST be "<System> opportunity".
- **OPP-2** An Opportunity document MUST include these sections:
  - **Opportunity**: what becomes possible, and for whom, in a short
    paragraph.
  - **Current situation**: how the need is met today and where that falls
    short, with any known evidence.
  - **Why now** *(optional)*: what makes the system worth building or
    changing now.
  - **Assumptions** *(optional)*: what must hold for the opportunity to stay
    worth pursuing, each with what would show that it no longer holds.
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
## Assumptions
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
[ownership tests](../references/profile.md#direction-job-opportunity-objectives-strategy-or-scope)
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

### Why now

Name what has already happened that makes the opportunity real now, such as a
change among those served, in the market, in the business, or in technology,
or the end of what serves the need today. A hope that something will happen is
an assumption, not a reason.

### Assumptions

An opportunity rests on beliefs about those served, the business, and the
world that may stop being true, so a reason to build that was sound can
quietly become obsolete. State the few assumptions whose failure would change
whether the opportunity is worth pursuing, and for each, what would show that
it no longer holds, so that the steward can notice:

~~~markdown
## Assumptions

- Contractors will plan crews around an online confirmation without calling a
  depot. It no longer holds if most online reservations are still followed by
  a call to the depot.
~~~

An assumption already known to be false is not an assumption; it changes the
opportunity. Assumptions about how the system is built or operated belong to
design and operations records.
