# conduct-codebase-research

Investigates explicit current-state questions and produces a cited, snapshot-bound
technical map. It is for engineers and coding-agent workflows that need reliable
evidence about behavior, ownership, flows, contracts, dependencies, and relevant
drift before choosing a design.

## Use it when

- A research brief or explicit question set is ready to investigate.
- Current behavior or architecture must be established from code, tests, runtime
  evidence, history, or version-matched primary documentation.

Do not use it to recommend a fix, choose a design, review code quality, write an
implementation plan, or modify code. Unanswered and conflicting evidence remain
visible rather than being filled with assumptions.

## Install

```sh
axm install @craigsmitham/skills/conduct-codebase-research
```

## Example

Ask your agent:

> Research Q1 and Q2 from this export-failure brief against the current checkout.
> Distinguish the incident, brief, and research snapshots; trace the request and
> worker flow; and report which relevant intervening changes affect each answer.

The skill returns a Codebase Research Report with explicit question status,
nearby citations, evidence classification, scoped drift, contracts, tests,
observability, contradictions, and a reproducible evidence index.

## Inspiration

This skill is an independent adaptation of the Research phase of QRSPI as
described in Alex Lavaee's [From RPI to QRSPI: Rebuilding the First Structured
Workflow for Coding
Agents](https://alexlavaee.me/blog/from-rpi-to-qrspi/). Lavaee's article credits
the QRSPI framework to Dex Horthy and links Horthy's [original
talk](https://www.youtube.com/watch?v=YwZR6tc7qYg). This package is not an
official or complete implementation of QRSPI.

## License

MIT.
