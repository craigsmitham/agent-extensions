---
name: question
description: Frames fast, concern-aware research by turning a subject or hypothesis-neutral brief into a compact Research Brief with prioritized, evidence-seeking questions. Use when asked to frame research, generate research questions, plan an independent investigation, blind-check prior findings, or invoke question or qrspi. Not for answering the questions, conducting the research, or writing surveys or interview guides.
---

# Question

Frame the smallest set of research questions most likely to improve an
important decision or understanding. Treat risk as consequential uncertainty,
including uncertainty about truth, value, context, feasibility, quality,
dependencies, opportunity, tradeoffs, consequences, and failure. Do not assume
the subject is defective.

## Frame

1. Bind the subject, intended decision or use, boundary, lifecycle stage,
   stakeholders, constraints, effort budget, and requested question count.
   Infer a missing intended use only when a reasonable default is possible and
   label it as an assumption. Ask one precise question only when the omission
   would materially change the priorities. Default to five through eight
   questions.
2. Determine whether independent or blind framing is required and whether the
   supplied material contains originating hypotheses, findings, diagnoses,
   suspected causes, preferred explanations, or proposed solutions.
3. For ordinary framing, derive the concern landscape and questions directly.
   For blind framing from contaminated material, follow the isolation workflow
   in `references/frame-contract.md`. Never call a same-context result blind.
4. Select three through six concerns that materially affect the intended use.
   Generate candidate questions, then prioritize them by importance,
   uncertainty, decision leverage, consequences of error or delay, dependency
   leverage, option value, and information gained relative to effort.
5. Keep questions neutral, distinct, evidence-seeking, and capable of changing
   a conclusion or action. Cover promise and peril in proportion to the
   subject; do not force a failure-oriented question into every frame.
6. Read `references/frame-contract.md` before composing the result. Apply its
   question-quality, blindness, and Research Brief presentation checks.

## Boundaries

- Frame the research; do not answer the questions or gather the evidence.
- Do not turn research questions into a survey, interview guide, test plan, or
  implementation plan unless separately requested.
- Do not manufacture comprehensive coverage. Name material omissions so the
  caller can challenge the prioritization.
- If neutral facts are insufficient, name the missing input rather than infer
  hidden originating material.

The job succeeds when the caller receives a compact Research Brief containing
an ordered, concern-aware set of answerable questions with stable IDs and the
evidence each would require, plus an honest statement of assumptions and
independence status. When isolation is required but unavailable, the completed
result is a neutral brief and an explicit fresh-context handoff rather than
questions falsely labeled blind.
