---
type: Explanation
title: Strategic evolution views
description: How strategic architecture views connect user need, dependency, evolution, sourcing, inertia, and movement to accepted structural consequences.
tags: [strategic-architecture, evolution, sourcing, wardley-mapping, inertia, architecture-strategy]
status: draft
generated:
  by: codex/gpt-5.6
  at: 2026-08-20T19:56:11Z
---

# Strategic evolution views

Architecture needs a strategic view when structural choices depend on how a
system creates value, which dependencies are visible to a need, how mature
those dependencies are, and how they are expected to move. This view belongs in
the architecture corpus when it explains accepted consequences that other
views must preserve.

Strategic maps and assessments are usually hypotheses, not timeless facts.
Separate three kinds of claim:

- **observation or hypothesis:** the current position, dependency, constraint,
  inertia, or expected movement;
- **strategic choice:** where to invest, differentiate, standardize, outsource,
  replace, or preserve optionality; and
- **architectural consequence:** the accepted boundary, dependency direction,
  interface, ownership, or reversibility requirement produced by that choice.

The map or assessment should identify its user or stakeholder need, value-chain
dependencies, evolution assumptions, evidence, consequential movement, and
review trigger. Time-sensitive positioning should carry an explicit freshness
date or remain in a live strategy system rather than becoming apparently
permanent architecture.

Architecture prose should not freeze every strategic hypothesis into desired
state. Preserve accepted consequences in the owning architecture documents and
link back to the strategic evidence that explains why. When the hypothesis
changes, reconsider the consequences instead of silently treating the newest
map as architectural authority.

Strategic elements can reference capabilities, bounded contexts, containers,
external systems, or other dependencies. Reuse their canonical names and make
the relationship explicit; do not create a second architecture model inside
the map.
