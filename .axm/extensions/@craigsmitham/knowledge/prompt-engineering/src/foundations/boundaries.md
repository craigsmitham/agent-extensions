---
type: Reference
title: Prompt, context, harness, skill, and evaluation boundaries
description: Which neighboring construction or assurance discipline owns each source of behavior, failure, and evidence.
tags: [prompt-engineering, context-engineering, harness-engineering, skill-engineering, eval-engineering, ownership]
status: stable
generated: { by: "codex/gpt-5.6", at: 2026-08-14T21:14:15Z }
stale_after: 2027-02-14
sources:
  - id: anthropic-context
    resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
    title: Anthropic — Effective context engineering for AI agents
  - id: anthropic-evals
    resource: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
    title: Anthropic — Demystifying evals for AI agents
---

# Prompt, context, harness, skill, and evaluation boundaries

Prompt engineering is a technique within the informational part of an agent
system, but it is used by more than one artifact type. Assign ownership by the
smallest surface whose change can explain and repair the observed failure.

| Discipline | Owns | Representative evidence |
| --- | --- | --- |
| Prompt engineering | Intentional instructions, examples, templates, and response contracts | Controlled prompt variants and response grading |
| Context engineering | Selection, provenance, ordering, routing, loading, compaction, and retirement of all information in attention | Retrieval, ablation, freshness, and context-use evidence |
| Harness engineering | Model configuration, tools, runtime, state, feedback, validation, permissions, and orchestration | End-to-end transcripts, environment state, safety and outcome checks |
| Skill engineering | Discoverable workflow packaging, routing, resources, execution contract, trust, admission, and lifecycle | Routing and activated-workflow evaluations |
| Evaluation engineering | Objectives, task distributions, trials, graders, baselines, uncertainty, aggregation, validity, and suite lifecycle | Attributable reports bound to target and evaluation identities |

Anthropic distinguishes prompt methods for writing and organizing instructions
from context engineering, which curates all tokens available during inference,
including tools, history, and external data.[^anthropic-context] It also
distinguishes a response or transcript from the environment outcome an agent
claims to have produced.[^anthropic-evals]

## Shared concerns, different owners

| Concern | Prompt responsibility | Neighbor responsibility |
| --- | --- | --- |
| Variables | Declare meaning, type, and expected placement | Context selects and supplies values; harness renders safely |
| Tool use | Explain selection, parameters, results, and error recovery | Harness implements, permissions, and validates the tool |
| Output schema | State semantic fields and interaction requirements | Structured-output or validation code enforces syntax |
| Safety | Communicate role, limits, and escalation behavior | Harness enforces least privilege, approvals, isolation, and monitoring |
| Evaluation | Define prompt-specific behavior and preserve rendered prompt identity | Evaluation engineering owns general measurement method; target disciplines define their specialized evidence |
| Versioning | Version prompt content and its compatibility evidence | Each neighboring artifact versions its own configuration and lifecycle |

No layer should absorb another merely because all of them ultimately influence
model behavior.

[^anthropic-context]: Anthropic — Effective context engineering for AI agents
[^anthropic-evals]: Anthropic — Demystifying evals for AI agents
