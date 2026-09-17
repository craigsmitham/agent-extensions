---
name: system-spec
description: >
  Creates and manages specifications for a software system. Use when asked to
  create, revise, organize, or maintain a system's specs.
---

# System Spec

Create and manage specifications for a software system.

Represent specs as an OKF v0.2 bundle that follows the
[Spec profile](references/profile.md). The profile states which parts are
normative, and its numbered rules are the checklist for writing and reviewing
a document. Examples follow the [running example](references/example.md).

## Concept types

Only `system.md` is required. Write a document of another type when there is
content for it and its Type contract's creation test, if any, is met.

Most systems start with these, writing `business.md` and `glossary.md` once
their content is known:

- [System](templates/system.md)
- [Business Requirements](templates/business-requirements.md)
- [User Class](templates/user-class.md)
- [External Interface](templates/external-interface.md)
- [Feature](templates/feature.md)
- [Use Case](templates/use-case.md)
- [Requirement](templates/requirement.md)
- [Glossary](templates/glossary.md)

Add the others when the system has their content:

- [Mission](templates/mission.md), [Vision](templates/vision.md), and
  [Principles](templates/principles.md), for the lasting purpose, pursued
  future, and decision guidance of the business or product the system serves,
  when the user or a source states them. Do not compose them from a system
  request.
- [Job to Be Done](templates/job-to-be-done.md), for the progress people seek
  that the system helps them make, apart from any solution, when the user,
  research, or another source states them.
- [Subsystem](templates/subsystem.md) and
  [Feature Component](templates/feature-component.md), when part of the
  system or of a feature meets the creation condition in its Type contract.
- [Business Rule](templates/business-rule.md), for rules the business would
  keep without the system.
- [Quality Characteristic](templates/quality-characteristic.md) and
  [Quality Requirement](templates/quality-requirement.md), for required levels
  of quality.
- [Entity Type](templates/entity-type.md) and
  [Value Type](templates/value-type.md), for the data the system keeps.

## Workflow

1. **Find the corpus.** Look for `spec/` at the repository root. When it is
   absent and the user wants a spec, create `spec/README.md`, `spec/index.md`,
   and `spec/system.md` as
   [Structure](references/profile.md#structure) requires. The README declares
   the profile version and any local exceptions.
2. **Load the rules.** Read the profile.
3. **Choose the type.** Pick the type whose description fits the content.
   When content borders two types, apply the profile's
   [ownership tests](references/profile.md#ownership-tests) before writing.
4. **Place the document.** Put it where the profile's
   [Structure](references/profile.md#structure) and
   [Placement](references/profile.md#placement) rules state, and update each
   affected `index.md`.
5. **Write from the template.** Start from the template's **Suggested
   document**, satisfy its Type contract and the profile's
   [content rules](references/profile.md#content-rules), and link to what
   other documents own instead of restating it. Omit optional and supporting
   sections that would add nothing, as
   [P-DOC-6](references/profile.md#document-conventions) states.
6. **Record gaps.** Record what a person must decide or find out under
   **Open questions** rather than inventing it, as
   [Record gaps instead of inventing](references/profile.md#record-gaps-instead-of-inventing)
   requires.
7. **Review.** Check the document against each numbered rule in its Type
   contract and the profile rules it touches, and cite rule
   identifiers in findings.
8. **Move, rename, or delete deliberately.** Update or remove every inbound
   link, as [Change](references/profile.md#change) requires.

When content concerns something the profile has not yet defined,
follow [P-CON-5](references/profile.md#concerns-not-yet-defined).
