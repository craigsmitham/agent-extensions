---
id: 2026-08-25T173655Z-v7n2
subject: axm-cli-interactions
key: evaluator-authored-root-discovery
observed_at: "2026-08-25T17:36:55Z"
session: m6q4
kind: workaround
status: open
---

**Expected:** The installed Agent Skill evaluator's repository-wide `validate`
command should have discovered workspace-authored skills after their canonical
packages moved to root `skills/<name>` directories.
**Observed:** Validation exited unsuccessfully with `No workspace-authored
Agent Skill packages were discovered; pass --package explicitly.`
**Impact:** The public-safety gate could not validate any of the repository's
authored Agent Skill suites through auto-discovery.
**Recovery:** The gate enumerated root `skills/*/skill.json` manifests and
invoked the evaluator once per explicit `--package` path.
**Detected by:** The workspace public-safety check after the AXM layout
migration.
**Observed factors:** AXM lint and sync convergence had already passed. The
evaluator was acquired from Registry source `agentxm` at version `0.2.2`.
**Diagnostic evidence:** The evaluator emitted its explicit-package recovery
instruction and returned exit status 1.
**Hypothesis:** The installed evaluator's auto-discovery still searches the
retired authored owner-root layout.

Evidence: Root-authored skills existed under `skills/`, each with `skill.json`,
`src/SKILL.md`, and versioned evaluation source; repository-wide discovery
returned zero packages.
