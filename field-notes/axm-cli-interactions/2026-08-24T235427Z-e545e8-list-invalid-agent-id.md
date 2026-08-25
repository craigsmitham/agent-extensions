---
id: 2026-08-24T235427Z-e545e8
subject: axm-cli-interactions
key: list-invalid-agent-id
observed_at: "2026-08-24T23:54:27Z"
session: a29d2849
kind: gap
status: open
---

**Expected:** `axm list --json` and `axm list --outdated --json` would return inventory documents for each discovered AXM workspace.
**Observed:** Both commands rejected one external checkout because `.axm/settings.json` contained `github-copilot` at `agents.6`, which the current settings schema does not accept.
**Impact:** One of 17 discovered AXM workspaces could not participate in the machine-wide inventory and required direct settings inspection. The elapsed delay was not measured.
**Recovery:** The inventory continued for the 16 valid workspaces. Direct inspection showed that the rejected settings file declared agents only and no extensions, so it was not an update target; the broader task remained in progress.
**Detected by:** The machine-wide `axm list` inventory loop.
**Observed factors:** AXM CLI version `0.27.17`; both list surfaces returned the same fixed JSON error envelope; the affected settings file contained only an `agents` array.
**Diagnostic evidence:** `ok=false`; code `validation`; title `Invalid Request`; cause tag `SettingsDecodeError`; cause message `agents.6: Expected ConfigurableAgentId`; suggested recovery `Edit the settings file to fix the invalid value, then re-run.`; process exit status unavailable — output was not retained.
**Hypothesis:** The checkout retains an agent identifier accepted by an earlier AXM catalog but no longer recognized by the current CLI.

Evidence: The complete primary JSON error envelopes and separate NDJSON diagnostics were retained for both commands. No credentials or opaque response bodies were present.
