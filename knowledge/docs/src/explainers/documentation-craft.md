---
type: Explainer
title: Documentation craft
description: What effective documentation craft is — matching form to reader need, keeping each job recognizable, and respecting host conventions over portable layout rules.
tags:
- docs
- craft
- quality
- diataxis
- explainer
status: stable
generated: { by: codex/gpt-6, at: 2026-11-22T00:10:36Z }
sources:
- id: diataxis-start
  resource: https://diataxis.fr/start-here/
  title: "Di\xE1taxis \u2014 Start here"
- id: diataxis-map
  resource: https://diataxis.fr/map/
  title: "Di\xE1taxis \u2014 The map"
- id: diataxis-foundations
  resource: https://diataxis.fr/foundations/
  title: "Di\xE1taxis \u2014 Foundations"
- id: prior-documentation-craft
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/docs/src/guides/documentation-craft.md
  title: Documentation craft guide
---

# Documentation craft

Suppose a choir keeps its rehearsal notes in a repository. A new singer
looking up a repeat sign needs a short definition. Someone learning to
follow repeats needs a passage to sing and a way to tell where to come
back in. Both readers can open the same site. Their questions call for
different documents.

Choose documentation by what the reader needs to do: learn, complete a task,
look up facts, or understand a subject. Diátaxis supplies these four reader
needs in its account of skilled practice.[^diataxis-foundations] The
[Documentation pattern collection](../patterns/index.md) describes
reusable document designs for these and more specific situations. Use a pattern to judge how well a design fits the
situation. For example, a runbook gives an operator a bounded, repeatable
procedure. Someone writing that runbook needs to work through the decisions
that make the directions usable during an incident. The
[authoring guides](../guides/index.md) serve that second reader. A third
reader might want to understand why an operator reaches for a runbook in
the first place. The [explainers](index.md) take up questions of that kind.

“Explainer” is another name for an explanation document. “Guide” can be an
umbrella term; use **how-to guide** when specifically referring to directions
for accomplishing a task. These names do not prescribe host metadata or folders.

For iterative remediation of an existing corpus, see [Documentation workflow](documentation-workflow.md). For
functional vs deep quality, see [Documentation quality](documentation-quality.md).
For choosing paths and names readers can find, see [Documentation organization and
discovery](documentation-organization-and-discovery.md).

## Why four reader needs

Diátaxis considers the [practitioner](practice.md) acquiring or applying
a skill. At either point the reader may need to act or to think something
through. These two distinctions yield four needs. They explain why a lesson
feels different from a lookup entry even when both cover the same subject.
The reader's need can change during a visit.[^diataxis-foundations][^diataxis-map]

| Need | Form | User mode | Documentation informs |
| --- | --- | --- | --- |
| Learning | Tutorial | Study + action | Skill acquisition through doing |
| Goals | How-to | Work + action | Task completion in the real world |
| Information | Reference | Work + cognition | Facts for lookup while working |
| Understanding | Explanation | Study + cognition | Context and reflection |

Crossing or blurring those boundaries is at the root of many documentation
failures: wrong voice, wrong structure, and content that cannot meet either
job well.

## Choose a form by need

| Reader need | Documentation pattern |
| --- | --- |
| Learn by doing | [Tutorial](../patterns/tutorial.md) |
| Achieve a concrete goal | [How-to guide](../patterns/how-to.md) |
| Look up facts or interfaces | [Reference](../patterns/reference.md) |
| Understand context and reasoning | [Explanation](../patterns/explanation.md) |

If a draft tries to do two of these at once, prefer splitting or making one
job primary and linking the rest.

## Cycle of interaction

Users do not always walk the map in order, but craft mastery often moves
through phases:

1. **Learning** — dive in under guidance (tutorial)
2. **Goals** — put skill to work (how-to)
3. **Information** — consult facts the head does not hold (reference)
4. **Understanding** — reflect away from the work (explanation)

Then back again for a deeper layer or a new skill. Documentation should
support that cycle without forcing a single linear site tour.

## Quality principles

Practical checks for authors. The two-layer model (functional vs deep quality)
is in [Documentation quality](documentation-quality.md).

1. **One primary reader job per ordinary document.** When a document
   needs several coordinated parts, keep each job recognizable so readers
   know whether they are learning, doing, looking up, or understanding.
2. **Match form to job.** Steps belong in tutorials and how-tos; exhaustive
   inventories in reference; discussion and rationale in explanation.
3. **Link rather than restate.** When another document owns a procedure or
   fact set, point to it; do not maintain a second full copy.
4. **Prefer clarity of outcome.** State what the document is for near the
   top so people and tools can skip the wrong page quickly.
5. **Make action documents selectable before opening.** In a description or
   other context-free preview, pair the supported outcome with the observable
   situation, event, symptom, or reader intent that makes the document
   relevant. Use a literal event only when work is event-driven; a
   voluntarily selected guide normally states reader intent. Keep selection
   conditions distinct from the access, knowledge, or state preconditions
   required after selection.
