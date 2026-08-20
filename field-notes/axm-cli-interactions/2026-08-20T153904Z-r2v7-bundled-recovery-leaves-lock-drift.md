---
id: 2026-08-20T153904Z-r2v7
subject: axm-cli-interactions
key: bundled-recovery-leaves-lock-drift
observed_at: "2026-08-20T15:39:04Z"
session: s9p4x2
kind: gap
status: open
---

**Expected:** Following lint's complete `install-bundled-skill` recovery plan would leave AXM's desired state and accepted resolution aligned for the official skill.
**Observed:** The bundled 0.27.13 skill installed successfully and became compatible, but the required follow-up lint reported `workspace/skills-lockfile-aligned`: Skill `axm` has an accepted resolution but is not desired.
**Impact:** The prescribed compatibility recovery required another reconciliation step before the original bundle removal could continue.
**Recovery:** In progress; compatibility is restored and accepted-resolution drift remains to reconcile.
**Detected by:** `axm lint --json` immediately after successful bundled installation.
**Observed factors:** AXM CLI and bundled skill are both 0.27.13; settings changed the skill source from Registry to `workspace:` with `origin: bundled`; lint still observed the prior accepted resolution.
**Hypothesis:** Bundled skill recovery changes desired source authority without deleting the obsolete Registry lock row.

Evidence: Bundled install reported `outcome: applied`; follow-up lint reported compatibility `status: compatible` and one `workspace/skills-lockfile-aligned` error for `axm`.
