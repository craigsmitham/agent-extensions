---
id: 2026-09-11T003627Z-a47d
subject: axm-cli-interactions
key: sync-selector-shape
observed_at: "2026-09-11T00:36:27.232049+00:00"
session: devops-docs-01a08dcc
kind: gap
status: open
---

**Expected:** The type-qualified `skills/devops-docs` identity shown in local workspace inventory would select the authored skill for scoped sync.
**Observed:** `axm sync skills/devops-docs --preview --fail-on-change --json` failed with no desired nodes matched; the FQN selector succeeded.
**Impact:** One failed read-only preview and one corrected preview were needed; elapsed cost not measured.
**Recovery:** `axm sync @craigsmitham/skills/devops-docs --preview --fail-on-change --json` returned no-op, exit 0.
**Detected by:** Structured sync-preflight failure.
**Observed factors:** AXM 0.28.12; the package had just been created by AXM and was configured as a workspace skill.
**Diagnostic evidence:** Failed result `ok: false`, `code: not_found`, title `Not Found`, detail `No desired extension nodes matched skills/devops-docs`; failed process exit unavailable — output was grouped with a subsequent successful help command. Corrected preview returned `ok: true`, contract `plan-result-v3`, outcome `no-op`, exit 0. No mutation was rerun.
**Hypothesis:** unknown
