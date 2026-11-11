---
type: Reference
title: Work-item evidence and provenance
description: Preserves attribution, claim maturity, decision authority, and safe access to evidence recorded in work items.
tags: [work-item, evidence, provenance, attribution, uncertainty, authority, source-inventory, software-engineering-foundations]
generated: { by: codex/gpt-6, at: 2026-11-11T19:45:59Z }
---

# Work-item evidence and provenance

Record evidence preserves what was observed, reported, measured, inferred,
or found unavailable, with the provenance that makes it attributable. Capturing
a claim does not establish that its conclusion is true. Outcome and assessment
claims retain their own criteria; see [Outcomes and evidence](../value/outcomes-and-evidence.md)
and [Verification and validation](../requirements/verification-and-validation.md).

## Source context

For each material occurrence, request, observation, finding, or decision,
preserve the smallest useful set of source system or kind, stable identity or
safe retrieval key, relevant time, environment or revision, conditions,
availability, and faithful statement or synopsis. Keep independently meaningful
occurrences traceable even when several inform one item.

## Claim kind and maturity

Do not convert:

- a report into a direct observation;
- an inference or hypothesis into a confirmed finding;
- a recommendation or proposal into an accepted decision; or
- implementation activity into approval, verification, or closure.

When understanding changes, retain the earlier attributable state or history
rather than rewriting the item to make new knowledge appear contemporaneous.

## Decisions and authority

Record each consequential decision, its time or revision, applicable authority,
and material rationale. Classification, severity, priority, assignment, scope,
desired behavior, technical approach, delivery, verification, and closure may
have different authorities.

Permission to edit a work item authorizes faithful recording, not invention.
When a missing decision controls dependent action, state the exact unresolved
choice and stop that action.

## Safe evidence channels

Keep credentials, personal information, private customer content, confidential
commercial information, restricted links, and exploitable security detail out
of public records. Prefer safe synopses, minimal redacted examples,
controlled-access evidence links, and non-sensitive correlation identifiers.
