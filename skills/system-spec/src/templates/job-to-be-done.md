# Job to Be Done template

Use for the progress that a group of people seek in their circumstances,
whatever product, service, or system helps them make it.

## Type contract

- **JOB-1** The title MUST state the progress sought as an active verb phrase
  in the present tense, such as "Get equipment on site when the work needs
  it".
- **JOB-2** A Job to Be Done document MUST include these sections:
  - **Job performer**: whose progress the job is, described so that a reader
    can tell them apart from others involved, such as those who buy or
    administer a solution.
  - **Circumstances**: the situation in which the job arises and that shapes
    what progress means.
  - **Progress sought**: the change the job performer seeks, in its
    functional dimension and, where they affect what the performer chooses,
    its emotional and social dimensions.
  - **Alternatives** *(optional)*: what job performers use or do today to make
    the progress, including workarounds and doing nothing, and where each
    falls short.
- **JOB-3** The **Job performer** MUST be described in the job itself, not by
  a link to a User Class.
- **JOB-4** A Job to Be Done MUST NOT name the system, its features, user
  interfaces, or technology, or any other solution, except under
  **Alternatives**.
- **JOB-5** A Job to Be Done MUST NOT state indicators or targets.

## Suggested document

```markdown
---
type: Job to Be Done
title: <Progress sought as an active verb phrase>
description: <Job performer> <seek what progress> when <circumstances>
---

# <Progress sought as an active verb phrase>

## Job performer
## Circumstances
## Progress sought
## Alternatives
## Open questions
## Related
```

## Writing guidance

### Jobs and use cases

A job is the progress people seek; a use case is how an actor pursues a goal
with the system. [Reserve equipment](<link>) is a use case, because it names
an interaction with the rental system; the contractor's progress it helps
with, getting equipment on site when the work needs it, is a job, because it
would hold if the business had no rental system or no business rented
equipment at all. The profile's
[ownership tests](../references/profile.md#job-to-be-done-or-use-case) decide
which is which.

Features state **serves** for the jobs they help with, such as
[Equipment search](<link>), [Equipment reservations](<link>), and
[Site delivery](<link>) for this job. The job does not list them.

### Job performer

The job performer is whoever makes the progress, which is often not the person
who uses the system. For this job, the job performer is the contractor who
runs work on a site and needs equipment there; the office administrator who
reserves it is a [Contractor customer](<link>), and a site foreman who never
uses the rental system is still a job performer. Describe the performer by
the role they play in the job, not by demographics, and link a user class
whose members perform the job under **Related** when readers need it.

### Circumstances and progress

- Include circumstances that change what progress means or which alternative
  a performer chooses, such as work scheduled on a site for a known period
  with equipment the contractor does not own. Leave out characteristics that
  change nothing.
- State the functional progress as the performer would, such as having
  serviceable equipment on site when the crew starts and gone when the work
  ends.
- Add emotional and social progress only where it affects choice, such as
  confidence that a start date will not slip, or standing with the main
  contractor who set the schedule.
- Write only jobs that a person, research, or another source states. Do not
  infer a job from the system's features.

### Level

Ask "why?" to move toward an aspiration and "how?" to move toward a step. "Run
a profitable contracting business" is too broad to guide a feature; "Book the
excavator for Monday" is a step, and "Reserve equipment online" names a
solution. Write the job at the level at which performers would choose between
alternatives. Job maps, job steps, and relationships between jobs are
[not yet defined](../references/profile.md#not-yet-defined).

### Jobs, direction, and objectives

The [mission](mission.md) and [vision](vision.md) say what the business does
and pursues; a job says what the people it serves are trying to do, whether or
not the business helps. The [Opportunity](opportunity.md) links the jobs that
are unmet rather than restating them, and a target for how well performers
make the progress is an indicator of an [objective](objectives.md), as the
profile's
[ownership tests](../references/profile.md#direction-job-opportunity-objectives-or-scope)
decide.

### Shared jobs

When several systems help with one job, one corpus holds it and the others
link it, as the profile's [Structure](../references/profile.md#structure)
requires.
