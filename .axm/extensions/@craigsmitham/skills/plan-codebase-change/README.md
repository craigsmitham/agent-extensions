# plan-codebase-change

Turns an accepted functional and technical codebase change specification into a
snapshot-validated implementation plan. It is for engineers, implementation
agents, and work management workflows that need executable, traceable work
without reopening design decisions.

## Use it when

- An approved specification is ready to become concrete implementation work.
- You need vertical slices, verified codebase anchors, dependencies, checkpoints,
  and objective completion evidence suitable for a fresh agent or issue tracker.
- Planning evidence is available as a Git revision or another named, versioned,
  time-bound codebase snapshot.

Do not use it for current-state research, design or specification decisions,
delivery estimates, code generation, or implementation. It reports when stale
evidence, missing contracts, or invalidated decisions require an earlier kind of
work.

## Install

```sh
axm install @craigsmitham/skills/plan-codebase-change
```

## Example

Ask your agent:

> Convert this accepted invoice-preview specification into an implementation
> plan for a fresh coding agent. Preserve its identifiers, verify every path,
> symbol, and repository-defined obligation against the supplied codebase
> snapshot, and give each vertical slice objective completion evidence.

The skill returns a vendor-neutral work graph and detailed items that trace the
accepted specification through implementation and verification.

## Inspiration

This skill is an independent adaptation of the Plan phase of QRSPI as described
in Alex Lavaee's [From RPI to QRSPI: Rebuilding the First Structured Workflow
for Coding
Agents](https://alexlavaee.me/blog/from-rpi-to-qrspi/). Lavaee's article credits
the QRSPI framework to Dex Horthy and links Horthy's [original
talk](https://www.youtube.com/watch?v=YwZR6tc7qYg). This package is not an
official or complete implementation of QRSPI.

## License

MIT.
