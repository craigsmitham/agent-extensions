---
type: Guide
title: How to write an explainer
description: When readers can follow a procedure but still have questions about the subject, or when a topic needs an introduction, turn their question into a focused, source-backed explainer.
tags: [docs, explanation, explainer, conceptual-documentation, authoring, how-to, diataxis]
status: draft
generated: { by: codex/gpt-6, at: 2026-11-22T00:10:36Z }
sources:
  - id: explanation
    resource: https://diataxis.fr/explanation/
    title: Diátaxis — Explanation
  - id: reference
    resource: https://diataxis.fr/reference-explanation/
    title: Diátaxis — The difference between reference and explanation
  - id: audience
    resource: https://developers.google.com/tech-writing/one/audience
    title: Google Technical Writing — Audience
  - id: location
    resource: https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm
    title: NIST/SEMATECH — Measures of Location
---

# How to write an explainer

Start with something a reader wants to understand. They may have noticed
a surprising result, heard two apparently conflicting accounts, or asked
for background that would take a how-to guide too far from its task.

## 1. Find the question behind the topic

Suppose a library volunteer asks for a knowledge-base article about
waiting times for reserved books. What have they already seen? In this
example, four of five borrowers waited two days, yet the desk reported
an average wait of four days. *How can both statements be true?* That
question gives the article a subject and a place to stop.[^explanation][^audience]

For a broad introduction, sketch the ideas a reader needs and how they
depend on one another. Here, “average” needs a definition. The mean
depends on the total time waited and the number of borrowers. Comparing
it with the middle wait needs one more idea, the borrowers’ order from
shortest wait to longest. *Why the average wait can exceed most borrowers’
waits* is enough for one page. Keep questions together when the answer to
one supplies the reasoning for the next. Give an independently sought
question its own entry. Which figure the library should publish, for
example, has its own audience and evidence.

## 2. Work out the answer and check its basis

Start with a concrete case. Label invented figures as examples. For an
actual report, check how the library defines a wait and which requests
it counted. A statistics handbook can define the measures. The desk’s
records establish what happened at this library.

Check the library example before drafting. For waits of 2, 2, 2, 2, and
12 days, verify that the arithmetic mean is four days and the median
is two.[^location]

Match the evidence to each claim in your own explanation. If the question
is why a group made a decision, look for its record or a participant’s
account. The consequences you observe today may give readers a reason to
value that decision while leaving its original motivation open.

## 3. Draft the connection the reader is missing

Introduce each idea when the reader needs it. If the opening example
could be mistaken for the subject of the page, give readers a sentence
or a descriptive heading that tells them what the example will help
explain. When the situation itself makes the question clear, you can
start there. The library page could open with the puzzle in the figures.

> How can the average wait for a library book be four days when most
> borrowers get theirs in two? Suppose four borrowers waited two days
> apiece and a fifth waited twelve. If each had waited two days, the
> group would have waited ten days altogether.
> The last borrower’s ten extra days doubled that total. Spread those
> twenty days across five borrowers and the mean wait is four days, even
> though nobody in this group waited exactly four.

Readers who wonder what a typical borrower experienced can now use the
sorted list to see why the median is two. Name the source for a definition
where you use it. Keep the reasoning and the numbers close enough that a
reader can check the claim without having the original report open.[^location]

Choose a different order when the question warrants one. An account of
a practice may begin with a choice people once faced, then follow the
evidence that changed their minds. For a worked example, see
[How explainers build understanding](../explainers/explanation.md). Its
kitchen history connects a practice with a theory its investigator
eventually gave up.[^explanation]

When credible accounts disagree, state what each proposes and which
observations it explains. Attribute the interpretations so readers can
tell where the evidence ends and a judgment begins.

## 4. Check what the draft lets a reader account for

Read the title and opening from the draft’s own link. Can a reader tell
what the page will explain? If you start with an example, can they tell
why it belongs here? Restore any context the draft assumes the reader
has just seen elsewhere. If it grew out of a how-to, leave that guide
the sentence needed for the task and link to the full explanation there.
Detailed instructions and tables of options have their own uses.
Keep the details that carry this explanation’s reasoning.[^reference]

Choose a check that fits the reader’s original question. For the library
figures, vary one wait. If the longest becomes 22 days, which measure
changes? A reader who can explain why the mean rises to six while the
median stays at two can use the account beyond the original figures. If
they can repeat only that a long wait “pulls up the average,” revisit
the sentence that connects an individual’s wait to the total.

For an explainer about a design decision, ask the reader why an
alternative looked reasonable at the time and which constraint shaped
the choice. If they can name only the winning design, revisit the
passage about what the team knew when it decided.

Without a reader, answer the question yourself using only the draft.
Identify the passage that supports your answer and report the check you
made. To judge whether the reader’s question calls for a different
design, consult the [Explanation pattern](../patterns/explanation.md).

[^explanation]: Daniele Procida, [Explanation](https://diataxis.fr/explanation/).
[^reference]: Daniele Procida, [The difference between reference and explanation](https://diataxis.fr/reference-explanation/).
[^audience]: Google Technical Writing, [Audience](https://developers.google.com/tech-writing/one/audience).
[^location]: NIST/SEMATECH, [Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm).
