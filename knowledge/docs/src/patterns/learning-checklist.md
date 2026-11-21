---
type: Pattern
title: Learning checklist
description: When learners need support during practice, prompt useful retrieval, reasoning, and reflection with feedback, then fade instructional support and assess later independent performance.
tags: [docs, documentation-pattern, checklist, learning-scaffold, learning, onboarding, practice, retention, transfer, authoring]
status: draft
sources:
- id: checklist-design-origin
  resource: https://github.com/craigsmitham/agent-extensions/blob/156c3d4346bee6874ab3d356c19446cf6425713b/skills/checklist-design/src/references/learning-checklists.md
  title: Craig Smitham — Learning checklists, version 0.1.10
- id: regulated-learning
  resource: https://pubmed.ncbi.nlm.nih.gov/37034913/
  title: Shao et al. — Effects of regulated learning scaffolding on regulation strategies and academic performance
- id: test-enhanced-learning
  resource: https://pubmed.ncbi.nlm.nih.gov/29390949/
  title: Green et al. — Test-enhanced learning in health professions education
- id: expertise-reversal
  resource: https://www.tandfonline.com/doi/abs/10.1207/S15326985EP3801_4
  title: Kalyuga et al. — The expertise reversal effect
generated:
  by: codex/gpt-6
  at: '2026-11-21T22:51:04Z'
---

# Learning checklist

Choose a learning checklist when learners can already attempt a bounded task
and prompts at particular moments would help them practice a judgment they
will later need to make independently. A novice reviewer, for example, might
predict where a draft misleads its reader, inspect the passage, and compare
their prediction with an experienced reader’s feedback. The activity needs
a way to discover which predictions held up.[^checklist-design-origin]

## When the aid earns its place

A few prompts can make practice more deliberate at relatively little cost.
If someone still needs a demonstration and a carefully arranged first
experience, the card can sit within a [tutorial](tutorial.md). If the job
calls for a reliable reminder every time, an
[execution checklist](execution-checklist.md) can continue to serve an
experienced practitioner. Removing a standing operational check changes how
the work is controlled and requires its own justification.

The learning form costs effort to design feedback, adjust prompts, and
observe later performance. Learners may copy an answer or come to rely on
a cue. A prompt that helps a novice can interrupt an expert’s practice.
Kalyuga and colleagues examine how prior knowledge can change the effects
of instructional techniques. Local performance is needed to decide what
support earns its place here.[^expertise-reversal]

## What the evidence supports

Shao and colleagues synthesized research on several kinds of regulated-learning
scaffolding. Green and colleagues reviewed test-enhanced learning in health
professions education. Both address broader interventions. Neither establishes
that a particular checklist improves independent judgment, nor specifies a
schedule for withdrawing it.[^regulated-learning][^test-enhanced-learning]

Completing a prompted task shows performance with the aid. Delayed work on a
familiar case can reveal retention. A changed case can show whether the learner
can adapt what they learned. If the claim concerns self-regulation, look for
planning, monitoring, and correction when the checklist no longer supplies
those cues. A record of attendance answers a different question.

For the relationship between prompting and independence, see
[How a learning checklist changes practice](../explainers/learning-checklist.md).
For a worked design with feedback and a transfer exercise, follow
[How to design a learning checklist](../guides/designing-a-learning-checklist.md).

[^checklist-design-origin]: Craig Smitham, Learning checklists, version 0.1.10.
[^regulated-learning]: Shao and colleagues, [Effects of regulated learning scaffolding on regulation strategies and academic performance](https://pubmed.ncbi.nlm.nih.gov/37034913/).
[^test-enhanced-learning]: Green and colleagues, [Test-enhanced learning in health professions education](https://pubmed.ncbi.nlm.nih.gov/29390949/).
[^expertise-reversal]: Kalyuga and colleagues, [The expertise reversal effect](https://www.tandfonline.com/doi/abs/10.1207/S15326985EP3801_4).
