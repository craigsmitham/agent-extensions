---
type: Explanation
title: Agents and workflow boundaries
description: The existing distinction between deterministic automation, LLM workflows, agents, and their surrounding
  workflows.
tags:
- software-engineering-foundations
status: draft
generated:
  by: codex/gpt-6
  at: '2026-11-11T18:36:09Z'
sources:
- id: migration-source
  resource: https://github.com/craigsmitham/agent-extensions/blob/c56a54cb5cdb2c14c0d71801709c2b38968c99dd/knowledge/product-engineering/src/overview.md
  title: Existing product-engineering material before the discipline migration
- id: anthropic-agents
  resource: https://www.anthropic.com/engineering/building-effective-agents
  title: Anthropic — Building effective agents
- id: openai-guide
  resource: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
  title: OpenAI — A practical guide to building agents
---

# Agents and workflow boundaries

Classify a system by who controls its meaningful next
steps — not by whether it uses a model, a tool, a graph, or a product that calls
itself an agent.[^anthropic-agents]

| Form | Control path | What agent engineering owns |
| --- | --- | --- |
| Deterministic automation | Code or rules choose every step | Nothing |
| LLM workflow | A predefined graph invokes models at known steps | Only local model behavior, where a step has bounded dynamic choice |
| Agent | A model-directed loop chooses meaningful next steps | Goal, planning, capability choice, recovery, delegation, and stopping |
| Agentic workflow | A durable workflow surrounds one or more bounded agent steps | The dynamic decisions inside each agent step and between delegated actors |

The first two rows are workflow automation. The last two involve agent
engineering: the surrounding trigger, dependencies, durable progress,
approvals, retries, cancellation, and compensation belong to workflow
automation, and the model-directed choice inside the agent step does
not.[^openai-guide]


[^anthropic-agents]: Anthropic — Building effective agents, which separates
    workflows whose steps are orchestrated through predefined code paths from
    agents that direct their own process and tool use.
[^openai-guide]: OpenAI — A practical guide to building agents, on what an
    agent independently decides and where a surrounding system keeps control.
