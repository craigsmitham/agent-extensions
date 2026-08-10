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

- The reported absence of email appears only under `Reported Evidence`; the EU
  population may bound `Scope`, and observation time appears only in the
  evidence timeline.
- The alleged EventBus cause is absent from the research handoff.
- Questions cover the current checkout-to-email flow, error handling,
  observability, state or timing, and relevant history only where evidence can
  answer them.
- The complete brief is `Ready` while its `Review status` is `Requested`.

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
- `Brief status` is `Blocked` with a concrete missing-input reason.
- The brief omits `Research Questions` rather than substituting a generic list
  for the missing input.

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

### 5. Report and framing snapshots differ

Prompt:

> Payment retries began duplicating charges on release 2.4 two weeks ago. The
> bug was filed yesterday. The repository is now on release 2.6, and several
> payment files have changed. Frame the research before we discuss a fix.

Expected invariants:

- The evidence timeline distinguishes observation time, report time, affected
  release, brief preparation time, and current anchor snapshot.
- Unavailable material provenance is marked unknown rather than invented;
  irrelevant version categories are omitted.
- The questions cover whether the symptom reproduces at the research snapshot
  and which relevant intervening changes affect the inquiry.
- The brief neither assumes the bug remains present nor concludes that a change
  fixed it.
- The drift question stays scoped to the affected boundaries instead of asking
  for a repository-wide history audit.

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
