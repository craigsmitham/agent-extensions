---
type: Guide
title: Documenting C4 components
description: Use when a cohesive responsibility inside one C4 Container needs component-level identity; create one Component with a defined interface and exactly one owning container.
tags: [architecture-documentation, c4-model, components, interfaces, containment, authoring]
status: draft
sources:
  - resource: /architecture/structure/c4-model.md
    title: C4 model
  - resource: /profile/gen-stack-application-profile.md#c4-component
    title: Gen Stack application profile — C4 Component
generated: { by: codex/gpt-5.6, at: "2026-08-26T14:02:36Z" }
---

# Documenting C4 components

## Goal

Create one `C4 Component` concept beneath exactly one owning container at
`architecture/structure/containers/<container>/components/`.

## Before you begin

Use a component only for architecturally significant functionality
encapsulated behind a defined interface inside one container. A package,
folder, service name, shared library, or bounded context is not automatically
a C4 component.

## Steps

1. Identify the one container in which the functionality executes and is
   deployed.
2. Name the component for its cohesive responsibility rather than its current
   implementation class or package.
3. Create its canonical file using the `C4 Component` type and fields from the
   [application profile](/profile/gen-stack-application-profile.md#c4-component), at the owning-container path.
4. State one concise active responsibility, its defined interface, material
   non-responsibilities, and consequential technology. Check that the name,
   interface, state, and dependencies align with the outcome, policy, state,
   or authority the component claims to own.
5. Identify dependencies and interactions by direction and meaning. Do not
   recursively contain components or duplicate one component under several
   containers.
6. Inherit lifecycle, ownership, decision-policy, and assurance context through
   the owning container from the system's required root concepts. Record only
   a consequential exception.
7. Link domain authority, capabilities, features, accepted Requirements, code
   evidence, and selected component views. Explain the component's structural
   response to linked invariant or guarantee Requirements without restating
   their binding predicates, then update the owning components index.

## Final check

- The component has one cohesive responsibility and defined interface.
- Its material non-responsibilities keep adjacent ownership outside the
  boundary.
- Its path proves exactly one owning container.
- It contains no C4 components recursively.
- Parent system context is not repeated without a meaningful
  exception.
- Shared code remains a dependency unless it has the required component boundary.

## Related

- [C4 model](/architecture/structure/c4-model.md)
- [Documenting C4 containers](documenting-c4-containers.md)
- [Documenting C4 views](documenting-c4-views.md)
- [Reviewing responsibilities with scenarios](/architecture/reviewing-responsibilities-with-scenarios.md)
