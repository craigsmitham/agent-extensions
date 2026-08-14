---
type: Explanation
title: Variance, baselines, and grading
description: How comparisons, repeated trials, and appropriate graders keep evaluation honest.
tags: [agent-skills, evaluation, baselines, graders, variance]
status: stable
generated: { by: "codex/gpt-5.6", at: 2026-08-14T19:36:04Z }
sources:
  - id: skillbench
    resource: https://arxiv.org/abs/2607.13987
    title: SkillBench — Benchmarking Agent Skills
---

# Variance, baselines, and grading

Agent behavior varies across runs, models, hosts, and catalog context. Repeat
nondeterministic cases enough to reveal material instability and report the
distribution, not only the best example. Expand repetition when a decision
would otherwise turn on one run. Recent benchmark work likewise treats skills
as artifacts that require comparative task evidence.[^skillbench]

Prefer a meaningful comparison: the same task without the skill, the accepted
published revision, or a named alternative. Hold model, host, fixtures, and
grader constant when attributing a difference to the skill.

Use the least subjective grader that can observe the contract:

- schema, file, command, and state assertions for structural outcomes;
- reference-based checks for bounded facts;
- explicit rubrics with anchored examples for qualitative work; and
- human review for consequential judgment, safety, or ambiguous value.

Define graders before seeing candidate outputs. Keep critical dimensions
separate from convenience scores, record grader uncertainty, and inspect cases
where graders disagree. A faster result is not better if it violates authority
or loses the intended outcome.

[^skillbench]: SkillBench — Benchmarking Agent Skills
