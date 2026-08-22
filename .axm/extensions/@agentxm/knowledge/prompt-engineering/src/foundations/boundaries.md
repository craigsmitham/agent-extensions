---
type: Reference
title: Prompt boundary responsibilities
description: How prompt engineering shares variables, tools, stopping, handoffs, output schemas, safety, evaluation, and versioning with neighboring owners without absorbing their authority.
tags: [prompt-engineering, boundaries, variables, tools, stopping, handoffs, output-schema, safety, evaluation, versioning]
status: stable
generated: { by: "codex/gpt-5.6", at: 2026-08-21T22:05:43Z }
stale_after: 2027-02-14
sources:
  - id: anthropic-context
    resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
    title: Anthropic — Effective context engineering for AI agents
  - id: anthropic-evals
    resource: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
    title: Anthropic — Demystifying evals for AI agents
---

# Prompt boundary responsibilities

Prompt engineering owns intentional model-facing instructions, examples,
templates, and response contracts. It is used by agents, tools, graders,
handoffs, skills, and other invocation surfaces, but it does not acquire those
artifacts' behavioral, informational, runtime, or assurance authority.

Anthropic distinguishes prompt methods for writing and organizing instructions
from context engineering, which curates all tokens available during inference,
including tools, history, and external data.[^anthropic-context] It also
distinguishes a response or transcript from the environment outcome an agent
claims to have produced.[^anthropic-evals]

Assign a prompt the smallest model-facing responsibility that can explain and
repair the observed failure. Use the following boundaries when the same
concern crosses several surfaces.

## Shared concerns, different owners

| Concern | Prompt responsibility | Neighbor responsibility |
| --- | --- | --- |
| Variables | Declare meaning, type, and expected placement | Context selects and supplies values; harness renders safely |
| Tool use | Express capability semantics, inputs, results, and model-facing error guidance | Agent engineering owns selection and recovery policy; harness implements, authorizes, executes, and validates |
| Stopping and escalation | Express the conditions and expected response | Agent engineering owns the behavioral policy; harness enforces hard limits and approval gates |
| Handoffs | Express responsibility and state to the receiving model | Agent engineering owns delegation and acceptance; harness dispatches and transfers durable state |
| Output schema | State semantic fields and interaction requirements | Structured-output or validation code enforces syntax |
| Safety | Communicate role, limits, and escalation behavior | Harness enforces least privilege, approvals, isolation, and monitoring |
| Evaluation | Define prompt-specific behavior and preserve rendered prompt identity | Evaluation engineering owns general measurement method; target disciplines define their specialized evidence |
| Versioning | Version prompt content and its compatibility evidence | Each neighboring artifact versions its own configuration and lifecycle |

No layer should absorb another merely because all of them ultimately influence
model behavior.

[^anthropic-context]: Anthropic — Effective context engineering for AI agents
[^anthropic-evals]: Anthropic — Demystifying evals for AI agents
