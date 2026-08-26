---
id: 2026-08-26T114024Z-t4k8
subject: axm-cli-interactions
key: owned-projection-became-missing
observed_at: "2026-08-26T11:40:24Z"
session: codex-j6p2
kind: gap
status: open
---

**Expected:** `axm lint --json` would remain clean after editing only canonical
project-authored Knowledge and pack sources; the same required preflight had
returned zero findings earlier in this session.
**Observed:** Lint loaded the workspace but reported that the AXM-owned root
`AGENTS.md` projection was missing and identified every enabled Knowledge
bundle as an affected contributor.
**Impact:** Final AXM workspace validation cannot be reported clean in this
documentation task; package and OKF validation continued without repairing the
unrelated projection.
**Recovery:** Continued with canonical-source validation and a non-mutating AXM
sync preview. Projection reconciliation remains outside this task.
**Detected by:** Required AXM post-authoring workspace lint.
**Observed factors:** AXM CLI `0.28.1`; compatible AXM skill `0.28.1`; project
workspace; only canonical Knowledge, pack documentation, metadata, notices, and
field-note files were intentionally changed during this task.
**Diagnostic evidence:** Process exit status `1`; result `ok: false`; rule
`workspace/projections-current`; severity `error`; subject `.`; affected
projection `AGENTS.md`; summary contained one error and no warnings or infos.
**Hypothesis:** unknown

Evidence: The structured lint result loaded the workspace successfully, reported
compatible CLI and skill versions, and returned exactly one missing-projection
finding. No AXM mutation was attempted.
