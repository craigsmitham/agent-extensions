---
name: evaluate-agent-skill
description: Evaluates an Agent Skill's routing, execution, outcomes, efficiency, safety, and robustness against representative cases, baselines, intended hosts, and observable expectations. Use when asked to test, benchmark, verify, compare, or measure Agent Skill or SKILL.md behavior. Not for silently changing the evaluated skill or conducting a supply-chain trust review.
---

# Evaluate an Agent Skill

Produce objective evidence about whether a skill is selected for the right work
and fulfills its promise after selection. Keep routing and destination quality
separate so one cannot conceal failure in the other.

This skill is coupled to direct siblings in the skill-engineering pack. From
the active AXM scope root, read:

- `.axm/extensions/@craigsmitham/knowledge/skill-engineering/src/evaluation/evaluation-model.md`;
- `evaluation/routing-evaluations.md` for implicit-selection cases; and
- `evaluation/execution-evaluations.md` for activated behavior.

Read `evaluation/variance-baselines-and-grading.md` when comparing versions,
hosts, models, or repeated trials. Read
`governance/portfolio-coherence-and-observability.md` when evaluation supports
admission, consolidation, or an active library cohort.

## Authority

Evaluation is read-only with respect to the target skill. It may create an
explicitly requested evaluation workspace and result artifacts, but it must not
revise, install, publish, enable, or replace the skill. Do not claim a host or
model was tested when it was unavailable. Do not use production systems or
externally mutable fixtures without separate authority.

## Workflow

1. **Bind the target.** Record the canonical skill identity, version or content
   revision, intended hosts and models, evaluator environment, evaluation time,
   and relevant active-cohort or catalog revision. Separate reported behavior
   from observed behavior.
2. **Recover the contract.** Extract what the description promises, when it
   should and should not activate, required inputs and capabilities, observable
   outcome, authority limits, and completion evidence. Mark ambiguity; do not
   invent expectations to make the skill testable.
3. **Choose comparison surfaces.** Prefer the same task without the skill, the
   current published version, or the prior accepted revision. Explain when no
   useful baseline exists.
4. **Build the case matrix.** Include clear positive, paraphrased positive,
   adjacent negative, ambiguous, and explicit-invocation cases. Add failure,
   recovery, permission, or resource cases material to the skill's job. For
   admission or library use, include semantic neighbors and the actual active
   cohort; do not substitute the entire catalog when it is not exposed.
5. **Define graders before runs.** Use deterministic assertions for structural
   contracts and observable state. Use bounded judgment rubrics for usefulness
   or quality. Avoid exact prose, volatile identifiers, or hidden preferences
   unless they are contractual.
6. **Test routing independently.** Withhold the skill body and expected answer;
   expose only the same metadata the host uses for discovery. Record correct
   selection, misses, false positives, ambiguity handling, and collisions. Test
   both isolation and relevant coexistence when a library claim is in scope.
7. **Test activated execution.** Explicitly activate the skill so routing cannot
   mask destination defects. Give only task-local fixtures, observe resource and
   tool use, and preserve raw outputs or traces needed for grading.
8. **Repeat proportionately.** Repeat nondeterministic cases enough to expose
   material variance. Test only the models and hosts the skill actually claims
   or the caller names.
9. **Grade by dimension.** Assess routing, instruction adherence, outcome,
   efficiency, safety and authority, recovery, and robustness. Distinguish a
   skill defect from an unavailable environment or inadequate evaluator.
10. **Report without repairing.** Use `references/evaluation-report.md`. Give
    each expectation its evidence, classify regressions and uncertainty, and
    identify the smallest responsible contract for later authoring.

## Disposition

- **Supported** — representative evidence supports every material claim in the
  tested scope with no unresolved critical regression.
- **Partially supported** — useful behavior exists, but one or more material
  claims or boundaries lack support.
- **Unsupported** — evidence contradicts a central routing, execution, outcome,
  or safety claim.
- **Inconclusive** — missing environment, provenance, fixtures, or evaluator
  reliability prevents a defensible conclusion.

Never convert `Inconclusive` to success because no failure was observed.

## Done when

The report names the exact target and tested scope; routing and execution have
independent evidence; baselines and graders are explicit; raw evidence is
preserved or cited; active-cohort and coexistence claims identify their catalog
revision; variance and untested claims are visible; and no target mutation
occurred.
