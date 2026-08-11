# Work Management

A bundle of portable extensions that help manage work throughout its lifecycle.
It is the installation point for related capabilities such as understanding,
assessing, refining, organizing, and dispositioning work. The pack is agnostic
of trackers and project-specific workflow conventions; supplied local criteria
remain authoritative.

## Included extensions

| Extension | Role |
| --- | --- |
| `@craigsmitham/skills/refine-work` | Assess whether work is accurate, proportionately articulated, and appropriately dispositioned for its current state |
| `@craigsmitham/skills/prune-work` | Remove accumulated work that no longer warrants attention while preserving useful evidence |

Each skill is independently installable. Pack membership does not create a
runtime dependency between them.

## Install

```sh
axm packs install @craigsmitham/packs/work-management
```

## Example

Ask your agent:

> Review this body of work. Identify items whose current status is appropriate,
> items that need a material clarification, and items that should be retained,
> investigated, advanced, reclassified, split, combined, deferred, or closed.

Or:

> Prune this backlog. Close work that is done, obsolete, superseded, or no
> longer warranted; preserve anything active or externally committed.

The skills distinguish ordinary refinement from an intentionally subtractive
pruning pass.

## License

MIT.
