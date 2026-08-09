---
type: Explanation
title: Progressive disclosure
description: How progressive disclosure keeps initial context small while preserving reliable routes to deeper knowledge, workflows, tools, and state.
tags: [harness, context, routing, retrieval, discovery, attention-budget]
status: stable
sources:
  - id: anthropic-context-engineering
    resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
    title: Anthropic — Effective context engineering for AI agents
  - id: openai-harness-engineering
    resource: https://openai.com/index/harness-engineering/
    title: OpenAI — Harness engineering
  - id: cursor-dynamic-context
    resource: https://cursor.com/blog/dynamic-context-discovery
    title: Cursor — Dynamic context discovery
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T20:53:20Z
---

# Progressive disclosure

**Progressive disclosure** is a context pattern that presents a small,
decision-useful route before loading the deeper material behind it. The agent
first learns that a capability or source exists and when it matters; it pays
the full context cost only after that condition is met.

```text
advertise a route  →  select it when relevant  →  load the needed depth
```

The pattern reconciles two competing needs. Agents need enough context to
discover what could help, but loading every potentially useful instruction,
tool, document, observation, and memory item would consume their finite
attention budget. Anthropic therefore recommends a small set of high-signal
tokens and just-in-time exploration rather than exhaustive context up
front.[^anthropic-context-engineering]

## The three-part structure

| Part | Responsibility | Examples |
| --- | --- | --- |
| Route | Advertise what exists, when it applies, and how to reach it | Index entry, skill description, tool group, search result |
| Selection | Decide whether the current task warrants the deeper context | Trigger, query, scope match, agent judgment |
| Depth | Supply the detailed material needed for the selected work | Skill body, reference, tool schema, file, trace, memory record |

All three parts matter. Depth without a route is invisible. A route without a
meaningful selection condition becomes an invitation to load everything. A
route whose destination does not fulfill its promise teaches the agent that
discovery metadata cannot be trusted.

## A route is a decision contract

The initial surface should not summarize all the hidden content. It should
provide the smallest information needed to make the next decision:

- what lies behind the route;
- the situations in which it changes action;
- meaningful boundaries with adjacent routes; and
- the cost or authority involved when that affects selection.

This is why routing metadata is behavioral. A skill description, index entry,
or compact tool summary influences whether the deeper capability ever
participates in the task.

OpenAI describes the repository form as “a map, not a 1,000-page instruction
manual”: a small instruction surface points into a structured knowledge base
instead of absorbing it.[^openai-harness-engineering] Cursor applies the same
idea beyond documentation by making histories, terminals, large tool results,
and tool definitions discoverable through compact file-like routes.[^cursor-dynamic-context]

## Disclosure is not merely lazy loading

Lazy loading is an implementation technique: defer fetching bytes until they
are requested. Progressive disclosure is an information architecture: expose
enough meaning for an agent to know that a request should be made.

A resource can be lazy-loaded yet undiscoverable. Conversely, a short catalog
can disclose a resource progressively even if the harness has already cached
its contents. The essential property is the staged decision surface, not the
storage mechanism.

## Relationship to scope

Scope and progressive disclosure reduce context cost in different ways:

- **Scope** excludes information that does not apply to the current user,
  component, environment, role, or task.
- **Progressive disclosure** defers applicable information until the task
  reaches a decision that needs it.

Good harnesses combine them. An organization-wide instruction may advertise a
domain route; the selected domain may advertise a workflow; the workflow may
load one reference only when a particular branch is taken.

## Where the pattern appears

| Surface | Initial disclosure | Deeper context |
| --- | --- | --- |
| Instruction system | Short invariant or trigger | Domain guide, skill, or reference |
| Skill catalog | Name and routing description | Workflow body, then optional resources |
| Knowledge bundle | Section index or search result | Concept document and related concepts |
| Tool system | Compact capability summary | Full schema, help, or live result |
| Memory | Topic, provenance, and freshness signal | Stored decision or history |
| Observability | Signal, summary, or trace index | Detailed logs, spans, metrics, or screenshots |

The pattern transfers across application domains because it depends on
attention and discovery, not on repositories or coding tools.

## Consequences and tradeoffs

Progressive disclosure reduces always-on context and makes large capability
surfaces navigable. It also introduces routing risk and retrieval latency. The
harness must make selection observable enough to distinguish “the deeper
knowledge was wrong” from “the route was never found or selected.”

This creates two separate evaluation questions:

1. **Routing quality** — did representative tasks select the right depth and
   reject adjacent routes?
2. **Destination quality** — once selected, did the deeper material enable the
   intended outcome?

Improving one does not compensate for failure in the other.

## Common failure modes

- **Invisible depth** — useful content exists without a route from likely
  entry points.
- **Encyclopedic entry point** — the route tries to contain the destination.
- **Descriptive-only route** — it names a topic but gives no selection signal.
- **Indiscriminate activation** — vague triggers load depth for adjacent work.
- **Broken promise** — metadata advertises help that the destination does not
  supply.
- **Unbounded descent** — each destination points elsewhere without providing
  enough information to act.
- **Hidden authority change** — following a route silently introduces stronger
  instructions or capabilities.
- **Unmeasured routing** — outcome failures are blamed on content without
  checking whether the right content entered context.

## Related

- [Context engineering](../foundations/context-engineering.md)
- [Agent legibility](../foundations/agent-legibility.md)
- [Context gardening](../practices/context-gardening.md)
- [Instruction files](../elements/instruction-files.md)
- [Agent skills](../elements/agent-skills.md)

[^anthropic-context-engineering]: Anthropic — Effective context engineering for AI agents
[^openai-harness-engineering]: OpenAI — Harness engineering
[^cursor-dynamic-context]: Cursor — Dynamic context discovery
