# Triage Work

Turn an incoming work item or a bounded intake queue into explicit initial
dispositions and next routes. The skill is tracker-agnostic, separates impact
from urgency, and preserves the evidence and rationale behind each decision.

## Use it when

- Reviewing a newly reported issue, request, bug, or feature.
- Processing an unreviewed queue or body of incoming work.
- Routing work, finding duplicates, requesting material clarification, or
  escalating protected or urgent signals.
- Deciding whether work should enter a downstream workflow.

It does not refine established work, rank otherwise viable work, prune an
accumulated backlog, or decide whether implementation can begin. Accepting an
item admits it to a workflow; it does not promise delivery.

## Install

```sh
axm install @craigsmitham/skills/triage-work
```

Or install it through the work-management pack:

```sh
axm packs install @craigsmitham/packs/work-management
```

## Example

Ask your agent:

> Triage this intake queue. Account for every item, handle protected or urgent
> work first, identify duplicates, and give each item a primary intake
> disposition plus any handling action without prioritizing accepted work.

The skill reports per-item primary dispositions, handling actions, routes,
decision authority, recommended-versus-applied state, rationale, follow-up
triggers, and collection-level patterns such as duplicate clusters and
ownership gaps.

## License

MIT.
