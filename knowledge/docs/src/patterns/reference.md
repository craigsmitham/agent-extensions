---
type: Pattern
title: Reference
description: When readers need authoritative facts during work, organize accurate, consistently structured entries around the system so they can locate and compare details quickly.
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
generated: { by: codex/gpt-6, at: 2026-11-21T22:46:07Z }
---

# Reference

## Design problem and context

A practitioner knows the subject or operation they need, but cannot reliably
remember its exact properties, parameters, constraints, or behavior. They need
to enter at an arbitrary point and compare entries. Narrative order and
inconsistent descriptions make that lookup difficult.

Use this pattern when the described surface and its authoritative source are
identifiable. Choose explanation for a connected account of why it works, or
a how-to when readers need a route to a goal.

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

An illustrative configuration reference might give each setting a stable name,
type, default, allowed values, and version-specific constraints. A reader can
compare two settings without following an introductory lesson.

The Python logging reference organizes classes and functions into addressable
entries and directs readers to tutorials and the cookbook for other needs. It illustrates
how a reader can move from lookup to learning or task guidance.[^python-logging-reference]
Diátaxis gives the rationale for following the structure of the described system.[^diataxis-reference]

This pattern description is a draft synthesis. The observed structure supports
the proposed arrangement, not a measured claim about lookup speed or the
accuracy of every documented entry.

For the relationship between an interface and its documentation, see
[Why reference follows the shape of the thing it describes](../explainers/reference.md).
To build and verify entries, use [How to write reference documentation](../guides/writing-reference-documentation.md).

A [how-to guide](how-to.md) answers a task that spans entries.
An [explainer](explanation.md#when-the-distinction-matters) connects facts
when their significance is what the reader needs to understand.

[^python-logging-reference]: Python, [Logging reference](https://docs.python.org/3/library/logging.html).
[^diataxis-reference]: Daniele Procida, [Reference](https://diataxis.fr/reference/).
