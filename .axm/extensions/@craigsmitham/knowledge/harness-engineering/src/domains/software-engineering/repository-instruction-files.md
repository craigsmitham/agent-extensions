---
type: Explanation
title: Repository instruction files
description: How repository instruction files establish scoped software-engineering invariants and discovery routes without becoming a codebase encyclopedia.
tags: [harness, instructions, agents.md, repositories, context, progressive-disclosure]
status: stable
sources:
  - id: agents-md
    resource: https://agents.md/
    title: AGENTS.md
  - id: openai-agents-md
    resource: https://learn.chatgpt.com/docs/agent-configuration/agents-md
    title: OpenAI — Custom instructions with AGENTS.md
  - id: openai-harness
    resource: https://openai.com/index/harness-engineering/
    title: OpenAI — Harness engineering
  - id: anthropic-context
    resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
    title: Anthropic — Effective context engineering for AI agents
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T22:12:38Z
verified:
  - by: codex/gpt-5.6
    at: 2026-08-09T22:13:44Z
stale_after: 2027-02-09
---

# Repository instruction files

An **instruction file** is persistent feedforward context that a harness loads
before or while an agent begins work. In software engineering, repository conventions include
`AGENTS.md`, `CLAUDE.md`, rules files, and host-specific alternatives. The open
`AGENTS.md` convention describes such a file as a predictable, agent-focused
counterpart to a human README.[^agents-md]

Instruction files occupy an unusually expensive and powerful position: they
shape behavior before the agent knows the specific task. That makes them good
homes for universally applicable constraints and discovery routes, and poor
homes for long procedures or broad reference material.

## Always-on feedforward

Instructions differ from ordinary documentation because their cost and effect
are paid whether or not a task needs them. Context is finite, and additional
tokens can dilute attention as well as consume capacity.[^anthropic-context]

This creates a value test:

> Is this information valuable for nearly every task in this scope, or does the
> agent merely need a reliable route to it when a narrower situation occurs?

If the answer is “only for a narrower situation,” an index entry is usually
more appropriate than the full content.

## The four useful jobs

| Job | Example shape |
| --- | --- |
| Invariants | Never commit generated credentials; preserve public API compatibility |
| Working commands | Run the package-specific test target after changing this surface |
| Discovery routes | Before changing migrations, read the migration guide |
| Non-obvious environment facts | This directory is generated; edit its canonical source instead |

These jobs change the agent's next decision. Background essays, exhaustive
option catalogs, and detailed workflows usually do not need to be present
before the task is known.

## Instruction files as maps

Large instruction manuals fail because importance becomes visually flat,
staleness becomes hard to detect, and relevant material competes with the task
itself. A stronger model treats the root instruction file as a map into
versioned, on-demand knowledge. OpenAI describes this as giving the agent a map
rather than a thousand-page manual.[^openai-harness]

```text
root instructions        universal invariants + high-value routes
  └─ local instructions  scope-specific differences
       ├─ knowledge      facts, context, and explanation
       ├─ skills         reusable workflows
       └─ checks         mechanically enforceable constraints
```

The map must remain **receivable**: the agent has to recognize the situation
that makes a route relevant. A label such as “Database topics” describes a
category. “Before adding a migration, read …” establishes a prerequisite and
is more likely to affect action.

## Layering and scope

Many harnesses construct an instruction chain from broad scope toward the
current working directory. Codex, for example, loads global guidance and then
walks from the project root toward the current directory, with nearer guidance
appearing later in the chain.[^openai-agents-md]

The portable principle is independent of exact precedence:

- broad scopes own rules that are genuinely universal;
- narrow scopes own only their differences;
- child files do not restate parents;
- overrides are explicit rather than accidental contradictions;
- the closest owner maintains facts that change locally.

Defaulting to no local file is healthy. A local file earns its ongoing context
and maintenance cost only when the scope repeatedly needs distinct guidance.

## Relationship to neighboring elements

