---
id: 2026-08-17T135416Z-25a95fbc
subject: axm-cli-interactions
key: whoami-expired-token-exit-contract
observed_at: "2026-08-17T13:54:16Z"
session: 0d115892
kind: gap
status: open
---

**Expected:** The AXM skill's registry-identity preflight says an unauthenticated `axm whoami --json` returns exit 13 (`auth_required`), which the wrapper may treat as an expected probe result.
**Observed:** With an expired stored token, `axm whoami --json` returned an `auth` error envelope for HTTP 401 and exit 4.
**Impact:** The documented portable wrapper propagated the result and stopped the combined preflight command; publication preparation now needs an explicit device-code login. Delay was not measured.
**Recovery:** Local work continued without publishing; registry authentication remains pending.
**Detected by:** The command's JSON output and captured shell exit status.
**Observed factors:** AXM skill metadata declares CLI 0.27.5; the registry response said the token was invalid or expired.
**Hypothesis:** The documented expected exit covers missing authentication but not an expired credential that reaches the server.
**Suggests:** Document the expired-token exit separately or normalize both signed-out states to the advertised `auth_required` contract.

Evidence: `axm whoami --json` returned HTTP 401 detail `Invalid or expired token.`, error code `auth`, and shell exit status 4 on 2026-08-17.
