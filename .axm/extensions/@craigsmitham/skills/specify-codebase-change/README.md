# specify-codebase-change

Produces a snapshot-bound functional and technical specification from an
accepted codebase design. It is for engineers and coding-agent workflows that
need precise behavior, interface, invariant, migration, and verification
contracts before implementation planning begins.

## Use it when

- Consequential design choices have been accepted but still need to be compiled
  into an implementation-constraining specification.
- You need traceable functional scenarios, technical contracts, and vertical
  slices that a fresh planner can use without inventing design decisions.

Do not use it for requirements discovery, current-state research, design
workshopping, tactical task planning, estimates, or implementation. It blocks
when the approved inputs or current evidence cannot support a complete
specification.

## Install

```sh
axm install @craigsmitham/skills/specify-codebase-change
```

## Example

Ask your agent:

> Turn this accepted retry design and its supporting current-state report into a
> functional and technical change specification. Preserve the decision IDs and
> stop if a missing policy or stale contract would require a new decision.

The skill returns a draft ready for review or a precise blocked result. After
explicit approval, the accepted specification provides functional scenarios,
technical contracts, vertical slices, evidence provenance, and end-to-end
traceability for implementation planning.

## Inspiration

This skill is an independent adaptation of the Structure phase of QRSPI as
described in Alex Lavaee's [From RPI to QRSPI: Rebuilding the First Structured
Workflow for Coding
Agents](https://alexlavaee.me/blog/from-rpi-to-qrspi/). Lavaee's article credits
the QRSPI framework to Dex Horthy and links Horthy's [original
talk](https://www.youtube.com/watch?v=YwZR6tc7qYg). This package is not an
official or complete implementation of QRSPI.

## License

MIT.
