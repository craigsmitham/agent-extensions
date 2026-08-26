---
type: Guide
title: Analyzing Requirement impact
description: Use when a work-item Signal may imply a change to desired state; Orient it against current authority before it becomes an unsupported Requirement or Implementation commitment.
tags: [ooda, orientation, signals, observations, work-items, requirement-impact, defects, features, incidents, delivery]
sources:
  - id: ooda-control-loop
    resource: /control-loop/ooda-control-loop.md
    title: OODA as the Gen Stack control loop
generated:
  by: codex/gpt-5.6
  at: 2026-08-26T14:02:36Z
---

# Analyzing Requirement impact

Use this guide whenever a software work item may affect accepted desired state
or evidence about it. The analysis records a relationship; it does not accept,
change, or retire a Requirement.

This is a bounded Orientation activity. Preserve the originating Signal and
its Observations, classify them against existing authority, and leave the
result unresolved when the evidence cannot support a repair
hypothesis.[^ooda-control-loop]

## Classify the relationship

Choose one or more only when supported:

| Classification | Meaning |
| --- | --- |
| `possible non-satisfaction` | Observed or suspected behavior may fail an existing Requirement |
| `candidate new obligation` | The request may justify a Requirement that has not been accepted |
| `proposed change or retirement` | The work questions an existing Requirement's desired state or continued force |
| `implementation-only` | Accepted desired state appears unchanged; Implementation may change |
| `evidence or interpretation gap` | The Requirement, evaluation, or their relationship is ambiguous, missing, stale, or insufficient |
| `unresolved` | Available evidence cannot yet classify the relationship honestly |

Record stable Requirement IDs and links when they exist. Do not copy the
Requirement into the work item as another normative statement. A short quoted
or paraphrased predicate may provide reader context when its authority and link
remain explicit.

## Work-item block

Use the smallest useful subset of:

```text
Signal:
Observations and evidence:
Applicable Requirements:
Relationship to desired state:
Architecture impact:
Evidence impact:
Required authority:
Unknowns:
```

`Architecture impact` names an affected responsibility, boundary, decision, or
response without designing it. `Evidence impact` names evaluations that may
need creation, correction, rerun, or reinterpretation. `Required authority`
identifies who or what can accept a Requirement change or resolve a conflict.

## Apply proportionately through lifecycle

- At raw intake, `unresolved` is often the truthful result.
- Before commitment, resolve enough impact to avoid treating a candidate
  obligation or disputed expectation as implementation authority.
- During delivery, maintain links when accepted Requirements, architecture, or
  evaluation definitions change.
- At closure, account for every claimed Requirement impact: satisfied,
  superseded, rejected, deferred with an owner, or still unknown.

An evaluation failure does not prove which artifact is wrong. A source request
or proposed Change Specification does not become a Requirement because a
verification condition can be written. Keep those boundaries visible in the
item.

[^ooda-control-loop]: [OODA as the Gen Stack control loop](/control-loop/ooda-control-loop.md)
    defines Orientation as evidence-bound interpretation rather than authority
    to change desired state.
