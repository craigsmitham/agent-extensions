---
type: Explanation
title: Spec-anchored
description: A specification pattern in which a feature spec persists across changes while humans continue maintaining both the specification and implementation.
tags: [software-engineering, specification, sdd, spec-anchor, living-specification, drift, traceability]
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
verified:
  - by: codex/gpt-5.6
    at: 2026-08-09T22:13:44Z
stale_after: 2027-02-09
---

# Spec-anchored

**Spec-anchored** development keeps a feature specification after its initial
implementation and uses it to orient later evolution and maintenance. Humans
continue to edit both the specification and the implementation; the spec is an
enduring anchor, not a generator boundary.[^boeckeler-sdd]

## Context

A feature has durable intent that is difficult to recover from implementation
details alone. Multiple contributors or agents need a stable account of that
intent across changes, but the software remains a human-maintained artifact
whose implementation discoveries can reshape the specification.

## Pattern

Maintain a specification at the lifecycle and scope of the feature or contract
it describes. Route relevant changes through that anchor, and define how
discoveries made in code, tests, review, or production are reconciled with it.

The pattern requires an explicit authority split. A useful default is:

| Surface | What it owns |
| --- | --- |
| Specification | Intended externally meaningful behavior and constraints |
| Code and configuration | Current implementation |
| Tests and schemas | Mechanically checked portions of the contract |
| Runtime evidence | Actual observed behavior |
| Decision history | Rationale and superseded alternatives |

This split does not resolve contradictions automatically. The team must say
whether a conflict blocks delivery, which owner initiates reconciliation, and
where intentional deviations are recorded.

## Change flow

Spec-anchored development supports more than one mutation model. A team can
update a living feature spec and flow implementation learning back into it, or
preserve successive immutable specifications linked as a lineage. GitHub Spec
Kit treats this mutation choice as separate from the spec's persistence
level.[^github-persistence]

Whatever model is chosen, later work should be able to determine:

- which specification currently anchors the affected behavior;
- which parts are normative rather than explanatory;
- what evidence demonstrates conformance;
- how the latest code discovery changed intent or implementation; and
- which earlier statements have been superseded.

## Consequences

The pattern preserves product intent and gives agents a durable planning and
evaluation surface. It can improve continuity across contributors and make
behavioral drift discussable before it becomes accidental policy.

Its central cost is synchronization. Specification and implementation can each
change legitimately, so the team owns two editable representations whose
relationship must remain legible. Tests and traceability can expose some drift,
but natural-language completeness and meaning still require judgment.

Spec-anchored is most useful for long-lived capabilities, externally important
behavior, and areas where implementation alone is a poor explanation of
intent. It is less attractive when behavior is cheap to reconstruct, changes
rapidly at low consequence, or no one will maintain the anchor.

## Harness and context implications

The specification should be discoverable by affected scope rather than loaded
for every task. Agents need its authority, owner, freshness, and relationship
to code and tests, not merely its filename.

Context gardening should look for silent divergence, orphaned specifications,
duplicated anchors, weak supersession, and specifications whose claimed scope
no longer matches the implementation. Gardening should not prune a maintained
anchor merely because the code is newer; the discrepancy is evidence to
resolve.

## Failure modes

- **Dual-authority ambiguity** — both spec and code are called authoritative
  without distinguishing intended from implemented behavior.
- **Decorative anchor** — the spec remains in the repository but later changes
  bypass it.
- **Silent drift** — code or intent changes without reconciliation.
- **Unbounded anchor** — one specification grows to cover a product or
  repository too broadly to remain coherent.
- **False executability** — prose is assumed to be mechanically enforced when
  no test or check establishes that relationship.
- **History loss** — continual rewriting preserves the current statement but
  erases important rationale.

## Related

- [Spec-driven development](../practices/spec-driven-development.md)
- [Spec-first](spec-first.md)
- [Spec-as-source](spec-as-source.md)
- [Context gardening](../../../practices/context-gardening.md)
- [Progressive disclosure](../../../patterns/progressive-disclosure.md)

[^boeckeler-sdd]: Birgitta Böckeler — Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl
[^github-persistence]: GitHub Spec Kit — Spec persistence models
