---
name: conduct-codebase-research
description: Investigates a codebase from a research brief or explicit questions and produces an evidence-backed, snapshot-bound current-state report and technical map. Use when asked to answer codebase research questions, trace existing behavior, locate ownership, explain control or data flow, identify contracts and invariants, assess relevant drift since a report or brief, or map architecture before design. Not for proposing changes, choosing a design, writing an implementation plan, reviewing code quality, or editing code.
---

# Conduct codebase research

Answer the supplied questions by documenting the system as it exists at a named
snapshot. Produce evidence another engineer or agent can inspect and challenge.

## Operating contract

- Research and explain; do not modify implementation files.
- Do not recommend a fix, design, refactor, optimization, or implementation plan.
- Preserve the supplied question IDs and account for every question.
- Distinguish observed behavior, implemented behavior, declared intent, and
  inference. Never present one as another.
- Bind material claims to the code, configuration, dependency, deployment, and
  runtime snapshot that supports them. A date alone does not establish validity.
- Prefer the source that owns each claim: runtime evidence for observed behavior,
  current code and configuration for implementation, tests or specifications for
  declared contracts, version history for rationale, and official version-matched
  documentation for external dependencies.
- Treat unanswered or conflicting evidence as a result, not an invitation to
  guess.

## Workflow

### 1. Establish scope and snapshot

Read the brief or questions and applicable repository instructions completely.
Do not seek the originating ticket or desired solution unless the brief names it
as required evidence. Extract the time and snapshot of each supplied observation
and the brief's preparation and anchor snapshot. Mark missing provenance unknown;
do not infer it.

Record the research time and current repository, branch, commit, worktree state,
configuration, dependency, deployment, and runtime versions relevant to the
questions. Note pre-existing worktree changes and leave them untouched. Compare
the current snapshot with each available reported or brief snapshot using scoped
history, diffs, or environment evidence around the affected boundaries. Record
whether intervening drift is relevant, irrelevant, or unassessable; do not turn
this into a repository-wide change audit.

Classify each question as current behavior, structure, dependency, history, or
runtime investigation. Identify boundaries that require evidence outside the
working tree before using external tools.

### 2. Locate, trace, and verify

Use repository-native navigation and validation tools. Start broad enough to
locate ownership, then narrow to relevant symbols and flows:

1. Find definitions, references, entry points, configuration, schemas, and
   directly related tests.
2. Trace control and data from entry through internal and external boundaries to
   state changes and outputs.
3. Inventory the capabilities within and adjacent to the traced boundaries, plus
   governing architectural, framework, or runtime capabilities that could shape
   the design space. Record what they do, their extension points, constraints,
   coupling, consumers, material versions, and the source or authority that makes
   each a binding rule, established pattern, or merely available dependency.
   Document what exists without judging whether it fits or is desirable; do not
   infer an obligation from dependency presence or common use alone.
4. For bugs, safely reproduce at the research snapshot when practical, relate
   the result to the reported snapshot, narrow the affected region, compare
   expected and observed paths, and inspect state, timing, error handling, and
   relevant intervening or regression history. If the symptom no longer
   reproduces, establish what changed only as far as the evidence permits.
5. For external semantics, use primary documentation matching the installed
   version. Label any version mismatch.

Use safe, read-only diagnostics and existing tests when they materially answer a
question. Record the command, environment, and relevant result. Do not add probes
or tests unless the caller separately authorizes code changes.

For a large brief, use separate fresh contexts for independent investigations
when the runtime supports them. Give each investigator only its bounded question
and require evidence. Do not recursively delegate; synthesize and verify the
returned claims centrally.

### 3. Classify evidence

Use these labels when the distinction matters:

- **Observed:** command, test, trace, log, or reproduction result.
- **Implemented:** current source, schema, or configuration directly establishes
  the claim.
- **Declared:** a test, specification, comment, or documentation states intent or
  contract.
- **Inferred:** multiple facts support the conclusion, but no source states it
  directly.

Cite every material claim near the claim. Prefer commit-pinned permalinks when
available; otherwise cite repository-relative paths, symbols, and line numbers.
Use history only for claims about change or rationale, and keep stale research
artifacts supplementary to fresh inspection.

### 4. Produce the report

Read `references/codebase-research-report.md` and adapt its shape rather than
leaving empty boilerplate.

Return the report in the response unless the caller specifies a path or the
repository defines a temporary research location. Do not invent a durable
documentation home, overwrite another artifact, or commit the report without
authorization.

### 5. Validate the report

Before handing off, confirm that:

- every supplied question has an explicit status and evidence trail;
- the technical map crosses every material boundary found;
- relevant existing and governing capabilities are inventoried with their
  authority and material versions, or their absence is stated;
- material claims are cited and inferences are labeled;
- material claims identify the snapshot that supports them;
- chronology, relevant drift, and unassessable provenance remain explicit;
- snapshot and version metadata make citations reproducible;
- contradictions and missing evidence remain visible; and
- the report contains no recommendation, design choice, or implementation plan.
