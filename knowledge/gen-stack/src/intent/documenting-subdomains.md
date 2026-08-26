---
type: Guide
title: Documenting subdomains
description: Use when a problem-space responsibility needs explicit identity and a justified strategic classification; create one Subdomain concept as core, supporting, or generic.
tags: [architecture-documentation, ddd, subdomains, strategic-classification, authoring]
status: draft
sources:
  - resource: /architecture/domains/domain-driven-design.md
    title: Domain-driven design
  - resource: ../profile/gen-stack-application-profile.md#subdomain
    title: Gen Stack application profile — Subdomain
generated: { by: codex/gpt-5.6, at: "2026-08-26T14:02:36Z" }
---

# Documenting subdomains

## Goal

Create one `Subdomain` concept under `intent/domains/core/`, `intent/domains/supporting/`, or
`intent/domains/generic/` that names an area of problem-space knowledge and its
strategic importance.

## Before you begin

Confirm the problem-space responsibility and strategic context. Do not infer a
subdomain from a code folder, team, service, or bounded context. Classification
is relative to the documented system and can change when strategy changes.

## Steps

1. Name the business or problem-space knowledge the system must address.
2. Choose exactly one classification: `core` for differentiating knowledge,
   `supporting` for necessary domain-specific knowledge, or `generic` for a
   well-solved problem normally obtained rather than differentiated.
3. Create the canonical file in the directory matching `classification`, using
   the `Subdomain` type and fields from the [application profile](../profile/gen-stack-application-profile.md#subdomain).
4. Explain the responsibility, important distinctions, classification
   rationale, and material exclusions.
5. Link bounded contexts that model all or part of the subdomain without
   implying containment or a one-to-one mapping.
6. Update the classification index. Treat a later reclassification as a path
   and concept-ID migration, updating inbound links and the log.

## Final check

- The concept describes problem knowledge, not implementation structure.
- Its classification is explicit, justified, and matches its path.
- Related bounded contexts remain sibling concepts.
- Exclusions prevent overlap with neighboring subdomains.

## Related

- [Domain-driven design](/architecture/domains/domain-driven-design.md)
- [Documenting bounded contexts](/architecture/domains/documenting-bounded-contexts.md)
