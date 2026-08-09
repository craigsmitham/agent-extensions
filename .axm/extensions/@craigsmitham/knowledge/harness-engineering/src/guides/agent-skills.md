---
type: Playbook
title: How to design an agent skill
description: Turn a recurring workflow into a focused, discoverable, portable skill with testable activation and execution behavior.
tags: [harness, skills, authoring, workflow, validation]
status: stable
sources:
  - id: agent-skills-spec
    resource: https://agentskills.io/specification
    title: Agent Skills specification
  - id: openai-build-skills
    resource: https://learn.chatgpt.com/docs/build-skills
    title: OpenAI — Build skills
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T20:30:58Z
---

# How to design an agent skill

Use this guide to turn a workflow you understand into a skill that agents can
discover and execute. It assumes the reader can create files in the target
harness and can run that host's validator. For the mental model and element
boundaries, read [Agent skills](../elements/agent-skills.md).

## Goal

Produce one self-contained skill whose activation, workflow, requirements, and
completion behavior can be tested independently.

## Before you start

Gather:

- observed examples of the workflow succeeding and failing;
- the intended users, application domains, and working environments;
- required tools, permissions, runtimes, and network access;
- the host's installation and validation rules;
- any material the skill would otherwise duplicate.

If the workflow has not repeated and cannot yet be stated coherently, capture
the observation first. Do not freeze an untested guess into a reusable skill.

## Steps

### 1. Bound one job

Write one sentence for each boundary:

- **Starts when:** the recognizable task or situation appears.
- **Succeeds when:** the observable outcome exists.
- **Does not own:** adjacent work that should remain elsewhere.

Split the skill if it has unrelated starting conditions or outcomes. Keep
branches that are genuine variations of the same job.

### 2. Choose the smallest implementation

Start with instructions. Add other resources only when their semantics require
them. OpenAI likewise recommends keeping each skill focused on one job and
preferring instructions unless deterministic behavior or external tooling
requires more.[^openai-build-skills]

| Need | Artifact |
| --- | --- |
| Judgment, sequencing, recovery | `SKILL.md` instructions |
| Detailed facts used by some branches | `references/` |
| Reusable templates or static inputs | `assets/` |
| Exact, repetitive transformation | `scripts/` |
| External action or live observation | A declared host tool or connector |

Do not create directories merely to make the skill look complete.

### 3. Write the routing description

Lead with what the skill does, then state when to use it. Add an explicit
negative boundary when neighboring tasks could match.

```yaml
---
name: review-api-contracts
description: Reviews API contract changes for compatibility and missing migration notes. Use when auditing an API diff or release. Not for implementing endpoints or load testing.
---
```

Use words that actually appear in likely requests: task verbs, artifact names,
file types, tools, and domain terms. Keep human-facing registry prose separate
from this model-facing routing contract.

### 4. Declare inputs, outputs, and authority

Near the beginning of the body, make clear:

- what the caller may provide;
- what the skill must discover;
- what artifact or decision it returns;
- which writes or external actions are allowed;
- which decisions require confirmation or escalation.

Do not hide destructive or externally mutable behavior inside a late step.

### 5. Write an executable workflow

Use imperative steps in the order work should happen. For every material step,
name the input it consumes and the evidence it produces. Include branches only
where the agent must make a real decision.

Prefer:

> Inspect the changed schema files, classify compatibility, then report each
> breaking change with its consumer and migration requirement.

Avoid vague aspirations such as “ensure the API is high quality.”

### 6. Route to supporting resources

Keep the main body as the control plane. Link a reference at the step where it
becomes necessary and say why to open it. Keep references shallow and focused
so one choice does not load an unrelated manual.[^agent-skills-spec]

Use relative paths within the skill package. Do not depend on an authoring
machine's absolute paths or undeclared neighboring extensions.

### 7. Add deterministic helpers selectively

Add a script when repeated model improvisation would be less reliable than
code. Make it:

- self-contained or explicit about dependencies;
- safe by default and scoped to resolved targets;
- non-interactive when automation may call it;
- clear about side effects;
- useful on failure, with actionable error output;
- testable outside the agent conversation.

The instructions should say when to run it, what inputs are allowed, and how to
interpret its output.

### 8. Test activation separately from execution

Build a small prompt set:

| Case | Expected behavior |
| --- | --- |
| Clear positive | Skill activates |
| Paraphrased positive | Skill still activates |
| Adjacent negative | Skill does not activate |
| Explicit invocation | Skill runs even when the task wording is sparse |
| Ambiguous case | Skill gathers context or stays out according to its boundary |

Revise the description when routing fails. Revise the body when execution
fails. Do not compensate for one contract by bloating the other.

### 9. Exercise the workflow

Run at least one representative task end to end and inspect:

- whether the agent loaded only relevant resources;
- whether every required tool and permission was available;
- whether decisions had enough evidence;
- whether failures produced a recovery path;
- whether the final result satisfied the stated completion condition;
- whether interruption leaves acquired resources or external state safe.

Use synthetic fixtures for portable public skills. Never copy sensitive
operational material into an example.

### 10. Validate and package with the host

Run the format validator and the package manager or harness checks required by
the installation target. The Agent Skills specification defines the portable
core; hosts may impose additional manifest, dependency, or distribution rules.[^agent-skills-spec]

Review the complete packaged contents, not only `SKILL.md`. Scripts, assets,
symlinks, examples, and generated metadata are part of the deliverable.

### 11. Maintain from observed failures

When the skill misses or mishandles a real task, classify the failure before
editing:

- routing failure → description or invocation policy;
- missing judgment → workflow instruction;
- missing fact → focused reference;
- repeated mechanical error → script or check;
- unavailable capability → tool or environment;
- wrong authority → permission or escalation boundary.

Add the smallest durable correction, then rerun the relevant activation and
execution cases.

## Done when

- one job and its non-goals are clear;
- positive and negative prompts route correctly;
- steps have explicit inputs, outputs, and completion evidence;
- optional resources load only when needed;
- dependencies, permissions, and side effects are truthful;
- the package validates and works from a clean installation.

## Related

- [Agent skills](../elements/agent-skills.md)
- [Instruction files](../elements/instruction-files.md)

[^agent-skills-spec]: Agent Skills specification
[^openai-build-skills]: OpenAI — Build skills
