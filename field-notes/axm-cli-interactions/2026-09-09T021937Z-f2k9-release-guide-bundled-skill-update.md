---
id: 2026-09-09T021937Z-f2k9
subject: axm-cli-interactions
key: release-guide-bundled-skill-update
observed_at: "2026-09-09T02:19:37Z"
session: maintenance-release-f2k9
kind: workaround
status: open
---

**Expected:** The publishing guide's `axm update @agentxm/skills/axm --ignore-release-age` refreshes the release-workflow skill.
**Observed:** AXM 0.28.12 rejected the command because the workspace uses its bundled skill.
**Impact:** One blocked update and an additional install command during release preflight; elapsed delay not measured.
**Recovery:** The suggested `axm skills install @agentxm/skills/axm --bundled --json` succeeded with one committed unit.
**Detected by:** CLI structured result and exit status.
**Observed factors:** CLI upgrade was already-current; initial lint reported compatible bundled skill 0.28.1.
**Diagnostic evidence:** Update exit 6, outcome `blocked`, class `policy-excluded`, causeCode `conflict`, reference `bundled-source`; settings, accepted resolution, canonical content, and projections reported unchanged. Recovery exit 0, outcome `applied`.
**Hypothesis:** Publishing instructions describe Registry-installed skills and omit the bundled-source case.
