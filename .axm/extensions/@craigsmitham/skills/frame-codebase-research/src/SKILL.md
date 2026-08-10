---
name: frame-codebase-research
description: Turns a bug report, incident symptom, feature request, or change idea into neutral current-state codebase research questions and a standalone brief. Use as a proactive question-framing stage before investigating or planning a non-trivial change when behavior, ownership, data flow, contracts, dependencies, failure conditions, or tests are uncertain. Completion is an intermediate handoff, not fulfillment of a request for research answers, diagnosis, design, planning, implementation, or code changes. Not for trivial changes with no material codebase uncertainty.
---

# Frame codebase research

Create a brief that lets a fresh researcher discover the relevant current state
without inheriting the source request's presumed cause or preferred solution.

## Operating contract

- Frame inquiry; do not answer it.
- Preserve reported observations, reproduction evidence, environment facts, and
  explicit research boundaries needed for the inquiry. Use desired outcomes and
  future-facing constraints to select questions, but keep them and proposed
  solutions out of the research handoff.
- Ask only questions that repository, runtime, history, or authoritative external
  evidence can answer. Keep human or product clarification gaps separate.
- Perform shallow discovery only to verify repository terminology and anchors.
  Do not trace the implementation deeply enough to become the researcher.
- Do not edit implementation files or recommend a design, fix, refactor, or plan.
- Scale the brief to the uncertainty. Do not force a fixed question count or a
  research phase when no material codebase uncertainty remains.
- When framing is one stage of a broader request, treat the brief as an
  intermediate handoff and do not claim the caller's later outcome is complete.

## Workflow

### 1. Normalize the source request

Extract:

- reported observations or current behavior;
- desired behavior or user outcome;
- reproduction details, environment, logs, and version information for a bug;
- use cases, success criteria, compatibility constraints, and exclusions for a
  feature;
- unverified causes, implementation preferences, and other assumptions.

Do not turn missing reporter knowledge into a codebase question. Resolve it from
available context or list it under `Human input gaps`. Mark the brief not ready
for handoff when such a gap prevents meaningful research. Put only reported
facts the researcher needs but cannot discover under `Reported evidence`; defer
choices about future behavior or implementation to design rather than listing
them as input gaps.

### 2. Learn the codebase vocabulary

Read applicable repository instructions and inspect only high-level structure,
exact request terms, and directly named files. Verify likely subsystem, symbol,
and path names before using them as anchors. Do not include a guessed anchor.

### 3. Select consequential questions

Cover only uncertainties relevant to the request. Useful dimensions include:

- entry points, ownership, and end-to-end control and data flow;
- state transitions, persistence, contracts, invariants, and consumers;
- analogous implementations and established tests or observability;
- configuration, authorization, dependency, deployment, and compatibility
  boundaries.

For a bug, consider reproduction conditions, the point where expected and
observed behavior diverge, error translation or suppression, state and timing,
and regression history. For a feature, consider the closest existing capability,
extension boundaries, affected contracts and consumers, and how comparable
behavior is verified.

Each question must:

- ask about current state, not what should be built;
- contain one research concern;
- avoid presuming a cause, location, or solution;
- be answerable with identifiable evidence;
- add information not already established by the source request; and
- state the evidence sought rather than why a future change needs it.

Merge overlaps and remove generic checklist questions that do not affect this
request.

### 4. Produce the brief

Use this shape:

```markdown
# Codebase Research Brief: <neutral topic>

**Handoff status:** <Ready | Blocked — reason>
**Review status:** <Accepted | Requested | Not required>

## Scope
<Current behavior or capability to investigate, without a presumed cause or
solution.>

## Reported Evidence
- <Reported observation, reproduction detail, environment, or version needed
  for research; label it as reported rather than verified. Omit when empty.>

## Known Anchors
- `<verified path, symbol, subsystem, or user-visible term>`

## Human Input Gaps
- <Only unresolved facts that codebase research cannot supply. Omit when empty.>

## Research Questions

### Q1 — <short current-state label>
**Question:** <one neutral, evidence-answerable question>
**Evidence sought:** <definitions, references, runtime observations, tests,
history, configuration, or authoritative external documentation>

## Boundaries
- <Intentionally excluded systems or concerns.>

## Completion Criteria
- Every question is answered, partially answered, or explicitly unresolved with
  the evidence searched.
```

Do not copy the original ticket, proposed solution, or presumed cause into the
brief. Use desired behavior only to select relevant current-state questions; do
not restate the desired outcome, future-facing constraint, or future change
mechanism anywhere in the research handoff. Include only enough neutral
current-state scope and reported evidence to make the questions answerable.

Return the brief in the response unless the caller specifies a path or the
repository has an explicit location for temporary research artifacts. Do not
invent a durable documentation home or commit the brief without authorization.

## Review and handoff

Treat the generated brief as a draft. For a consequential change, ask the caller
to accept or revise the reported evidence, question coverage, omissions, and
boundaries before research begins. Until then, set `Review status` to `Requested`
and `Handoff status` to `Blocked`. For a low-stakes inquiry where review would
add no material judgment, use `Not required`. Set the handoff to `Blocked`
whenever an indispensable human input is missing; otherwise set it to `Ready`
after the applicable review condition is satisfied.

## Handoff check

Before handing off, confirm that:

- all anchors are verified;
- every question is neutral and evidence-answerable;
- no question asks for design or implementation advice;
- human input gaps are visibly separate and contain no deferred design choice;
- reported evidence contains no presumed cause, desired outcome, proposed
  solution, or future-facing constraint;
- scope contains no desired outcome or future change mechanism;
- handoff and review statuses agree with the unresolved gaps and review state;
  and
- the brief stands alone without exposing unnecessary source-request framing.

Recommend giving only the brief to a fresh research context when practical.
