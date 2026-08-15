---
type: Explanation
title: YAGNI and speculative complexity
description: How to defer unsupported capability, compare the costs of premature flexibility, and preserve changeability without neglecting present quality.
tags: [yagni, simple-design, evolutionary-design, speculative-generality, premature-abstraction, reversibility]
status: draft
sources:
  - id: fowler-yagni
    resource: https://martinfowler.com/bliki/Yagni.html
    title: Martin Fowler — Yagni
  - id: agile-simple-design
    resource: https://agilealliance.org/glossary/simple-design/
    title: Agile Alliance — Simple Design
  - id: metz-wrong-abstraction
    resource: https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction
    title: Sandi Metz — The Wrong Abstraction
  - id: aws-review-process
    resource: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/the-review-process.html
    title: AWS Well-Architected Framework — The review process
  - id: anthropic-effective-agents
    resource: https://www.anthropic.com/engineering/building-effective-agents
    title: Anthropic — Building effective agents
  - id: openai-gpt5-coding
    resource: https://cdn.openai.com/API/docs/gpt-5-for-coding-cheatsheet.pdf
    title: OpenAI — GPT-5 for Coding
generated:
  by: codex/gpt-5
  at: 2026-08-15T15:20:54Z
---

# YAGNI and speculative complexity

YAGNI—“you aren't gonna need it”—rejects capability whose value depends only
on a possible future requirement. It is an evidence rule, not a preference for
short code: choose the smallest complete solution justified by present needs.

## What counts as present evidence

Added complexity should serve at least one of these:

- an accepted, verifiable outcome;
- an existing contract or invariant;
- observed behavior or a reproduced failure;
- an applicable repository or platform obligation; or
- a concrete risk to correctness, security, data integrity, compatibility, or
  operability.

“Might,” “eventually,” “future-proof,” and “make it generic” identify a possible
need, not evidence that the need exists. A vague request for extensibility should
be translated into a concrete variation or quality requirement before it drives
design.

## The cost of building early

Speculative capability imposes more than its initial implementation cost.
Fowler distinguishes the cost to build it, the value delayed while building it,
the continuing cost of carrying its complexity, and the cost of repairing a
guess that later proves wrong.[^fowler-yagni] These costs apply to features,
abstractions, configuration, extension points, dependencies, architecture, and
process.

Premature abstraction is particularly expensive because it guesses which cases
should vary together. When later requirements differ, callers accumulate
parameters and conditional paths to preserve a shared shape that was never
actually shared. Metz argues that visible duplication can be cheaper than this
wrong abstraction while the real commonality is still emerging.[^metz-wrong-abstraction]

## A practical decision test

Before adding an option, layer, dependency, migration, abstraction, tool, or
workflow step, ask:

1. What present evidence requires it?
2. What smaller conventional solution satisfies the same evidence?
3. What complexity will every intervening change have to carry?
4. How costly would it actually be to add the capability when the need appears?
5. Is the current decision reversible?

If the only answer is a hypothetical future, defer the capability. Simple
design treats design as continuous work and delays decisions until the last
responsible moment, when more evidence is available.[^agile-simple-design]

## Preserve changeability, not imagined capability

YAGNI depends on evolutionary design. Local refactoring, clear responsibilities,
tests, continuous integration, and delivery automation can be justified by the
present need to keep change safe and affordable. They do not implement a future
feature merely because they make one easier to add.

This distinction prevents two opposite mistakes:

- building unused flexibility in the name of maintainability; and
- accepting brittle, opaque, or unverified work in the name of minimalism.

## Irreversible decisions and required qualities

Reversibility changes the amount of evidence and review a decision deserves.
AWS distinguishes lightweight, reversible “two-way door” decisions from
difficult-to-reverse “one-way doors” that warrant earlier inspection.[^aws-review-process]
When delay would create material lock-in, preserve the cheapest useful option:
record the constraint, isolate volatile knowledge, run a focused experiment, or
choose a reversible seam. Do not implement the full imagined future.

YAGNI does not override present quality obligations. Required security,
correctness, data integrity, accessibility, compatibility, reliability, and
verification are current constraints even when the feature request does not
repeat them.

## Agentic work

For an agent, speculative complexity includes activity as well as artifacts:
broad research, adjacent cleanup, extra tooling, delegation, orchestration, and
continued polishing after the accepted outcome is verified. Anthropic advises
starting with the simplest agentic solution and increasing complexity only when
needed because additional orchestration trades cost and latency for capability
and creates opportunities for compounded error.[^anthropic-effective-agents]
OpenAI likewise recommends controlling coding-agent eagerness and tool budgets
because default thoroughness can exceed what a task needs.[^openai-gpt5-coding]

An agent should therefore:

- gather only evidence that can affect the current decision;
- keep unrelated improvements outside the change;
- use tools and delegation only when they materially help the current outcome;
- verify against observable acceptance evidence; and
- stop when the required outcome is met.

[^fowler-yagni]: Fowler explains YAGNI's build, delay, carry, and repair costs
    and distinguishes speculative capability from practices that keep code
    malleable.
[^agile-simple-design]: The Agile Alliance describes simple design as ongoing
    design in which design elements justify their costs and decisions are
    deferred to gather evidence.
[^metz-wrong-abstraction]: Metz describes how an incorrect shared abstraction
    accumulates parameters and conditionals as new cases diverge.
[^aws-review-process]: AWS recommends proportionate review based on whether a
    decision is easy or difficult to reverse.
[^anthropic-effective-agents]: Anthropic recommends beginning with the simplest
    solution and adding workflows or autonomous agents only when their tradeoffs
    are justified.
[^openai-gpt5-coding]: OpenAI recommends specifying coding-agent eagerness and
    tool budgets because broad context gathering can be overdone.
