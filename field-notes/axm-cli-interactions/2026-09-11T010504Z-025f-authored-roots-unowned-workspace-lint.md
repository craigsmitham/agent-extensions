---
id: 2026-09-11T010504Z-025f
subject: axm-cli-interactions
key: authored-roots-unowned-workspace-lint
observed_at: "2026-09-11T01:05:04.463803+00:00"
session: release-docs-0131
kind: workaround
status: open
---

**Expected:** Release preflight recognizes configured workspace-authored skill roots as canonical packages.
**Observed:** AXM 0.28.12 workspace lint reported ten authored skill directories as unowned agent artifacts; the workspace safety gate exited 1 while sync preview reported no-op.
**Impact:** Workspace validation stopped before remaining checks. Required the repository's Git-index safety gate; delay not measured.
**Recovery:** Preserved authored packages and selected the full Git-index validation used by the commit hook. Its result is reported with the release.
**Detected by:** Complete lint JSON and safety-gate process exit status.
**Observed factors:** CLI and bundled skill both 0.28.12 and compatible; docs is an enabled project workspace knowledge bundle. Prior repository notes document the same discrepancy.
**Diagnostic evidence:** Initial lint exit 0, ok true, errors 0, warnings 10, infos 0. All findings use workspace/managed-file-unowned at ./skills/<name>. Workspace safety gate exit 1; sync outcome no-op.
**Hypothesis:** unknown.
