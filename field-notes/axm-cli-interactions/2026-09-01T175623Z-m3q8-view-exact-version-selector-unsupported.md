---
id: 2026-09-01T175623Z-m3q8
subject: axm-cli-interactions
key: view-exact-version-selector-unsupported
observed_at: "2026-09-01T17:56:23Z"
session: 01a05abb-9d2a-75e1-91b9-5d7f5fe344fb
kind: workaround
status: open
---

**Expected:** After publishing an immutable extension version, the required
exact-version Registry readback could use the published selector
`@craigsmitham/knowledge/software-engineering@2.2.0` with `axm view`.
**Observed:** `axm view
@craigsmitham/knowledge/software-engineering@2.2.0 --json` exited 3 with
`not_found`, even though the immediately preceding publish reported that exact
version as successful.
**Impact:** Registry verification required a different metadata query and one
additional read-only command; elapsed impact was not measured.
**Recovery:** Query the extension's supported `versions` field and verify that
`2.2.0` is present, while retaining the successful publish result and archive
integrity as mutation evidence.
**Detected by:** The complete structured `axm view` result and nonzero process
exit status.
**Observed factors:** AXM CLI version 0.28.2; default Registry `agentxm`; the
publish result identified version `2.2.0`, status `success`, and a deterministic
SHA-512 archive integrity; no mutation was retried.
**Diagnostic evidence:** Exit status 3; error code `not_found`; detail `No
extension named "@craigsmitham/knowledge/software-engineering@2.2.0" was
found`; request or correlation ID was not supplied.
**Hypothesis:** `axm view` resolves only extension identities and exposes
versions through fields rather than accepting an exact-version selector.
**Suggests:** Document an exact-version Registry readback command or add
version-selector support to `axm view`.

Evidence: The exact version was successfully uploaded immediately before the
failed readback attempt; only the metadata selector form changed.
