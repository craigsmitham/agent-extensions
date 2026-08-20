---
type: Explanation
title: C4 structural views
description: How to apply C4 system, container, component, and code scopes while preserving ownership, avoiding false nesting, and separating shared modules.
tags: [c4-model, software-system, containers, components, modules, structural-views]
status: draft
sources:
  - id: c4-model
    resource: https://c4model.com/
    title: The C4 model for visualising software architecture
generated:
  by: codex/gpt-5.6
  at: 2026-08-20T19:56:11Z
---

# C4 structural views

The C4 model supplies a nested set of abstraction levels for structural
communication: software system, container, component, and code.[^c4-model]
Use the levels to answer increasingly detailed questions about one system of
interest, not as a universal ontology for every architecture concern.

## Containment and scope

The useful containment is:

```text
software system
  └─ container
       └─ component
            └─ code
```

A **container** is a separately runnable or deployable unit or data store in
C4's sense; it is not a generic operating-system container. A **component** is
a cohesive unit inside one container, described at an architectural rather than
class level.

Containers do not recursively contain containers, and components do not
recursively contain components. If a supposed child has an independent runtime
or deployment boundary, reconsider whether it is another container. If a
component needs further implementation detail, use a code view or local design
rather than creating arbitrary component depth.

Place a component beneath its owning container so containment is unambiguous.
Do not maintain one global component directory that makes ownership a matter of
cross-reference alone.

## Structural views are not every view

System context and container views usually provide the broadest structural
orientation. Add component views only for containers whose internal
responsibilities, dependencies, or risks are not clear enough from code.
Dynamic and deployment views are supporting views: they explain runtime
interaction sequences and environment allocation, but they do not add new C4
containment levels.

An application can be both an actor-facing surface and a C4 container. A
service can be a container, a software system, or merely an informal name; the
chosen system boundary decides. State the scope rather than deriving identity
from the noun.

## Shared modules

Reusable libraries and packages that are loaded into several containers do not
have one runtime container owner. Model them as shared modules or code
dependencies, with explicit policy ownership and consumers, rather than as
global C4 components. If a shared package is independently deployed or invoked
over a runtime boundary, it may instead be a container or external software
system.

C4 views remain selective. Do not mirror every package, class, route, or
dependency. Include structural elements whose responsibility, boundary,
interaction, or architectural significance must survive implementation change.

[^c4-model]: The C4 model defines software system, container, component, and
    code as hierarchical levels of abstraction and treats dynamic and
    deployment diagrams as supplementary views.
