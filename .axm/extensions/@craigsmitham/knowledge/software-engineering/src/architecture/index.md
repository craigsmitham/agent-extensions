# Software architecture

Durable structural decisions about responsibilities, boundaries, authority,
dependencies, invariants, and views. Use this section when local implementation
details are insufficient to explain what the system must continue to preserve.

## Start here

- [Software architecture overview](overview.md) - What software architecture owns, what it deliberately leaves to other authorities, and how it relates desired structure to current implementation.

## Boundaries and change

- [Responsibilities and non-responsibilities](responsibilities-and-non-responsibilities.md) - How stating both what an element owns and what it excludes prevents overlapping authority and accidental coupling.
- [Boundaries, authority, and state](boundaries-authority-and-state.md) - How authority and state ownership give structural boundaries meaning and constrain what may cross them.
- [Dependency direction and change](dependency-direction-and-change.md) - How information hiding and dependency direction limit the effects of likely change and preserve policy ownership.

## Confidence and communication

- [Invariants, preservation, and enforcement](invariants-and-enforcement.md) - What makes a property invariant, how state and observation boundaries qualify its preservation, and how invariants relate to requirements, correctness, and enforcement.
- [Expressing invariants](expressing-invariants.md) - How to distinguish an invariant from neighboring requirements, state its scope and observation boundary precisely, and connect it to preservation obligations and evidence.
- [Views and concerns](views-and-concerns.md) - Why architecture uses concern-specific views and how to keep multiple views from becoming competing models of the system.
