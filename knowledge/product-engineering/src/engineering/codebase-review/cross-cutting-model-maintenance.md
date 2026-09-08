---
type: Explainer
title: Maintaining the cross-cutting concern model
description: How the eight cross-cutting records should be stored, projected into views, trialled through classification, task, portability, and review-performance validation, and merged, split, or retired once observed use contradicts the current synthesis.
tags: [codebase-review, cross-cutting-concerns, knowledge-organization, validation, model-evaluation, lifecycle, research-limits, pe-engineering]
status: draft
sources:
  - id: nist-ai-rmf
    resource: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
    title: NIST AI Risk Management Framework — Core
generated: { by: claude/opus-5, at: 2026-09-08T00:00:00Z }
---

# Maintaining the cross-cutting concern model

The eight records in [Cross-cutting concern records](cross-cutting-concern-records.md)
and their [typed pillar edges](cross-cutting-pillar-relationships.md) are a
draft synthesis. This concept covers how that material should be stored,
projected, validated, and eventually revised, so the model is neither frozen
by editorial habit nor rebuilt whenever a new topic appears.

## Organize the knowledge as a lightweight hybrid

Use one canonical typed record for each concern, then derive or maintain
purpose-specific views:

```text
canonical typed records
    -> three-role orientation: context / six concern families / evidence
    -> concern-by-pillar relationship matrix
    -> pillar review criteria and cross-cutting review aids
    -> migration and validation reports
```

This combines the strengths of four organization forms:

| Form | Keep | Avoid |
| --- | --- | --- |
| Layered hierarchy | Fast orientation and clear distinction from product pillars | Pretending a concern has only one parent |
| Faceted classification | Independent subject and role axes | Uncontrolled tags with no definitions |
| Concern-by-pillar matrix | Visible gaps, overlaps, and conditional reach | Treating eighty cells as eighty mandatory checks |
| Typed relationship graph | Explicit direction and mechanism | Requiring graph tooling before the model proves useful |

Do not build a schema, generator, or scoring tool yet. The stable IDs,
definitions, typed tables, and links in these concepts are the canonical source
for the draft. Introduce a machine-readable registry only if comparative use
shows that projections drift or that tools materially improve retrieval and
classification.

When a record becomes machine-readable, preserve at least:

- stable ID, label, aliases, definition, inclusion, and exclusion;
- one primary assessment subject and conceptual role;
- applicability by entity, stakeholder, environment, lifecycle, criticality,
  prerequisites, and explicit non-applicability;
- typed pillar edges with direction, mechanism, conditions, and limitations;
- the assurance claim or review question separately from supporting evidence;
- evidence sources and their validity, representativeness, freshness,
  sufficiency, provenance, and uncertainty limits;
- metrics with construct, unit, method, threshold basis, and uncertainty;
- heuristics marked as defeasible, including overrides and false positives;
- review procedures as separate aids;
- threats, tradeoffs, authority, provenance, version, review date, and known
  disagreement; and
- distinct states for unknown, not assessed, not applicable, and insufficient
  evidence.

## Keep the implementation outcome-first

The implemented criteria start from a pillar outcome and identify which
cross-cutting records materially affect its assessment. The framework does not
create eight additional ten-item checklists. A cross-cutting concept deserves a
separate checklist only when its own subject has a distinct review job and
verdict.

## Validate before treating the model as stable

This synthesis resolves the research alternatives, but it has not yet been
validated in representative reviews. Use four forms of validation:

1. **Classification trials:** have independent reviewers classify a held-out
   sample of criteria and findings by subject, role, canonical record, and
   relationship type. Analyze disagreements by field instead of collapsing
   them into one agreement score.
2. **Task trials:** test whether users can find a concern, explain why it is
   not a pillar, distinguish it from its nearest neighbor, and state when a
   pillar edge does not apply.
3. **Portability trials:** use libraries, interactive applications, services,
   data systems, embedded or safety-relevant systems, and multi-package
   repositories across different technology stacks.
4. **Review-performance trials:** compare the model with an unconstrained
   review, credible alternative quality models, and alternative layer
   presentations on material coverage, overlap, unsupported claims, false
   assurance, evidence quality, uncertainty preservation, time, and cost.

For frontier-model use, bind every result to the exact model, version,
configuration, prompt, tool access, repository revision, record version, and
case set. Test ID, subject, role, edge, applicability, abstention, and citation
accuracy separately. Include overlapping terms, paraphrases, reordered
material, missing context, contradictory evidence, irrelevant signals, and
unknown cases. NIST's AI RMF similarly connects evaluation to declared context,
representative conditions, documented measures, uncertainty, and continuing
assessment of the measurement process itself.[^nist-ai-rmf]

Do not use majority model agreement as ground truth. Predeclare acceptance
thresholds by the consequence of each error class, preserve harness errors and
unknowns, and rerun the same cases after a taxonomy, prompt, model, or tool
change.

## Research limits and lifecycle

The eight records are a design synthesis, not categories asserted verbatim by
one authority. The research compared product-quality, requirements,
architecture, measurement, assurance, V&V, configuration, secure-development,
supply-chain, observability, testing, and model-evaluation sources. No located
source establishes a natural number of cross-cutting concerns, a universal
breadth threshold, or a context-free relationship matrix.

The candidate rejects a flat list because product outcomes, supporting
artifacts, engineering-system capabilities, methods, and evidence have
different subjects and verdicts. It also rejects an immediately implemented
knowledge graph because the maintenance cost is unjustified before
classification and task trials. The hybrid is intended to be the smallest
structure that preserves subject, role, conditionality, and evidence limits.

Review the model when the product-pillar taxonomy changes, classification
trials show persistent overlap or gaps, a record loses independent
assessability, or a new concern passes the admission gate more cleanly than an
existing one. Merge, split, demote, or retire records based on observed use;
do not preserve eight as an editorial quota.

[^nist-ai-rmf]: NIST, [AI Risk Management Framework core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).
