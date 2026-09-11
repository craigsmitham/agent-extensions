---
id: 2026-09-11T173236Z-4ad4
subject: axm-cli-interactions
key: authored-roots-unowned-workspace-lint
observed_at: "2026-09-11T17:32:36.646463+00:00"
session: 01a09180-7995-7971-8c44-c53ec4e5ca0c
kind: workaround
status: open
---

**Expected:** The publishing guide's workspace safety gate can validate a converged workspace with configured authored skills.
**Observed:** AXM 0.28.12 reports ten `workspace/managed-file-unowned` warnings on authored `skills/*` roots. The workspace safety gate exits 1 at strict lint, while sync preview reports no-op.
**Impact:** Effect knowledge 1.0.4 release preparation requires separate validation of the exact staged tree. Elapsed cost not measured.
**Recovery:** Preserved authored packages and their projection symlinks; continuing with the documented Git-index safety gate. Publication has not yet been attempted.
**Detected by:** Release preflight results.
**Observed factors:** CLI and bundled AXM skill both 0.28.12; the authored roots are configured as workspace sources. Author-docs projection symlinks point to its canonical src directory.
**Diagnostic evidence:** Initial lint exit 0, ok true, errors 0, warnings 10; all findings use ruleId `workspace/managed-file-unowned`. Workspace safety gate exit 1. Sync preview exit 0, outcome no-op, total 0, failed 0, blocked 0.
**Hypothesis:** unknown
