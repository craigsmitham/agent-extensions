---
type: Pattern
title: Pattern library
description: Maintain recurring guidance as a problem-indexed, evidence-bearing catalog shaped by reader needs, with consistent anatomy, meaningful relationships, ownership, and feedback from use.
tags: [docs, pattern-library, catalog, evidence, discovery, lifecycle]
status: stable
sources:
  - id: hillside-patterns
    resource: https://hillside.net/patterns
    title: Hillside Group — Design Patterns Library
  - id: patterns-faq
    resource: https://gee.cs.oswego.edu/dl/pd-FAQ/pd-FAQ.html
    title: Patterns-discussion FAQ
  - id: pattern-writing-language
    resource: https://www.hillside.net/index.php/a-pattern-language-for-pattern-writing
    title: Meszaros and Doble — A Pattern Language for Pattern Writing
  - id: fowler-writing-patterns
    resource: https://martinfowler.com/articles/writingPatterns.html
    title: Martin Fowler — Writing Software Patterns
  - id: azure-cloud-patterns
    resource: https://learn.microsoft.com/en-us/azure/architecture/patterns/
    title: Microsoft Azure Architecture Center — Cloud design patterns
  - id: govuk-pattern
    resource: https://design-system.service.gov.uk/patterns/check-a-service-is-suitable/
    title: GOV.UK Design System — Check a service is suitable
  - id: va-maturity
    resource: https://design.va.gov/about/maturity-scale
    title: VA Design System — Maturity scale
  - id: collection-value
    resource: https://wirfs-brock.com/rebecca/papers/valueofpatterncollections/
    title: Wirfs-Brock and Hvatum — The Value of Pattern Collections (2026 preprint)
  - id: who-will-read
    resource: https://wirfs-brock.com/rebecca/papers/whowillread/
    title: Wirfs-Brock and Hvatum — Who Will Read My Patterns?
  - id: pattern-smells
    resource: https://wirfs-brock.com/rebecca/papers/patternsmells/
    title: Wirfs-Brock and Kohls — Pattern Smells, Get Rid of Them (2026 preprint)
  - id: generative-patterns
    resource: https://wirfs-brock.com/rebecca/papers/explrgenpat2023/
    title: Hvatum and Wirfs-Brock — Exploring the Generative Nature of Patterns
generated: { by: "codex/gpt-6", at: 2026-10-30T20:12:16Z }
---

# Pattern library

Maintain recurring guidance as a **problem-indexed, evidence-bearing catalog
shaped by reader needs, with consistent anatomy, meaningful relationships,
ownership, and feedback from use**.

## Context

A community has accumulated recurring solutions across projects, systems, or
teams. The knowledge is too conditional to reduce to universal rules and too
variable to ship as one reusable implementation. Practitioners need to
recognize, compare, adapt, and combine the solutions.

## Problem

How can a community preserve reusable experience without producing an
unsearchable folder of essays, a rigid standards manual, or a catalog of
unsubstantiated preferences?

Isolated pages do not establish shared vocabulary or reveal alternatives.
Uniform templates can improve scanning while encouraging authors to fill
headings without establishing recurrence, evidence, or useful relationships.

## Forces

- **Consistency versus expressive fit** — entries must be comparable without
  forcing every subject into identical prose.
- **Scanability versus depth** — readers need quick selection and enough
  rationale to adapt safely.
- **Evidence versus contribution cost** — trust requires known uses and review,
  while excessive gates prevent useful candidates from emerging.
- **Local autonomy versus shared vocabulary** — realizations vary, but names
  and invariants must remain stable enough for collaboration.
- **Stability versus learning** — adopted patterns need dependable identities,
  yet evidence can narrow, supersede, or invalidate them.
- **Individual usefulness versus composition** — each entry should stand alone
  while relationships help solve larger problems.

## Solution

Identify who needs the collection and what improvement they seek. Begin with
a useful core, test it with practitioners, and grow from feedback about its
application.[^collection-value] Make underlying design values explicit so
readers can judge compatibility with their own context.[^generative-patterns]

Create a maintained **pattern library** with:

1. a concise intent thumbnail for every pattern;
2. problem-first discovery by context, problem, force, or goal rather than
   technology alone;
3. a consistent semantic core — name, context, problem, forces, solution,
   consequences, applicability, evidence, and related patterns;
4. flexible optional sections for diagrams, examples, variants, or
   implementation notes;
5. visible maturity that distinguishes candidates, established guidance, and
   deprecated patterns;
6. typed relationships such as *alternative to*, *complements*, *precedes*,
   *follows*, *specializes*, and *conflicts with*;
7. named ownership, contribution, review, and retirement paths; and
8. stable identities and redirects when a pattern is renamed or superseded.

