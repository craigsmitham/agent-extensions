# Codebase Change Workflow

Turn a bug report, feature idea, or change request into an evidence-grounded
functional and technical design plus a traceable implementation plan. The pack
preserves evidence provenance and checks relevant code, configuration,
dependency, deployment, and runtime drift across five distinct stages:

1. Frame neutral current-state research questions.
2. Investigate the current system and produce an evidence-backed technical map.
3. Workshop consequential functional and technical decisions with a developer.
4. Compile the accepted design into an implementation-constraining specification.
5. Plan independently verifiable vertical slices and concrete work items.

| Stage | Start when | Produces | Continue when |
| --- | --- | --- | --- |
| Frame research | Material current-state uncertainty remains | Codebase Research Brief | The brief is `Ready` and any required review is accepted |
| Conduct research | Neutral questions and evidence boundaries are available | Codebase Research Report | Every question has a status and evidence trail |
| Workshop design | Change intent and sufficient current-state evidence are available | Codebase Design Record | The design is explicitly `Accepted` against a named evidence identity |
| Specify change | The accepted design and supporting evidence are current | Codebase Change Specification | The specification is explicitly `Accepted` |
| Plan change | An accepted specification and verifiable codebase snapshot are available | Implementation Plan | The plan is `Ready` with complete traceability and completion evidence |

Skip a stage when its work is already supplied by equivalent accepted evidence
or no material uncertainty or decision exists. A `Blocked` artifact returns only
the affected scope to the named earlier kind of work; it does not invalidate
unaffected accepted scope.

Use it before implementing a non-trivial codebase change when current behavior,
design choices, functional scenarios, technical contracts, or delivery steps
need to be made explicit. It does not modify code, estimate delivery, or create
vendor-specific work items.

Install the complete workflow with:

```sh
axm install @craigsmitham/packs/codebase-change-workflow
```

For example, begin with a bug report to produce a research brief, use that brief
to build a cited current-state report, then use the report and original change
intent to workshop and accept a Codebase Design Record. Compile that accepted
record into a functional and technical Change Specification, then turn the
specification into a snapshot-validated Implementation Plan suitable for a fresh
coding agent or translation into a work management system.
