---
id: 2026-08-26T114206Z-r9v3
subject: axm-cli-interactions
key: sync-preview-applied-projection
observed_at: "2026-08-26T11:42:06Z"
session: codex-j6p2
kind: gap
status: open
---

**Expected:** `axm sync --preview --fail-on-change --json` would report the
materialization plan without writing files, as stated by `axm sync --help`.
**Observed:** The command restored the previously missing AXM-owned root
`AGENTS.md` projection. A repeated preview reported `mode: apply` and `no-op`
because the projection was then current.
**Impact:** The verification step made one unplanned generated-file change and
required inspection to distinguish it from authored documentation changes.
**Recovery:** Confirmed the projection diff contains only the updated Gen Stack
bundle description and continued validation without another mutation.
**Detected by:** Git status, the projection diff, and the file modification
time after the first preview.
**Observed factors:** AXM CLI `0.28.1`; compatible AXM skill `0.28.1`; project
workspace; `--preview`, `--fail-on-change`, and `--json`; one missing generated
projection before the command.
**Diagnostic evidence:** First command process status and final structured
result are unavailable because its output was not retained after context
compaction. The repeated command exited `0`, returned `ok: true`, contract
`plan-result-v3`, outcome `no-op`, mode `apply`, and zero planned units.
**Hypothesis:** The preview flag was not reflected in the resolved sync mode.

Evidence: `axm sync --help` says preview does not apply changes. The root
projection modification time follows the canonical manifest edit, and its sole
diff updates the Gen Stack description to match that manifest.
