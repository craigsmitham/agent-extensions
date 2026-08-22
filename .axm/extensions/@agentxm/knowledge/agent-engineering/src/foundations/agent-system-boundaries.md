---
type: Reference
title: Agent-system boundaries
description: Distinguishes agent, prompt, context, harness, workflow, skill, and evaluation responsibilities across an agent system.
tags: [agent-systems, boundaries, ownership, harness, context, prompt, workflow, skills, evaluation]
status: stable
sources:
  - id: openai-sdk
    resource: https://openai.github.io/openai-agents-python/
    title: OpenAI Agents SDK
  - id: anthropic-agents
    resource: https://www.anthropic.com/engineering/building-effective-agents
    title: Anthropic — Building effective agents
  - id: anthropic-context
    resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
    title: Anthropic — Effective context engineering for AI agents
  - id: anthropic-evals
    resource: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
    title: Anthropic — Demystifying evals for AI agents
generated: { by: "codex/gpt-5.6", at: 2026-08-21T22:05:43Z }
stale_after: 2027-02-14
---

# Agent-system boundaries

This reference owns the cross-discipline comparison for an agent system.
Assign responsibility to the smallest surface whose design can explain and
repair the behavior. Influence is shared; ownership should not be.

## Discipline boundaries

| Discipline | Owns | Boundary cue |
| --- | --- | --- |
| Agent engineering | Agency choice, goals, control loops, planning, capability and memory policy, delegation, recovery, stopping, and human control | Defines goal-directed behavior rather than the whole application around it |
| Prompt engineering | Intentional model-facing instructions, examples, templates, and response contracts | Expresses behavior to a model but cannot enforce external effects |
| Context engineering | Selection, provenance, ordering, routing, loading, compaction, and retirement of information in attention | Owns the information lifecycle rather than the behavioral policy or runtime |
| Harness engineering | Model invocation, tool implementation, runtime, persistence, mechanical feedback, validation, permissions, and enforcement | Implements operating conditions around the agent rather than deciding its goals |
| Workflow automation | Predefined schedules, dependencies, gates, retries, cancellation, compensation, and durable process state | Owns inspectable process control rather than model-directed choice inside an agent step |
| Skill engineering | Discoverable workflow packaging, routing, resources, execution contract, trust, admission, and lifecycle | Owns one reusable job rather than the actor or host that selects it |
| Evaluation engineering | Objectives, task distributions, trials, graders, baselines, uncertainty, aggregation, validity, and suite lifecycle | Owns general measurement method while the target discipline defines consequential behavior and risk |

Prompt engineering is one technique within the informational surface of an
agent system, while context engineering governs all information made available
for inference.[^anthropic-context] Evaluation combines automated evidence,
production signals, experiments, and human judgment without turning any one of
those methods into the target's engineering owner.[^anthropic-evals]

## Shared concerns

| Concern | Primary owner | Neighboring responsibility |
| --- | --- | --- |
| Goal and completion | Agent engineering defines outcome, responsibility, evidence, stopping, escalation | Prompt expresses; harness enforces hard limits and captures evidence |
| Tool use | Agent engineering defines when, why, and how capability is selected | Harness implements, authorizes, executes, and validates; prompt describes |
| Observation | Agent engineering defines what evidence decisions require | Harness exposes signals; context selects and represents them |
| Memory | Agent engineering defines what may influence later behavior | Context owns provenance, scope, freshness, compaction, retirement; harness persists |
| Planning and recovery | Agent engineering defines decisions, replanning, retry, fallback, escalation | Harness reports failure and applies budgets or limits |
| Delegation and handoff | Agent engineering defines actors, responsibilities, authority, artifacts, acceptance | Harness dispatches and transfers state; prompt carries model-facing wording |
| Durable process | Agent engineering owns dynamic choices inside an agent step | Workflow automation owns schedules, dependencies, retries, cancellation, and compensation |
| Reusable job | Agent engineering may select or delegate a job | Skill engineering owns routing, packaged procedure, resources, trust, and lifecycle |
| Evaluation | Agent engineering defines behaviors, risks, and scenarios that matter | Evaluation engineering owns sampling, trials, graders, uncertainty, validity, and reporting |

An SDK may package agents, tools, loops, handoffs, guardrails, sessions,
human-in-the-loop controls, and tracing together.[^openai-sdk] Product
co-location does not erase the conceptual boundaries: each failure still needs
an accountable design surface. The same holds for practitioner patterns that
combine routing, parallel workers, evaluators, and agents in one implementation.[^anthropic-agents]

Use cross-layer changes when evidence shows several surfaces jointly caused a
failure, but state each change's responsibility. Avoid “the agent” as a label
for the entire application, platform, harness, or workflow graph.

[^openai-sdk]: OpenAI Agents SDK
[^anthropic-agents]: Anthropic — Building effective agents
[^anthropic-context]: Anthropic — Effective context engineering for AI agents
[^anthropic-evals]: Anthropic — Demystifying evals for AI agents
