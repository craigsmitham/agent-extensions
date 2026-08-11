# Codebase Change Workflow

Move a bug report, feature idea, or change request from current-state evidence
through accepted design and planning, assess whether implementation can safely
begin, then verify the completed change. The pack preserves evidence provenance
and checks relevant code, configuration, dependency, deployment, and runtime
drift across seven distinct stages:

1. Frame neutral current-state research questions.
2. Investigate the current system and produce an evidence-backed technical map.
3. Workshop consequential functional and technical decisions with a developer.
4. Compile the accepted design into an implementation-constraining specification.
5. Plan independently verifiable vertical slices and concrete work items.
6. Assess whether implementation can begin without unresolved consequential choices.
7. Verify the completed implementation against its accepted contract and snapshot.

| Stage | Start when | Produces | Continue when |
| --- | --- | --- | --- |
| Frame research | Material current-state uncertainty remains | Codebase Research Brief | The brief is `Ready` and any required review is accepted |
| Conduct research | Neutral questions and evidence boundaries are available | Codebase Research Report | Every question has a status and evidence trail |
| Workshop design | Change intent and sufficient current-state evidence are available | Codebase Design Record | The design is explicitly `Accepted` against a named evidence identity |
| Specify change | The accepted design and supporting evidence are current | Codebase Change Specification | The specification is explicitly `Accepted` |
| Plan change | An accepted specification and verifiable codebase snapshot are available | Implementation Plan | The plan is `Ready` with complete traceability and completion evidence |
| Assess readiness | Accepted scope, current evidence, and an implementation path are available | Codebase Change Readiness Assessment | The disposition is `Ready` with no material unresolved choice |
| Verify change | Implementation is complete at a named snapshot with an accepted contract | Codebase Change Verification Report | The disposition is `Verified` with every material obligation evidenced |

Skip a stage when its work is already supplied by equivalent accepted evidence
or no material uncertainty or decision exists. A `Blocked` artifact returns only
the affected scope to the named earlier kind of work; it does not invalidate
unaffected accepted scope.

Use it around a non-trivial codebase change when current behavior, design
choices, functional scenarios, technical contracts, delivery steps, readiness,
or completion evidence need to be made explicit. Implementation itself occurs
outside the pack between readiness assessment and verification. The pack does
not modify code, estimate delivery, or create vendor-specific work items.

Install the complete workflow with:

```sh
axm install @craigsmitham/packs/codebase-change-workflow
```

For example, begin with a bug report to produce a research brief, use that brief
to build a cited current-state report, then use the report and original change
intent to workshop and accept a Codebase Design Record. Compile that accepted
record into a functional and technical Change Specification, then turn the
specification into a snapshot-validated Implementation Plan suitable for a fresh
coding agent or translation into a work management system. Assess that complete
case before implementation begins; after implementation, verify the accepted
obligations against the actual change and objective evidence.
