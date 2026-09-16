# Subsystem template

Use for a part of the system with its own boundary. Apply the
[Spec profile](../references/profile.md). The Type contract is normative; the
remaining sections guide authoring.

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

A subsystem is specified as the system is, at its own boundary, as
[P-DEC-1](../references/modules/decomposition.md#vocabulary) requires. Its
own folder holds its use cases, requirements, and features, whose subject is
the subsystem, and the subsystem document links them rather than describing
them. Concepts specific to it that live at the system level, such as
[Technician](<link>), link it under **Related**, and its operating conditions
and quality priorities are stated in the System's sections, as the module's
[Not yet defined](../references/modules/decomposition.md#not-yet-defined)
describes.

Parties of the subsystem, such as technicians and equipment telematics for
Fleet maintenance, are also outside the system, so they appear in the
System's **Boundary and context** too.

### Boundary and context

Apply the System's
[boundary and context guidance](system.md#boundary-and-context) at the
subsystem's boundary. For what passes between sibling subsystems, follow
[Not yet defined](../references/modules/decomposition.md#not-yet-defined); the
subsystem document does not otherwise describe the sibling.

**Related** links records that describe how the subsystem is realized, such
as services or repositories.
