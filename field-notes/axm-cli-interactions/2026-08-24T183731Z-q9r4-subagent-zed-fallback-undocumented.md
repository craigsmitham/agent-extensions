---
id: 2026-08-24T183731Z-q9r4
subject: axm-cli-interactions
key: subagent-zed-fallback-undocumented
observed_at: "2026-08-24T18:37:31Z"
session: sess-q9r4
kind: gap
status: open
---

**Expected:** `axm help subagents` should describe projection behavior for every configured target that `axm subagents new` may reconcile.
**Observed:** Creating `@craigsmitham/subagents/researcher` reported `Degraded subagent researcher to a role skill for zed`, while the Subagents help topic did not describe a Zed role-skill fallback.
**Impact:** The authoring run encountered an unanticipated target-specific projection; no retry was required and the implementation continued.
**Recovery:** Treated the CLI warning as the observed projection result and continued with portable source authoring.
**Detected by:** Warning emitted by `axm subagents new researcher --owner @craigsmitham --yes --json --non-interactive`.
**Observed factors:** Project agents include Zed; AXM version is 0.27.15; the subagent package was created successfully.
**Hypothesis:** The help topic omits a supported fallback adapter for hosts without native subagents.
**Suggests:** Document target-specific fallback projections in `axm help subagents`.

Evidence: The command returned `ok: true`, `outcome: applied`, and the warning `Degraded subagent researcher to a role skill for zed`.
