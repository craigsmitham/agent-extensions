---
id: 2026-09-11T022435Z-18a3
subject: axm-cli-interactions
key: authored-ownership-warning
observed_at: "2026-09-11T02:24:35.752992+00:00"
session: 000812d1
kind: workaround
status: open
---

**Expected:** Workspace lint and current projection inspection should agree on authored package ownership.
**Observed:** AXM 0.28.12 reports ten workspace/managed-file-unowned warnings at authored skills/* roots; skills show devops-docs reports workspace source and all five agent projections current. Sync preview reports no-op; lint --fix leaves the same warnings.
**Impact:** Workspace safety gate exited 1, requiring separate Git-index validation; elapsed cost not measured.
**Recovery:** Preserved authored content and projections. Git-index safety validation is running; publication has not yet been attempted.
**Detected by:** Release preflight command results.
**Observed factors:** Public extension workspace, AXM 0.28.12, bundled official skill, devops-docs 0.5.1 release preparation.
**Diagnostic evidence:** Initial lint exit 0 with errors 0 and warnings 10; lint --fix exit 0 with the same findings. Workspace safety gate exit 1. Sync preview exit 0, outcome no-op, failed 0, blocked 0.
**Hypothesis:** unknown
