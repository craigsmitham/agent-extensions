---
id: 2026-08-20T155027Z-t6n2
subject: axm-cli-interactions
key: release-gate-blocked-by-bundled-authority
observed_at: "2026-08-20T15:50:27Z"
session: s9p4x2
kind: gap
status: open
---

**Expected:** The publishing guide's required `axm update @agentxm/skills/axm --ignore-release-age` step would update or confirm the workspace skill after confirming the CLI was current.
**Observed:** Its preview hard-blocked with `source-authority` because the official AXM skill had been installed from the CLI's bundled source by lint's earlier required compatibility recovery.
**Impact:** The documented release-gate command could not run; compatibility had to be established from the bundled skill identity and lint instead.
**Recovery:** Retain the AXM 0.27.13 bundled skill, verify it matches CLI 0.27.13 with lint, and continue the public-safety gate.
**Detected by:** Structured output from the targeted update preview.
**Observed factors:** Registry identity was `@craigsmitham`; CLI 0.27.13 was current; settings identify `workspace:@agentxm/skills/axm` with `origin: bundled`; update reported every effect unchanged.
**Hypothesis:** The publishing guide assumes Registry authority for the official skill and does not account for the supported bundled-recovery authority state.

Evidence: The update preview returned `ok: false`, `errorCode: conflict`, `blocker: source-authority`, and described the skill as workspace-authored; no mutation was planned or applied.
