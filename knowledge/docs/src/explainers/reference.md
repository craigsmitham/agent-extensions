---
type: Explainer
title: Why reference follows the shape of the thing it describes
description: How stable names, comparable entries, and precise limits help a reader find a fact in the middle of
  work.
tags:
- docs
- reference
- lookup
- interface
- diataxis
status: draft
generated:
  by: codex/gpt-6
  at: '2026-11-21T22:43:55Z'
sources:
- id: reference
  resource: https://diataxis.fr/reference/
  title: Diátaxis — Reference
- id: iter
  resource: https://docs.python.org/3/library/itertools.html
  title: Python — itertools
---

# Why reference follows the shape of the thing it describes

A programmer sees `islice(records, 2)` in a report generator. Will it
skip two records or keep two? The answer changes which customers appear
in the report. Python's itertools reference shows two call forms. In the
shorter one the number is the stopping position. The result yields the
first two records. In the longer form there is a separate starting
position.[^iter]

The programmer already had a name and a question. The module heading,
the function name and the signatures took them to the answer. Someone
looking up `pairwise` on the same page can reuse that route. A consistent
arrangement lets the reader bring their knowledge of the interface to
the page and take a fact straight back to work.[^reference][^iter]

## Why the small print belongs beside the name

A reader who knows Python's usual slicing syntax might try a negative
index to select items from the end. The entry for `islice` names the
restriction on negative arguments at the point of lookup. An example
with positive arguments alone would leave that question open. A signature
answers which arguments fit where. A restriction answers which uses a
caller can rely on. Both belong with the same function.[^iter]

Diátaxis describes reference as a faithful account of the thing a reader
consults it about. That obligation includes choosing the right unit.
A module summary lets a reader scan for an operation. A function entry
can give its precise behavior. A reader can enter at either level and
leave as soon as the uncertainty is resolved.[^reference]

For a practical method, see [How to write reference documentation](../guides/writing-reference-documentation.md).

[^reference]: [Diátaxis — Reference](https://diataxis.fr/reference/).
[^iter]: [Python — itertools](https://docs.python.org/3/library/itertools.html).
