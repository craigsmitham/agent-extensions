# Refine Work

Assess whether an established work item or body of work is accurate, proportionately
articulated, and appropriately dispositioned for its current lifecycle state.
The skill supports backlog refinement, lifecycle-state review, and issue hygiene without
assuming a particular tracker, workflow, or definition of development-ready.

## Use it when

- Checking whether work belongs in its current status.
- Refining an issue, ticket, request, epic, objective, or backlog.
- Finding duplicates, overlaps, conflicts, dependencies, or stale work.
- Clarifying work while preserving legitimate uncertainty.

It does not prioritize work without supplied goals, plan implementation, or
perform initial intake triage. It does not require every item to meet a universal
completeness standard. Keeping an item as-is or confirming that an established
item appropriately remains in Triage are valid outcomes.

## Install

```sh
axm install @craigsmitham/skills/refine-work
```

Or install it through the work-management pack:

```sh
axm packs install @craigsmitham/packs/work-management
```

## Example

Ask your agent:

> Refine these backlog items. Check whether each item belongs in its current
> status, but do not require items in Triage to be ready for development.

The skill reports its current understanding, disposition fit, material
findings, smallest useful next action, and any consequential evidence limits.

## License

MIT.
