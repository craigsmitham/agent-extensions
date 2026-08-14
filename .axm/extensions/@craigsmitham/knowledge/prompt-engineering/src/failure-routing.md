---
type: Reference
title: Failure routing
description: How to distinguish prompt defects from context, harness, skill, model, or deterministic-contract defects.
tags: [diagnosis, prompt-failure, context-failure, harness-failure, skill-failure, routing]
status: stable
generated: { by: "codex/gpt-5.6", at: 2026-08-14T20:43:46Z }
---

# Failure routing

Repair the smallest responsible surface, then evaluate the complete system for
regressions.

| Observation | Likely owner | First test |
| --- | --- | --- |
| Goal, constraint, label, or output expectation is ambiguous | Prompt | Clarify one contract field and rerun the same cases |
| Correct behavior appears only for one phrasing or order | Prompt | Paraphrase and reorder controlled variants |
| Required fact is absent, stale, excessive, or arrives too late | Context | Inspect source, selection, routing, and freshness |
| Model cannot observe state or act on the environment | Harness | Inspect tool and observation interfaces |
| Model says an effect occurred but state does not prove it | Harness | Add or inspect deterministic outcome verification |
| Prompt asks the model not to exceed authority but tools still permit it | Harness | Constrain permissions, credentials, approval, or sandbox |
| Reusable workflow activates incorrectly or omits packaged resources | Skill | Separate routing from activated-workflow evaluation |
| Exact syntax varies despite clear intent | Deterministic contract | Use structured output, schema validation, or code |
| Representative tasks fail across sound prompts and systems | Model or task design | Compare models, decomposition, task scope, or non-LLM mechanics |

Do not add prompt text merely because it is the cheapest surface to edit. A
prompt workaround for a context, interface, authority, or capability defect
usually hides the missing contract and increases future variance.
