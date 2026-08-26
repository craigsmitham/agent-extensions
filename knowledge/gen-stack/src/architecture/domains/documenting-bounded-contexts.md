---
type: Guide
title: Documenting bounded contexts
description: Use when a coherent domain model and language need explicit authority and boundaries; create one Bounded Context concept that declares them.
tags: [architecture-documentation, ddd, bounded-contexts, authority, ubiquitous-language, authoring]
status: draft
sources:
  - resource: /architecture/domains/domain-driven-design.md
    title: Domain-driven design
  - resource: /profile/gen-stack-application-profile.md#bounded-context
    title: Gen Stack application profile — Bounded Context
generated: { by: codex/gpt-5.6, at: "2026-08-26T14:02:36Z" }
---

# Documenting bounded contexts

## Goal

Create one `Bounded Context` concept under `architecture/domains/contexts/` that declares
where a domain model and its language apply consistently.

## Before you begin

Confirm a coherent model boundary with accepted purpose and authority. A code
folder, service, team, or database is evidence only when it actually realizes
that model; none establishes a bounded context by itself.

## Steps

1. Name the context for the model understood by domain experts and
   maintainers, not for its current deployment unit.
2. Create its canonical file using the `Bounded Context` type and common fields
   from the [application profile](/profile/gen-stack-application-profile.md#bounded-context). Do not add `classification`.
3. State the context's purpose, model and ubiquitous-language scope, policy or
   state authority, and material exclusions.
4. Identify the subdomains it models, allowing many-to-many mappings. Link
   reciprocally without nesting the context beneath a subdomain.
5. Link the context map that owns the complete inter-context relationship
   view; keep only the context's consequential local relationships here. Link
   accepted invariant and boundary Requirements colocated beneath this context
   or another eligible subject.
6. Link code, schemas, configuration, tests, or architecture checks as current
   realization or conformance evidence, then update `architecture/domains/contexts/index.md`.

## Final check

- Purpose, model, language, authority, and exclusions are explicit.
- The context is not classified as core, supporting, or generic.
- Implementation structure is evidence rather than the definition.
- Inter-context obligations have one Requirement authority and are not copied
  from the Context Map.

## Related

- [Domain-driven design](/architecture/domains/domain-driven-design.md)
- [Documenting subdomains](/intent/documenting-subdomains.md)
- [Documenting context maps](documenting-context-maps.md)
