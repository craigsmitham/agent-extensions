---
type: Explainer
title: Cross-cutting relationships to the quality pillars
description: Supplies the seven directed relationship types that replace a bare "relates to" edge, the compact concern-by-pillar discovery matrix, and the placement of testing, testability, and test-suite quality across those edges.
tags: [codebase-review, cross-cutting-concerns, relationship-types, traceability-matrix, testability, test-suite-quality, tradeoffs, pe-engineering]
status: draft
sources:
  - id: test-desiderata
    resource: https://testdesiderata.com/
    title: Test Desiderata
  - id: pstack
    resource: https://github.com/cursor/plugins/tree/main/pstack
    title: Cursor plugins — pstack
generated: { by: claude/opus-5, at: 2026-09-08T00:00:00Z }
---

# Cross-cutting relationships to the quality pillars

Each record defined in [Cross-cutting concern records](cross-cutting-concern-records.md)
reaches the [ten quality pillars](software-quality-pillars.md) through typed,
conditional edges. This concept supplies the edge vocabulary, the compact
matrix used to discover candidate edges, and the specific placement of testing
terms that otherwise migrate between layers. The admission gate that decides
which records exist at all is in
[Cross-cutting concerns for software quality](cross-cutting-concerns.md).

## Type the relationships to the pillars

Use these directed relationship types. Do not write a bare “relates to” edge.

| Code | Relationship | Meaning |
| --- | --- | --- |
| `CON` | Constitutes | The source is part of the definition of the target outcome; use rarely because most cross-cutting records should not constitute a pillar. |
| `CTR` | Contributes | The source can causally help or impair the target without being necessary or sufficient. |
| `EN` | Enables | The source makes achievement or assessment of the target feasible or materially easier. |
| `EV` | Evidences | The source can provide grounds for a judgment about the target. |
| `CS` | Constrains | The source sets scope, bounds, obligations, or decision conditions for the target. |
| `TH` | Threatens | The source describes a way the target can be impaired. |
| `TR` | Trades off | A decision involving the source may improve one target while impairing another. |

Every maintained edge should record its direction, mechanism, applicability,
evidence basis, limitation or counterexample, and lifecycle scope. The matrix
below is a compact discovery view, not a proof or an instruction to force a
finding into every cell. Parentheses mean the relationship is especially
context-dependent. An enabling edge refers to the record's desired state; a
threatening edge can refer to a deficiency in that state or to an adverse
element represented by the record.

| Record | Suitability | Correctness | Reliability | Security | Safety | Efficiency | Usability | Compatibility | Evolvability | Intelligibility |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Claim context | `CS` | `CS` | `CS` | `CS` | `CS` | `CS` | `CS` | `CS` | `CS` | `CS` |
| Specification | `EN·EV` | `EN·EV` | `EN·EV` | `EN·EV` | `EN·EV` | `EN·EV` | `EN·EV` | `EN·EV` | `(EN·EV)` | `(EN·EV)` |
| Structure | `(CTR·TR)` | `CTR·EV` | `CTR` | `CTR·TR` | `CTR·TR` | `CTR·TR` | `(CTR·TR)` | `CTR·TR` | `CTR` | `CTR` |
| Lifecycle integrity | `(EN·TH)` | `EN·EV·TH` | `EN·EV·TH` | `EN·EV·TH` | `EN·EV·TH` | `(EN·EV)` | `(EN·TH)` | `EN·EV·TH` | `EN` | `EN·EV` |
| Risk | `TH·CS·TR` | `TH·CS·TR` | `TH·CS·TR` | `TH·CS·TR` | `TH·CS·TR` | `TH·CS·TR` | `TH·CS·TR` | `TH·CS·TR` | `TH·CS·TR` | `TH·CS·TR` |
| Assurance | `EN·EV` | `EN·EV` | `EN·EV` | `EN·EV` | `EN·EV` | `EN·EV` | `EN·EV` | `EN·EV` | `EN·EV` | `EN·EV` |
| Feedback | `EV` | `EV` | `EN·EV` | `EN·EV·TH` | `EN·EV·TH` | `EV·TR` | `(EV·TR)` | `(EV)` | `EN·EV` | `EN·EV` |
| Evidence | `EV·CS·TR` | `EV·CS·TR` | `EV·CS·TR` | `EV·CS·TR` | `EV·CS·TR` | `EV·CS·TR` | `EV·CS·TR` | `EV·CS·TR` | `EV·CS·TR` | `EV·CS·TR` |

The matrix deliberately contains no `CON` edges. If a proposed cross-cutting
record routinely constitutes only one pillar, it is probably a subquality of
that pillar. If it appears to constitute many pillars, it is probably a broad
synonym for product quality rather than a useful cross-cutting record.

## Place testing and testability precisely

Testing occupies several positions because the word can name different
subjects and roles.

| Term | Subject and role | Placement |
| --- | --- | --- |
| Product testability | Product; subquality | Primarily a subquality of Evolvability in this taxonomy whose presence affords assurance across any pillar whose behavior must be investigated |
| Testing | Review or lifecycle activity; assurance mechanism | `XC-06` Assurance; one member of a portfolio, not the product-quality outcome |
| Test-suite quality | Supporting-artifact quality | Assessed within Assurance and governed by `XC-08` Evidence; it asks whether tests are valuable and sustainable as grounds for claims |
| Test result | Evidence item | `XC-08` Evidence; its relevance, validity, provenance, representativeness, freshness, and limits determine what it can support |
| Test process | Review protocol or engineering-system practice | Method guidance outside the product pillars and outside the stable concern definitions |
| Passing tests | Observation | Evidence for only the claims, versions, conditions, and oracles the tests actually cover; never a synonym for product quality |

Test Desiderata is therefore a valuable model for the **quality of tests**,
not a rival product-quality taxonomy. Its properties include isolation,
composability, determinism, speed, writability, readability, behavioral
sensitivity, structure insensitivity, automation, specificity, predictive
power, and confidence—and explicitly recognize interactions and
tradeoffs.[^test-desiderata] Those properties should inform Assurance and
Evidence criteria without being collapsed into product testability or treated
as independently maximizable scores. The
[Test-suite quality criteria](supporting/test-suite-quality.md) checklist is
where that supporting-artifact verdict is recorded.

The pstack plugin supplies a complementary practitioner datapoint. It combines
product goals, design principles, verification practices, model-coordination
protocols, and code-shape heuristics in one operating system.[^pstack] The
typed model preserves that useful material while routing it to Structure,
Assurance, Feedback, Evidence, or an optional method aid instead of treating
the entire operating system as a timeless quality category.

[^test-desiderata]: Beck and Sutton, [Test Desiderata](https://testdesiderata.com/).
[^pstack]: Cursor, [pstack](https://github.com/cursor/plugins/tree/main/pstack).
