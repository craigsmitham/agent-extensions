# User Class template

Use for a group of people who use the system or its outputs directly in a
similar way and need similar things from it. Apply the
[Spec profile](../references/profile.md). The Type contract is normative; the
remaining sections guide authoring.

## Type contract

- **USR-1** The title MUST name the class as a role, such as "Depot staff" or
  "Contractor customer".
- **USR-2** A User Class document MUST include these sections:
  - **Membership**: who belongs to the class, stated so that a reader can tell
    it apart from the other user classes.
  - **Use of the system**: the goals members pursue with the system, how
    often, and in what circumstances, in summary.
  - **Needs**: what the class needs from the system that other classes do
    not.
  - **Characteristics** *(optional)*: characteristics of the class that shape
    its requirements.
- **USR-3** Each characteristic MUST show how it affects what the system does
  for the class.

## Suggested document

```markdown
---
type: User Class
title: <Role name>
description: <Who they are>, who <use the system for what>, needing <what distinguishes them>
status: draft
---

# <Role name>

## Membership
## Use of the system
## Needs
## Characteristics
## Illustrations
## Open questions
## Related
```

## Writing guidance

### Membership and needs

Name the distinction from similar classes, such as depot staff who hand over
equipment versus technicians who repair it. **Needs** are what the class needs
from the system that other classes do not, such as speed for frequent use,
guidance for occasional use, or audit evidence.

**Use of the system** summarizes the goals members pursue, how often, and in
what circumstances, without listing or describing the use cases, features, or requirements that
serve the class; those documents link to it.

### Characteristics and personas

Include only characteristics that shape requirements, such as domain
expertise, technical expertise, frequency of use, working environment, access
level, language, or accessibility needs, each with its effect.

A persona, under **Illustrations**, is an individual who makes the class
concrete. It illustrates a class; it does not define it.

### Users and stakeholders

A user class is made of people who use the system or its outputs directly,
including those who operate it. In the running example,
[Technician](<link>) is a user class of fleet maintenance because technicians
record inspections and repairs in it. The [Equipment insurer](<link>) has an
interest in the system but does not use it, so it is a stakeholder in the
Business Requirements, not a user class. An organization is described through
the user classes of the people, or the external interfaces of the systems,
through which it acts.

A user class specific to one subsystem, such as Technician, still lives in the
system's `users/` folder and links [Fleet maintenance](<link>) under
**Related**.
