---
id: 2026-09-09T174310Z-r7c2
subject: axm-cli-interactions
key: authored-roots-unowned-workspace-lint
observed_at: "2026-09-09T17:43:10.266274+00:00"
session: release-r7c2
kind: gap
status: open
---

**Expected:** The release safety gate recognizes configured workspace-authored skill directories as canonical packages.
**Observed:** AXM 0.28.12 workspace lint reports nine authored skills as unowned agent artifacts while sync preview reports no-op with zero warnings.
**Impact:** The workspace safety gate exited 1 before remaining checks; release preparation required the documented Git-index validation route. Delay not measured.
**Recovery:** Preserved authored packages and selected the complete Git-index safety gate used by the pre-commit hook; its result is reported with the release.
**Detected by:** Full lint JSON and safety-gate exit status.
**Observed factors:** Bundled skill and CLI both 0.28.12; prior repository notes record the same discrepancy. Sync counts total 0, blocked 0, failed 0.
**Diagnostic evidence:** Initial lint exit 0; summary errors 0, warnings 9, infos 0, exitCategory warnings. All findings have ruleId workspace/managed-file-unowned, severity warning, paths ./skills/<name>. Workspace safety gate exit 1. No unfamiliar artifact was overwritten or removed.
**Hypothesis:** Workspace artifact discovery may classify authored skill roots as agent projection directories.
