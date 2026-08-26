---
type: Guide
title: Documenting surfaces
description: Use when an actor-facing encounter point needs identity independent of its structural realization; create one Surface concept that defines it.
tags: [architecture-documentation, surfaces, interactions, applications, apis, authoring]
status: draft
sources:
  - resource: /architecture/capabilities/capabilities.md
    title: Capabilities in software architecture
  - resource: /intent/goal-oriented-behavior.md
    title: Goal-oriented behavior and use cases
  - resource: /profile/gen-stack-application-profile.md#surface
    title: Gen Stack application profile — Surface
generated: { by: codex/gpt-5.6, at: "2026-08-26T14:02:36Z" }
---

# Documenting surfaces

## Goal

Create one `Surface` concept under `architecture/surfaces/` that defines where actors
encounter system behavior.

## Before you begin

Use a surface when an application, API, command line, protocol, device, or
console has a consequential interaction boundary. Do not infer its C4 type
from its interaction role.

## Steps

1. Name the encounter point in language its actors and maintainers recognize.
2. Create its canonical file using the `Surface` type and common fields from
   the [application profile](/profile/gen-stack-application-profile.md#surface).
   A surface may use a same-named adjacent directory for independently named
   narrower surfaces, such as a CLI command or subcommand.
3. Identify the actors in scope and the interaction boundary they encounter.
4. State the recognizable behavior available there and material exclusions
   from adjacent surfaces. Do not copy the actor goal or scenario owned by a
   Use Case; one use case may be enacted through several surfaces.
5. Explain accessibility, trust, protocol, availability, or operational
   concerns only when they materially shape the interaction. Link accepted
   obligations as subject-colocated Requirements rather than recording
   constraints in the Surface prose.
6. Link features available through the surface, use cases it supports, C4
   elements realizing it, and relevant evidence. Colocate accepted surface
   obligations beneath its `requirements/<requirement_type>/` collection, then
   update the immediate surface index.

## Final check

- The document answers where actors encounter behavior.
- It does not redefine every feature exposed through the surface.
- It exposes use-case behavior without claiming ownership of the goal or
  scenario.
- Interaction meaning remains distinct from runtime structure.
- Material constraints and realization evidence are linked, not duplicated.
- Recursive surface navigation communicates the product interaction model,
  not the test runner's suite hierarchy.

## Related

- [Capabilities in software architecture](/architecture/capabilities/capabilities.md)
- [Goal-oriented behavior and use cases](/intent/goal-oriented-behavior.md)
- [Documenting features](/architecture/features/documenting-features.md)
- [Documenting C4 containers](/architecture/structure/documenting-c4-containers.md)
