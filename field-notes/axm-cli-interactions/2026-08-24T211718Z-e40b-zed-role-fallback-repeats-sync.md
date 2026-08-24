---
id: 2026-08-24T211718Z-e40b
subject: axm-cli-interactions
key: zed-role-fallback-repeats-sync
observed_at: "2026-08-24T21:17:18Z"
session: E40B630B-6CBB-4433-B0DB-7EFC3F64027C
kind: gap
status: open
---

**Expected:** Synchronizing changed Field Notes rule and knowledge content would reconcile only stale instruction and discovery projections.
**Observed:** The preview also proposed the unchanged `researcher` subagent from `previous source=none` with reason `stale-projection`; apply re-synced it and emitted the Zed role-skill degradation warning.
**Impact:** One unrelated projection was re-applied during the required workspace sync; elapsed cost was not measured and the original rollout continued.
**Recovery:** No separate recovery was required because the sync completed successfully; continue validating the authorized Field Notes changes independently.
**Detected by:** Structured preview and apply results from `axm sync`.
**Observed factors:** The same workspace already contains a Zed role-skill fallback for the researcher subagent and an earlier independent occurrence reports that this projection does not converge.
**Diagnostic evidence:** AXM CLI `0.27.17`; preview candidate `907b441250f80fb0270b930311fecc71a663acec511f41b22d37eecf3aa5f6b8`; result `ok: true`, outcome `applied`, three applied steps, warning `Degraded subagent researcher to a role skill for zed`; external request ID not applicable.
**Hypothesis:** The sync observer still does not recognize its generated Zed fallback as satisfying the researcher projection.

Evidence: The preview labeled researcher `reason=stale-projection` with no previous source, and the immediately following apply reported `Synced subagent researcher` while the Field Notes instruction and Knowledge projections also succeeded.
