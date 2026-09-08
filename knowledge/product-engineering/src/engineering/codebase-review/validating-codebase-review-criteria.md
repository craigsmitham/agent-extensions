---
type: Guide
title: Validating codebase-review criteria
description: Use when deciding whether the review criteria may carry stronger claims than candidate design coherence; design comparative trials, measure coverage and false assurance against bound conditions, read the existing design-review evidence for what it does not establish, and retire criteria that fail.
tags: [codebase-review, validation, comparative-evaluation, measurement, evidence, lifecycle, retirement, pe-engineering]
status: draft
generated: { by: claude/opus-5, at: 2026-09-08T00:00:00Z }
---

# Validating codebase-review criteria

Use this guide when someone proposes to treat the codebase-review collection as
more than a candidate: to gate a release on it, to publish an effectiveness
claim, or to retire part of it. Authoring and revision belong to
[Maintaining codebase-review criteria](maintaining-codebase-review-criteria.md);
this concept owns the evidence a stronger claim would require.

## Validate the design comparatively

Compare the complete [product-quality criteria](criteria/) and any selected
[supporting checklist](supporting/) with an unconstrained review, credible
alternative quality models, and—when useful—variants that expose evidence or
method aids differently. Do not treat the synthetic [framework design
review](framework-design-review.md) as observed effectiveness evidence.

Bind every comparison to the repository revision, review scope, reviewer or
exact model and configuration, tool access, prompt, and criterion version.
Use representative libraries, applications, services, and multi-package
repositories, including intentional exceptions and previously adjudicated or
seeded defects.

Measure:

- valid material findings, omissions, overlap, and unique findings;
- unsupported findings, false acceptance, and false rejection;
- criterion-level agreement and incompatible interpretations;
- evidence quality and diagnostic-cause accuracy separately from verdicts;
- review coverage, time, and token or tool cost;
- use of `Indeterminate`, `Not applicable`, and `Not assessed`; and
- material findings discovered beyond the criteria.

Evidence against the design includes reduced material-issue coverage,
increased unsupported conclusions, persistent ambiguity, ritual completion,
important issues missed across reviewers, or a feasible alternative that
performs the intended job more reliably. Do not reinterpret adverse or null
results as success by narrowing the original claim after the fact.

## Current design-review evidence

The 2026-09-01 [Codebase-review framework design
review](framework-design-review.md) challenged all ten pillars, the supporting
test-suite assessment, cross-cutting relationships, and method separation
against six synthetic product forms and seven boundary cases. It caused
material revisions: binary checkbox presentation was removed, several
contributor-shaped or umbrella criteria were replaced, compound questions were
narrowed, and source scope was corrected.

That record supports only candidate design coherence. No actual repository or
reviewer comparison has yet established material-issue coverage,
unsupported-finding rate, agreement, decision validity, or cost.

## Lifecycle

The package's declared owner controls publication and versioning. An
accountable field-validation owner, representative repository population, and
acceptance thresholds are not yet declared, so the collection remains
`status: draft`.

Review affected criteria or aids when:

- their sources, supported software practices, or terminology change;
- recurring reviews produce disagreements, false findings, or escaped issues;
- repository structures, tools, model capabilities, or available evidence
  change materially;
- `Not applicable`, `Indeterminate`, or `Not assessed` results become
  disproportionate; or
- an automated control, narrower checklist, rubric, or other aid performs the
  job with less omission or false assurance.

Replace, merge, or retire a criterion when it no longer represents a material
distinct outcome, cannot be assessed consistently, or displaces a stronger
control. Preserve the revision rationale and inbound discovery when doing so.
