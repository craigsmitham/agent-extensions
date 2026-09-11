---
id: 2026-09-11T022435Z-2d2e
subject: axm-cli-interactions
key: release-guide-bundled-skill-update
observed_at: "2026-09-11T02:24:35.752992+00:00"
session: 000812d1
kind: gap
status: open
---

**Expected:** docs/publishing.md directs axm update @agentxm/skills/axm --ignore-release-age after upgrading the CLI.
**Observed:** The command exited 6 because this workspace uses the AXM skill embedded in the executable, which cannot advance from the Registry.
**Impact:** The documented command failed; one recovery command was needed.
**Recovery:** axm skills install @agentxm/skills/axm --bundled exited 0 with outcome applied. CLI and bundled skill are 0.28.12; no tracked file differences resulted.
**Detected by:** Release preflight command results.
**Observed factors:** Public extension workspace, AXM 0.28.12, bundled official skill, devops-docs 0.5.1 release preparation.
**Diagnostic evidence:** Update: ok false, outcome blocked, class policy-excluded, subject @agentxm/skills/axm, phase planning, causeCode conflict, reference bundled-source. Upgrade had already exited 0 with disposition already-current.
**Hypothesis:** unknown
