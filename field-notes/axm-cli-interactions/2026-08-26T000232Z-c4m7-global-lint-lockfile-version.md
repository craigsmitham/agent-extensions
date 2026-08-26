---
id: 2026-08-26T000232Z-c4m7
subject: axm-cli-interactions
key: global-lint-lockfile-version
observed_at: "2026-08-26T00:02:32Z"
session: s8k2q
kind: workaround
status: open
---

**Expected:** `axm lint --json` should inspect the workspace and report AXM skill compatibility before editing the project-authored Knowledge bundle.
**Observed:** The command exited during workspace validation because the installed CLI expected lockfile version 5.
**Impact:** Workspace-wide AXM lint and its compatibility result were unavailable; package verification required scoped and format-specific validators.
**Recovery:** `axm knowledge lint --path ./knowledge/gen-stack --json` completed successfully, and the OKF validator independently confirmed the bundle; the documentation change could continue.
**Detected by:** The global lint command returned exit status 9 with structured validation output.
**Observed factors:** `axm --version` returned `0.27.18`; the active AXM skill declares CLI compatibility `>=0.28.0 <0.29.0`; the affected workspace lockfile was `axm-lock.yaml`.
**Diagnostic evidence:** Exit status: `9`. Code: `validation`. Title: `Invalid Request`. Detail: `Workspace lockfile at '/Users/craig/Code/craigsmitham/agent-extensions/axm-lock.yaml' is invalid: lockfileVersion: Expected 5`.
**Hypothesis:** The installed CLI is older than the workspace lockfile format.

Evidence: The installed CLI version, skill compatibility declaration, command, exit status, structured error fields, scoped recovery command, and successful recovery result are retained above.
