---
type: Guide
title: Documenting context maps
description: Use when relationships between Bounded Contexts need explicit direction and consequences; create one Context Map concept that makes them visible.
tags: [architecture-documentation, ddd, context-maps, integration, dependencies, authoring]
status: draft
sources:
  - resource: /architecture/domains/domain-driven-design.md
    title: Domain-driven design
  - resource: /profile/gen-stack-application-profile.md#context-map
    title: Gen Stack application profile — Context Map
generated: { by: codex/gpt-5.6, at: "2026-08-26T14:02:36Z" }
---

# Documenting context maps

## Goal

Create one `Context Map` concept under `architecture/domains/context-maps/` that owns a
maintained relationship view among bounded contexts.

## Before you begin

Identify the contexts and accepted integration consequences in scope. Do not
create an untyped box diagram or infer relationships only from current network
calls and dependencies.

## Steps

1. Choose a map scope that one reader can reason about coherently: a system,
   domain area, or consequential integration boundary.
2. Create its canonical file using the `Context Map` type and common fields
   from the [application profile](/profile/gen-stack-application-profile.md#context-map).
3. Identify every bounded context in scope by its canonical concept.
4. For each material relationship, state dependency direction, influence,
   translation or published-language boundary, and the meaning exchanged.
5. Identify consistency, compatibility, failure, recovery, and coordination
   concerns. Link accepted Requirements on eligible Bounded Context or
   structural subjects; do not make the Context Map their normative owner.
6. Explain accepted consequences and link current interface, schema, test, or
   runtime evidence without copying it. Update `architecture/domains/context-maps/index.md`.

## Final check

- Every relationship has direction and meaning.
- Translation and ownership boundaries are visible.
- Consequential failure and consistency Requirements are linked without
  becoming obligations of the Context Map.
- Individual context documents do not maintain competing copies of the map.

## Related

- [Domain-driven design](/architecture/domains/domain-driven-design.md)
- [Documenting bounded contexts](documenting-bounded-contexts.md)
