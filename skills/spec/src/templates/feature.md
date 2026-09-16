# Feature template

Use for one coherent unit of capability that the system provides to its users, such as equipment reservations or late returns. Apply
the [Spec profile](../references/profile.md). The Type contract is normative;
the remaining sections guide authoring.

## Type contract

- **FEA-1** The title MUST name the capability as a noun phrase, such as
  "Equipment reservations".
- **FEA-2** A Feature document MUST include these sections:
  - **Purpose**: what capability the feature provides, stating **serves** for
    each user class and business objective it serves.
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

**Purpose** describes the capability in a paragraph and links the user classes
and business objectives it **serves**, such as [Contractor customer](<link>)
and `business.md#objective-1`.

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

For a feature that presents a user interface of its own, a sketch under
**Illustrations** can show the information it presents, the actions it
offers, and where those actions lead, linked to the use case steps they serve.
Keep it rough but accurate. It is illustrative content, so it agrees with the
use cases and requirements placed under the feature and adds no obligations,
as the profile's
[binding and illustrative content](../references/profile.md#binding-and-illustrative-content)
rules require; an obligation it reveals is a Requirement. Include it only when
it helps readers understand the behavior, even when the feature is a user
interface.

Use cases do not name user interface elements. When readers need to know what
a screen presents to follow the behavior, sketch it under the
**Illustrations** of the narrowest placement level whose use cases it serves,
and let the use case steps stay technology-neutral. For example, Equipment search presents available
equipment by type, depot, and rental period, and each result leads to
[Reserve equipment](<link>).

### Size

A feature is large enough to hold several use cases or a set of requirements.
Capability with a single use case and nothing around it usually belongs to an
existing feature. The feature's use cases and requirements sit in its
`use-cases/` and `requirements/` folders, and share its subject.

### Related

Link the concepts the feature is about, such as external interfaces, rules,
and data, rather than restating use case steps, requirements, rules, or data
details. Undecided coverage or user
interface goes under **Open questions**.