Keep illustrative examples distinct from known uses. Treat the library as a
maintained knowledge product, not a directory convention.

Support both quick lookup and learning through a connected example or story.
Readers may enter with different experience and purposes; test their routes
through the collection. Where related papers become one collection, reconcile
terminology, repetition, and reading order instead of merely gathering the
papers in one place.[^who-will-read]

Provide a route for users to report adaptations, failures, and outcomes.
Use those reports to revise the collection and decide what to add, replace,
or retire. Plan how intended readers will discover it and learn about
updates, and who will sustain that work. Publication alone does not establish
value; assess benefits for practitioners and the people affected by their
designs.[^collection-value]

## Consequences

- Practitioners gain shared vocabulary and can compare tradeoffs before
  choosing a solution.
- Evidence and maturity make uncertainty visible instead of hiding it behind
  “best practice.”
- Typed relationships enable composition and reveal gaps or overlaps.
- Consistent anatomy improves browsing but creates ongoing editorial work.
- Ownership, review, and deprecation require durable governance capacity.
- A library without active use and maintenance becomes a graveyard of plausible
  advice.

## Illustrative use

A documentation team starts with [Runbook](runbook.md) and
[Playbook](playbook.md) entries for recurring operational writing problems.
An author chooses Runbook to document a rollback procedure, then Playbook to
support incident diagnosis and coordination, linking that playbook to the
runbook. The produced documents are instances; the library holds reusable
pattern descriptions. Trial authors confuse the two entries, so maintainers
revise their selection cues and relationship before expanding the catalog.
This hypothetical sequence illustrates adaptation and feedback; it is not a
known use or a mandatory order of patterns.

## When to use

Use this pattern when:

- several reusable solutions recur across independent contexts;
- practitioners need to choose or combine them;
- their applicability and tradeoffs cannot be captured as unconditional rules;
  and
- someone can own evidence, review, and lifecycle.

## When not to use

- There is only one unvalidated idea — publish a candidate note or continue
  observing.
- One reusable implementation already solves the problem without material
  contextual variation.
- The collection is authoritative interface description — use reference
  documentation.
- No community is willing to maintain or use the catalog.

## Evidence and known uses

The Hillside patterns community demonstrates shared vocabulary, known uses,
review, and relationships across pattern collections. Azure makes problem and
tradeoff matching central to selection. GOV.UK surfaces when to use, when not
to use, research, known issues, and contribution. The VA Design System makes
maturity depend on evidence, adoption, stability, and deprecation. Together
these independent libraries support the recurring solution while showing that
no single page template is universal.

Wirfs-Brock and Hvatum propose the product-lifecycle framing used here as a
way to improve collections' continuing value. Their essay is a rationale for
the approach, not empirical validation of this whole library
pattern.[^collection-value]

## Pattern language threshold

A library becomes a **pattern language** only when relationships and useful
sequences help readers generate coherent larger solutions. A catalog with
cross-links is not automatically a language. Make the stronger claim only when
the collection guides movement from context through related choices and
resulting problems.

Show a plausible route through a larger problem, including patterns at the
scales needed to resolve its subproblems and enough coverage to support the
intended whole. A map should expose useful local connections and entry points.
Keep it open to alternatives and patterns from
other collections; an exhaustive link graph is insufficient.[^pattern-smells]

## Related patterns

- [Concept boundaries](concept-boundaries.md) — complements the library when
  readers repeatedly confuse neighboring concepts and need one canonical
  comparison.
- [Playbook](playbook.md) — guides assessment, response choices, and coordination
  for a recurring class of situations.
- [Runbook](runbook.md) — specifies repeatable execution of a bounded operational
  task.
- [Pattern explainer](../explainers/pattern.md) — defines the pattern form and
  its boundaries.
- [Pattern guide](../guides/pattern.md) — supplies the mining, authoring,
  review, and maintenance process for individual entries.

[^collection-value]: Wirfs-Brock and Hvatum, [The Value of Pattern Collections](https://wirfs-brock.com/rebecca/papers/valueofpatterncollections/), 2026 preprint.
[^who-will-read]: Wirfs-Brock and Hvatum, [Who Will Read My Patterns?](https://wirfs-brock.com/rebecca/papers/whowillread/).
[^pattern-smells]: Wirfs-Brock and Kohls, [Pattern Smells, Get Rid of Them](https://wirfs-brock.com/rebecca/papers/patternsmells/), 2026 preprint.
[^generative-patterns]: Hvatum and Wirfs-Brock, [Exploring the Generative Nature of Patterns](https://wirfs-brock.com/rebecca/papers/explrgenpat2023/).
