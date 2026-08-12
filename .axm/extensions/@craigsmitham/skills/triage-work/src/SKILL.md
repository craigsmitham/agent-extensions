---
name: triage-work
description: Triages an incoming work item or bounded body of work into an initial disposition and next route using supplied goals, workflow policies, authority, impact, urgency, duplication, and available evidence. Use for issue intake, request queues, unreviewed tickets, bug or feature triage, support escalations, or deciding whether new work should be accepted, routed, clarified, escalated, combined, deferred, or closed. Not for refining established work, prioritizing viable work, pruning accumulated work, or assessing implementation readiness.
---

# Triage work

Turn unreviewed signals into explicit, accountable next handling. Treat
`accept` as admission to a downstream workflow, not a promise to deliver.

## Establish the frame

- Identify the item or exact collection boundary and the intake decision being
  made.
- Identify who may decide and who may apply the outcome. Use supplied goals,
  workflow policies, authority, routes, owners, service expectations, and
  protected categories. Map to local fields or statuses only when their meaning
  is known; do not invent policy or authority.
- Inspect referenced and readily available evidence only as far as it could
  change the intake decision. Separate facts, inferences, and unknowns.
- Do not change a source system unless the user asks.

## Screen and decide

Screen first for safety, security, compliance, data-loss, active-incident, or
other supplied expedite conditions. When authorized, route or escalate these
immediately through the applicable path; otherwise surface the recommended
immediate handling prominently without changing the source system. Ordinary
queue order must not delay them.

Keep impact and urgency distinct. Set priority only when a supplied policy
defines how to derive it.

Choose the smallest honest primary disposition:

- **Accept** — admit the work to its intended downstream workflow.
- **Defer** — postpone the intake decision only when supplied intake policy or
  an external gating condition requires it, with an owner and explicit date,
  event, or condition for return. Once work is accepted, scheduling belongs to
  the downstream workflow.
- **Close** — decline work that is out of scope, already satisfied, invalid, or
  otherwise not admitted; give the reason and a reopening path when useful.
- **Cannot determine** — identify the missing policy, evidence, route, or
  authority without guessing.

Then add any necessary handling actions; these accompany rather than replace the
primary disposition:

- **Route** — send the item to the appropriate domain, queue, or owner.
- **Clarify** — request the smallest material missing information and retain a
  clear follow-up state.
- **Escalate** — invoke required authority or exceptional handling.
- **Combine** — connect a duplicate or substantially equivalent item to a
  canonical item while preserving provenance and useful evidence. The primary
  disposition still states what happens to the duplicate record.

For example, use `accept` with `route` for admitted work sent to its owning
queue, `cannot determine` with `clarify` when material intake evidence is
missing, or `close` with `combine` when a duplicate is linked to its canonical
item.

Do not deepen triage into refinement, prioritization, research, planning, or
readiness assessment. Recommend that separate work only when the initial route
depends on it.

## Handle a body of work

- Account for every item in the bounded collection; never silently sample.
- Review protected and urgent candidates first, then use bulk dispositions only
  where the same explicit rule and evidence apply.
- Preserve per-item outcomes even when summarizing. No item disappears into an
  aggregate; use `cannot determine` where necessary.
- Report primary-disposition and handling-action counts, duplicate clusters,
  ownership or routing gaps, policy conflicts, and intake-quality patterns.
  Expand exceptions and items needing judgment rather than repeating routine
  rationale.

## Respond

For one item, report the primary disposition, any handling actions, route or
owner, impact and urgency when material, concise rationale and evidence,
decision authority, whether the outcome was recommended or applied, and any
follow-up trigger or needed clarification.

For many items, state the boundary and use a compact table such as `Item |
Primary disposition | Handling action | Route/owner | Authority/action state |
Rationale | Follow-up`, followed by counts and collection-level findings. State
consequential assumptions, unknowns, and which outcomes were recommended or
actually applied.
