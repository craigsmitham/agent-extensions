---
type: Explanation
title: The Gen Stack method
description: How the Gen Stack authority model, compositional Specifications, proportional Change Design, reusable Processes, and OODA control loop connect Signals, Intent, canonical Requirements, Architecture, Implementation, Evaluations, and operational learning.
tags: [generative-stack, specifications, processes, ooda, control-loop, signals, observations, software-change, requirements, architecture, change-design, evaluations, feedback]
sources:
  - id: fowler-generative-stack
    resource: https://chadfowler.com/regenerative-software/3miwhqqvwxc2x/
    title: Chad Fowler — The Generative Stack
  - id: boyd-ooda
    resource: https://www.coljohnboyd.com/documents/1995-06-28__Boyd_John_R__The_Essence_of_Winning_and_Losing__PPT-PDF.pdf
    title: John R. Boyd — The Essence of Winning and Losing
generated:
  by: codex/gpt-5
  at: 2026-08-26T15:42:30Z
---

# The Gen Stack method

Gen Stack combines an authority model with an adaptive control loop. The
authority model distinguishes what each representation owns:

```text
Intent → canonical Requirement → eligible Architecture subject and response
                                      ↓
Compilation → Implementation Units
                                      ↓
                    Evaluation Definition → Execution → Result
```

OODA governs how the stack learns which authority or activity should change:

```text
Observe Signals and contextual Observations
                  ↓
Orient across Intent, Requirements, Architecture,
Implementation, Evaluations, operations, and Provenance
                  ↓
Decide on an authorized repair hypothesis
                  ↓
Act to investigate, change, compile, evaluate, deploy, or roll back
                  └───────────────────────────────↺
```

[Change Design](design/change-design.md) supplies proportional technical
reasoning between accepted meaning and bounded Action. It may remain in the
conversation, be captured in a work item, or exceptionally be maintained as a
dedicated document. It is not another required authority layer: Requirements
still own obligations, Architecture owns durable response meaning, Work items
own delivery state, Implementation owns realized state, and Evaluations own
assessment and evidence.

A [Specification](glossary.md#specifications) gives one bounded system or
change a navigable whole by composing the relevant representations. It is not
another layer in the diagram: its Intent, Requirements, Architecture, Change
Design, verification context, and Work items retain their own authority and
lifecycle. Change Specifications compose bounded proposed or authorized system
or Architecture changes, while Bugfix Specifications specialize them for
authorized corrective work. Neither is a mandatory document template. A
Bugfix Specification remains linked to its provenance-bearing Defect Reports;
it is never a report under a new title.

[Evaluation as bounded evidence](evaluations/evaluation-as-bounded-evidence.md)
explains why tests are only one Evaluation method and how Definitions,
Executions, Results, observations, assurance, and decisions retain distinct
authority. [Designing a system evaluation
approach](evaluations/designing-a-system-evaluation-approach.md) turns those
distinctions into subject- and Requirement-navigable portfolios and separate
Requirement-satisfaction and Architecture-realization reports.

The loop is inspired by Chad Fowler's account of a generative stack that moves
from human intent through structured clauses, evaluations, implementation, and
runtime feedback, with overlapping representations and explicit composition
points between layers.[^fowler-generative-stack] Boyd's OODA model supplies the
complementary control semantics: Orientation shapes what is observed and which
actions are available, Decision is a hypothesis, and Action is a test that
produces further observations.[^boyd-ooda] This bundle combines those
influences into a practical software-change method with explicit authority
boundaries.

[Processes](processes/) give recurring coordination a stable
trigger-to-outcome model across the stack. A Process may use OODA to adapt one
enactment, but OODA is not a mandatory Process template and the Process does
not become another authority over Intent, Requirements, Architecture,
Implementation, or Evaluations.

Neither model transfers authority automatically. A Signal or Observation is
not Intent. Intent is human-oriented direction, not raw feedback. A Requirement
canonically expresses accepted Intent but must obligate an eligible
Architecture subject. Intent is not a direct Compilation input. A Requirement
is not its architecture response. An Evaluation is not the Requirement it
evaluates. An OODA Decision selects a repair hypothesis but does not authorize
it beyond the applicable human or institutional authority.

## What the method optimizes for

- Preserve a single normative authority for each accepted obligation.
- Permit useful, diverse redundancy among representations with different
  purposes and failure modes.
- Make changes traceable from originating signal through desired state,
  Implementation, and evidence without requiring one universal document or
  traceability matrix.
- Develop only the Change Design needed to resolve present technical ambiguity
  and preserve it no more durably than implementation, review, and handoff
  require.
- Use evidence-bound Orientation to identify the smallest authority capable of
  explaining and correcting a Signal.
- Treat each authorized repair as a hypothesis tested through bounded Action
  and new Observations.
- Keep contradiction, uncertainty, and unavailable evidence visible until an
  authorized decision resolves them.
- Let fast-changing Implementation Units remain replaceable while conserving
  data, contracts, Requirements, operational memory, and rollback paths.
- Compact obsolete structure and explanations after learning has stabilized.

## Boundaries

Gen Stack does not choose product priority, accept Requirements, approve
architecture, implement evaluator infrastructure, or authorize production
release. It supplies a shared method for keeping those decisions and artifacts
coherent. It also does not require every implementation-local test to map to a
maintained Requirement; only an evaluation that claims Requirement coverage
needs the stable relationship.

The method is deliberately opinionated but not a claim that fully autonomous
regenerative software is mature. Adopt only the next step supported by current
needs and evidence.

See [OODA as the Gen Stack control loop](control-loop/ooda-control-loop.md) for
the complete mapping and [Analyzing Requirement
impact](control-loop/analyzing-requirement-impact.md) for bounded work-item
intake when a Signal may imply a change to desired state.

[^fowler-generative-stack]: Fowler describes the motivating layered pipeline,
    overlapping representations, and feedback direction. “One authority, many
    witnesses” and the lifecycle contracts in this bundle are this package's
    synthesis.
[^boyd-ooda]: Boyd's [The Essence of Winning and Losing](https://www.coljohnboyd.com/documents/1995-06-28__Boyd_John_R__The_Essence_of_Winning_and_Losing__PPT-PDF.pdf)
    supplies the OODA control-loop semantics adapted across the Gen Stack.
