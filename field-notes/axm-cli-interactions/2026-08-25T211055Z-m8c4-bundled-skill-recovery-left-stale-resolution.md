---
id: 2026-08-25T211055Z-m8c4
subject: axm-cli-interactions
key: bundled-skill-recovery-left-stale-resolution
observed_at: "2026-08-25T21:10:55Z"
session: s8f2n
kind: gap
status: open
---

**Expected:** Installing the compatible bundled AXM skill after the CLI reported an incompatible Registry skill would leave desired, accepted, canonical, and projected state reconcilable.
**Observed:** The bundled install updated the canonical skill and desired entry, but lint still reported the old Registry resolution as accepted but undesired and reported a materialization mismatch.
**Impact:** Release preflight required an exact uninstall followed by a fresh bundled install before ordinary projection sync could converge.
**Recovery:** Previewed and uninstalled only the `axm` skill, reinstalled the bundled `0.28.0` skill, synced the stale rules projection, then verified clean lint and a no-change sync preview.
**Detected by:** Required AXM lint after CLI and official-skill convergence.
**Observed factors:** AXM CLI `0.28.0`; previous accepted Registry skill `0.27.15`; bundled skill `0.28.0`; project lockfile version `6`.
**Diagnostic evidence:** Initial lint returned three errors: `materialization-mismatch`, `workspace/projections-current`, and `workspace/skills-lockfile-aligned`. Final lint returned zero findings and compatibility status `compatible`.
**Hypothesis:** Bundled recovery replaced canonical and desired state without retiring the prior accepted Registry resolution in the same transaction.

Evidence: Every mutation was previewed at the exact `axm` skill target. No unrelated extension was removed or reinstalled.
