---
id: 2026-08-21T154313Z-w5n2
subject: axm-cli-interactions
key: bundled-recovery-leaves-lock-drift
observed_at: "2026-08-21T15:43:13Z"
session: 01a024da-8386-7640-a9e3-92070912bb1f
kind: blocked
status: open
---

**Expected:** Installing the bundled official AXM skill would align desired settings, accepted resolution, canonical content, and strict lint as the recovery guidance describes.
**Observed:** Settings changed to `workspace:@agentxm/skills/axm` with bundled origin and the compatible skill materialized, but the registry `0.27.13` lock row remained; strict lint reported `workspace/skills-lockfile-aligned`, while `axm sync --preview` reported a no-op.
**Impact:** Strict validation remained blocked after one successful recovery apply and one sync preview.
**Recovery:** Preview AXM's uninstall/reinstall lifecycle so the CLI, rather than a manual lockfile edit, can rebuild coherent desired and accepted state; original task completion remained pending at capture time.
**Detected by:** `axm lint --strict --json`, followed by `axm sync --preview --json --non-interactive`.
**Observed factors:** CLI and bundled skill both reported `0.27.15`; settings desired a workspace bundled source; the lockfile still resolved Registry version `0.27.13`.
**Hypothesis:** Bundled recovery changed desired authority without pruning the superseded Registry resolution.

Evidence: Lint reported `Skill 'axm' has an accepted resolution but is not desired`; sync returned `outcome: no-op` with zero steps.
