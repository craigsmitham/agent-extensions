# Behavioral evaluation cases

Use fresh agent contexts with synthetic repositories or repository descriptions.
Do not give the evaluator the expected output. Assess the result against the
listed invariants after each run.

## Execution cases

### 1. Relevant drift from report through research

Prompt:

> Research this brief against the synthetic repository provided. The failed
> export was observed on commit `a111` with worker image 3.2 and reported three
> days later. The brief was prepared on commit `b222`. Research is running on
> commit `c333`, where the export state machine changed between `b222` and
> `c333`. Q1: What is the current export flow? Q2: Does the reported failure
> reproduce, and what relevant intervening changes affect that result?

Expected invariants:

- The report distinguishes observation, report, brief, and research times or
  snapshots.
- The current-state answer is explicitly bound to `c333` and its relevant
  environment.
- The drift check is scoped to the export boundaries and explains how the state
  machine change affects each finding without treating correlation as cause.
- Reproduction at `c333` is related to, but not substituted for, the reported
  observation at `a111`.
- The report recommends no fix or design.

### 2. Missing report provenance

Prompt:

> Investigate why webhook deliveries were reported as delayed. The brief does
> not identify the affected commit, deployment, or dependency versions. Answer
> the current-state questions against the checked-out repository.

Expected invariants:

- Missing report provenance remains explicitly unknown and is not inferred from
  the research snapshot.
- Current-state research proceeds when the questions remain answerable.
- Historical comparison is labeled unassessable rather than silently omitted or
  treated as a blocker without a material reason.
- Material findings still identify their supporting research snapshot.

### 3. Irrelevant intervening changes

Prompt:

> Research the current invoice-number allocation flow. The brief was prepared
> at `d444`; the checkout is now `e555`. The only intervening commits change the
> documentation site and an unrelated image optimizer.

Expected invariants:

- The report records the snapshot difference and evidence that the drift is
  irrelevant to the invoice boundaries.
- It does not expand into a repository-wide change narrative.
- It answers the supplied current-state questions at `e555` with normal evidence
  classification and citations.

## Pass condition

The prompt set passes when reports are reproducible at the research snapshot,
preserve supplied provenance, assess only relevant drift, keep unknown history
visible, and remain research rather than design.
