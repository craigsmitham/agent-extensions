---
id: 2026-08-22T002454Z-r8v2
subject: axm-cli-interactions
key: registry-token-expired
observed_at: "2026-08-22T00:24:54Z"
session: s-k7p3
kind: workaround
status: open
---

**Expected:** Registry identity preflight would confirm the saved publishing
identity before an authored-catalog preview.
**Observed:** `axm whoami --json` returned an authentication error stating that
the saved token was invalid or expired.
**Impact:** Publishing preflight paused for one browser authorization flow;
elapsed time was not measured.
**Recovery:** Ran the supported `axm login --yes --json` flow, authorized the
CLI in the already signed-in AgentXM browser session, and resumed as
`@craigsmitham`.
**Detected by:** The required registry identity check before publication.
**Observed factors:** AXM 0.27.15 used its restricted credential-file fallback
because the OS keychain was unavailable.
**Hypothesis:** The previously cached refresh credential had expired or been
invalidated.

Evidence: the first identity request returned HTTP 401; the login command then
reported `status: logged-in`, registry host `registry.agentxm.ai`, and handle
`@craigsmitham`.
