---
type: Explanation
title: Wardley Mapping
description: How Wardley Mapping combines user needs, dependency, and evolution to make strategic assumptions visible without choosing a strategy by itself.
tags: [wardley-mapping, situational-awareness, value-chain, user-needs, evolution, movement, inertia]
status: draft
sources:
  - id: wardley-strategy-cycle
    resource: https://medium.com/wardleymaps/on-being-lost-2ef5f05eb1ec
    title: Simon Wardley — On being lost
  - id: wardley-map-grammar
    resource: https://medium.com/wardleymaps/finding-a-path-cdb1249078c0
    title: Simon Wardley — Finding a path
  - id: wardley-evolution
    resource: https://medium.com/wardleymaps/finding-a-new-purpose-8c60c9484d3b
    title: Simon Wardley — Finding a new purpose
  - id: wardley-inertia
    resource: https://medium.com/wardleymaps/i-wasnt-expecting-that-dcfe122a2234
    title: Simon Wardley — I wasn't expecting that
  - id: wardley-limitations
    resource: https://www.dannybuerkli.com/2025/02/02/where-the-map-ends
    title: Danny Buerkli — Where the map ends
generated:
  by: codex/gpt-5.6
  at: 2026-08-29T20:34:30Z
---

# Wardley Mapping

Wardley Mapping is a strategic sensemaking practice for improving situational
awareness before choosing action. A **Wardley map** represents a chain of
components that satisfies a user need, connects those components by dependency,
and positions each one according to its stage of evolution.[^wardley-map-grammar]

The map makes assumptions about a landscape visible and challengeable. It is
not a forecast, roadmap, architecture diagram, or decision engine. Mapping is
also broader than the diagram: it sits within an iterative strategy cycle of
purpose, landscape, climate, doctrine, and leadership.[^wardley-strategy-cycle]

## The map grammar

A map combines visibility, evolution, and a dependency graph:

```text
more visible to the user
           ↑
      user need
           │
       capability
           │
       dependency
           │
less visible

           genesis ─ custom-built ─ product/rental ─ commodity/utility
                                  evolution →
```

Its essential parts are:

| Part | Meaning |
| --- | --- |
| **Anchor** | A user or stakeholder and the need defining the point of view. |
| **Components** | Activities, practices, data, knowledge, capabilities, or other elements needed to satisfy the need. |
| **Dependency** | A higher component needs a lower component for the mapped outcome. |
| **Evolution** | Each component is positioned from genesis to commodity according to how ubiquitous and well understood it is. |

Vertical position expresses visibility to the selected user. It does not show
organizational rank, architectural layering, implementation order, or general
importance. Changing the user, need, question, or scope can produce a different
and equally legitimate map.

## Evolution is not maturity or time

The four evolution stages characterize changing contexts:

| Stage | Characteristic situation |
| --- | --- |
| **Genesis** | Novel, rare, uncertain, and poorly understood; exploration dominates. |
| **Custom-built** | Bespoke for a context, uncommon, and still changing as understanding grows. |
| **Product or rental** | Repeatable, increasingly defined, and differentiated through a developing market. |
| **Commodity or utility** | Widespread, standardized, well understood, and increasingly shaped by scale and operational efficiency. |

Evolution is not component age, delivery progress, adoption of one product, or
a quality score. It differs from diffusion, which describes a particular
version spreading through a population over time. The axis has no calendar
scale, so it can support anticipation but cannot establish when movement will
occur.[^wardley-evolution]

Rightward is not inherently better. Novel components may create learning or
differentiation; industrialized components may introduce concentration,
resilience, regulatory, or switching risks. A component's stage changes the
character of uncertainty and the methods likely to fit, but it does not dictate
a sourcing model, technology, process, or team structure.

Positions are estimates. Movement arrows express hypotheses about expected or
intended change. Coordinates do not make those claims precise measurements.

## Situational awareness and strategic choice

Mapping separates questions that a plan often collapses:

| Factor | Question |
| --- | --- |
| **Purpose** | What are we trying to achieve, for whom, and why? |
| **Landscape** | What is the current position and dependency structure? |
| **Climate** | Which external patterns act on the landscape regardless of preference? |
| **Doctrine** | Which generally useful ways of operating should improve action? |
| **Leadership** | Which context-specific choices or plays will be made? |

The map primarily represents landscape. Climate and doctrine inform reasoning;
leadership makes the strategic commitment. A map may expose where custom
investment, standardization, sourcing, migration, optionality, or capability
development deserves consideration, but it cannot choose where to play or how
to win.

Expected movement may encounter **inertia** associated with past success,
investment, contracts, skills, identity, incentives, or operating models.
Inertia is not automatically irrational: it may reveal a transition cost,
protected good, or constraint the map missed. Mapping makes resistance and its
consequences discussable; it does not make overcoming it the right choice.[^wardley-inertia]

## Connection to the wider strategy system

Use a map alongside, not instead of, strategic choices:

1. State the strategic question and purpose.
2. Map the user need, dependency chain, evolution, expected movement, and
   relevant inertia.
3. Compare serious where-to-play and how-to-win alternatives.
4. Identify capabilities and management systems each alternative requires.
5. Commit to an integrated choice and record the landscape assumptions on
   which it depends.
6. Review the map and choices when evidence or the landscape changes.

This preserves a useful boundary: the map owns no strategic decision merely
because it informed one. The choice remains accountable in the team's strategy
authority, while downstream disciplines own their accepted consequences.

## Limits and responsible use

A map is a deliberately partial model. It can omit unknown dependencies,
reflect author bias, choose the wrong user or resolution, and become stale.
It cannot reveal novel components its authors have not perceived.[^wardley-limitations]

Common misreadings include:

- mapping a technology inventory without a user need;
- reading evolution as a roadmap, maturity model, quality score, or timeline;
- deriving build-versus-buy or organization design mechanically from a stage;
- treating coordinates as measurements or predictions;
- replacing domain, process, structural, financial, or risk models; and
- preserving a workshop snapshot after its evidence expires.

[^wardley-map-grammar]: Wardley's mapping chapter constructs a value chain from
    user needs and dependencies, then positions components by evolution.
[^wardley-strategy-cycle]: Wardley's opening chapter describes an iterative
    cycle of purpose, landscape, climate, doctrine, and leadership.
[^wardley-evolution]: Wardley's evolution account distinguishes evolution from
    diffusion and time and treats current positions as estimates.
[^wardley-inertia]: Wardley relates inertia to lost capital, established
    practice, uncertainty, and transition.
[^wardley-limitations]: Buerkli highlights dependence on mapper knowledge,
    chosen scope and resolution, and perception of the relevant components.
