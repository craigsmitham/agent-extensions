---
okf_version: "0.2"
---
# Software architecture

Portable principles for reasoning about the durable structure and boundaries of
software systems.

## Start here

- [Overview](overview.md) — What software architecture owns and how it differs
  from proposals, code inventories, and implementation plans.

## Boundaries and change

- [Responsibilities and non-responsibilities](responsibilities-and-non-responsibilities.md)
  — How explicit ownership and exclusion make components composable.
- [Boundaries, authority, and state](boundaries-authority-and-state.md) — How
  decision rights and state ownership define meaningful boundaries.
- [Dependency direction and change](dependency-direction-and-change.md) — How
  dependencies expose policy to change and how information hiding reduces its
  reach.

## Confidence and communication

- [Invariants and enforcement](invariants-and-enforcement.md) — Which
  constraints belong in architecture and how executable checks support them.
- [Views and concerns](views-and-concerns.md) — Why architecture is communicated
  through selected views rather than one exhaustive diagram.
