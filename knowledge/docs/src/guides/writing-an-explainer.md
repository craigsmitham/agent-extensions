---
type: Guide
title: How to write an explainer
description: When readers can follow a procedure but still have questions about the subject, or when a topic needs an introduction, turn their question into a focused, source-backed explainer.
tags: [docs, explanation, explainer, conceptual-documentation, authoring, how-to, diataxis]
status: draft
generated: { by: codex/gpt-6, at: 2026-11-21T21:39:54Z }
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
  - id: booklet
    resource: https://helpx.adobe.com/acrobat/desktop/print-documents/booklets-posters-banners/print-booklets.html
    title: Adobe Acrobat — Print booklets
  - id: booklet-overview
    resource: https://helpx.adobe.com/acrobat/desktop/print-documents/booklets-posters-banners/about-booklets-printing.html
    title: Adobe Acrobat — Booklet printing with Adobe Acrobat
---

# How to write an explainer

Use this guide to turn a reader’s question into a document they can read
away from the task that prompted it. You can start with a new topic or
with a passage of background material that has outgrown a how-to guide.

## 1. Find the question behind the topic

Write down what the reader has already seen and what they still want to
understand. Use a question from a reader if you have one. For a broad
request such as “explain booklet printing,” picture a specific encounter
with the subject. Someone opens a print preview and sees page eight beside
page one. They know how to read a booklet. *Why would the pages look out of
order before printing?* That question gives the draft a subject and a
sensible place to stop.[^explanation][^audience]

A topic that needs an introduction usually holds several questions. Start
with the one the others depend on. A reader who understands why the preview
pairs page eight with page one is ready to ask why a ten-page program
prints with two blank pages. Take each later question through the same
steps. Give it a section on the same page when its answer builds on the one
before, and a page of its own when readers arrive with it separately. When
a subject has many concepts that lean on one another, map them before you
draft. The [Explanation pattern](../patterns/explanation.md#authoring-steps)
shows how.

Give the page a working title that names what it explains, such as *Why
booklet pages look out of order*. If the reader is actually asking which
print setting to select, direct them to the printing guide.[^explanation]
If both questions recur, link the two pages at the point where readers
encounter the surprise. When the material began as a passage in a how-to
guide, leave the guide the one sentence the task needs, such as *The
preview shows the pages as they will sit on each sheet*, and link that
sentence to the new page. The [How-to guide pattern](../patterns/how-to.md#what-belongs)
asks a guide to point to explanation instead of absorbing it.

## 2. Work out the answer and check its basis

Begin with the encounter itself. A reader’s report gives you their account
of it. If you pictured it instead, confirm that it happens before you
explain it. Open an eight-page file in Acrobat, choose Booklet in the print
dialog, and look at the preview. Adobe’s overview says the feature places
two pages on each sheet and provides a preview of the layout. Which two
pages appear together is something to see for yourself.[^booklet-overview]

Write a provisional answer in plain language. Underline any phrase that
hides a step in the reasoning. Then open up each one until every step is
something you have worked out for yourself or found in a source that can
establish it.

For the booklet, “Acrobat rearranges the pages for booklet printing” leaves
*for booklet printing* doing most of the work. What does folding change?
Sketch the outer sheet of an eight-page booklet, or fold two sheets, number
the pages, and open them again. Check the claim about what Acrobat does
against Adobe’s documentation. Each part of the answer now has its own
basis. The preview is your observation. The folded paper accounts for the
page positions. Adobe’s documentation says what the software sets out to do
when it arranges them.[^booklet]

Choose evidence that fits your own question. For the reason behind a design
decision, look for the decision record or the designer’s account. If you
can establish only that the design has a useful consequence, describe that
consequence and leave the designer’s motive open.

## 3. Draft the connection the reader is missing

Start with the familiar experience. Introduce each idea where the reader
needs it, and follow the connection through to its consequence. Here is
an opening paragraph for *Why booklet pages look out of order*.

> In the preview of an eight-page program, page eight sits beside page one.
> Picture the closed program. Its front cover is page one and its back
> cover is page eight. Open the outer sheet flat and those covers are
> neighbors. The preview shows their positions on the paper. Folding the
> paper puts them at opposite ends of the program.

Where a claim rests on a source, name the source at that point. The reader
can check the fold with two sheets of paper. What Acrobat is built to do
is Adobe’s to say, so the next paragraph of the draft opens with the
attribution: *Adobe’s booklet instructions say that Acrobat arranges the
pages for folding.*[^booklet]

Choose a different order when the question calls for it. To explain how a
practice arose, start with the constraint people faced at the time and
trace the choice it prompted. When people disagree about that choice, give
the reasons each side finds persuasive and identify whose interpretation
you are offering. Include the history or alternative that changes how the
reader sees the subject.[^explanation] For an explainer organized around
the history of a practice, read
[How explainers build understanding](../explainers/explanation.md). It
follows a kitchen custom from an eighteenth-century engraving to a theory
its investigator later gave up.

## 4. Read the draft away from the task

Read it without the product open. Restore any context the reader would
otherwise need the screen to supply. Move click sequences to the how-to
guide and detailed option descriptions to reference.[^explanation][^reference]
Keep concrete details that carry the reasoning. Removing the page numbers
from the booklet example would make the passage shorter and the fold harder
to picture.

Return to the opening question. Can someone give the answer from the
passage and say why it follows? Try a nearby case. Which pages would share
the outside of a twelve-page program? If a reader is available, ask them,
and listen for the reason as well as the numbers. If they remember “eight
beside one” but miss that the covers share a sheet, revise the sentence or
add the sketch that makes the fold visible.

Without a reader, work the nearby case yourself from the draft alone, and
point to the sentence that supplies the reason. That shows the reasoning
is on the page. Whether readers follow it is something only a reader can
show. Finish when the draft answers the original question and each step of
the reasoning can be traced to the example or its evidence.

For an example of the form, read [How explainers build understanding](../explainers/explanation.md).
An explainer is the kind of document the [Explanation pattern](../patterns/explanation.md)
describes. Follow this guide to draft and revise one. The pattern’s
[authoring steps](../patterns/explanation.md#authoring-steps) go further
into concept maps, consequential distinctions, and competing perspectives,
for subjects that need them. See the pattern as well for scope, evidence,
and tradeoffs.

[^explanation]: Daniele Procida, [Explanation](https://diataxis.fr/explanation/).
[^reference]: Daniele Procida, [The difference between reference and explanation](https://diataxis.fr/reference-explanation/).
[^audience]: Google Technical Writing, [Audience](https://developers.google.com/tech-writing/one/audience).
[^booklet]: Adobe Acrobat, [Print booklets](https://helpx.adobe.com/acrobat/desktop/print-documents/booklets-posters-banners/print-booklets.html).
[^booklet-overview]: Adobe Acrobat, [Booklet printing with Adobe Acrobat](https://helpx.adobe.com/acrobat/desktop/print-documents/booklets-posters-banners/about-booklets-printing.html).
