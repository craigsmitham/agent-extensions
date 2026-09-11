---
id: 2026-09-11T021144Z-a7f2
subject: axm-cli-interactions
key: authored-ownership-warning
observed_at: "2026-09-11T02:11:44Z"
session: devops-fallback-a7f2
kind: blocked
status: open
---

**Expected:** Workspace-authored packages and current projections pass ownership checks.
**Observed:** AXM 0.28.12 lint reports ten `workspace/managed-file-unowned` warnings at authored `skills/*` roots, including `skills/devops-docs`. Its show result identifies devops-docs as workspace-authored with all five agent projections current; scoped sync preview reports no-op.
**Impact:** The workspace public-safety gate exits 1 before its remaining checks.
**Recovery:** Unresolved at capture; checking the Git-index gate next.
**Detected by:** Release preflight.
**Observed factors:** `axm.json` declares the packages as workspace sources; the Codex devops-docs projection is a symlink to canonical `src/`.
**Diagnostic evidence:** `axm lint --json` exits 0 with ok=true, errors=0, warnings=10, compatibility=compatible; strict lint in the gate exits 1. Scoped sync exits 0, outcome=no-op.
**Hypothesis:** unknown
