---
type: Pattern
title: Tutorial
description: When readers need to acquire a skill, lead them through a safe, bounded lesson with meaningful actions and visible results that build confidence for further practice.
tags:
- docs
- tutorial
- learning
- diataxis
- explanation
- documentation-pattern
- pattern
- authoring
status: draft
sources:
- id: diataxis-tutorials
  resource: https://diataxis.fr/tutorials/
  title: Diátaxis — Tutorials
- id: diataxis-tutorials-how-to
  resource: https://diataxis.fr/tutorials-how-to/
  title: Diátaxis — The difference between a tutorial and how-to guide
- id: python-tutorial
  resource: https://docs.python.org/3/tutorial/
  title: Python — The Python Tutorial
generated: { by: codex/gpt-6, at: 2026-11-21T22:44:26Z }
---

# Tutorial

A tutorial fits a reader who wants practice and can give the teacher
responsibility for choosing a useful exercise. A lesson can be someone’s
first encounter with an entire craft or an experienced practitioner’s
first use of one technique. The deciding question is what the activity
lets this particular learner experience.[^diataxis-tutorials]

## Where a lesson earns its place

The Python Tutorial addresses programmers learning Python and assumes
some programming experience. Its opening interpreter examples let a
reader type short expressions and see their values. The author has
chosen a particular encounter with Python while leaving a much larger
language available for later exploration. The audience assumption
matters when choosing that tutorial for a class of complete beginners.
The presence of examples establishes what the text offers. Evidence of
what learners acquire would have to come from their use of it.[^python-tutorial]

## The cost of choosing the exercise

A teacher can arrange one working environment, an attainable goal,
small actions with recognizable results, and a chance to try again.
Taking choices off the learner’s hands gives them attention to spend
on the skill in front of them. It also makes the author responsible
for the path. A changed default or missing prerequisite early in the
lesson can spoil everything after it.[^diataxis-tutorials]

An operator restoring a service brings an immediate goal and
conditions the author cannot choose. A [how-to guide](how-to.md) can
accommodate that work. Someone who can already perform the task but
wonders why it behaves as it does has a question for an
[explainer](explanation.md). For repeated practice where learners can
increasingly direct themselves, consider whether a
[learning checklist](learning-checklist.md) provides enough support.[^diataxis-tutorials-how-to]

To understand what a chosen activity gives the learner, read
[Why a tutorial gives the learner something to do](../explainers/tutorial.md).
To develop and check a lesson, follow
[How to write a tutorial](../guides/writing-a-tutorial.md).

[^diataxis-tutorials]: Daniele Procida, [Tutorials](https://diataxis.fr/tutorials/).
[^diataxis-tutorials-how-to]: Daniele Procida, [The difference between a tutorial and how-to guide](https://diataxis.fr/tutorials-how-to/).
[^python-tutorial]: Python, [The Python Tutorial](https://docs.python.org/3/tutorial/).
