---
type: Explanation
title: Capabilities, features, and surfaces
description: How capabilities, features, and surfaces provide complementary scale-neutral views of system outcomes, recognizable behavior, and actor interaction points.
tags: [capabilities, features, surfaces, applications, system-modeling, architecture-views]
status: draft
generated:
  by: codex/gpt-5.6
  at: 2026-08-20T19:56:11Z
---

# Capabilities, features, and surfaces

Capabilities, features, and surfaces answer different questions about a system.
Treating them as synonyms or forcing them into one containment tree obscures
relationships that architecture needs to make visible.

The model begins with a **system of interest**: the system, subsystem,
application, service, or other bounded subject whose architecture is being
described. A commercial product can be modeled when it matters, but it is not a
required root.

## Three complementary elements

- A **capability** is a stable ability or responsibility that produces an
  outcome. Capabilities can decompose recursively when each child remains an
  outcome-oriented ability rather than an implementation unit.
- A **feature** is a durable, recognizable behavior or coherent set of
  behaviors available to an actor. It is not automatically a backlog item,
  release increment, screen, or component.
- A **surface** is a place where an actor encounters behavior, such as an
  application, API, command-line interface, protocol endpoint, device, or
  operational console.

These elements are many-to-many. A feature can contribute to several
capabilities, appear through several surfaces, and be realized by several
structural elements. A surface can expose many features. A capability can be
fulfilled by many features and by operational behavior that no actor sees as a
feature.

## Use typed relationships

Prefer explicit relationships over implied folder ancestry:

| Relationship | Meaning |
| --- | --- |
| system **provides** capability | The system is responsible for making the outcome possible. |
| system **exposes** surface | The surface is part of the system's actor-facing boundary. |
| feature **contributes to** capability | The recognizable behavior advances the outcome. |
| feature **is available through** surface | Actors can encounter the behavior there. |
| feature **is governed by** bounded context | The context owns the language, rules, or state that give the behavior meaning. |
| feature **is realized by** container or component | Structural elements implement or operate the behavior. |
| surface **is realized by** container | A deployable or runnable element presents the interaction point. |

An application commonly has two identities: it is a surface in the actor view
and a container in a structural view. Record both identities and their
relationship rather than selecting one universal label. At a narrower scope the
same application may itself be the system of interest.

## Organize without inventing ownership

Give each maintained feature one canonical document. Group feature documents by
a stable, primary behavioral family only when the grouping helps readers scan;
do not nest features under applications merely because one application happens
to expose them today. Link from every relevant capability, surface, context,
and structural element.

Capabilities may form a recursive decomposition because outcome relationships
can be hierarchical. Features usually benefit more from a flat or shallow
family grouping plus typed links. Surfaces describe encounter points, not
feature ownership.

Create an element document only when it carries durable meaning that passes the
architecture admission test. A complete-looking feature or application catalog
is not an architecture outcome when code, tests, or a live catalog owns the
inventory better.
