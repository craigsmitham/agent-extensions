---
type: Reference
title: Harness engineering glossary
description: Concise definitions for the disciplines, domains, topologies, environments, and elements used throughout the harness-engineering bundle.
tags: [harness, context, coding-agents, terminology, vocabulary]
status: stable
sources:
  - id: microsoft-agent-experience
    resource: https://developer.microsoft.com/blog/the-ax-stack-whats-fixed-where-you-can-win
    title: Microsoft — The AX stack
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T20:53:20Z
---

# Harness engineering glossary

This glossary establishes the bundle's working vocabulary. Product ecosystems
may use the same words differently; individual concept documents explain the
important distinctions and tradeoffs.

## Core disciplines

**Harness engineering**
: The discipline of designing, evaluating, and maintaining the system around
  an agent so model capability becomes useful, bounded, and verifiable
  behavior. See [Harness engineering](foundations/harness-engineering.md).

**Context engineering**
: The discipline of shaping the informational environment an agent receives,
  discovers, produces, and carries through a task. See
  [Context engineering](foundations/context-engineering.md).

**Prompt engineering**
: Designing instructions or inputs for a particular model interaction. It is
  one technique within context engineering, not a synonym for it.

## System and specialization

**Agent**
: A model operating in a loop that can observe, decide, act, and incorporate
  the results of its actions.

**Agent harness**
: The concrete system that mediates among an agent, a task, and a working
  environment. It may provide context, tools, runtime, state, feedback, and
  controls.

**Agent experience (AX)**
: An emerging lens on how effectively an agent can operate with a technology,
  harness, and working environment. It includes discoverability and
  legibility, tool affordances, feedback quality, authority, continuity, and
  recovery. In this bundle, harness engineering names the engineering
  discipline; agent experience describes the resulting conditions from the
  agent's perspective.[^microsoft-agent-experience]

**Agent legibility**
: The degree to which a harness and working environment render task-relevant
  intent, state, capabilities, constraints, and consequences discoverable and
  usable by an agent. It is one dimension of agent experience. See
  [Agent legibility](foundations/agent-legibility.md).

**Application domain**
: The kind of work for which a harness is designed, such as software
  engineering, research, operations, or computer use.

**Domain profile**
: A documented specialization of general harness principles for one
  application domain.

**Harness element**
: An identifiable constituent used to shape or operate a harness, such as an
  instruction file, skill, tool, hook, check, state store, or execution
  environment.

**Coding harness**
: A common term for a software engineering harness, ranging from a local coding
  agent with repository context to a distributed remote-agent runtime. See
  [Software engineering harnesses](domains/software-engineering/harnesses.md).

**Runtime topology**
: The arrangement in which agents execute and coordinate, such as local,
  remote, interactive, background, persistent, ephemeral, single-agent, or
  multi-agent.

**Working environment**
: The systems and artifacts an agent observes and changes while working, such
  as a repository, worktree, container, browser, CI system, or cloud account.

## Context and continuity

**Context**
: Information available to the agent for its current decisions, including
  instructions, task state, retrieved knowledge, observations, and feedback.

**Context source**
: An artifact or system from which context can be selected, such as a file,
  search index, tool result, event stream, or memory store.

**Progressive disclosure**
: Advertising a small description or route first, then loading deeper context
  only when it becomes relevant. See
  [Progressive disclosure](patterns/progressive-disclosure.md).

**Context gardening**
: The recurring practice of cultivating useful context from observed work by
  repairing discovery, pruning noise, and moving knowledge to the right
  harness elements. See [Context gardening](practices/context-gardening.md).

**Repository context**
: Context supplied or discovered from repository-local artifacts, including
  code, instructions, documentation, plans, tests, and history.

**Coding context**
: All information relevant to a software-engineering task. It can include
  repository context as well as product intent, runtime state, review,
  observability, and delivery information.

**Task state**
: The explicit account of a task's goals, decisions, progress, open questions,
  and completion status.

**Execution state**
: Current facts about actions and environmental changes, such as what was
  inspected, modified, attempted, or verified.

**Memory**
: Persisted information made available beyond the interaction in which it was
  learned. Memory may be personal, domain-level, environment-local,
  task-specific, or execution-derived; those scopes should not be conflated.

## Interfaces, evidence, and control

**Tool**
: An action or observation interface the agent can invoke. A tool exposes a
  capability; it does not by itself define the workflow surrounding its use.

**Feedback**
: Information returned after an action that helps the agent update its
  understanding, such as tool output, errors, tests, metrics, or review
  findings.

**Verification**
: Establishing with appropriate evidence that an outcome or requirement holds.

**Evaluation**
: Measuring the behavior or quality of the model–harness–environment system
  across representative tasks or conditions.

**Observability**
: The ability to inspect a harness run and its environment through logs,
  traces, metrics, events, artifacts, and state.

**Authority**
: The actions and resources an agent is permitted to use or affect.

**Containment**
: Structural limits on the effects an agent can produce, using boundaries such
  as sandboxes, isolated credentials, filesystem scopes, or network policy.

**Guardrail**
: A control that guides, checks, blocks, or escalates agent behavior. A
  guardrail may be advisory and probabilistic or mechanically enforced.

## Common harness elements

**Instruction file**
: Persistent feedforward context that establishes scoped invariants, working
  facts, and discovery routes. See
  [Instruction files](elements/instruction-files.md).

**Agent skill**
: A reusable workflow packaged behind routing metadata and loaded on demand,
  often with references, assets, or scripts. See
  [Agent skills](elements/agent-skills.md).

**Hook**
: Logic invoked automatically at a defined lifecycle event, such as before a
  tool call, after an action, or before context compression.

**Knowledge artifact**
: A document or structured resource that supplies facts, explanation, or
  reference material without necessarily prescribing a workflow.

**Plan**
: An explicit representation of intended work, dependencies, decisions, and
  progress that can support review and continuation.

**Check**
: An executable mechanism that decides a property and returns evidence, such
  as a test, linter, schema validator, policy check, or finish gate.

**Trace**
: A chronological record of model interactions, tool calls, observations, and
  state transitions during a harness run.

**Receipt**
: A compact, attributable record of an action or verification result intended
  for review, handoff, or audit.

[^microsoft-agent-experience]: Microsoft — The AX stack
