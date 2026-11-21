---
type: Guide
title: How to write reference documentation
description: When readers keep looking up interface details, turn the supported surface into entries they can locate,
  compare, and check.
tags:
- docs
- reference
- authoring
- interface
- lookup
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

# How to write reference documentation

Take one concrete lookup request. Suppose a team has asked for a desk
reference to the iterator functions used in its reporting scripts.
Readers want to know what `islice(records, 2)` yields, and what happens
to the original iterator. Those questions give you a first entry to
draft and a way to test it.

## Bound the surface and find its authority

Identify the interface and version your readers have. In the example,
inventory the functions imported by the scripts and check their entries
in the documentation for the installed Python release. Title the page
*Iterator functions used in our reports*. That title explains why a
function outside this small inventory may be absent. For a public API
reference, compare the inventory against the exported interface instead.
Keep any unresolved difference visible until the owner settles it.[^reference]

## Write the entry someone could land on directly

Use the public identifier as a heading. For each function, put the call
forms first, then the result, constraints and an example where it settles
a likely ambiguity. Here is part of the entry for the team's first question.[^iter]

> `itertools.islice(iterable, stop)`
>
> `itertools.islice(iterable, start, stop[, step])`
>
> Yields selected items in input order, starting at zero by default and
> ending before the stopping position. A stop of `None` continues to the
> end of the input. The step defaults to one and must be positive.
> Starting and stopping positions must be nonnegative or `None`.
>
> With `rows = iter(['oak', 'elm', 'ash'])`,
> `list(islice(rows, 2))` returns `['oak', 'elm']`. The next item in
> `rows` is `'ash'`.

That final sentence supplies a fact a caller needs before reusing the
input. If the draft starts telling the programmer how to design the
report, move that work into the report-writing guide. Link it where
someone looking up the function might want to continue.[^reference]

## Test a lookup from the middle of the page

Start at the entry and answer both original questions using its text.
Run the example with a fresh iterator. Then vary the argument that
caused confusion. On a fresh copy of the same input,
`list(islice(rows, 2, None))` should yield only `['ash']`. Check the
limits against the supported version as well. A successful example
cannot establish every allowed argument.[^iter]

Repeat with a neighboring entry. Can a reader find the corresponding
return behavior in the same place? If the two functions differ in a
way that matters to a caller, make the difference visible. Record the
release or interface change that should prompt the maintainer to check
these entries again.

[^reference]: [Diátaxis — Reference](https://diataxis.fr/reference/).
[^iter]: [Python — itertools](https://docs.python.org/3/library/itertools.html).
