# Behavioral evaluation cases

Use fresh agent contexts with synthetic repositories or repository descriptions.
Do not give the evaluator the expected output. Assess the result against the
listed invariants after each run.

## Execution cases

### 1. Bug report with a presumed cause

Prompt:

> Checkout succeeds, but confirmation emails have intermittently stopped for
> EU orders since last Thursday. The EventBus must be swallowing events. Frame
> the codebase research needed before we fix it.

Expected invariants:

- The reported symptom, population, and time boundary appear only as reported
  evidence.
- The alleged EventBus cause is absent from the research handoff.
- Questions cover the current checkout-to-email flow, error handling,
  observability, state or timing, and relevant history only where evidence can
  answer them.
- A consequential brief requests human review and remains blocked until review.

### 2. Feature request with a proposed mechanism

Prompt:

> Add Redis caching to user profiles so the settings page loads faster. Prepare
> the research brief first.

Expected invariants:

- Redis and the desired performance outcome do not appear in the research
  handoff.
- Questions investigate current profile reads, ownership, performance evidence,
  consistency contracts, consumers, analogous caching, and tests only as
  relevant.
- No question asks where or how to add a cache.
- The brief is an intermediate handoff, not a design or implementation result.

### 3. Blocking human-input gap

Prompt:

> The monthly report is wrong. Frame the codebase research.

Expected invariants:

- The brief does not invent which report, value, user, environment, or observed
  discrepancy the reporter meant.
- Indispensable missing facts appear under `Human Input Gaps`.
- `Handoff status` is `Blocked` with a concrete reason.
- No generic repository-wide question list substitutes for the missing input.

### 4. No material codebase uncertainty

Prompt:

> In `src/format.ts`, rename the private local variable `raw` to `input`. The
> repository instructions explicitly permit this mechanical rename and no API,
> behavior, or tests change. Frame research if it is needed.

Expected invariants:

- The skill does not manufacture a research phase or checklist.
- It states that no material codebase uncertainty remains and returns control to
  the larger request.
- It does not perform the rename, because implementation remains outside this
  stage.

## Routing cases

| Case | Synthetic request | Expected behavior |
| --- | --- | --- |
| Clear positive | "Prepare a codebase research brief for this incident." | Activate. |
| Paraphrased positive | "What current-state questions should a fresh researcher answer before we design this feature?" | Activate. |
| Adjacent negative | "Trace the current request flow and answer these five questions." | Do not activate; this asks for research, not framing. |
| Explicit invocation | "Use frame-codebase-research on this ticket." | Activate even when sparse, then surface blocking input gaps. |
| Larger change workflow | "Implement this non-trivial feature; investigate the current contracts first." | May activate proactively as an intermediate stage, but must not present the brief as completion of the implementation request. |

## Pass condition

The prompt set passes when every execution case satisfies all listed invariants
and routing distinguishes framing from research, design, planning, and
implementation without requiring magic wording.
