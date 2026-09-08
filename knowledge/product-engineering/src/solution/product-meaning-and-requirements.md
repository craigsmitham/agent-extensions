---
type: Explanation
title: Product meaning and requirements
description: Where product meaning ends, requirements begin, and use cases provide a bridge without becoming the sole authority.
tags: [product-management, requirements, use-cases, traceability, authority, pe-solution]
status: draft
sources:
  - id: product-value-demand
    resource: ../problem/value-and-demand-model.md
    title: What to solve — Value and demand model
  - id: requirements-neighbors
    resource: requirements/foundations/requirements-and-neighboring-artifacts.md
    title: What to build — Requirements and neighboring artifacts
generated:
  by: claude/opus-5
  at: 2026-09-08T00:00:00Z
---

# Product meaning and requirements

Product meaning explains why an offering should matter: the relevant audience,
need, job, value proposition, strategy, and intended outcome. Requirements state
normative expectations that a system, service, process, or other subject must
satisfy. One informs the other, but neither should silently become the other's
authority.[^requirements-neighbors]

A useful flow is:

1. Product concepts express candidate meaning and value.
2. Behavioral views explore how value could appear at a system or service
   boundary.
3. Requirement candidates make proposed obligations explicit.
4. An authorized requirements process accepts, changes, or rejects normative
   requirements.
5. Architecture and design choose a realization.
6. Verification and product evidence test conformance and value respectively.

This is a relationship model, not a mandatory sequence or document set.
Iteration may revise an earlier concept, and teams may represent several views
in one tool if authority remains clear.

## Use cases as a bridge

A use case describes an actor pursuing an outcome through interactions at a
system boundary. It can connect a Job, Need, or Value Proposition to observable
behavior and expose candidate requirements.

A use case is not automatically:

- the authoritative statement of a customer Job;
- a complete set of requirements;
- an implementation design;
- evidence that the proposed behavior creates value; or
- a mandatory product-management artifact.

Keep preconditions, main and alternate flows, outcomes, and exceptions at the
behavioral boundary. Move normative obligations into the project's accepted
requirements form, and move realization decisions into design or architecture.

## Preserve traceability without authority leakage

Traceability should answer why a requirement exists, what product meaning it
supports, how it is realized, and what evidence tests it. A link does not grant
the source artifact permission to overwrite the target.

When product evidence challenges an assumption, revisit the affected product
concepts and deliberately assess linked requirements. When requirements change,
assess the value hypothesis and intended outcome rather than assuming they are
unchanged. Record unresolved conflict instead of forcing artificial
consistency.[^product-value-demand]

[^requirements-neighbors]: [Requirements and neighboring
    artifacts](requirements/foundations/requirements-and-neighboring-artifacts.md)
    owns the portable boundary between a requirement and the goals, designs,
    plans, tests, evidence, and work items around it.
[^product-value-demand]: [Value and demand model](../problem/value-and-demand-model.md) —
    product meaning remains evidence-backed and revisable; a normative
    downstream artifact does not prove it true.
