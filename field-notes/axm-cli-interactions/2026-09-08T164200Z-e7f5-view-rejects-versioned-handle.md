---
id: 2026-09-08T164200Z-e7f5
subject: axm-cli-interactions
key: view-rejects-versioned-handle
observed_at: "2026-09-08T16:42:00Z"
session: e7e59242-8a18-40da-b6ae-f081325bf2f3
kind: workaround
status: open
---

**Expected:** After `axm publish @craigsmitham/skills/spot-spew` reported
`published: 1`, the AXM skill requires an exact-version Registry readback, so
`axm view @craigsmitham/skills/spot-spew@0.0.1` was expected to return the
published metadata for that version.
**Observed:** The command failed with `✖ No extension named
"@craigsmitham/skills/spot-spew@0.0.1" was found (not_found)` and the guidance
"Check the name, pass --type, or use a fully-qualified name." The name was
already fully qualified; `axm view --help` shows `<extension>` as
`@owner/skills/name` with no version suffix, unlike `axm uninstall`, whose
argument is documented as `<extension[@version]>`.
**Impact:** One failed command plus one help read before readback succeeded;
the verification step was completed with `axm view <fqn> versions`, `latest`,
and `visibility` instead. Elapsed cost not measured. The publish itself was
unaffected.
**Recovery:** `axm view @craigsmitham/skills/spot-spew versions` returned
`0.0.1`, `latest` returned `0.0.1`, and `visibility` returned `public`. The
task completed.
**Detected by:** Non-zero exit and the `not_found` result line from the
readback command.
**Observed factors:** axm 0.28.11 (with `AXM_UPDATE_AVAILABLE latest=0.28.12`
banner); registry `https://registry.agentxm.ai`; workspace
`craigsmitham/agent-extensions`; the extension had just been published in the
same session.
**Diagnostic evidence:** tool version 0.28.11; command surface `axm view`;
affected artifact `@craigsmitham/skills/spot-spew@0.0.1`; error class
`not_found`; request or correlation ID not supplied; retryability not supplied;
recovery command `axm view @craigsmitham/skills/spot-spew versions`.
**Hypothesis:** unknown — the `view` argument parser may treat the whole
`name@version` string as an extension name rather than splitting the version,
but this was not investigated.
**Suggests:** The suggestion is not grounded enough to record beyond noting
that `view` and `uninstall` document their extension argument differently.

Evidence: the failing command, its `not_found` message and next-step guidance,
the `axm view --help` argument spec, and the three succeeding field reads used
instead.
