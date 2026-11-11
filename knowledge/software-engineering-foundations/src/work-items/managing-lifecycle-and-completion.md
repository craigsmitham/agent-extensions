---
type: Reference
title: Work-item lifecycle and completion
description: Distinguishes handoff, disposition, delivery, verification, operational state, and authorized closure.
tags: [work-item, lifecycle, completion, disposition, delivery, verification, closure, handoff, software-engineering-foundations]
generated: { by: codex/gpt-6, at: 2026-11-11T19:45:59Z }
---

# Work-item lifecycle and completion

One workflow status rarely carries all material state. Preserve evidence and
understanding, decision, delivery, verification, operational, follow-up, and
closure dimensions separately when they matter.

## Completion boundaries

| Boundary | What is complete | Does not imply |
| --- | --- | --- |
| Handoff | Current truth, evidence, uncertainty, ownership, and next action are recoverable | Disposition, delivery, or closure |
| Disposition | An authorized response is recorded with rationale and review or reopening conditions | Implementation or verified correction |
| Delivery | The authorized action occurred and the resulting revision or state is identifiable | That verification conditions hold |
| Verified closure | Applicable conditions were assessed, residual state and follow-up are explicit, and closure was authorized | Closure of related or independently owned work |

Select the boundary relevant to the next transition instead of inventing one
universal definition of done.

## Record transitions

For every consequential transition preserve previous and new state, time,
actor or authority, evidence or rationale, residual risk, open follow-up, and
reopening trigger. Closing one item does not automatically close related
incidents, reports, corrective work, or follow-up.

Distinguish:

- **Disposition** — the selected response to the case.
- **Delivery** — performance of an authorized action.
- **Verification** — bounded evidence about stated conditions.
- **Closure** — an authorized end to this item's active lifecycle.

A merge, deployment, mitigation, completed task, or cleared alert is not
verification by itself. Map lifecycle dimensions into local workflow fields
without claiming that the host status proves them.
