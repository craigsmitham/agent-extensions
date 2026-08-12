---
name: refine-work
description: Refines established work items or bodies of work by assessing their accuracy, articulation, and current status or disposition relative to their lifecycle position. Use for backlog refinement or grooming, lifecycle-state review, issue or ticket hygiene, checking whether established work belongs in its current status, or clarifying it without necessarily making it ready for development. Not for initial intake triage, prioritizing without supplied goals, planning implementation, or enforcing a particular work-management system.
---

# Refine work

Make the current treatment of established work understandable, proportionate, and
defensible. Treat an issue, ticket, request, epic, objective, or collection as
work; do not assume software development or a particular tracker.

Do not perform initial intake. When the decision is only what a new signal is
and where it should go next, stop at that intake-routing boundary rather than
refining it as established work.

## Judge proportionately

- Separate **intrinsic integrity**, **fitness for the current state**, and
  **readiness to advance**. Do not penalize an item for lacking information its
  current state does not require.
- Treat `Triage`, for example, as potentially appropriate when there is only
  enough information to understand and route a signal. Missing scope or
  acceptance criteria does not by itself make that disposition wrong.
- Prefer supplied workflow criteria. Otherwise use an explanation of the
  current state, then available local conventions, then common semantics
  cautiously. State the limit when a label is ambiguous; do not invent a gate.
- Separate observed facts, inferences, assumptions, and unknowns. Do not add
  certainty, rationale, requirements, or priority that the evidence does not
  support.
- Accept `keep as-is` as a successful outcome. More text is not necessarily
  better refinement.

## Assess the work

1. Identify the subject, its current status or disposition, the decision at
   hand, and any supplied goals, criteria, constraints, history, or evidence.
   Inspect referenced and readily available evidence proportionately when a
   material claim or suspected staleness could change the assessment. Treat
   inaccessible evidence as unknown; do not widen into unrelated research.
   Ask only when a missing answer could materially change the assessment.
2. Restate the work neutrally enough to expose differing interpretations
   without silently rewriting it.
3. Assess:
   - **Intrinsic integrity:** Is the work understandable and internally
     consistent? Are its material claims current and supported at the level
     available?
   - **Current-state fitness:** Is there enough information for the purpose of
     the present state?
   - **Disposition fit:** Does the present state honestly represent what is
     known, decided, and still unresolved?
   - **Advancement readiness:** Assess separately only when requested or when
     it materially explains a disposition recommendation.
4. Recommend the smallest semantic action that improves the treatment of the
   work: retain, clarify, investigate, advance, reclassify, split, combine,
   defer, or close. Map it to project-specific statuses only when their meaning
   is known.
5. Propose minimal wording changes only when they help. Preserve meaningful
   uncertainty and the distinction between the reported need and a possible
   solution. Do not change the source item unless the user asks.

For a body of work, also examine duplicates, substantial overlap, conflicting
assumptions, dependencies, useful grouping, stale items, and inconsistent
dispositions. Do not infer missing work without an objective or other basis.
Summarize collection-level patterns, then expand only the items needing a
decision.

## Respond

Scale the response to the material findings. Usually provide:

1. **Current understanding** — a neutral account of the work.
2. **Disposition fit** — `appropriate`, `likely mis-dispositioned`, or `cannot
   determine`, with a concise rationale.
3. **Material findings** — only gaps or relationships that affect the current
   treatment or the decision at hand. Put any needed material clarification or
   evidence that the work is no longer warranted here.
4. **Recommended action** — the smallest useful next action and, when known,
   its project-specific status mapping.
5. **Minimal refinement** — revised wording only if warranted.
6. **Limits** — consequential open questions, assumptions, and confidence.

For many items, prefer a compact table of disposition, rationale, and action.
Do not produce a generic quality score or a readiness checklist unless the
user requests one and supplies a meaningful bar.
