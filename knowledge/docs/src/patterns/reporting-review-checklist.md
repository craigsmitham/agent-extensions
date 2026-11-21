---
type: Pattern
title: Reporting and review checklist
description: When a report or review can omit important topics, map explicit coverage criteria to located evidence, findings, and justified exclusions without treating completeness as proof of quality.
tags: [docs, documentation-pattern, checklist, reporting-review, reporting, inspection, review, traceability, authoring]
status: draft
sources:
- id: checklist-design-origin
  resource: https://github.com/craigsmitham/agent-extensions/blob/156c3d4346bee6874ab3d356c19446cf6425713b/skills/checklist-design/src/references/validation-and-lifecycle.md
  title: Craig Smitham — Validation and lifecycle, version 0.1.10
- id: prisma
  resource: https://www.prisma-statement.org/prisma-2020
  title: PRISMA — PRISMA 2020 statement and reporting checklists
- id: inspection-comparison
  resource: https://publica.fraunhofer.de/entities/publication/eb2a71d4-2bfc-43c8-a5bf-8a03f643c016
  title: Perspective-based versus checklist-based software inspection
generated:
  by: codex/gpt-6
  at: '2026-11-21T22:51:04Z'
---

# Reporting and review checklist

Use a reporting and review checklist when a report or an inspection needs
coverage that others can trace. Each criterion gives a reviewer a question,
and the review record connects their answer to a passage, observation, or
finding. An exclusion earns its place when someone can establish why the
criterion falls outside the case. A blank record leaves the question open.

## When coverage or inspection is the job

PRISMA 2020 shows this design in published reporting guidance. Its checklist
lets an author indicate where each item appears, so another reader can inspect
how the work was reported.[^prisma] A design review might instead direct
attention to a consequence an author overlooked. A passage that addresses
that consequence can satisfy a reporting obligation and still reveal a
defect when a reviewer examines it.

A [verification checklist](verification-checklist.md) fits a different
question about whether completed work meets stated conditions. A rubric is
useful when readers need to distinguish levels of performance. A form alone
can suffice when the need is simply to collect values.

## Costs and evidence

A common set of prompts makes omissions and disagreements visible across
reviews. It can also focus attention so tightly on listed concerns that
an unexpected issue goes unreported. When reviewers need judgment,
allow a finding outside the listed topics and preserve the evidence for it.
A long list of generic questions costs time even where most are inapplicable.

Evaluate a reporting aid by whether someone else can trace required coverage
and find unresolved gaps. For an inspection aid, examine whether findings
are material and supported, which defects were missed, how often people
reported the same defect, and how much review effort it took. Empirical
comparisons of inspection methods apply to the artifacts, participants, and
conditions studied. A higher raw count alone can include repeated or invalid
findings.[^inspection-comparison][^checklist-design-origin]

For an account of what a located passage establishes, read
[What a reporting checklist makes visible](../explainers/reporting-review-checklist.md).
For a worked review with an exclusion and an open finding, follow
[How to design a reporting and review checklist](../guides/designing-a-reporting-and-review-checklist.md).

[^checklist-design-origin]: Craig Smitham, Validation and lifecycle, version 0.1.10.
[^prisma]: PRISMA, [PRISMA 2020 statement and reporting checklists](https://www.prisma-statement.org/prisma-2020).
[^inspection-comparison]: [Perspective-based versus checklist-based software inspection](https://publica.fraunhofer.de/entities/publication/eb2a71d4-2bfc-43c8-a5bf-8a03f643c016).
