---
name: research
description: Conducts bounded, evidence-backed research from a research brief or explicit questions and returns a consistent question-by-question report with citations, confidence, counterevidence, decision implications, and unresolved gaps. Use when asked to research, investigate, gather evidence for, or execute framed research questions. Not for initially framing research questions, writing surveys or interview guides, or making a decision the caller did not request.
---

# Research

Execute a bounded research brief and return an intelligible, manageable report
whose structure remains stable across subjects and research depth.

## Execute

1. Bind the brief. Require at least one explicit research question or objective.
   Preserve supplied question IDs and priority; assign `Q1`, `Q2`, and so on
   only when explicit questions lack IDs. If the input is merely a subject or a
   blind brief without questions, request framing rather than silently inventing
   the investigation.
2. Record the intended decision or use, subject and boundary, observable
   context, constraints, deliberate omissions, evidence standard, and research
   budget. Label absent material as not supplied; do not manufacture it.
3. Select `standard` depth unless the caller supplies another budget:
   - `rapid` prioritizes decision-critical questions and may leave lower
     priorities not reached;
   - `standard` investigates every question proportionately and follows
     material contradictions or second-order leads; and
   - `deep` continues through important contradictions and implications until
     further work is unlikely to change the conclusions or the budget ends.
4. Read `references/evidence-practice.md`, then plan and perform the research
   using available read-only sources and tools. Research may inspect public,
   caller-provided, repository, or other authorized evidence. Do not modify
   systems, contact people, purchase access, or perform another externally
   mutable action merely to answer a question.
5. Preserve the original questions. Add an emergent `E1`, `E2`, and so on only
   when discovered evidence raises an in-scope question that could materially
   change the intended decision or understanding. State what triggered it.
6. Read `references/report-contract.md`, then emit that report exactly. Scale
   detail to the brief, but do not remove required sections or question fields.
7. Verify before release: every input question has a dashboard status and one
   corresponding finding; material external claims have nearby citations;
   source statements, synthesis, and inference remain distinguishable; material
   counterevidence and gaps are visible; and no unsupported recommendation is
   introduced.

## Boundaries

- Research and synthesize; do not silently reframe the supplied investigation.
- State decision implications, but recommend or decide only when the brief
  explicitly asks and supplies the relevant authority or criteria.
- Never fill an evidence gap from memory while presenting it as researched.
- Preserve source licensing and quotation limits. Prefer paraphrase and link to
  the source rather than reproducing substantial source text.

The job succeeds when the stable report accounts for every input question,
supports material findings with traceable evidence, calibrates confidence and
limitations, and makes remaining uncertainty actionable.
