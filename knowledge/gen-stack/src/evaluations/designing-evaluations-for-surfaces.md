---
type: Guide
title: Designing evaluations for Surfaces
description: Use when Surface behavior or realization needs evaluation coverage; define subject- and Requirement-navigable evidence without turning interaction hierarchy into a runner taxonomy.
tags: [evaluations, surfaces, requirements, usability, accessibility, interaction]
status: draft
sources:
  - resource: designing-a-system-evaluation-approach.md
    title: Designing a system evaluation approach
  - resource: ../architecture/surfaces/documenting-surfaces.md
    title: Documenting surfaces
---

# Designing evaluations for Surfaces

> **Authority:** This Guide applies the canonical meaning in the [Gen Stack
> vocabulary and relationship model](/glossary.md). When it authors a
> profile-governed corpus concept, the [Gen Stack application
> profile](/profile/gen-stack-application-profile.md) owns its required
> representation. This Guide supports action and adds neither semantic authority
> nor profile-conformance rules.

## Goal

Evaluate actor-facing behavior and the Implementation that realizes each
canonical Surface while preserving the Surface interaction hierarchy.

## Representation

Author Definitions, Suites, Executions, Results, and Reports in their
repository-native formats. Use exact native fields for identity, Evaluation
Role, Surface subject, Requirement IDs, method, conditions, oracle, thresholds,
Implementation revision, and evidence links when available. Add residual prose
only for meaning the schema cannot carry. Prefer Definition content in this
logical order: bounded claim, subject and criteria authority, method and cases,
conditions and sampling, oracle and thresholds, then evidence and lifecycle.
Do not wrap concrete Evaluations in OKF or duplicate native links in prose.

## Steps

1. Select the narrowest Surface whose interaction boundary owns the claim.
   Use the parent only for behavior or quality that genuinely spans its
   children.
2. For `requirement-satisfaction`, reference the Surface-colocated Requirement
   IDs. Derive scenarios from relevant Use Cases without making the Use Case
   or test the obligation authority.
3. Cover recognizable success behavior and material extensions, failures,
   recovery, trust transitions, accessibility, usability, human factors,
   compatibility, and operational conditions in proportion to consequence.
4. For `architecture-realization`, assess whether the implemented encounter
   point preserves the Surface boundary, actors, exposed behavior, feature and
   Use Case mappings, trust boundary, and consequential accessibility or
   operational response.
5. Use the cheapest credible combination of examples, properties, protocol or
   contract checks, human studies, accessibility review, security analysis,
   and operational measures. Record the population, task, device, locale,
   assistive technology, or environment when it bounds the result.
6. Project Results through the canonical parent-child Surface navigation and
   by Requirement ID. Keep runner Suites organized for execution; do not infer
   Surface containment from their folders.
7. Report Requirement satisfaction separately from Surface realization.
   Expose uncovered children and `unknown`; passing child Surfaces do not by
   themselves prove a parent-level claim.

## Final check

- Each claim is attached to the narrowest responsible Surface.
- Actor-visible failures and quality conditions receive proportional coverage.
- Surface hierarchy drives navigation, not physical suite layout.
- Requirement satisfaction and realization reports remain distinct.
- Cross-Surface behavior is located at the narrowest common parent or linked
  explicitly across subjects.

## Related

- [Designing a system evaluation approach](designing-a-system-evaluation-approach.md)
- [Documenting surfaces](../architecture/surfaces/documenting-surfaces.md)
- [Goal-oriented behavior and use cases](../intent/goal-oriented-behavior.md)
