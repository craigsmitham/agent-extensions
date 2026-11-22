---
type: Explainer
title: How-to guides and the work they serve
description: Why a how-to guide takes its shape from the reader’s goal, how it draws on practical judgment, and why even an experienced practitioner might reach for one.
tags: [docs, how-to, guide, practitioner, task, tutorial, diataxis]
status: draft
generated: { by: claude/fable-5-2, at: 2026-11-22T01:10:10Z }
sources:
  - id: how-to
    resource: https://diataxis.fr/how-to-guides/
    title: Diátaxis — How-to guides
  - id: tutorial
    resource: https://diataxis.fr/tutorials-how-to/
    title: Diátaxis — The difference between a tutorial and how-to guide
  - id: foundations
    resource: https://diataxis.fr/foundations/
    title: Diátaxis — Foundations
  - id: conflict
    resource: https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/resolving-a-merge-conflict-using-the-command-line
    title: GitHub Docs — Resolving a merge conflict using the command line
---

# How-to guides and the work they serve

The fix has been approved, and the pull request still can’t be merged.
While it waited for review, a teammate changed one of the same lines.
The developer knows how to commit and push. The puzzle is the file Git
leaves behind when the two branches meet. Both versions of the line are
in it, one above the other, set off by Git’s conflict markers. The merge
can’t finish until someone settles what the line should say.

A **how-to guide** gives a practitioner a way to accomplish a particular
task. In Diátaxis, the reader comes to a guide with a purpose of their
own and some skill they can put to work. The developer would recognize
a finished merge and still needs directions for getting there. Consulting
them is a normal part of practicing a craft, even for someone who has
done the job before.[^how-to][^foundations]

## The task gives the guide its shape

GitHub’s guide *Resolving a merge conflict using the command line* starts
in a local repository that already has the conflict. It ends with the
resolution committed and the developer free to push and merge the pull
request. A description of the merge command could account for every
option it accepts and still leave the developer where the command
stopped. Their question carries on past that point. A commit counts as
success only if the line says what the project needs and the pull request
can go in.[^conflict]

That purpose also explains where the guide begins. Writing the fix and
getting it reviewed belong to the larger job of shipping it. By the time
the developer looks for directions, that work is done. A how-to guide
can cover one stretch of a larger undertaking because the reader knows
what came before and what they intend to do next.[^how-to]

## Why directions leave room for judgment

Two developers could find the same markers in a file and need different
results. For one, the teammate’s version replaces their own. For the
other, both changes matter and the line has to be written a third way.
GitHub’s guide names the choice and leaves it with the reader.

> Decide if you want to keep only your branch’s changes, keep only the
> other branch’s changes, or make a brand new change, which may
> incorporate changes from both branches.

Git can mark where the two versions collide. What the line should say
depends on the project.[^conflict]

This is why a decision can be as much a part of a how-to guide as a typed
command. The author knows what the markers mean and where the choice
falls. The developer knows what the line is for. Useful directions bring
those two pieces of knowledge together at the moment of choice.[^how-to]

## The same conflict in a lesson

In a Git workshop, an instructor might ask two learners to change the
same line of a practice file and then merge. Seeing the markers appear
is the point of the exercise. At work, the developer may learn exactly
the same thing along the way. The fix is still waiting to go out.

Diátaxis locates the difference between a tutorial and a how-to guide in
what each owes its reader. A lesson owes the learner an experience, which
is why the instructor arranges the collision. A guide owes the developer
help with work already in hand.[^tutorial]

Months later, that same developer might open the guide again when a
teammate deletes a file they have edited. The guide gives that conflict
directions of its own. Diátaxis notes that a chef may follow a recipe for
a dish made many times, to be sure of making it correctly. Remembering
every command was never the point of that first merge.[^conflict][^how-to]

To turn a task like the developer’s into usable directions, follow
[How to write a how-to guide](../guides/writing-a-how-to-guide.md).
For a choice among document designs, see the
[How-to guide pattern](../patterns/how-to.md).

[^how-to]: Daniele Procida, [How-to guides](https://diataxis.fr/how-to-guides/).
[^foundations]: Daniele Procida, [Foundations](https://diataxis.fr/foundations/).
[^conflict]: GitHub Docs, [Resolving a merge conflict using the command line](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/resolving-a-merge-conflict-using-the-command-line).
[^tutorial]: Daniele Procida, [The difference between a tutorial and how-to guide](https://diataxis.fr/tutorials-how-to/).
