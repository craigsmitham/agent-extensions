# Subsystem template

Use for a part of the system with its own boundary. Apply the
[Spec profile](../references/profile.md). The Type contract is normative; the
remaining sections guide authoring.

It parallels the [System template](system.md), with the
[differences](#differences-from-the-system-template) recorded below.

## Type contract

- **SUB-1** The title MUST be the subsystem's name.
- **SUB-2** A Subsystem document MUST include these sections:
  - **Purpose**: what the subsystem is and does within the system.
  - **Relationship to the system**: which condition in SUB-3 it meets, and
    what it provides to or needs from the rest of the system.
  - **Boundary and context**: what is inside the subsystem and what is outside
    it, naming each party the subsystem interacts with.
- **SUB-3** A subsystem MUST be defined only when part of the system has at
  least one of: quality characteristics specific to it; user classes specific
  to it; external interfaces specific to it; or separate delivery or
  operation.
- **SUB-4** When a subsystem needs subsystems of its own, it MUST be
  specified as a separate system in its own corpus, and the two corpora
  linked.
- **SUB-5** **Boundary and context** MUST link each party to its User Class,
  External Interface, or, for a sibling subsystem, Subsystem.

## Suggested document

```markdown
---
type: Subsystem
title: <Subsystem name>
description: <What the subsystem is and who it serves within the system, in one sentence>
status: draft
---

# <Subsystem name>

## Purpose
## Relationship to the system
## Boundary and context
## Open questions
## Related
```

## Writing guidance

### Differences from the System template

| Difference | Reason |
| --- | --- |
| No **Operating environment** or **Quality priorities** | The System's sections cover the whole system, including what is specific to a subsystem, as the module's [Not yet defined](../references/modules/decomposition.md#not-yet-defined) describes. |

### Relationship to the system

Name the condition and the fact that meets it:

```markdown
Fleet maintenance is a subsystem because it has its own user class,
[Technician](<link>), and its own external interface,
[Equipment telematics](<link>). It records equipment condition and operating
hours, which the rest of the rental system uses to decide what can be rented.
```

A quality requirement that applies to one feature does not make the feature a
subsystem, and a service, container, or module does not by itself make a
subsystem.

The user classes, external interfaces, and quality characteristics specific to
a subsystem live at the system level with the others, and link the subsystem
under **Related**, as P-DEC-1 describes. The subsystem's own folder holds only its use cases, requirements,
and features, whose subject is the subsystem. The subsystem document links
them rather than describing them.

### Boundary and context

Apply the System's [boundary and context guidance](system.md#boundary-and-context)
at the subsystem's boundary. For what passes between sibling subsystems, follow
[Not yet defined](../references/modules/decomposition.md#not-yet-defined); the subsystem
document does not otherwise describe the sibling.

**Related** links records that describe how the subsystem is realized, such
as services or repositories.
