---
type: Explanation
title: Spec-first
description: A specification pattern in which a spec guides one change, then yields durable authority to the implemented system rather than remaining a maintained feature contract.
tags: [software-engineering, specification, sdd, temporary-spec, change-spec, code-authority, historical-spec]
status: stable
sources:
  - id: boeckeler-sdd
    resource: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
    title: Understanding Spec-Driven-Development — Kiro, spec-kit, and Tessl
    author: human:birgitta-boeckeler
  - id: github-persistence
    resource: https://github.github.com/spec-kit/concepts/spec-persistence.html
    title: GitHub Spec Kit — Spec persistence models
    author: team:github
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T21:16:04Z
---

# Spec-first

**Spec-first** uses a specification to shape a particular software change
before implementation begins. After the change is complete, the specification
does not have to remain the maintained contract for the feature. Humans
continue to edit the implementation directly, and later work may begin with a
new specification.[^boeckeler-sdd]

## Context

A team benefits from clarifying intent before coding but does not want the
long-term cost or dual authority of maintaining feature specifications beside
the software. The specification is valuable to the decision and delivery of
one change rather than to the entire future life of the feature.

## Pattern

Create and review a specification before implementation. Use it to derive the
plan, acceptance criteria, and verification for the current change. Once that
change is accepted, make its post-completion status explicit:

- discard it when it has no durable historical value;
- retain it as an immutable change record; or
- mark it superseded and link to the implemented behavior or later change.

Do not leave the completed specification looking like an actively maintained
feature contract.

## Authority and lifecycle

| Concern | Authority after completion |
| --- | --- |
| Current implemented behavior | Code and configuration |
| Mechanically checked behavior | Tests, schemas, and policy checks |
| Original requested change | Historical specification, if retained |
| Later desired change | A new decision or specification |

Retaining a spec-first document for history does not turn it into a
spec-anchored document. Its value is evidentiary: it explains what one change
intended at that time. A flow-forward repository can therefore keep many
spec-first records without treating any one of them as the current feature
contract.[^github-persistence]

## Consequences

The pattern keeps specification overhead proportional to the change and avoids
requiring permanent synchronization between prose and code. It works well for
bounded work, repositories where code and tests already provide strong
navigation, and teams that want structured agent input without changing their
long-term authority model.

The tradeoff is loss of a maintained statement of product intent. Future work
may need to reconstruct behavior from code, tests, production evidence, and a
series of historical changes. Important intent that cannot be recovered from
those surfaces needs another durable owner.

## Harness and context implications

The harness should distinguish **active change context** from **historical
change records**. Agents should discover an active spec while working on its
change, but old specifications should not flood ordinary repository context or
silently override current code and tests.

Useful signals include lifecycle status, completion date, affected scope,
links to implementation, and supersession. Context gardening should demote
unmarked old specs from active discovery rather than assuming their prose is
current.

## Failure modes

- **Ghost authority** — an old spec remains prominent and is mistaken for the
  current contract.
- **Premature disposal** — the team deletes rationale that has no other durable
  owner.
- **Spec theater** — a document is generated but not reviewed or used to
  evaluate the implementation.
- **Repeated rediscovery** — every change reconstructs the same product intent
  because nothing durable owns it.
- **Unclear completion** — no event changes the spec from active input to
  historical record.

## Related

- [Spec-driven development](../practices/spec-driven-development.md)
- [Spec-anchored](spec-anchored.md)
- [Spec-as-source](spec-as-source.md)
- [Context gardening](../../../practices/context-gardening.md)

[^boeckeler-sdd]: Birgitta Böckeler — Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl
[^github-persistence]: GitHub Spec Kit — Spec persistence models
