# frame-codebase-research

Turns a bug report, incident symptom, feature request, or change idea into a
neutral set of current-state questions for a fresh codebase researcher. It
preserves when evidence was observed and reported, when the brief was prepared,
and which repository snapshot supplied its anchors. It is for engineers and
coding-agent workflows that need an evidence-grounded technical map before
choosing a design or implementation plan.

## Use it when

- A non-trivial code change depends on uncertain current behavior, ownership,
  control or data flow, contracts, dependencies, failure conditions, or test
coverage.
- A future design depends on governing architectural, framework, or runtime
  capabilities whose authority and constraints need to be established.
- You want to isolate factual codebase research from the original request's
  presumed cause or preferred solution.

Do not use it to answer the questions, diagnose a bug, propose a design, write
an implementation plan, or change code. It may frame the first stage of a
larger request, but the brief is an intermediate handoff rather than completion
of that larger request.

## Install

```sh
axm install @craigsmitham/skills/frame-codebase-research
```

## Example

Ask your agent:

> Frame the current-state codebase research needed to understand why scheduled
> exports sometimes remain pending. Treat the proposed queue rewrite as an
> assumption, not a research conclusion.

When research is warranted, the skill returns a brief with independent readiness
and review states, a provenance-only evidence timeline, verified anchors,
reported evidence, human input gaps, neutral questions, drift coverage,
architecture and capability evidence, boundaries, and completion criteria.

## Inspiration

This skill is an independent adaptation of the Questions phase of QRSPI as
described in Alex Lavaee's [From RPI to QRSPI: Rebuilding the First Structured
Workflow for Coding
Agents](https://alexlavaee.me/blog/from-rpi-to-qrspi/). Lavaee's article credits
the QRSPI framework to Dex Horthy and links Horthy's [original
talk](https://www.youtube.com/watch?v=YwZR6tc7qYg). This package is not an
official or complete implementation of QRSPI.

## License

MIT.
