# Decomposition module

A module of the [Spec profile](../profile.md), version **0.1.0**. It adds
subsystems, which give part of the system its own boundary, and feature
components, which give part of a feature its own placement level. Its tables
extend the profile's tables of the same name.

## Concept types

| Type | Description |
| --- | --- |
| [`Subsystem`](../../templates/subsystem.md) | A part of the system with its own boundary, because it has its own user classes, external interfaces, quality characteristics, or delivery or operation. |
| [`Feature Component`](../../templates/feature-component.md) | A distinct part of a feature's behavior, such as a command, workflow, or screen, that has its own use cases or requirements. |

## Vocabulary

| Term | Meaning |
| --- | --- |
| System-level feature | A feature placed directly under the system. |
| Subsystem-level feature | A feature placed under a subsystem. |

A subsystem is specified as a system is, at its own boundary:

- **P-DEC-1** Wherever the profile, a module, or a template describes the
  system as a boundary, a subject, or the other end of an External Interface,
  or places features, use cases, or requirements under the system, the same
  MUST apply to a subsystem at its own boundary, except where this module
  states otherwise.

A Use Case or Requirement placed within a subsystem has that Subsystem as its
subject.

## Structure

```text
spec/
  features/
    <feature>/
      components/
        <component>/
          <component>.md           # Feature Component
          use-cases/
          requirements/
  subsystems/
    <subsystem>/
      <subsystem>.md               # Subsystem
      use-cases/                   # Placed at the subsystem
      requirements/
      features/                    # Same structure as spec/features/
```

### Folders

| Folder | Holds |
| --- | --- |
| `subsystems/` | A folder for each `Subsystem` |
| `<subsystem>/` | Its concept document, `use-cases/`, `requirements/`, and `features/` |
| `components/` | A folder for each `Feature Component` of its feature |
| `<component>/` | Its concept document, `use-cases/`, and `requirements/` |
| `<feature>/` | Also `components/` |

Subsystems and feature components are folders, as P-STR-5 requires.

## Placement

### Placement levels

Features belong to the system or to one subsystem. Feature components belong
to one feature. A Use Case or Requirement whose subject is a Subsystem is
placed within that subsystem: at the subsystem, or at one of its features or
feature components. A concept shared by two subsystems is placed at the
system, and its subject is the System.

### Fixed locations

| Type | Location |
| --- | --- |
| `Subsystem` | `subsystems/<subsystem>/` |
| `Feature Component` | `components/<component>/` within its feature |
| `Feature` | Also `features/<feature>/` within a subsystem |

Every type other than those placed within a subsystem lives at the system
level, even when it is specific to one subsystem, such as a user class, an
external interface, or a glossary term.

- **P-DEC-2** A concept that lives at the system level but is specific to one
  subsystem SHOULD link that subsystem under **Related**.
- **P-DEC-3** A meaning specific to one subsystem MUST take a name distinct
  from the system's other names.
- **P-DEC-4** The **Scope** of the Business Requirements MUST link each
  subsystem it includes.

## Not yet defined

| Topic | Interim practice |
| --- | --- |
| Operating environment conditions and quality priorities specific to one subsystem | State them in the System's **Operating environment** or **Quality priorities**, naming and linking the subsystem. |
| Connections between subsystems of the same system | Describe what passes between them in each Subsystem's **Boundary and context**, linking the sibling Subsystem. |
| Use cases and requirements whose subject is a subsystem but that belong to a system-level feature | Place them within the subsystem, at the subsystem or in a subsystem-level feature, and link the system-level feature under **Related**. |
