---
name: spec
description: >
  Creates and manages specifications for a software system. Use when asked to
  create, revise, organize, or maintain a system's specs.
---

# Spec

Create and manage specifications for a software system.

Represent specs as an OKF v0.2 bundle that follows the
[Spec profile](references/profile.md) and the modules the corpus adopts. The
profile, each adopted module, and each template's **Type contract** are
normative, and the other template sections guide authoring. The numbered
rules are the checklist for writing and reviewing a document. Examples follow
the [running example](references/example.md).

## Concept types

The core types specify most systems. Only `system.md` is required at the
start; write `business.md` and `glossary.md` once their content is known.

- [System](templates/system.md)
- [Business Requirements](templates/business-requirements.md)
- [User Class](templates/user-class.md)
- [External Interface](templates/external-interface.md)
- [Feature](templates/feature.md)
- [Use Case](templates/use-case.md)
- [Requirement](templates/requirement.md)
- [Glossary](templates/glossary.md)

Adopt a module when the system needs its types:

- [Decomposition](references/modules/decomposition.md):
  [Subsystem](templates/subsystem.md) and
  [Feature Component](templates/feature-component.md), when part of the
  system or of a feature meets the creation condition in its Type contract.
- [Rules](references/modules/rules.md):
  [Business Rule](templates/business-rule.md), for rules the business would
  keep without the system.
- [Quality](references/modules/quality.md):
  [Quality Characteristic](templates/quality-characteristic.md) and
  [Quality Requirement](templates/quality-requirement.md), for required levels
  of quality.
- [Data](references/modules/data.md): [Entity Type](templates/entity-type.md)
  and [Value Type](templates/value-type.md), for the data the system keeps.

## Workflow

1. **Find the corpus.** Look for `spec/` at the repository root. When it is
   absent and the user wants a spec, create `spec/README.md`, `spec/index.md`,
   and `spec/system.md` as
   [Structure](references/profile.md#structure) requires. The README declares
   the profile version, the adopted modules, and any local exceptions.
2. **Load the rules.** Read the profile and each module the README declares.
   Adopt a module, and declare it, before writing the first document of its
   types.
3. **Choose the type.** Pick the type whose description fits the content.
   When content borders two types, apply the ownership tests of the profile
   and adopted modules before writing. When the owning type belongs to a
   module the corpus has not adopted, follow the profile's
   [modules](references/profile.md#modules) table or adopt the module.
4. **Place the document.** Put it where the profile's
   [Placement](references/profile.md#placement) rules and adopted modules
   state, and update each affected `index.md`.
5. **Write from the template.** Start from the template's **Suggested
   document**, satisfy its Type contract and the profile's
   [content rules](references/profile.md#content-rules), and link to what
   other documents own instead of restating it. Omit empty optional sections.
6. **Record gaps.** Record what is unknown under **Open questions** rather
   than inventing it, as
   [Record gaps instead of inventing](references/profile.md#record-gaps-instead-of-inventing)
   requires, and keep the document `status: draft`.
7. **Review.** Check the document against each numbered rule in its Type
   contract and the profile and module rules it touches, and cite rule
   identifiers in findings.
8. **Change status deliberately.** Only a person with authority to accept a
   document makes it `stable`, as
   [Status and change](references/profile.md#status-and-change) requires.
   Deprecate rather than delete a concept that others link to, and update
   inbound links when moving or renaming.

When content concerns something the profile or a module has not yet defined,
follow [P-CON-5](references/profile.md#concerns-not-yet-defined).
