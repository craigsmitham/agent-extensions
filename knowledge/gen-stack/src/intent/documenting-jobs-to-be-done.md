---
type: Guide
title: Documenting Jobs to Be Done
description: Use when evidence shows progress sought in particular circumstances and that progress needs solution-independent identity; create one Job to Be Done concept.
tags: [architecture-documentation, jobs-to-be-done, jtbd, demand, evidence, authoring]
status: draft
sources:
  - resource: jobs-to-be-done.md
    title: Jobs to Be Done
  - resource: ../profile/gen-stack-application-profile.md#job-to-be-done
    title: Gen Stack application profile — Job to Be Done
generated: { by: codex/gpt-5.6, at: "2026-08-26T14:02:36Z" }
---

# Documenting Jobs to Be Done

## Goal

Create one `Job to Be Done` concept under `intent/jobs/` that explains progress
an audience seeks in particular circumstances.

## Before you begin

Start from accepted evidence about actual choices, constraints, alternatives,
or struggling moments. A plausible sentence is not evidence. Keep interview
records, named participants, tentative segmentation, and opportunity scoring
in their research authority.

## Steps

1. Identify the audience and circumstances in which demand arises. Circumstance
   should explain more than a demographic or permanent persona attribute.
2. State the sought progress without naming a preferred product, feature,
   surface, or implementation.
3. Create the canonical file using the `Job to Be Done` type and common fields
   from the [application profile](../profile/gen-stack-application-profile.md#job-to-be-done).
4. Explain relevant functional, social, or emotional forces. Include only
   dimensions supported by evidence; do not create empty classifications.
5. State exclusions that distinguish the job from neighboring needs, jobs,
   use cases, and capabilities.
6. Link the evidence and consequential relationships to audiences, offerings,
   propositions, use cases, and capabilities, then update `intent/jobs/index.md`.

## Final check

- The statement combines circumstances with sought progress.
- It remains valid if the current response changes.
- It is not a source request, Change Specification, use-case flow, or provider
  capability.
- Evidence, confidence, and material exclusions are honest and visible.

## Related

- [Jobs to Be Done](jobs-to-be-done.md)
- [Documenting needs](documenting-needs.md)
- [Documenting use cases](documenting-use-cases.md)
