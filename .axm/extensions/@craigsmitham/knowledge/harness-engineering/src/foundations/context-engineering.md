---
type: Explanation
title: Context engineering
description: How context engineering shapes the informational environment an agent receives, discovers, produces, and carries through a task.
tags: [context, retrieval, memory, routing, progressive-disclosure, provenance]
status: stable
sources:
  - id: anthropic-context-engineering
    resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
    title: Anthropic — Effective context engineering for AI agents
  - id: openai-harness-engineering
    resource: https://openai.com/index/harness-engineering/
    title: OpenAI — Harness engineering
  - id: context-files-evaluation
    resource: https://arxiv.org/abs/2602.11988
    title: Evaluating AGENTS.md — Are Repository-Level Context Files Helpful for Coding Agents?
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T20:48:38Z
---

# Context engineering

**Context engineering** is the discipline of shaping the informational
environment in which an agent makes decisions. It determines what information
is available, how it is represented, when it enters attention, how it changes
during work, and when it should be refreshed or discarded.

It is a responsibility within [harness engineering](harness-engineering.md),
not a synonym for the whole harness. Context can help an agent decide, but it
does not provision an execution environment, enforce a permission boundary, or
prove that an external effect occurred.

## Context is a lifecycle

Context engineering is more than composing an initial prompt:

```text
source → select → structure → route → load → use → refresh or retire
```

Each transition is a design choice. An accurate document can still be harmful
if it is loaded for every task, arrives after the relevant decision, lacks
provenance, or survives after the underlying state changes.

Anthropic frames context as a finite resource whose contents should remain
high-signal, using just-in-time retrieval and compact tools rather than loading
everything in advance.[^anthropic-context-engineering]

## Forms of context

| Form | Role | Examples |
| --- | --- | --- |
| Persistent guidance | Shapes decisions across tasks in a scope | Instructions, policies, routes |
| Task context | States the present goal and constraints | Request, issue, acceptance criteria |
| Retrieved knowledge | Supplies detail when a situation becomes relevant | Documentation, schemas, examples |
| Observed environment | Describes current external state | Files, API results, UI state, logs |
| Feedback | Reports consequences of an action | Test failures, validation output, review findings |
| Working state | Keeps the current task coherent | Plan, decisions, completed steps, checkpoints |

These forms have different owners and lifetimes. Persistent instructions should
not become a task backlog. A conversation transcript should not be the only
record of durable decisions. Retrieved reference material should not remain
authoritative after the underlying environment changes.

## Context quality is not context quantity

Useful context is:

- **relevant** to the next decisions;
- **sufficient** to act without hiding necessary constraints;
- **scoped** to the work and authority at hand;
- **current** with respect to the environment;
- **trustworthy and attributable** enough for its consequence;
- **economical** in attention, latency, and retrieval cost.

More context can reduce quality by flattening importance, introducing
contradictions, or distracting the agent from the task. A 2026 evaluation
found that repository context files caused agents to explore and test more but
increased cost by more than twenty percent without a significant improvement
in task success. The authors recommend minimal, necessary requirements and
evaluation rather than assuming additional instructions are beneficial.[^context-files-evaluation]

## Scope and progressive disclosure

Two complementary structures control context cost:

1. **Scope** places information with the users, components, or tasks to which
   it applies. Broad scopes contain genuine invariants; narrower scopes contain
   their differences.
2. [**Progressive disclosure**](../patterns/progressive-disclosure.md)
   advertises a small route first and loads deeper instructions or knowledge
   only when the route becomes relevant.

Together they create a context map: a small initial surface tells the agent
where to look without pretending that everything must already be in attention.
OpenAI describes using a short instruction file as a table of contents for
structured repository knowledge rather than as an encyclopedia.[^openai-harness-engineering]

## Feedforward and feedback

Context reaches an agent from both directions:

- **Feedforward context** arrives before action: intent, constraints,
  procedures, examples, and known state.
- **Feedback context** arrives after action: observations, errors, test
  results, review findings, and changed environmental state.

Weak context engineering concentrates on the initial prompt. Strong context
engineering also makes feedback compact, specific, and actionable so the agent
can revise its understanding. An executable check with a useful error can
carry more decision value than several paragraphs of advance instruction.

## Memory is not one thing

“Memory” often collapses several distinct concerns:

- personal preferences that span domains;
- shared domain or organizational knowledge;
- environment-local facts;
- task decisions and progress;
- mechanically derived execution state;
- compressed history from a conversation.

These differ in audience, authority, freshness, and retention. Context
engineering assigns each kind to an appropriate store and retrieval policy
instead of accumulating an undifferentiated memory blob.

## Common failure modes

- **Context dumping** — loading everything that might be relevant.
- **Missing route** — useful knowledge exists but cannot be discovered at the
  point of need.
- **Wrong scope** — local guidance consumes attention or changes behavior
  globally.
- **Stale authority** — plausible old context overrides current evidence.
- **History dependence** — essential task state exists only in a transcript.
- **Feedback flooding** — raw tool output crowds out its actionable result.
- **Untrusted injection** — external or repository-provided content gains more
  authority than its provenance warrants.
- **Compaction loss** — summarization drops decisions, evidence, or unresolved
  constraints needed later.

## Relationship to harness elements

Instruction files, skills, knowledge documents, search tools, plans, hooks,
and memory stores are context mechanisms. Context engineering determines their
information roles and lifecycle; their formats and host behavior remain
element-specific.

For the software-engineering application domain, see
[Software engineering harnesses](../domains/software-engineering/harnesses.md).
For ongoing maintenance of the context system, see
[Context gardening](../practices/context-gardening.md).
For shared definitions, see the [glossary](../glossary.md).

[^anthropic-context-engineering]: Anthropic — Effective context engineering for AI agents
[^openai-harness-engineering]: OpenAI — Harness engineering
[^context-files-evaluation]: Evaluating AGENTS.md — Are Repository-Level Context Files Helpful for Coding Agents?
