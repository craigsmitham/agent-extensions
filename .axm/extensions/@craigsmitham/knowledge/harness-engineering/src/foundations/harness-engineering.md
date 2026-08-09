---
type: Explanation
title: Harness engineering
description: How harness engineering designs the context, runtime, interfaces, feedback, and controls that turn model capability into reliable agent behavior.
tags: [harness, agents, runtime, feedback, controls, systems]
status: stable
sources:
  - id: openai-harness-engineering
    resource: https://openai.com/index/harness-engineering/
    title: OpenAI — Harness engineering
  - id: ai-harness-runtime
    resource: https://arxiv.org/abs/2605.13357
    title: AI Harness Engineering — A Runtime Substrate for Foundation-Model Software Agents
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T20:53:20Z
---

# Harness engineering

**Harness engineering** is the discipline of designing, evaluating, and
maintaining the system around an agent so that a model's latent capability
becomes useful, bounded, and verifiable behavior. The harness mediates between
intent, the model, and the environment in which work happens.

The central idea is that an agent's behavior is a property of a system, not of
the model alone:

```text
intent → harness → model ↔ working environment → evidence and outcome
```

A capable model can still fail when it receives the wrong context, cannot
observe the relevant state, uses a poor action interface, loses task progress,
or has no reliable way to establish completion. Conversely, a well-designed
harness can make the same model more effective by shaping those conditions.
OpenAI describes this shift as engineering environments, intent, and feedback
loops rather than focusing only on writing code or prompts.[^openai-harness-engineering]

## What the harness owns

A harness may be small or distributed, but it normally carries some combination
of these responsibilities:

| Responsibility | Question |
| --- | --- |
| Intent and task specification | What outcome is sought, and what counts as done? |
| Context | What should the agent know now, and where can it find more? |
| Action and observation interfaces | What can the agent do and inspect? |
| Runtime and environment | Where does work execute, and how is it isolated and reproduced? |
| State and continuity | What has happened, what remains current, and how can work resume? |
| Feedback and verification | What evidence shows progress, failure, or completion? |
| Authority and containment | What may the agent affect, and where must it stop or escalate? |
| Operation and improvement | How are runs observed, evaluated, diagnosed, and improved? |

Recent research describes a similar runtime substrate spanning task
specification, context selection, tool access, project memory, task state,
observability, failure attribution, verification, permissions, and maintenance
state.[^ai-harness-runtime] The exact decomposition matters less than preserving
the whole-system view.

## More than prompting

Prompting supplies language to a model at a particular moment. Harness
engineering decides the larger conditions under which prompts are assembled,
actions are permitted, state changes, and outcomes are judged.

An instruction such as “run the tests” is prompt-level guidance. A harness can
also provide the test command, provision its dependencies, execute it in an
isolated workspace, summarize its output, block completion on failure, and
retain the result as evidence. The instruction may still help, but reliability
comes from the surrounding arrangement.

Harness engineering is also broader than selecting an agent framework. A
framework supplies implementation primitives; harness engineering decides how
those primitives should work together for a particular distribution of tasks.

## Principles that transfer across domains

### Design the model–harness–environment system

Judge the behavior of the complete system. Replacing the model may help, but
many failures originate in missing information, poor interfaces, environmental
friction, ambiguous authority, or weak feedback.

### Make relevant state legible

An agent can reason only about state it can observe in a usable form. Harnesses
therefore expose the environment through files, structured tools, logs,
metrics, traces, screenshots, schemas, or other representations appropriate to
the domain. [Agent legibility](agent-legibility.md) describes this quality and
its relationship to action, feedback, and verification.

### Prefer feedback to repeated admonition

When compliance is mechanically decidable, executable checks are stronger than
additional prose. Useful failures return specific evidence and a recovery path
to the agent.

### Bound capability structurally

Probabilistic instructions influence what an agent tends to do. Sandboxes,
scoped credentials, tool policies, and approval boundaries constrain what it
can do. Reliable harnesses use both kinds of control for different purposes.

### Keep state explicit enough to resume

Long or remote work should not depend entirely on one conversation transcript.
Plans, checkpoints, task records, and execution state let another session or
worker determine what is current and continue safely.

### Improve from observed work

Agent failures are evidence about the system. A recurring miss may indicate a
context, interface, environment, verification, or authority gap. The durable
response is the smallest change to the responsible harness surface, followed
by evaluation on representative work. [Context gardening](../practices/context-gardening.md)
applies this principle to the context system.

## Domains, topologies, and environments

Harness engineering is a general discipline. Its principles are specialized
through a **domain profile**, such as software engineering, research, or
operations. The domain is distinct from the **runtime topology**—local,
remote, background, or multi-agent—and from the **working environment**, such
as a repository, browser, CI system, or cloud account.

This distinction prevents a domain from being confused with one element or
deployment choice. A coding harness, for example, may be a local agent working
in one repository or a distributed service coordinating remote workers. Both
specialize harness engineering for software work.

## Relationship to neighboring concepts

- [Context engineering](context-engineering.md) owns the informational
  environment and its lifecycle.
- [Agent legibility](agent-legibility.md) describes whether task-relevant
  intent, state, interfaces, and evidence are usable by the agent.
- [Software engineering harnesses](../domains/software-engineering/harnesses.md)
  apply the discipline to software work.
- [Instruction files](../elements/instruction-files.md) and
  [agent skills](../elements/agent-skills.md) are elements that implement
  parts of a harness; neither is the harness by itself.
- [Progressive disclosure](../patterns/progressive-disclosure.md) and
  [context gardening](../practices/context-gardening.md) describe a reusable
  context structure and its ongoing maintenance practice.
- [Glossary](../glossary.md) defines the vocabulary used across the bundle.

[^openai-harness-engineering]: OpenAI — Harness engineering
[^ai-harness-runtime]: AI Harness Engineering — A Runtime Substrate for Foundation-Model Software Agents