| Artifact | Primary job | Instruction-file relationship |
| --- | --- | --- |
| README | Orient human contributors and explain the project | Link when it already owns shared orientation |
| Knowledge document | Explain or describe material on demand | Route to it instead of embedding it |
| Skill | Execute a reusable workflow on demand | State the trigger, not the full procedure |
| Tool | Provide an action or observation primitive | Mention only non-obvious usage constraints |
| Test or linter | Enforce a mechanically decidable rule | Prefer the check; keep minimal remediation guidance |
| Task specification | State the current goal and acceptance criteria | Do not turn persistent instructions into a task backlog |

Instructions are not the universal control surface. Reliable harnesses place a
concern in the cheapest durable element that expresses it truthfully.

## Trim content, protect discovery

When an instruction file grows, body content and routing content have different
value:

| Content | Typical action |
| --- | --- |
| Universal invariant | Keep concise |
| High-leverage trigger and link | Protect or sharpen |
| Full procedure | Move to a skill or guide; leave a route |
| Explanation or reference | Move to knowledge; leave a route if needed |
| Parent duplication | Remove |
| Mechanically enforceable convention | Promote to a check |
| Stale or aspirational statement | Correct or remove |

Deleting discovery rows solely to reduce length can save tokens while making
the remaining knowledge unreachable. The better sequence is to trim duplicated
bodies first, then improve grouping and trigger precision.

## Guidance and enforcement

Prose is appropriate when agents must exercise judgment. It is weak when the
desired rule is deterministic. Formatting, dependency direction, generated
file ownership, and schema constraints often belong in formatters, linters, or
structural tests. OpenAI's harness account describes encoding architectural and
taste invariants mechanically while allowing local implementation freedom.[^openai-harness]

Actionable check failures can return both evidence and remediation into the
agent's context. This closes a feedback loop that prose alone cannot guarantee.

## Audit finding classes

| Class | Signal | Typical response |
| --- | --- | --- |
| Duplicate body | Restates a guide or parent instruction | Cut the copy and keep the route |
| Procedure in always-on context | Long reusable how-to in an instruction file | Move it to a skill or guide and leave a trigger |
| Weak trigger | Descriptive topic label does not establish when to act | Rewrite it as a receivable imperative |
| Missing route | Agents repeatedly rediscover an existing owner | Add the smallest useful route |
| Stale | Dead path, retired command, or superseded policy | Correct, retire, or remove it |
| Wrong layer | Local detail appears at a broad scope | Move it to the nearest truthful owner |
| Unjustified file | A local instruction file adds no distinct guidance | Remove it after confirming no hidden role |
| Index over-cut risk | A proposed trim strands useful depth | Reject the cut or regroup the routes |

These classes support evidence-led audits; they do not require a rewrite when
the current instruction surface already serves its scope well.

## Living interfaces

Instruction files are interfaces between repository maintainers and future
agent runs. They decay when commands, paths, owners, or policies change. Their
maintenance should therefore follow observed work:

1. notice a repeated miss or unnecessary context load;
2. identify whether the missing owner is an instruction, route, skill,
   knowledge document, tool, or check;
3. make the smallest durable correction;
4. verify discovery and behavior from a fresh run in the affected scope.

## Common failure modes

- **Encyclopedia** — the root file attempts to contain all repository knowledge.
- **Flat importance** — every preference is phrased as an invariant.
- **Wrong scope** — package-specific facts occupy the root or universal rules
  are copied into every child.
- **Duplicate procedure** — an instruction file forks a guide or skill body.
- **Descriptive routing** — topic labels do not tell the agent when to load the
  linked material.
- **Prose-only enforcement** — a deterministic rule is repeatedly violated
  because no mechanical check owns it.
- **Stale authority** — old commands remain plausible enough to be followed.
- **Over-cut index** — routes disappear during token reduction, leaving deeper
  knowledge effectively nonexistent.

## Related

- [How to design repository instruction files](guides/repository-instruction-files.md)
- [Instruction files](../../elements/instruction-files.md)
- [Agent skills](../../elements/agent-skills.md)

[^agents-md]: AGENTS.md
[^openai-agents-md]: OpenAI — Custom instructions with AGENTS.md
[^openai-harness]: OpenAI — Harness engineering
[^anthropic-context]: Anthropic — Effective context engineering for AI agents
