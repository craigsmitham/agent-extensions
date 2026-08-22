---
id: 2026-08-21T154215Z-r3v8
subject: axm-cli-interactions
key: registry-preflight-expired-token
observed_at: "2026-08-21T15:42:15Z"
session: 01a024da-8386-7640-a9e3-92070912bb1f
kind: workaround
status: open
---

**Expected:** The required `axm whoami --json` preflight would establish either an authenticated identity or the documented signed-out state before a public official-skill update.
**Observed:** The preflight returned `Unauthorized` because the stored token was invalid or expired.
**Impact:** Registry-backed recovery could not proceed without changing authentication state, so one alternate preview/apply path was required.
**Recovery:** Left authentication unchanged and used `axm skills install @agentxm/skills/axm --bundled`, which installed the compatible official skill without Registry access; the original task continued.
**Detected by:** `axm whoami --json`.
**Observed factors:** AXM reported that the OS keychain was unavailable and it was using a restricted credential file; the Registry returned HTTP 401 with problem code `unauthorized`.
**Hypothesis:** A stored credential remained present after its Registry validity expired.

Evidence: The preflight returned `Invalid or expired token`; the bundled recovery preview and apply both completed successfully for `@agentxm/skills/axm`.