6. **Check what can change.** Revisit a page when the behavior, policy,
   terminology, or other evidence its readers depend on changes.
7. **Respect the host.** Paths, indexes, metadata fields, and naming are
   project choices. Portable craft does not mandate a folder tree or a
   single frontmatter profile.
8. **Test the route from the reader’s question.** A topic index can lead
   straight to a definition yet bury the lesson a newcomer needs. Follow
   each route from the place that reader is likely to enter.

Identify the authority for the claim.[^prior-documentation-craft] A recording
can establish what happened at a rehearsal, an adopted policy settles the
choir’s attendance rule, and a reproducible example can establish what a
software command does. Label proposals and illustrative cases so readers
know what they can rely on.

## Neighbour bleed (where reader-need forms collapse)

Each form has affinity with its neighbours; blur is common:

| Shared quality | Neighbours that bleed |
| --- | --- |
| Guide action | tutorial ↔ how-to |
| Serve application of skill | reference ↔ how-to |
| Propositional knowledge | reference ↔ explanation |
| Serve acquisition of skill | tutorial ↔ explanation |

Worst case: tutorials and how-tos fully collapse, so neither study nor work
is served. Return to the reader’s immediate purpose when the form of a draft starts to slip.

## Other named documents

The collection also includes designs for more specific purposes that may
combine several reader needs:

- A [Principle document](../patterns/principle.md) articulates a recognized good
  and gives sourced direction for judgment, with scope and limits. The pattern
  describes the document design; the principle is the direction it communicates.
- A [playbook](../patterns/playbook.md) supports assessment, response selection,
  and coordination as a situation develops.
- A [runbook](../patterns/runbook.md) supports repeatable execution of a bounded
  operational task, including verification and recovery.
- A [checklist](../patterns/checklist.md) puts bounded prompts at the point of
  work to address omissions or coordination gaps. Its purpose-specific patterns
  cover execution, verification, readiness, reporting and review, and learning.
  The use protocol, evidence, and response to unmet items are part of its design.

A [practice](practice.md) is the activity documentation supports, not another
document type. A [standard](standard.md) supplies a recognized basis for
judgment or coordination; documenting it does not by itself establish authority.

## Select and combine patterns

Consider documentation for a service that accepts requests and sometimes needs
recovery. This illustrative sequence shows complementary choices, not a required
set of pages:

1. A **tutorial** gives a new practitioner a safe first request and visible
   result. Link to **reference** for the exact request fields.
2. An **explanation** connects retries, failures, and duplicate effects. A
   **principle document** can communicate the warranted direction that governs
   choices where those concerns conflict.
3. A **how-to guide** helps a competent practitioner configure the service for
   a real goal, drawing on the same reference.
4. A **playbook** guides assessment when errors rise. If rollback is selected,
   a **runbook** supplies its bounded execution, verification, and recovery.
5. A **verification checklist** can support a consequential runbook pause,
   while a **readiness checklist** brings current evidence to the role deciding
   whether to proceed. A **learning checklist** can scaffold the tutorial's
   practice; its learning claim needs later independent evidence.

Start with the actual problem, choose only the patterns it needs, and follow
their relationships when another reader need emerges. Pattern descriptions
help authors make those choices; they do not require every resulting document
to reproduce the description's headings.

The docs bundle maintainer owns this collection with the rest of the bundle.
Apply the [collection maintenance guidance](../guides/curating-a-pattern-collection.md)
to proposed changes, and record revisions and retirements in the bundle log.

## What this bundle does not define

- Where files must live in a repository
- Required metadata keys or validators
- Always-on agent instruction files (harness / instruction guidance)
- Product marketing or user-facing site IA unless the host maps those
  surfaces onto these four reader-need forms

The bundle does offer portable criteria for choosing among host-compatible
organizations. It does not prescribe the resulting paths; see [Documentation
organization and discovery](documentation-organization-and-discovery.md).

Diátaxis encourages authors to start with a change they can use today.[^diataxis-start]
For an example of a collection growing from recurring reader questions,
see [Documentation workflow](documentation-workflow.md).

## Related

- [Documentation pattern collection](../patterns/index.md)
- [Documentation quality](documentation-quality.md)
- [Documentation audits](documentation-audits.md)
- [Documentation organization and discovery](documentation-organization-and-discovery.md)

[^diataxis-foundations]: Diátaxis, [Foundations](https://diataxis.fr/foundations/).
[^diataxis-map]: Diátaxis, [The map](https://diataxis.fr/map/).
[^diataxis-start]: Diátaxis, [Start here](https://diataxis.fr/start-here/).
[^prior-documentation-craft]: [Earlier documentation craft guide](https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/docs/src/guides/documentation-craft.md).
