---
type: Explanation
title: Spec-driven development
description: How spec-driven development uses structured statements of intent to guide software change while leaving teams to choose how long specifications remain authoritative.
tags: [software-engineering, specification, requirements, sdd, agentic-development, source-of-truth, change-management]
status: stable
sources:
  - id: boeckeler-sdd
    resource: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
    title: Understanding Spec-Driven-Development — Kiro, spec-kit, and Tessl
    author: human:birgitta-boeckeler
  - id: github-spec-driven
    resource: https://github.com/github/spec-kit/blob/main/spec-driven.md
    title: GitHub Spec Kit — Spec-driven development
    author: team:github
  - id: github-persistence
    resource: https://github.github.com/spec-kit/concepts/spec-persistence.html
    title: GitHub Spec Kit — Spec persistence models
    author: team:github
  - id: sdd-paper
    resource: https://arxiv.org/abs/2602.00180
    title: "Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants"
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T21:16:04Z
---

# Spec-driven development

**Spec-driven development** (SDD) is a family of software-development
practices in which a structured statement of intent is created before
implementation and used to direct planning, coding, and verification. The
specification makes desired behavior reviewable before implementation details
consume attention.

The name does not identify one complete method. Current SDD tools and accounts
differ in what they call a specification, how much workflow they impose, and
whether the specification remains authoritative after the initial change.[^boeckeler-sdd]
The durable idea is therefore the relationship between expressed intent and
software change, not a particular sequence of generated Markdown files.

## A specification is scoped intent

An SDD specification describes the behavior or outcome of a particular product,
feature, component, or change. It may include requirements, acceptance
criteria, constraints, interfaces, or examples. It is more structured and
durable than a conversational request, but it need not be a single file or a
formal language.

A specification is also distinct from broad repository context. Architecture
principles, coding conventions, and agent instructions may apply to many tasks;
a feature specification should enter context when work creates, changes, or
evaluates that feature. Treating all repository guidance as a specification
makes the term too broad to establish useful authority or lifecycle rules.

## The shared development loop

SDD approaches commonly move through a loop like this:

```text
express intent → refine the specification → derive a plan → implement
              → verify against intent → feed discoveries back
```

Implementation is still a learning activity. Technical discoveries, user
feedback, and production behavior can expose errors or omissions in the
original specification. An SDD practice must provide a return path for that
learning rather than treating the first specification as complete by
definition.

GitHub's aspirational account places the specification at the center and treats
plans, tasks, and code as successively derived expressions of it.[^github-spec-driven]
Other implementations use a specification only to improve the current change.
Both are called SDD, which makes the authority model an essential additional
choice.

## Authority and persistence

Three patterns describe how long the specification matters and what humans
continue to edit:[^boeckeler-sdd][^sdd-paper]

| Pattern | Role during creation | Role during later maintenance | Human code edits |
| --- | --- | --- | --- |
| [Spec-first](../patterns/spec-first.md) | Directs the current change | May be archived or discarded | Yes |
| [Spec-anchored](../patterns/spec-anchored.md) | Directs the current change | Remains a maintained feature anchor | Yes |
| [Spec-as-source](../patterns/spec-as-source.md) | Directs generated implementation | Remains the canonical human-edited source | Normally no |

These patterns form a progression of stronger persistence and authority.
Spec-driven does not by itself mean spec-as-source.

## Change propagation is a separate decision

The authority pattern does not fully determine how a team handles discoveries
and later requirements. GitHub Spec Kit distinguishes three mutation models:
[^github-persistence]

| Mutation model | How change moves |
| --- | --- |
| Flow-back | Any artifact may change first; the team reconciles specification, plan, tasks, tests, and implementation |
| Flow-forward | Completed artifacts remain historical; a later requirement creates a new linked change record |
| Living spec | The canonical specification changes first; downstream artifacts are revised or regenerated |

The axes can be combined. A spec-anchored team might reconcile code discoveries
back into one living feature specification or preserve a chain of immutable
change specifications. Spec-as-source normally favors a living specification,
but still needs a policy for history and implementation feedback.

## “Source of truth” is plural unless qualified

Different surfaces answer different questions:

| Question | Likely authority |
| --- | --- |
| What behavior is intended? | Current specification or product decision |
| What behavior is implemented? | Source code and configuration |
| What contract is mechanically checked? | Tests, schemas, and policy checks |
| What actually happened? | Runtime observation and production evidence |
| Why was this choice made? | Decision history and rationale |

A team should say which kind of truth a specification owns. Otherwise “the
spec is the source of truth” can hide a conflict between desired, implemented,
verified, and observed behavior.

## Forces and tradeoffs

SDD makes ambiguity visible earlier and gives humans and agents a shared object
for planning and verification. It can also create substantial review and
maintenance overhead. Elaborate workflows are poorly proportioned to many
small fixes, while large unclear initiatives need discovery and stakeholder
learning before a detailed specification can be trusted.[^boeckeler-sdd]

The practice is most valuable when the cost of misunderstanding, coordination,
or behavioral drift exceeds the cost of specifying and maintaining intent. The
appropriate rigor can vary by change size, risk, component, and lifecycle; a
repository need not impose one SDD pattern everywhere.

## Harness and context implications

An agent can use specifications safely only when the harness makes their status
legible. Discovery should communicate:

- which work has an applicable specification;
- whether it is proposed, active, historical, superseded, or generated;
- which authority and mutation patterns govern that area;
- where implementation, verification, and rationale live; and
- how contradictions and implementation discoveries flow back.

Without those signals, old task specifications can masquerade as current
requirements and living specifications can be mistaken for disposable planning
notes. [Context gardening](../../../practices/context-gardening.md) should
therefore evaluate specification authority and lifecycle before pruning,
promoting, or routing specification files.

## Related

- [Spec-first](../patterns/spec-first.md)
- [Spec-anchored](../patterns/spec-anchored.md)
- [Spec-as-source](../patterns/spec-as-source.md)
- [Context gardening](../../../practices/context-gardening.md)
- [Progressive disclosure](../../../patterns/progressive-disclosure.md)
- [Repository instruction files](../repository-instruction-files.md)

[^boeckeler-sdd]: Birgitta Böckeler — Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl
[^github-spec-driven]: GitHub Spec Kit — Spec-driven development
[^github-persistence]: GitHub Spec Kit — Spec persistence models
[^sdd-paper]: Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants
