---
type: Guide
title: Documenting systems
description: Use when establishing a Gen Stack corpus for one system or clarifying its root subject; create the required System concept that anchors the boundary and system-wide Requirements.
tags: [architecture-documentation, system, boundary, requirements]
status: draft
sources:
  - resource: /profile/gen-stack-application-profile.md#system
    title: Gen Stack application profile — System
generated:
  by: codex/gpt-5.6
  at: 2026-08-26T14:02:36Z
---

# Documenting systems

Create `system.md` at the corpus root before assigning system-wide
requirements.

1. Name the single documented system and the purpose that distinguishes it.
2. State the boundary in terms a reader can apply when deciding what is inside
   or outside the corpus.
3. Name material exclusions and important environmental relationships.
4. Use the exact `System` type and common profile fields.
5. Link narrower Offering, Surface, domain, or C4 views when maintained; do not
   restate their inventories.
6. Create `system/requirements/` only when the first accepted system-wide
   Requirement exists. Link that collection as the normative authority rather
   than repeating its binding statements in `system.md`.

The System concept is a semantic anchor, not a synonym for a C4 Software
System. It may correspond closely to one, but the two concepts answer different
documentation questions. Purpose, boundary, relationships, exclusions, and
responsibility belong here. An independently accepted statement of what the
System must do, preserve, prevent, constrain, or achieve belongs in a
subject-colocated Requirement.
