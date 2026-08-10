# Behavioral evaluation cases

Run each case in a fresh agent context with only `src/SKILL.md` and the prompt.
Withhold expected outputs and assertions until grading. The machine-readable
suite is `evals.json`; this file is its human-readable review companion.

## Execution cases

### 1. Accepted design with an unresolved product policy

An accepted asynchronous bulk-export design omits what a second request for the
same account observes while an export is active.

Expected: `Blocked`, classified `Needs design`, with the duplicate-request policy
named precisely and no implied choice in dependent behavior, state, interface,
or slice content.

### 2. Complete design with vertical behavior

A complete accepted invoice-preview design supplies outcomes, behaviors,
decisions, contracts, failures, compatibility, verification criteria, and
matching current evidence across an endpoint, application service, calculator,
and renderer.

Expected: a `Draft` preserving source IDs, defining concrete scenarios and
contract IDs, distinguishing accepted rationale from future verification, and
outlining cross-boundary vertical slices without implementation tasks.

### 3. Material drift after design acceptance

An event schema and invariant used by an accepted decision changed between the
research, design, and specification identities, with no refreshed evidence.

Expected: `Blocked`, classified `Needs research`, with the three identities and
affected boundaries distinguished; the stale decision and its dependents are not
silently rebound.

### 4. Direct evidence without Git provenance

An accepted retry design and current-state architecture export are identified by
name, version, approver, and capture time, but no repository checkout exists.

Expected: proceed to `Draft` using those identities, state their limits, and
invent no repository, branch, commit, or worktree metadata.

### 5. Harmless drift

The repository advanced after design acceptance, but supplied evidence shows the
only change is to an unrelated marketing page.

Expected: record the scoped basis for irrelevance and continue to `Draft` without
demanding refreshed research or weakening the accepted contract.

### 6. Explicit acceptance transition

A reviewer explicitly approves a complete draft against its recorded evidence
identity and names the accepted scope and time.

Expected: change the status to `Accepted`, record the exact acceptance boundary,
permit planning handoff, and neither generate a plan nor alter the contract.

### 7. Structural-only decision and justified non-applicability

An accepted internal registry rename preserves all observable behavior and has
equivalence evidence.

Expected: represent the structural rule with a `C<n>` ID, use a reasoned `N/A`
for functional coverage rather than inventing behavior, and retain an explicit
equivalence verification obligation.

### 8. Specification request that also asks for planning details

A complete accepted design is accompanied by a request for file-by-file tasks,
shell commands, estimates, and assignees.

Expected: return only a `Draft` specification, omit planning artifacts, and state
that planning begins only after explicit specification acceptance.

## Pass condition

The suite passes when the skill compiles accepted choices into complete,
traceable contracts; distinguishes accepted sources from future verification;
uses the strongest available evidence identity without invented Git provenance;
blocks rather than inventing consequential decisions; handles irrelevant and
material drift proportionately; permits justified traceability non-applicability;
and enforces the draft, acceptance, and planning boundary.
