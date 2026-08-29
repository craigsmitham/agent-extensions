---
type: Guide
title: Developing value and demand concepts
description: Use this guide when a team needs to draft, relate, test, or maintain Offering, Audience, Need, Job to Be Done, and Value Proposition concepts without adopting a prescribed artifact system.
tags: [product-management, offering, audience, needs, jobs-to-be-done, value-proposition]
status: draft
sources:
  - id: product-value-demand
    resource: value-and-demand-model.md
    title: Product Management — Value and Demand Model
  - id: product-jtbd
    resource: jobs-to-be-done.md
    title: Product Management — Jobs to Be Done
generated:
  by: codex/gpt-5.6
  at: 2026-08-29T20:34:30Z
---

# Developing value and demand concepts

Use the smallest set of concepts needed to make a product decision. A team may
store them in product documentation, a research repository, a canvas, a model,
or another native system. The content contract matters more than the form.

## 1. Frame the decision

State the decision these concepts must inform, who will use them, the scope,
and the evidence horizon. Avoid creating a complete taxonomy when the immediate
question concerns one offering and one audience.

## 2. Draft the relevant concepts

For each concept, include enough content to distinguish it and test it:

| Concept | Minimum useful content | Common failure |
| --- | --- | --- |
| **Offering** | Name, coherent boundary, value-bearing capabilities, delivery context | Naming a feature or internal component as if it were a complete offering |
| **Audience** | Shared circumstances or behavior, inclusion boundary, decision-relevant variation | Demographics or role labels with no relevance to the decision |
| **Need** | Actor or audience, desired state or problem, context, evidence | Restating a preferred solution as a need |
| **Job to Be Done** | Actor, circumstance, progress sought, relevant dimensions | Writing a task list or product interaction |
| **Value Proposition** | Offering, audience, need or job, expected benefit, alternatives, differentiator | An unsupported slogan or generic benefit |

Use identifiers only where the hosting system needs stable references. Do not
make a field mandatory merely because another tool or process uses it.

## 3. Relate without collapsing

Record only relationships that matter to the decision, such as:

- Offering serves Audience;
- Audience experiences Need;
- Audience pursues Job;
- Job relates to Need; and
- Value Proposition connects Offering to an Audience and a Need or Job.

Keep the concepts distinct even when a single document presents them together.
The model is a graph, so do not invent parent-child ownership where evidence
only supports an association.[^product-value-demand]

## 4. Attach evidence and maturity

For each material assertion, record:

- evidence or a traceable source;
- whether it is candidate, supported, contested, or retired;
- important counterevidence or alternatives;
- an owner or steward; and
- the event or date that should trigger review.

Choose evidence that can answer the claim. Preference surveys do not prove
choice, a stakeholder assertion does not prove a customer need, and initial
adoption does not prove sustained value.

## 5. Test the risky relationships

Prioritize assumptions whose failure would change the product decision. Test
whether the audience actually encounters the circumstance, whether the need or
job matters enough to cause action, whether the offering supplies the promised
benefit, and whether alternatives undermine the proposed differentiation.
Jobs-oriented inquiry should be anchored in actual decisions and change, not
only hypothetical preference.[^product-jtbd]

## 6. Project into downstream work

Translate supported product meaning into the consuming project's native
artifacts. A requirements process may derive requirement candidates; a product
team may frame an outcome or opportunity; a strategy process may revise a
choice; a tracker may coordinate work.

Preserve links and the distinct authority of each artifact. Updating a work
item must not silently rewrite a customer need, and changing a value
proposition must not silently change an accepted requirement.

## Review

Before relying on the result, check that:

- every concept answers its own question;
- no solution is disguised as a Need or Job;
- Value Propositions name an expected benefit and relevant alternative;
- material relationships have evidence and visible uncertainty;
- terms are understandable outside the authoring team; and
- downstream commitments are governed by their own authority and lifecycle.

[^product-value-demand]: The value and demand model explains why these concepts
    form an evidence-backed graph rather than a document hierarchy.
[^product-jtbd]: The Jobs to Be Done explanation covers circumstance, progress,
    behavior, and forces around change.
