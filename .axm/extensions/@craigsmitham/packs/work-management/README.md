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

This initial release contains one independently installable skill. The pack
provides a durable bundle for related work-management extensions as they are
added; membership does not create a runtime dependency between extensions.

## Install

```sh
axm packs install @craigsmitham/packs/work-management
```

## Example

Ask your agent:

> Review this body of work. Identify items whose current status is appropriate,
> items that need a material clarification, and items that should be retained,
> investigated, advanced, reclassified, split, combined, deferred, or closed.

The assessment distinguishes fitness for the current state from readiness to
advance, so early-stage work is not judged by a development-ready standard.

## License

MIT.
