---
type: Explanation
title: Software engineering harnesses
description: How software engineering harnesses apply harness and context engineering across local development, repositories, remote workers, and distributed runtimes.
tags: [coding-agents, software-engineering, repositories, remote-agents, runtime, domain-profile]
status: stable
sources:
  - id: openai-harness-engineering
    resource: https://openai.com/index/harness-engineering/
    title: OpenAI — Harness engineering
  - id: openai-symphony
    resource: https://openai.com/index/open-source-codex-orchestration-symphony/
    title: "OpenAI — An open-source spec for Codex orchestration: Symphony"
  - id: cursor-remote-agents
    resource: https://cursor.com/blog/agent-computer-use
    title: Cursor — Agents can control their own computers
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T20:53:20Z
---

# Software engineering harnesses

A **coding harness** is an agent harness specialized for software engineering.
The term usefully covers a wide range: a coding agent launched in a local
repository, an isolated worker producing a pull request in the background, or
a distributed runtime coordinating many agents and tasks.

What makes each one a coding harness is not its size or location. It is the
combination of a software-engineering goal, an agent runtime, a working
environment, and the context and feedback needed to change software reliably.

## One domain, several scales

```text
local assistant
    → isolated task worker
        → remote background agent
            → distributed coding-agent system
```

At the small end, a harness may be a model, an agent loop, shell and editing
tools, repository instructions, and the developer's existing environment. At
the large end, it may provision remote machines, isolate branches, broker
credentials, schedule dependent tasks, persist state, collect logs and test
artifacts, and integrate results with issue and review systems.

These are differences in runtime topology and operational responsibility, not
different application domains. OpenAI's account of an agent-first codebase
includes repository knowledge, per-worktree applications and observability,
skills, checks, and review loops.[^openai-harness-engineering] Its Symphony
specification extends the same domain into task orchestration with isolated
workspaces and a project-management control plane.[^openai-symphony]

## The repository matters, but is not the whole harness

The repository is usually both:

- a **working environment** containing code and versioned artifacts; and
- a **context source** containing structure, instructions, documentation,
  examples, plans, and history.

Calling the whole discipline “repository harness engineering” would omit
important infrastructure outside that boundary. A remote coding harness may
also depend on worker images, queues, sandboxes, credential brokers, network
policies, caches, browsers, observability services, CI, and pull-request
automation.

“Repository context engineering” remains a useful narrower phrase for shaping
what repository-local information agents can discover and use. It is one
concern inside a coding harness.

## Coding-harness concerns

| Concern | Representative design questions |
| --- | --- |
| Task specification | Is the issue actionable, bounded, and verifiable? |
| Repository context | Can the agent find architecture, conventions, owners, and canonical examples without loading everything? |
| Code navigation | Can it search symbols, dependencies, history, and related changes efficiently? |
| Development environment | Can it install, build, run, and debug the software reproducibly? |
| Change isolation | Does each task have an appropriate branch, worktree, container, or VM? |
| Feedback | Can the agent read tests, compiler output, logs, metrics, UI state, and review findings? |
| Task continuity | Can work survive context compression, interruption, retry, or worker replacement? |
| Authority | Which files, repositories, services, credentials, and deployment actions are permitted? |
| Delivery integration | How do changes enter review, CI, merge, rollout, and recovery workflows? |

Remote agents make these concerns more visible because the developer's machine
and tacit knowledge are absent. Cursor describes provisioning full remote
development environments and returning screenshots, videos, and logs so a
human can validate the agent's work.[^cursor-remote-agents] The same needs
exist locally; local tools often satisfy them implicitly.

## Coding context

[Context engineering](../../foundations/context-engineering.md) in this domain includes more
than selecting source files. Relevant context can include:

- the task, acceptance criteria, and product intent;
- repository instructions and scoped conventions;
- architecture, domain vocabulary, and dependency structure;
- reusable workflows and repository-specific commands;
- source, tests, schemas, examples, and version history;
- the current branch, diff, task plan, and execution state;
- live application behavior and verification results;
- review comments, CI failures, and deployment evidence.

The useful unit is therefore **coding context**, not merely code context. A
source snippet may explain implementation while omitting the reason for a
change, the command that verifies it, or the operational evidence that makes
it safe to ship.

## Term boundaries

| Term | Meaning |
| --- | --- |
| Coding agent | The agent that reasons and acts on software work |
| Coding harness | The system around that agent for software-engineering tasks |
| Coding environment | The filesystem, tools, dependencies, services, and compute where work executes |
| Repository context | Information supplied or discovered from repository-local artifacts |
| Coding context | All task-relevant information, including repository, runtime, product, and feedback context |

A product name may refer to both an agent and its harness in ordinary speech.
The distinction becomes important when diagnosing failures: changing the model
will not repair a broken environment, missing repository route, stale task
state, or inadequate verification surface.

## A domain profile, not a separate discipline

Software engineering harnesses apply the general principles of
[harness engineering](../../foundations/harness-engineering.md) to software
work. [Agent legibility](../../foundations/agent-legibility.md) provides one
cross-domain quality for evaluating how well source structure, application
state, tools, and evidence are exposed. Local and remote implementations should
be compared by how well they fulfill the same
responsibilities, not by whether they use the same files or infrastructure.

See the [glossary](../../glossary.md) for the bundle's shared terminology.

[^openai-harness-engineering]: OpenAI — Harness engineering
[^openai-symphony]: OpenAI — An open-source spec for Codex orchestration: Symphony
[^cursor-remote-agents]: Cursor — Agents can control their own computers
