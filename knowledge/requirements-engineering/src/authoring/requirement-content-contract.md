---
type: Reference
title: Requirement content contract
description: Defines the minimum semantic content needed for a durable, reviewable, assessable requirement.
tags: [requirement, content-contract, identity, evidence, traceability, requirements-engineering]
generated: { by: codex/gpt-6, at: 2026-11-11T19:45:59Z }
sources:
- id: prior-authoring-requirements
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/requirements-engineering/src/authoring/authoring-requirements.md
  title: Authoring requirements
---

# Requirement content contract

A durable requirement should preserve these semantics, whether they appear as
native fields, prose, a model, or linked records:

| Content | Purpose |
| --- | --- |
| Stable identity and title | Supports reference, change, and lineage |
| Maturity and authority | Distinguishes candidate from normative obligation |
| Obligated subject | Identifies what must comply |
| Conditions and trigger | Bounds when the obligation applies |
| Required or prohibited outcome | States the obligation itself |
| Scope, exceptions, and terms | Prevents hidden interpretations |
| Source and rationale | Preserves provenance and intent |
| Classification | Supports discovery and fit-for-purpose review |
| Relationships | Links parents, refinements, conflicts, realization, and evidence |
| Verification approach | Identifies a credible way to assess satisfaction |
| Validation basis | Identifies why the obligation serves intended need |
| Open questions and assumptions | Makes uncertainty visible |
| Change history or decision evidence | Preserves authority over time |

Not every item must be a heading. Prefer native structured fields when they
carry the semantics exactly. Omit inapplicable content deliberately; do not
silently omit information that remains unknown.

This contract governs requirements. The work item that investigates, proposes,
or coordinates a change to one has its own slots in the work-item content
contract (shared concept: `@craigsmitham/knowledge/software-engineering-foundations#work-items/work-item-content-contract`).
The two are often filled at the same time and neither supplies the other's
semantics: reference the requirement from the work item instead of restating
it.

## Obligation and level

The obligation names a subject, applicable condition or trigger, explicit
normative force, and observable outcome, limit, or prohibition. Terms, units,
scope, and exceptions bound its interpretation. Rationale explains the
obligation without becoming another obligation.

Stakeholder needs may precede solution selection. System obligations belong at
the externally meaningful boundary; lower-level allocation requires an accepted
decision or genuine constraint and links back to parent intent. An implementation
preference is not an accepted constraint.

Separate independently decidable obligations; retain an atomic rule or invariant
whose meaning would be destroyed by splitting. Vague qualifiers and unbounded
terms need an explicit interpretation, not invented precision.

The [individual review criteria](../review/reviewing-individual-requirements.md)
and [set review criteria](../review/reviewing-requirement-sets.md) define the
quality checks used with this contract. Local policy and host representation
(shared concept: `@craigsmitham/knowledge/software-engineering-foundations#local-policy-and-host-representation`)
owns adaptation rules; requirement authority remains independent of its host's
workflow status.
