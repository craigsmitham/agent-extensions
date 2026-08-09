---
type: Explanation
title: Context gardening
description: How context gardening continually cultivates useful context by observing work, repairing discovery, pruning noise, and promoting knowledge to the right harness elements.
tags: [harness, context, maintenance, pruning, freshness, feedback, context-hygiene, doc-gardening, knowledge-gardening]
status: stable
sources:
  - id: anthropic-context-engineering
    resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
    title: Anthropic — Effective context engineering for AI agents
  - id: openai-harness-engineering
    resource: https://openai.com/index/harness-engineering/
    title: OpenAI — Harness engineering
  - id: cursor-harness-improvement
    resource: https://cursor.com/blog/continually-improving-agent-harness
    title: Cursor — Continually improving our agent harness
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T20:53:20Z
---

# Context gardening

In this bundle, **context gardening** names the recurring practice of
cultivating the context system from observed work. It keeps useful knowledge
discoverable, removes stale or distracting material, repairs weak routes, and
moves recurring guidance to the harness element that can express it most
truthfully.

The gardening metaphor emphasizes that context is not finished when it is
written. It grows through new tasks, tool results, decisions, failures, and
feedback. Without maintenance, useful routes disappear into clutter while
obsolete guidance can retain undeserved authority.

Anthropic describes context engineering as iterative curation over a changing
universe of possible information rather than a one-time prompt-writing
exercise.[^anthropic-context-engineering] Context gardening is the maintenance
practice implied by that lifecycle.

## Broader than documentation gardening

Documentation is one part of the garden, but context can also come from
instructions, skills, retrieval indexes, tool descriptions, error messages,
memory, plans, traces, and representations of live environment state.

| Context surface | Gardening concern |
| --- | --- |
| Persistent instructions | Relevance, scope, duplication, and always-on cost |
| Knowledge and references | Accuracy, provenance, freshness, and discoverability |
| Skills and workflows | Routing, boundaries, dependencies, and completion evidence |
| Tool interfaces | Compact schemas, actionable results, and useful failures |
| Task and memory state | Ownership, retention, summarization, and retirement |
| Feedback and observability | Signal quality, attribution, and recovery paths |

OpenAI reports both a recurring documentation-gardening agent and broader
background cleanup that repairs drift and reinforces repository principles.[^openai-harness-engineering]
The general practice is therefore better understood as tending the whole
context ecosystem, not merely editing prose.

## The cultivation loop

```text
observe work → classify the context gap → change the responsible surface
             → verify the effect → keep, revise, or retire
```

The loop begins with evidence. A missed constraint, repeated search, stale
answer, tool error, or successful workaround reveals how the context system
actually behaves. The gardener then asks which kind of failure occurred:

- relevant context did not exist;
- it existed but could not be discovered;
- it arrived in the wrong scope or at the wrong time;
- it was too noisy, stale, or weakly attributable;
- it prescribed work that another element should perform; or
- it shaped behavior correctly but lacked verification.

Only then is a durable change selected. Cursor describes harness improvement
similarly as a product discipline driven by hypotheses, evaluations,
instrumentation, and real usage rather than by intuition alone.[^cursor-harness-improvement]

## Typical gardening moves

| Move | Purpose |
| --- | --- |
| Plant | Capture missing context whose recurrence and owner are understood |
| Prune | Remove stale, redundant, irrelevant, or excessively detailed context |
| Transplant | Move content to the scope or harness element where it belongs |
| Connect | Add or strengthen routes, indexes, triggers, and cross-links |
| Promote | Replace repeated prose with a skill, tool, check, schema, or policy |
| Retire | Mark superseded context and remove it from active selection |
| Verify | Test discovery and behavior on representative work |

These are maintenance moves, not a mandate to change something after every
run. A single surprising result may be noise. Repeated observations or a
high-consequence gap justify a durable intervention; evaluation determines
whether that intervention helped.

## Context should have an owner and a lifecycle

Gardening becomes tractable when each piece of context has a responsible
surface, scope, source, and freshness expectation. Otherwise no one can tell
whether to update, relocate, or discard it.

The strongest owner is the one that matches the concern:

- broad invariants belong in appropriately scoped persistent instructions;
- reusable judgment and sequence belong in a skill or guide;
- detailed facts belong in knowledge or reference material;
- live facts belong behind observations and tools;
- mechanically decidable constraints belong in checks or policies;
- current goals and progress belong in task state.

This owner-selection discipline prevents gardening from degenerating into
instruction-file accretion.

## Relationship to progressive disclosure

[Progressive disclosure](../patterns/progressive-disclosure.md) structures how
deeper context is found and loaded. Context gardening maintains that structure
over time. It checks whether routes still lead somewhere useful, whether new
depth needs a route, and whether frequently loaded material belongs at a
different layer.

The two form a useful pair:

- progressive disclosure controls when context enters attention;
- context gardening keeps the disclosure system accurate and economical.

## Domain specialization

The practice transfers across domains, but observations and owners differ. A
software-engineering garden may include repository instructions, architecture
maps, build output, and traces. An operations harness may tend runbooks, live
service state, escalation policy, and incident evidence. A research harness
may emphasize source provenance, experimental state, and uncertainty.

The general practice should describe the maintenance logic. Domain profiles
should own the concrete signals, risks, and verification methods.

## Common failure modes

- **Accretion-only gardening** — every incident adds context and nothing is
  pruned.
- **Premature cultivation** — one anecdote becomes a universal rule.
- **Wrong owner** — all improvements are written into persistent instructions.
- **Aesthetic pruning** — concise-looking context replaces necessary context
  without outcome evidence.
- **Route neglect** — accurate material exists but entry points no longer lead
  to it.
- **Stale authority** — superseded context remains active because retirement
  is not represented.
- **Unowned garden** — no cadence or responsibility exists for reviewing
  context health.
- **Activity without evaluation** — changes are counted, but their effect on
  discovery, cost, and outcomes is unknown.

## Related

- [Context engineering](../foundations/context-engineering.md)
- [Harness engineering](../foundations/harness-engineering.md)
- [Agent legibility](../foundations/agent-legibility.md)
- [Progressive disclosure](../patterns/progressive-disclosure.md)
- [Instruction files](../elements/instruction-files.md)
- [Agent skills](../elements/agent-skills.md)

[^anthropic-context-engineering]: Anthropic — Effective context engineering for AI agents
[^openai-harness-engineering]: OpenAI — Harness engineering
[^cursor-harness-improvement]: Cursor — Continually improving our agent harness
