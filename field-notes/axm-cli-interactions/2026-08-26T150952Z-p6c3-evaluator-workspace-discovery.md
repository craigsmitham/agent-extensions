---
id: 2026-08-26T150952Z-p6c3
subject: axm-cli-interactions
key: evaluator-workspace-discovery
observed_at: "2026-08-26T15:09:52Z"
session: codex-v8m2
kind: workaround
status: open
---

**Expected:** The repository-mandated `agent-skill-eval.mjs validate` command would discover and validate every workspace-authored Agent Skill suite, including the three new Gen Stack skill packages.
**Observed:** The validator reported that no workspace-authored Agent Skill packages were discovered and required `--package` explicitly.
**Impact:** Suite validation stopped before validating the changed Gen Stack packages and required explicit per-package reruns; elapsed impact was not measured.
**Recovery:** Rerun the trusted validator once for each changed package with its explicit `--package` path; the documentation cleanup remained in progress.
**Detected by:** The repository-mandated evaluator validation command exited nonzero.
**Observed factors:** The three Gen Stack skill package directories were untracked in Git during an in-progress package migration; evaluator version 0.2.2 was installed and enabled according to `axm list --json`.
**Diagnostic evidence:** Exit status 2; output: `No workspace-authored Agent Skill packages were discovered; pass --package explicitly.`
**Hypothesis:** Default workspace discovery relies on tracked package paths and omits new untracked workspace-authored skills.

Evidence: The exact command result, exit status, affected package state, and explicit recovery are preserved above.
