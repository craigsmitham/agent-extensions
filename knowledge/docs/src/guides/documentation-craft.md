---
type: Guide
title: Documentation craft guide
description: Use when writing or revising one document; select and adapt a documentation pattern to its reader need, draft it, and verify its usefulness and accuracy.
tags:
- docs
- craft
- authoring
- how-to
- diataxis
status: stable
sources:
- id: documentation-craft
  resource: ../explainers/documentation-craft.md
  title: Documentation craft
- id: principle
  resource: ../patterns/principle.md
  title: Principle document
generated:
  by: codex/gpt-6
  at: '2026-11-11T16:59:49Z'
---

# Documentation craft guide

Use this process to write or revise one document. For a corpus-wide change,
use [Documentation workflow](documentation-workflow.md).

## Before writing

Identify the reader, intended outcome, authoritative source material, and any
local documentation rules. Do not invent product behavior or policy to fill a
gap; identify what needs an owner or further evidence.

## Steps

1. **Name the reader's need.** Are they learning, completing a task, looking up
   facts, or developing understanding?
2. **Select a pattern.** Start with the reader problem in the
   [Documentation pattern collection](../patterns/index.md). Check the pattern's
   applicability, tradeoffs, and evidence before adapting its design. Keep one
   primary reader job and link to material serving adjacent needs.
3. **Bound the document.** State the intended result or understanding near the
   start. An action document's description should pair its outcome with the
   situation or intent that makes it relevant. State readiness prerequisites
   separately from that selection cue.
4. **Draft for the job.** Apply the pattern's authoring guidance. Use authoritative
   sources and distinguish observed facts, proposals, and illustrative examples.
   When a maintained principle governs a decision, respect its scope and warrant.
5. **Place and name it.** Follow host conventions and the guidance in
   [Organizing and naming documentation](organizing-and-naming-documentation.md).
   Update affected indexes and links rather than creating another copy.
6. **Verify.** Check claims and instructions against available authority;
   exercise procedures where appropriate and authorized. Read from the target
   reader's perspective and run the host's relevant validators. An author's
   review does not establish actual reader comprehension.
7. **Maintain.** Record ownership and refresh triggers when the host supports
   them. Retire or revise material that no longer matches the system.

## Check before delivery

Can a reader tell the document's purpose and when to choose it? Does it fulfill
that purpose? Are source gaps, stale instructions, duplicate facts, and broken
links resolved or clearly identified? Keep repository-specific schemas and
layout rules local rather than turning them into universal craft rules.

## Related

- [Documentation craft](../explainers/documentation-craft.md)
- [Documentation pattern collection](../patterns/index.md)
- [Documentation quality](../explainers/documentation-quality.md)
