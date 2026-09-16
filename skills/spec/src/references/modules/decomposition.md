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
| Subsystem-level feature | A feature placed under a subsystem. |

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

User classes, external interfaces, and the types of other modules live at the
system level even when they are specific to one subsystem.

- **P-DEC-1** A User Class, External Interface, Quality Characteristic,
  Business Rule, Entity Type, or Value Type that is specific to one subsystem
  SHOULD link that subsystem under **Related**.
- **P-DEC-2** A meaning specific to one subsystem MUST take a name distinct
  from the system's other names.

## Not yet defined

| Topic | Interim practice |
| --- | --- |
| Folders for concepts specific to one subsystem, such as a subsystem glossary or subsystem quality characteristics | Place them at the system level, as the profile's [Fixed locations](../profile.md#fixed-locations) requires, and give a subsystem-specific meaning a distinct name. |
| Operating environment conditions and quality priorities specific to one subsystem | State them in the System's **Operating environment** or **Quality priorities**, naming and linking the subsystem. |
| Connections between subsystems of the same system | Describe what passes between them in each Subsystem's **Boundary and context**, linking the sibling Subsystem. |
| Use cases and requirements whose subject is a subsystem but that belong to a system-level feature | Place them within the subsystem, at the subsystem or in a subsystem-level feature, and link the system-level feature under **Related**. |
