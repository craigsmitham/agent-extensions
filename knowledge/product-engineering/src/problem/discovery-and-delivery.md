---
type: Explanation
title: Discovery and delivery
description: How product discovery reduces uncertainty while product delivery creates and operates a trustworthy solution, with learning continuing across both.
tags: [product-discovery, product-delivery, prototypes, production, learning, pe-problem]
status: draft
sources:
  - id: svpg-product-model-concepts
    resource: https://www.svpg.com/product-model-concepts/
    title: SVPG — Product Model Concepts
  - id: svpg-build-to-learn
    resource: https://www.svpg.com/build-to-learn-faq/
    title: SVPG — Build To Learn FAQ
  - id: product-value-demand
    resource: value-and-demand-model.md
    title: What to solve — Value and demand model
generated:
  by: claude/opus-5
  at: 2026-09-08T00:00:00Z
---

# Discovery and delivery

Product discovery seeks evidence for an effective solution before the team
commits unnecessarily to building it. Product delivery builds, tests, deploys,
and operates a production-quality solution. They are different kinds of work,
not separate departments or a one-way phase gate.[^svpg-product-model-concepts]

Discovery optimizes for learning. It uses the cheapest responsible evidence
capable of testing a material product risk: conversation, data, prototype,
simulation, technical investigation, or limited experiment. A prototype is
allowed to omit production qualities that are irrelevant to the question being
tested.[^svpg-build-to-learn]

Offerings, audiences, needs, jobs, and value propositions begin as candidate
product meaning. Discovery tests their important relationships and competing
explanations; it should not turn early labels into facts merely because they
appear in a planning artifact.[^product-value-demand]

Delivery optimizes for trustworthy value in real use. Reliability, security,
performance, accessibility, maintainability, observability, support, and safe
operation cannot be inferred from a discovery prototype.

Learning continues after release. Production behavior provides evidence that
discovery could not, including adoption, unintended consequences, operational
cost, and whether the expected outcome occurred. That evidence may reopen the
problem or invalidate the solution.

Discovery without delivery produces learning but no sustained value. Delivery
without discovery efficiently produces untested bets. Product teams remain
responsible for joining both.

[^svpg-product-model-concepts]: SVPG — Product Model Concepts, which treats
    discovery and delivery as distinct kinds of product work carried out by the
    same team.
[^svpg-build-to-learn]: SVPG — Build To Learn FAQ, which distinguishes building
    to learn from building to earn and explains why a prototype need not carry
    production qualities.
[^product-value-demand]: [Value and demand model](value-and-demand-model.md)
    requires evidence and explicit maturity for these concepts and their
    relationships.
