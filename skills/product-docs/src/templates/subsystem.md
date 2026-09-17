# Subsystem template

Use for a part of the system with its own boundary.

## Type contract

- **SUB-1** The title MUST be the subsystem's name.
- **SUB-2** A Subsystem document MUST include these sections:
  - **Purpose**: what the subsystem is and does within the system, which
    condition in SUB-3 it meets, and what it provides to or needs from the
    rest of the system.
  - **Boundary and context**: what is inside the subsystem and what is outside
    it, naming each party the subsystem interacts with.
  - **Operating environment** *(optional)*: conditions specific to the
    subsystem that it must work in.
- **SUB-3** A subsystem MUST be created only when part of the system has at
  least one of: required levels of quality specific to it; user classes
  specific to it; external interfaces specific to it; or separate delivery or
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
---

# <Subsystem name>

## Purpose
## Boundary and context
## Operating environment
## Open questions
## Related
```

## Writing guidance

### Purpose

Name the condition that makes the part a subsystem, and the fact that meets
it:

```markdown
Fleet maintenance is a subsystem because it has its own user class,
[Technician](<link>), and its own external interface,
[Equipment telematics](<link>). It records equipment condition and operating
hours, which the rest of the rental system uses to decide what can be rented.
```

A required level of quality that applies to one feature does not make the
feature a subsystem, and a service, container, or module does not by itself
make a subsystem.

### Specified as a system

A subsystem is specified as the system is, at its own boundary, as
[P-DEC-1](../references/profile.md#vocabulary) requires. Its
own folder holds its use cases, requirements, and features, whose subject is
the subsystem; the folder indexes list them, and the subsystem document does
not describe them. Concepts specific to it that live at the system level,
such as [Technician](<link>), link it under **Related**.

Use cases and requirements whose subject is the subsystem but that belong to
a system-level feature are
[not yet defined](../references/profile.md#not-yet-defined). Until they are,
place such a concept within the subsystem, and link the system-level feature
under **Related**.

### Boundary and context

Apply the System's
[boundary and context guidance](system.md#boundary-and-context) at the
subsystem's boundary. Parties of the subsystem, such as technicians and
equipment telematics for Fleet maintenance, are also outside the system, so
they appear in the System's **Boundary and context** too. Describe what passes
between sibling subsystems here, linking the sibling Subsystem; the subsystem
document does not otherwise describe the sibling.

**Related** links records that describe how the subsystem is realized, such
as services or repositories.

### Operating environment

State only conditions specific to the subsystem, as the System's
[operating environment guidance](system.md#operating-environment) describes;
conditions of the whole system stay in the System.
