---
type: Explanation
title: Documentation craft
description: What effective documentation craft is — four jobs from user needs (tutorial, how-to, reference, explanation), one job per document, and host conventions over portable layout rules.
tags: [docs, craft, quality, diataxis, explanation]
status: stable
sources:
  - id: diataxis
    resource: https://diataxis.fr/
    title: Diátaxis documentation system
  - id: diataxis-start
    resource: https://diataxis.fr/start-here/
    title: Diátaxis — Start here
  - id: diataxis-start-src
    resource: https://github.com/evildmp/diataxis-documentation-framework/blob/main/source/start-here.rst
    title: Diátaxis source — start-here.rst
  - id: diataxis-map
    resource: https://diataxis.fr/map/
    title: Diátaxis — The map
  - id: diataxis-map-src
    resource: https://github.com/evildmp/diataxis-documentation-framework/blob/main/source/map.rst
    title: Diátaxis source — map.rst
  - id: diataxis-foundations
    resource: https://diataxis.fr/foundations/
    title: Diátaxis — Foundations
  - id: diataxis-foundations-src
    resource: https://github.com/evildmp/diataxis-documentation-framework/blob/main/source/foundations.rst
    title: Diátaxis source — foundations.rst
  - id: johnson-diataxis
    resource: https://idratherbewriting.com/blog/what-is-diataxis-documentation-framework
    title: Tom Johnson — What is Diátaxis
  - id: mintlify-content-types
    resource: https://www.mintlify.com/guides/content-types
    title: Mintlify — Content types
generated:
  by: grok/grok-4.5
  at: 2026-08-07T22:41:37Z
---

# Documentation craft

Portable **understanding** of documentation quality — not repository layout,
frontmatter schemas, or tooling. Host projects may add structure, metadata,
and validators; those local rules win when they exist.

This bundle follows the four documentation types in Diátaxis
(tutorial, how-to guide, reference, and explanation). Each type has an
**explainer** (what the type is for) and a **guide** (how to write one). For
how to apply this craft in practice, see
[Documentation craft guide](docs-guide.md). For iterative remediation of an
existing corpus, see [Documentation workflow](workflow-explainer.md). For
functional vs deep quality, see [Documentation quality](quality-explainer.md).

## Why four types

Documentation must serve the **practitioner in a craft** — someone who both
**acquires** and **applies** skill, and who needs both **action** (knowing
*how*) and **cognition** (knowing *that*). Those two dimensions define four
quarters; there is no fifth kind waiting off the map.

| Need | Type | User mode | Documentation informs |
| --- | --- | --- | --- |
| Learning | Tutorial | Study + action | Skill acquisition through doing |
| Goals | How-to | Work + action | Task completion in the real world |
| Information | Reference | Work + cognition | Facts for lookup while working |
| Understanding | Explanation | Study + cognition | Context and reflection |

Crossing or blurring those boundaries is at the root of many documentation
failures: wrong voice, wrong structure, and content that cannot meet either
job well.

## Choose a type by need

| Need | Type | Explainer | Guide |
| --- | --- | --- | --- |
| Learn by doing, first success path | Tutorial | [Tutorial explainer](tutorial-explainer.md) | [Tutorial guide](tutorial-guide.md) |
| Achieve a concrete goal in a real system | How-to | [How-to explainer](how-to-explainer.md) | [How-to guide](how-to-guide.md) |
| Look up facts, interfaces, or terms | Reference | [Reference explainer](reference-explainer.md) | [Reference guide](reference-guide.md) |
| Understand why, context, or tradeoffs | Explanation | [Explanation explainer](explanation-explainer.md) | [Explanation guide](explanation-guide.md) |

If a draft tries to do two of these at once, prefer splitting or making one
job primary and linking the rest.

Quick compass (content + user mode → type):

| If the content… | …and serves the user’s… | …then it belongs to… |
| --- | --- | --- |
| informs action | acquisition of skill | tutorial |
| informs action | application of skill | how-to guide |
| informs cognition | application of skill | reference |
| informs cognition | acquisition of skill | explanation |

## Form follows job

Diátaxis pairs each need with a characteristic form (paraphrased):

| | Tutorial | How-to | Reference | Explanation |
| --- | --- | --- | --- | --- |
| Does | introduce, educate, lead | guide | state, describe, inform | explain, clarify, discuss |
| Answers | *Can you teach me to…?* | *How do I…?* | *What is…?* | *Why…?* / *About…* |
| Oriented to | learning | goals | information | understanding |
| Form | a lesson | a series of steps | dry description | discursive discussion |
| Everyday analogy | teaching a child to cook | a recipe | label on a food packet | culinary social history |

Secondary writeups treat these as **information patterns** authors can keep
distinct so readers get the voice and structure they need.

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
is in [Documentation quality](quality-explainer.md).

1. **One primary job per document.** Readers should know whether they are
   learning, doing, looking up, or understanding.
2. **Match form to job.** Steps belong in tutorials and how-tos; exhaustive
   inventories in reference; discussion and rationale in explanation.
3. **Link rather than restate.** When another document owns a procedure or
   fact set, point to it; do not maintain a second full copy.
4. **Prefer clarity of outcome.** State what the document is for near the
   top so people and tools can skip the wrong page quickly.
5. **Stay accurate enough for the job.** How-tos and reference go stale
   fastest; refresh or retire when commands, APIs, or ownership change.
6. **Respect the host.** Paths, indexes, metadata fields, and naming are
   project choices. Portable craft does not mandate a folder tree or a
   single frontmatter profile.
7. **Resist feature-shaped IA as the only scheme.** Organizing only by
   product surface, without need-based types, produces wild inconsistency
   across a portfolio.

## Neighbour bleed (where types collapse)

Each type has affinity with its neighbours; blur is common:

| Shared quality | Neighbours that bleed |
| --- | --- |
| Guide action | tutorial ↔ how-to |
| Serve application of skill | reference ↔ how-to |
| Propositional knowledge | reference ↔ explanation |
| Serve acquisition of skill | tutorial ↔ explanation |

Worst case: tutorials and how-tos fully collapse, so neither study nor work
is served. Keep the compass and the hard-boundary sections on
each type explainer when form starts to slip.

## What this bundle does not define

- Where files must live in a repository
- Required metadata keys or validators
- Always-on agent instruction files (harness / instruction guidance)
- Product marketing or user-facing site IA unless the host maps those
  surfaces onto these four types

Diátaxis itself is pragmatic: use what helps; you need not adopt every
theoretical layer to improve one page today. Prefer small iterative
improvements over empty type shells — see
[Documentation workflow](workflow-explainer.md).

## Related

- [Documentation craft guide](docs-guide.md)
- [Documentation workflow](workflow-explainer.md) · [Documentation workflow guide](workflow-guide.md)
- [Documentation quality](quality-explainer.md)
- [Tutorial explainer](tutorial-explainer.md) · [Tutorial guide](tutorial-guide.md)
- [How-to explainer](how-to-explainer.md) · [How-to guide](how-to-guide.md)
- [Reference explainer](reference-explainer.md) · [Reference guide](reference-guide.md)
- [Explanation explainer](explanation-explainer.md) · [Explanation guide](explanation-guide.md)
