---
type: Explanation
description: How prose, executable contracts, instructions, evidence, and live systems own different kinds of knowledge.
tags: [knowledge-forms, executable-authority, documentation, evidence, current-state]
status: draft
---

# Knowledge forms

The strongest form for a claim is the one that can express and maintain it with
the least ambiguity.

| Kind of claim | Natural authority |
| --- | --- |
| Supported observable behavior | Behavior and contract tests |
| Exact accepted or produced shape | Schemas, types, and generated contracts |
| Current implementation | Source code and configuration |
| Required conduct or repeatable procedure | Instructions, rules, and operational guides |
| Purpose, boundaries, and rationale | Maintained explanatory prose |
| Planned and active work | Work tracking |
| Current runtime condition | Operational and observability systems |
| Historical observation | Evidence with provenance |

Prefer executable authority when the claim can be decided mechanically. Prose
that enumerates every option, field, or test scenario usually becomes a stale
copy. Prose remains necessary for meaning that code cannot reveal reliably:
responsibilities, non-responsibilities, rationale, tradeoffs, and relationships
spread across many executable sources.

## Desired and current state

Every maintained claim should make clear whether it describes what ought to be
true or what evidence says is true now. Policy and accepted architecture can own
desired state. Code, deployed systems, and observations provide current-state
evidence. A difference between them is something to reconcile, not permission
to silently relabel one as the other.

No form is universally superior. The purpose of the classification is to keep
each claim close to the mechanism capable of sustaining it.
