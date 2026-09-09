---
id: 2026-09-08T221039Z-b4k2
subject: axm-cli-interactions
key: view-rejects-versioned-handle
observed_at: "2026-09-08T22:10:39Z"
session: 01BJvgpqyTJjsDzUYBVeWEct
kind: workaround
status: open
---

**Expected:** After `axm publish @craigsmitham/skills/spot-spew` reported
`Published @craigsmitham/skills/spot-spew@0.1.0`, the AXM skill requires an
exact-version Registry readback, so
`axm view @craigsmitham/skills/spot-spew@0.1.0` was expected to return the
published metadata for that version.
**Observed:** The command failed with `✖ No extension named
"@craigsmitham/skills/spot-spew@0.1.0" was found (not_found)` and the guidance
"Check the name, pass --type, or use a fully-qualified name." The name was
already fully qualified. `axm view --help` documents `<extension>` as
`@owner/skills/name` with no version suffix, while `axm update --help` and
`axm install --help` document theirs as `<extension[@version]>`.
**Impact:** One failed command plus one help read before the readback
succeeded; the exact-version verification was completed with
`axm view <fqn> versions`, `latest`, and `description` instead. This is a
second occurrence of the same surface and symptom, recorded earlier today under
key `view-rejects-versioned-handle` in a different session. Elapsed cost not
measured. The publish itself was unaffected.
**Recovery:** `axm view @craigsmitham/skills/spot-spew versions` returned
`0.1.0` and `0.0.1`, `latest` returned `0.1.0`, and `description`
returned the republished text. The task completed.
**Detected by:** The `not_found` result line and non-zero outcome from the
readback command.
**Observed factors:** axm 0.28.11 (with `AXM_UPDATE_AVAILABLE latest=0.28.12`
banner); registry `https://registry.agentxm.ai`; workspace
`craigsmitham/agent-extensions`; the extension had just been published in the
same session.
**Diagnostic evidence:** tool version 0.28.11; command surface `axm view`;
affected artifact `@craigsmitham/skills/spot-spew@0.1.0`; error class
`not_found`; request or correlation ID not supplied; retryability not
supplied; recovery command `axm view @craigsmitham/skills/spot-spew versions`.
**Hypothesis:** unknown — not investigated.
**Suggests:** omitted; the prior note already records the `view` versus
`install`/`update` argument-spec difference.

Evidence: the failing command, its `not_found` message and next-step guidance,
the `axm view --help` argument spec, and the three succeeding field reads used
instead.
