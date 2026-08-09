---
type: Explanation
title: Spec-as-source
description: A specification pattern in which the spec is the canonical human-edited source and implementation artifacts are regenerated from it.
tags: [software-engineering, specification, sdd, generated-code, code-generation, model-driven-development, canonical-source]
status: stable
sources:
  - id: boeckeler-sdd
    resource: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
    title: Understanding Spec-Driven-Development — Kiro, spec-kit, and Tessl
    author: human:birgitta-boeckeler
  - id: sdd-paper
    resource: https://arxiv.org/abs/2602.00180
    title: "Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants"
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T21:16:04Z
---

# Spec-as-source

**Spec-as-source** makes the specification the canonical human-edited source
for a software capability. Implementation artifacts are generated or
regenerated from it, and direct human edits to generated code are not durable
changes.[^boeckeler-sdd][^sdd-paper]

This is the strongest specification-authority pattern. It is not merely a team
saying that requirements are important or that a spec is a “source of truth.”
The defining constraint is that lasting implementation change flows through
the specification or its generation system.

## Context

A team wants to maintain intent at a higher level than implementation and can
generate an acceptable implementation from that representation. The boundary
is sufficiently well-defined that generated artifacts can be replaced rather
than hand-maintained as an independent source.

## Pattern

Designate the specification as canonical and the implementation as derived.
Make that relationship visible in repository layout, metadata, generated-file
markers, review, and tooling. When behavior must change:

```text
change the specification or generator → regenerate → verify the result
```

An emergency or diagnostic code edit may reveal the needed correction, but the
durable fix must be represented upstream before regeneration. Otherwise the
next generation pass will erase it or, worse, preserve unexplained divergence.

## Required boundaries

The pattern depends on stronger engineering support than the other SDD models:

- a clear mapping from canonical specs to derived artifacts;
- an explicit policy forbidding durable direct edits to generated output;
- repeatable generation with versions and dependencies controlled;
- independent verification of behavior, security, and quality;
- a route for implementation and production discoveries to change the spec or
  generator; and
- preservation of rationale that regeneration would otherwise discard.

LLM generation makes richer source representations possible but introduces
nondeterminism. Repeated generation from unchanged inputs may not produce
identical code, so the system must distinguish acceptable implementation
variation from unintended behavioral change.[^boeckeler-sdd]

## Authority model

| Concern | Authority |
| --- | --- |
| Intended behavior and durable change | Canonical specification |
| Translation rules and constraints | Generator, harness, and generation configuration |
| Current derived implementation | Generated code and configuration |
| Accepted behavior and qualities | Independent tests, checks, and review evidence |
| Actual runtime behavior | Production observation |

Generated tests alone are weak independent evidence when the same
specification and generator produce both implementation and oracle. Important
contracts benefit from checks whose failure modes are not identical to those
of generation.

## Consequences

Spec-as-source can concentrate review on intent, regenerate multiple
implementations, and eliminate manual drift within the generated boundary. It
also moves substantial complexity into specification design, generation,
validation, and debugging. A vague or incomplete spec no longer merely guides
poor code; it repeatedly reproduces it.

The pattern resembles model-driven development, with natural language or agent
interpretation replacing some formal modeling and deterministic generators.
That can reduce modeling constraints while also losing guarantees of
parseability, completeness, and repeatability.[^boeckeler-sdd]

It fits bounded components with stable contracts and strong verification more
readily than irregular brownfield systems whose essential behavior is implicit
in code, operational history, and undocumented coupling.

## Harness and context implications

Agents must know which files are canonical and which are derived before they
edit. The generation workflow, supported scope, verification requirements, and
recovery path should be discoverable beside the spec-to-output relationship.

Context gardening should protect canonical specifications, identify unmarked
generated output, detect manual drift, remove obsolete generated artifacts,
and retain runtime learning that has not yet been represented upstream. It
must not “fix” generated code as though that file owned the behavior.

## Failure modes

- **Generated-code hand editing** — a local fix bypasses the canonical source.
- **Unstable regeneration** — unchanged intent produces unreviewable churn or
  behavioral variation.
- **Incomplete source** — essential security, operational, or quality
  constraints exist only in generated implementation.
- **Shared failure oracle** — implementation and tests repeat the same
  misunderstanding of the spec.
- **Generator opacity** — contributors cannot explain why output changed.
- **Overextended boundary** — the pattern is applied where behavior cannot be
  specified or verified economically.
- **Lost rationale** — regeneration replaces artifacts that contained the only
  record of an implementation decision.

## Related

- [Spec-driven development](../practices/spec-driven-development.md)
- [Spec-first](spec-first.md)
- [Spec-anchored](spec-anchored.md)
- [Context gardening](../../../practices/context-gardening.md)
- [Repository instruction files](../repository-instruction-files.md)

[^boeckeler-sdd]: Birgitta Böckeler — Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl
[^sdd-paper]: Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants
