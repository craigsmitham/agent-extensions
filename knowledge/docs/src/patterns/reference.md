---
type: Pattern
title: Reference
description: When readers need authoritative facts during work, organize accurate, consistently structured entries around the subject so they can locate and compare details quickly.
tags:
- docs
- reference
- diataxis
- explanation
- documentation-pattern
- pattern
- authoring
status: draft
sources:
- id: diataxis-reference
  resource: https://diataxis.fr/reference/
  title: Diátaxis — Reference
- id: python-logging-reference
  resource: https://docs.python.org/3/library/logging.html
  title: Python — Logging reference
generated: { by: codex/gpt-6, at: 2026-11-22T00:06:36Z }
---

# Reference

## Design problem and context

A practitioner knows the subject or operation they need, but cannot reliably
remember its exact properties, parameters, constraints, or behavior. They need
to enter at an arbitrary point and compare entries. Narrative order and
inconsistent descriptions make that lookup difficult.

Use this pattern when you can name what the reference covers and who or
what establishes its facts. Choose explanation for a connected account of
why something works, or a how-to when readers need a route to a goal.

## Design response and tradeoffs

Mirror the subject's useful structure in named, addressable entries. Give
comparable items consistent fields and vocabulary, identify the supported
version or scope, and connect each assertion to the maintained system or
other authority. Use concise examples to clarify facts.

- **Coverage versus scanability:** cover the promised surface while keeping
  each entry easy to inspect.
- **Consistency versus variation:** use common structure without hiding
  meaningful differences between items.
- **Exactness versus maintenance effort:** generated facts can help, but
  semantics, limits, and examples still need review.

Readers can find and compare facts without reading a lesson first. The
resulting material may be poor teaching on its own, and even a small stale
detail can invalidate a decision or procedure that depends on it.

## Example and evidence

The Python logging reference gives each class and function its own entry.
A reader arriving at the page for a first lesson or a practical recipe
can follow its links to tutorials or the cookbook. Those routes illustrate
the design. Assessing lookup speed would require observing readers with
a question in hand.[^python-logging-reference] Diátaxis describes how
the arrangement of reference entries can reflect the thing they
describe.[^diataxis-reference]

For an example of how the structure of a subject guides lookup, see
[Why reference follows the shape of the thing it describes](../explainers/reference.md).
To build and verify entries, use [How to write reference documentation](../guides/writing-reference-documentation.md).

A [how-to guide](how-to.md) answers a task that spans entries.
An [explainer](explanation.md#when-the-distinction-matters) connects facts
when their significance is what the reader needs to understand.

[^python-logging-reference]: Python, [Logging reference](https://docs.python.org/3/library/logging.html).
[^diataxis-reference]: Daniele Procida, [Reference](https://diataxis.fr/reference/).
