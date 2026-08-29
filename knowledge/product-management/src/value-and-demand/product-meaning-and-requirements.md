---
type: Explanation
title: Product meaning and requirements
description: Where product meaning ends, requirements begin, and use cases provide a bridge without becoming the sole authority.
tags: [product-management, requirements, use-cases, traceability, authority]
status: draft
sources:
  - id: product-value-demand
    resource: value-and-demand-model.md
    title: Product Management — Value and Demand Model
  - id: requirements-neighbors
    resource: https://github.com/craigsmitham/agent-extensions/blob/main/knowledge/requirements-engineering/src/foundations/requirements-and-neighboring-artifacts.md
    title: Requirements Engineering — Requirements and neighboring artifacts
generated:
  by: codex/gpt-5.6
  at: 2026-08-29T20:34:30Z
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
6. verification and product evidence test conformance and value respectively.

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

[^requirements-neighbors]: The Requirements Engineering bundle owns the
    portable boundary between requirements and neighboring artifacts.
[^product-value-demand]: Product meaning remains evidence-backed and revisable;
    a normative downstream artifact does not prove it true.
