---
type: Explanation
title: Agent Skill evaluation model
description: The dimensions, identities, and evidence required for a defensible skill evaluation.
tags: [agent-skills, evaluation, evidence, contracts]
status: stable
generated: { by: "codex/gpt-5.6", at: 2026-08-14T19:36:04Z }
sources:
  - id: anthropic-best-practices
    resource: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
    title: Anthropic — Skill authoring best practices
---

# Agent Skill evaluation model

A useful evaluation binds evidence to an exact skill revision, host, model,
configuration, fixture set, and time. A result without those identities is an
anecdote: skill behavior is produced by their interaction, not by `SKILL.md`
alone. Anthropic likewise recommends evaluating skills on the models they are
intended to support.[^anthropic-best-practices]

Evaluate two independent stages:

1. **Routing** — whether metadata selects the skill for intended work and
   rejects neighboring work.
2. **Execution** — whether an already activated skill completes its promised
   job within its authority.

Then grade the material dimensions of the contract: outcome, instruction
adherence, efficiency, safety, recovery, and robustness. A single aggregate
score must not hide a critical failure or untested claim.

## Evidence hierarchy

Prefer observable state and deterministic checks, then bounded rubric judgments,
then self-report. Preserve prompts, fixtures, outputs, traces, grader version,
and environmental limitations. Distinguish `failed` from `not testable`.

## Defensible conclusions

- **Supported** means representative evidence supports every material claim in
  the tested scope.
- **Partially supported** means useful behavior exists but a material claim or
  boundary does not hold.
- **Unsupported** means evidence contradicts a central claim.
- **Inconclusive** means the available evidence cannot decide.

Absence of an observed failure is not evidence of support.

[^anthropic-best-practices]: Anthropic — Skill authoring best practices
