---
name: frame-codebase-research
description: Turns a bug report, incident symptom, feature request, or change idea into neutral current-state codebase research questions and a standalone, time-aware brief. Use as a proactive question-framing stage before investigating or planning a non-trivial change when behavior, ownership, data flow, contracts, dependencies, failure conditions, tests, or codebase drift are uncertain. Completion is an intermediate handoff, not fulfillment of a request for research answers, diagnosis, design, planning, implementation, or code changes. Not for trivial changes with no material codebase uncertainty.
---

# Frame codebase research

Create a brief for discovering relevant current state without inheriting the
source request's presumed cause or preferred solution.

## Operating contract

- Frame inquiry; do not answer it or recommend a change.
- Preserve only the reported observations, reproduction evidence, environment
  facts, and boundaries needed for research. Use desired outcomes, constraints,
  and implementation preferences to select questions, but omit them from the
  handoff.
- Distinguish observation time, report time, affected snapshot or environment,
  brief time, and anchor-verification snapshot. Never transfer evidence from one
  point in time to another.
- Ask only questions that repository, runtime, history, or authoritative external
  evidence can answer. Keep human or product clarification gaps separate.
- Perform shallow discovery only to verify repository terminology and anchors.
  Do not trace the implementation deeply enough to become the researcher.
- Do not edit implementation files.
- Scale the brief to the uncertainty. Do not force a fixed question count or a
  research phase when no material codebase uncertainty remains.
- In a broader request, treat the brief as an intermediate handoff rather than
  claiming the later outcome is complete.

## Workflow

### 1. Normalize the source request

Extract:

- reported observations, reproduction details, logs, and their provenance;
- desired behavior, success criteria, constraints, and exclusions;
- unverified causes, implementation preferences, and other assumptions.

Do not turn missing reporter knowledge into a codebase question. Resolve it from
available context or list indispensable non-repository facts under `Human Input
Gaps`. Mark a material missing time, snapshot, or environment fact `Unknown`;
omit irrelevant provenance categories rather than enumerating them. Put reported
facts under `Reported Evidence`, but keep their times, snapshots, and environment
identifiers only in the timeline. Do not list deferred design choices as gaps.
If missing input makes the subject unidentifiable, stop after `Human Input Gaps`
instead of inventing generic research questions.

### 2. Learn the codebase vocabulary

Read applicable repository instructions; inspect only high-level structure,
request terms, and named files. Verify likely subsystem, symbol,
and path names before using them as anchors, along with the domain vocabulary of
the capability area, so research can search by concept rather than only the
request's wording. Record the verification time,
repository, branch, commit, and worktree state, plus only the configuration,
dependency, deployment, or runtime versions material to the anchors. Do not
include a guessed anchor.

### 3. Select consequential questions

Cover only relevant uncertainties, such as:

- entry points, ownership, and end-to-end control and data flow;
- state transitions, persistence, contracts, invariants, and consumers;
- existing capabilities carrying responsibility of this kind, and established
  tests or observability;
- configuration, authorization, dependency, deployment, and compatibility
  boundaries.

Unless the change would build nothing new, include a standing question about
what capabilities already exist within and adjacent to the scope and what
constrains their use. Phrase it as what exists, never as whether a particular
capability can be reused. Scale it to what the change would build, not to the
size of the report.

For a bug, consider reproduction, divergence, error handling, state, timing, and
scoped regression history. When report and framing snapshots differ, ask whether
current behavior still matches the report and which relevant changes matter. For
a feature, consider extension boundaries, contracts, consumers, and
verification.

Each question must:

- ask one current-state research concern;
- avoid presuming a cause, location, or solution;
- be answerable with identifiable evidence;
- add information not already established; and
- state the evidence sought, not why a future change needs it.

Merge overlaps and remove generic checklist questions that do not affect this
request.

### 4. Produce the brief

Read `references/codebase-research-brief.md` and adapt its shape rather than
leaving empty boilerplate.

Include only enough neutral current-state scope and reported evidence to make
the questions answerable. Keep the original ticket, desired outcome, future
constraint, presumed cause, and proposed mechanism out of the brief.

Return the brief in the response unless the caller specifies a path or the
repository has an explicit location for temporary research artifacts. Do not
invent a durable documentation home or commit the brief without authorization.

## Review and handoff

Treat the generated brief as a draft. Set `Brief status` to `Blocked` only when
an indispensable human input prevents meaningful research; otherwise use
`Ready`. When question coverage, omissions, or boundaries require material human
judgment, set `Review status` to `Requested` until the caller accepts or revises
them. Pending review means research authorization is pending, not that a complete
brief is blocked. Use `Not required` for low-stakes inquiry where review adds no
material judgment.

## Handoff check

Before handing off, confirm that:

- anchors are verified, the timeline contains provenance rather than duplicated
  observations, and material unknowns are not invented;
- every question is neutral, single-concern, and evidence-answerable;
- human input gaps contain only indispensable non-repository facts, and no
  generic questions appear when those gaps leave the subject unidentifiable;
- reported evidence and scope contain no desired outcome, deferred design
  choice, presumed cause, proposed mechanism, or repeated timeline fact;
- potentially material drift is covered by a scoped question or explicitly
  identified as unassessable from the available provenance;
- brief and review statuses agree with missing inputs and review state; and
- the brief stands alone without exposing unnecessary source-request framing.

When practical, give only the brief to a fresh research context.
