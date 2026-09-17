# Feature Component template

Use for one distinct part of a feature's behavior, such as a command,
workflow, or screen, that has its own use cases or requirements.

## Type contract

- **CMP-1** The title MUST name the part as a noun phrase, such as
  "Reservation calendar" or "Cancellation".
- **CMP-2** A Feature Component document MUST include these sections:
  - **Purpose**: which part of its feature's behavior the component covers,
    and how it differs from sibling components.
- **CMP-3** A feature component MUST be created only when part of a feature
  has its own use cases or requirements that readers need to find and discuss
  separately.
- **CMP-4** When a feature component needs components of its own, it MUST
  be promoted to a feature at the same placement level as its parent, and the
  two linked.

## Suggested document

```markdown
---
type: Feature Component
title: <Part as a noun phrase>
description: <What part of the feature the component covers, in one sentence>
status: draft
---

# <Part as a noun phrase>

## Purpose
## Illustrations
## Open questions
## Related
```

## Writing guidance

### When to create a component

A part that is only a grouping of requirements, or only a user interface
description, stays within the feature. A component is present wherever its
feature is; an optional part with its own use cases is a separate feature.

### Purpose

State the part of the feature's behavior the component covers, and how it
differs from sibling components, such as Reservation calendar choosing days
and Cancellation ending a confirmed reservation. **Purpose** has no
**Coverage** beside it and states no **serves**: distinguishing the component
from its siblings is the coverage a reader needs, and the component serves
the user classes and business objectives its feature serves.

### Illustrations

A user interface sketch of a component is rough and linked to the use case
steps it serves, as the
[Feature illustrations guidance](feature.md#illustrations) describes:

~~~markdown
## Illustrations

For chosen equipment and a depot, the reservation calendar shows which days
are available, and choosing days leads to
[Reserve equipment](<link>).
~~~
