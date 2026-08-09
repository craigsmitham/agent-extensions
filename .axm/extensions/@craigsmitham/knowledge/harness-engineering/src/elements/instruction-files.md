---
type: Explanation
title: Instruction files
description: How instruction files provide persistent, scoped feedforward context while leaving task-specific workflows and knowledge on demand.
tags: [harness, instructions, context, scope, routing, progressive-disclosure]
status: stable
sources:
  - id: anthropic-context
    resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
    title: Anthropic — Effective context engineering for AI agents
  - id: context-files-evaluation
    resource: https://arxiv.org/abs/2602.11988
    title: Evaluating AGENTS.md — Are Repository-Level Context Files Helpful for Coding Agents?
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T20:48:38Z
verified:
  - by: codex/gpt-5.6
    at: 2026-08-09T22:13:44Z
stale_after: 2027-02-09
---

# Instruction files

An **instruction file** is a persistent context element through which a harness
supplies feedforward context to an agent. “File” describes a common storage
form; the defining property is that the harness loads its instructions for a
scope without requiring the caller to restate them for every task.

Instruction files can appear in many application domains. They may establish
organization-wide constraints, describe a working environment, state
interaction preferences, or route an agent to deeper procedures and knowledge.
Repository conventions such as `AGENTS.md` are one software-engineering
specialization, not the definition of the element.

## An expensive context position

Persistent instructions shape decisions before the harness knows every detail
of the current task. Their context cost is therefore paid broadly, and
irrelevant guidance can dilute more useful information. Effective context
engineering keeps the active context high-signal and retrieves depth when it
becomes relevant.[^anthropic-context]

This creates a durable test:

> Must the agent know this throughout the scope, or does it need a reliable
> route to the information only in a narrower situation?

The first belongs in persistent instructions. The second usually belongs
behind a route to a skill, knowledge artifact, reference, tool, or domain guide.

## Useful responsibilities

| Responsibility | Typical content |
| --- | --- |
| Invariants | Safety, compatibility, authority, or quality constraints that apply throughout the scope |
| Operating facts | Non-obvious facts about the environment that change the next action |
| Working agreements | Stable expectations for collaboration, evidence, and handoff |
| Discovery routes | Conditions under which the agent should load a procedure, reference, or domain profile |

An instruction file should not become the universal owner of background
explanation, exhaustive reference, task backlogs, or long procedures.

## Scope and composition

Harnesses may compose instructions across personal, organizational,
application, environment, component, or session scopes. The portable design
principles are:

- broad scopes own only genuinely broad guidance;
- narrow scopes own their differences;
- repeated content should have one authoritative owner;
- precedence and overrides should be inspectable;
- the effective instruction set should be testable from representative entry
  points.

The mechanism used to discover and order files is host-specific. A filesystem
hierarchy is natural for repositories; another harness might select files by
tenant, workflow, role, resource, or runtime environment.

## Guidance, routing, and enforcement

Instruction files influence reasoning. They are appropriate when judgment is
required, but they are not the strongest owner of every constraint.

| Need | Better owner |
| --- | --- |
| Reusable multi-step procedure | Agent skill or how-to guide |
| Detailed facts or explanation | Knowledge or reference artifact |
| External action or observation | Tool |
| Mechanically decidable property | Check, policy engine, schema, or hook |
| Current goal and acceptance criteria | Task specification or plan |

The instruction surface can route to those owners and explain when they apply.
This preserves discovery without paying for their full content on every task.

## Effectiveness must be evaluated

Instruction following does not prove that an instruction improves outcomes. A
2026 study found that repository context files changed agent behavior and
increased cost by more than twenty percent without a significant improvement
in task success. It recommends retaining only necessary requirements and
evaluating context files rather than assuming that more guidance helps.[^context-files-evaluation]

The same caution applies outside software engineering: compare representative
work with and without a proposed instruction, inspect its activation scope,
and measure both outcomes and attention cost.

## Domain specialization

A domain profile should own the assumptions that do not transfer. In software
engineering, directory scope, repository commands, source ownership, generated
files, build checks, and version-control workflows materially change how
instruction files are designed. See
[Repository instruction files](../domains/software-engineering/repository-instruction-files.md)
for that specialization.

## Common failure modes

- **Universal manual** — persistent instructions absorb every fact and
  procedure the harness might need.
- **Wrong scope** — local guidance affects unrelated work.
- **Hidden precedence** — the agent receives conflicting instructions without
  a visible way to resolve them.
- **Descriptive routing** — a topic is named without stating when deeper
  context should be loaded.
- **Prose-only control** — a deterministic constraint lacks an executable
  owner.
- **Stale authority** — outdated instructions remain plausible and continue
  to shape behavior.
- **Unmeasured accretion** — every failure adds text, but no change is tested
  or removed.

## Related

- [Context engineering](../foundations/context-engineering.md)
- [Progressive disclosure](../patterns/progressive-disclosure.md)
- [Context gardening](../practices/context-gardening.md)
- [Agent skills](agent-skills.md)
- [Repository instruction files](../domains/software-engineering/repository-instruction-files.md)
- [How to design repository instruction files](../domains/software-engineering/guides/repository-instruction-files.md)

[^anthropic-context]: Anthropic — Effective context engineering for AI agents
[^context-files-evaluation]: Evaluating AGENTS.md — Are Repository-Level Context Files Helpful for Coding Agents?
