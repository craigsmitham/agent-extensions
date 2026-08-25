---
id: 2026-08-25T173333Z-m6q4
subject: axm-cli-interactions
key: subagent-fallback-stale-projection
observed_at: "2026-08-25T17:33:33Z"
session: m6q4
kind: blocked
status: open
---

**Expected:** After `axm sync` materialized the workspace `researcher`
subagent as a Zed role-skill fallback, `axm sync --preview --fail-on-change`
should have reported the workspace as up to date.
**Observed:** Every convergence preview proposed the identical `researcher`
workspace materialization again with reason `stale-projection`.
**Impact:** The repository migration could not pass its required no-op sync
validation until AXM was corrected; repeated previews remained divergent.
**Recovery:** AXM was changed to recognize an exact AXM-owned subagent
role-skill fallback marker as a current per-agent projection. The same preview
then exited successfully with a no-op result.
**Detected by:** The post-migration convergence assertion.
**Observed factors:** The configured agent was Zed, which has a supported Skill
surface but no native subagent surface. The fallback existed under
`.agents/skills/researcher/SKILL.md`.
**Diagnostic evidence:** The proposed transition reported
`previous source=none`, `proposed source=workspace`, `previous version=none`,
`proposed version=0.0.1`, and `reason=stale-projection`.
**Hypothesis:** The sync observation path recognized only native subagent
origins and did not inspect the AXM-owned role-skill fallback.

Evidence: The fallback materialization completed and emitted `Degraded
subagent researcher to a role skill for zed`; the next convergence preview
proposed the same materialization. After AXM commit `b707fc185`, the unchanged
repository produced `plan-result-v3` with `outcome=no-op` and zero units.
