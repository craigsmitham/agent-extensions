# Feature template

Use for one coherent unit of capability that the system provides to its users,
such as equipment reservations or late returns.

## Type contract

- **FEA-1** The title MUST name the capability as a noun phrase, such as
  "Equipment reservations".
- **FEA-2** A Feature document MUST include these sections:
  - **Purpose**: what capability the feature provides, stating **serves** for
    each user class, job to be done, and business objective it serves.
  - **Coverage**: what the capability covers, and what it does not cover where
    a reader might assume it does.

## Suggested document

```markdown
---
type: Feature
title: <Capability as a noun phrase>
description: <What the feature provides, and to whom, in one sentence>
status: draft
---

# <Capability as a noun phrase>

## Purpose
## Coverage
## Illustrations
## Open questions
## Related
```

## Writing guidance

### Purpose and coverage

**Purpose** describes the capability in a paragraph and links the user
classes, jobs to be done, and business objectives it **serves**, such as
[Contractor customer](<link>),
[Get equipment on site when the work needs it](<link>), and
`business.md#objective-1`.

**Coverage** summarizes what the capability covers and names exclusions a
reader might otherwise assume. An exclusion that the system must enforce is a
Requirement, not coverage. The folder index lists the feature's use cases,
requirements, and any placement levels below it; when how they fit together
is not obvious from the index, explain it in **Purpose**.

When the feature is present only in some editions, configurations, or
locations, state the condition in **Coverage**, as
[P-CON-5](../references/profile.md#concerns-not-yet-defined) describes. For
example, Site delivery covers delivery only from depots that offer delivery.

### Illustrations

When readers cannot follow the behavior without seeing a user interface,
sketch it under **Illustrations**: the information it presents, the actions it
offers, and where those actions lead, linked to the use case steps they serve.
The use case steps own what the interface presents, as
[where content goes](../references/profile.md#where-content-goes) states; the
sketch only makes them concrete. Keep it rough but accurate, as
[binding and illustrative content](../references/profile.md#binding-and-illustrative-content)
describes, so that use case steps stay technology-neutral and detailed design
stays in design records. For example,
Equipment search presents available equipment by type, depot, and rental
period, and each result leads to [Reserve equipment](<link>).

### Size

A feature is large enough to hold several use cases or a set of requirements.
Capability with a single use case and nothing around it usually belongs to an
existing feature.
