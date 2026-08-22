---
id: 2026-08-21T154443Z-c4t9
subject: axm-cli-interactions
key: isolated-whoami-retains-expired-credential
observed_at: "2026-08-21T15:44:43Z"
session: 01a024da-8386-7640-a9e3-92070912bb1f
kind: gap
status: open
---

**Expected:** Setting `AXM_USER_HOME` to a new temporary directory would relocate credentials and make `axm whoami --json` report the documented signed-out state.
**Observed:** `whoami` still reported the same invalid or expired stored token, and its process status did not distinguish the failed JSON envelope in the calling shell; the following guarded preview did not run.
**Impact:** One attempted signed-out preflight was unusable and the public Registry install had to be previewed directly.
**Recovery:** Ran the public install preview and apply under the isolated `AXM_USER_HOME`; both resolved the public package successfully without changing the user's stored credential.
**Detected by:** Guarded shell execution of `AXM_USER_HOME=<temporary directory> axm whoami --json` before the Registry install preview.
**Observed factors:** No `AXM_TOKEN`, `AXM_TOKEN_FILE`, or `AXM_USER_HOME` variable was present in the parent environment; AXM reported restricted-file credential fallback.
**Hypothesis:** The restricted credential fallback or `whoami` exit behavior does not honor the documented user-home isolation in this environment.

Evidence: The isolated `whoami` output remained `Invalid or expired token`; the same isolated process configuration successfully previewed and installed public skill version `0.27.15`.
