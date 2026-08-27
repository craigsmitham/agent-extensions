---
id: 2026-08-27T144340Z-dbb02a
subject: axm-cli-interactions
key: exact-version-view
observed_at: "2026-08-27T14:43:40Z"
session: cf3619971650
kind: workaround
status: open
---

**Expected:** AXM live help would expose a read-only command for an exact-version
Registry readback after publication.
**Observed:** `axm view @craigsmitham/knowledge/gen-stack@0.19.0 --json
--non-interactive` exited `3` with code `not_found`; `axm help registry` also
exited `3` because that help topic does not exist. `axm view
@craigsmitham/knowledge/gen-stack versions --json --non-interactive` succeeded
and returned the published version list.
**Impact:** Two extra read-only commands were needed and exact-version release
verification had to use membership in the Registry version list; publication
was delayed but not blocked.
**Recovery:** Use the published version list and require the candidate version
to appear exactly; the release workflow continued.
**Detected by:** The exact-version `view` command returned a structured
`not_found` result during readback planning.
**Observed factors:** AXM CLI `0.28.1`; project workspace; public Knowledge
extension `@craigsmitham/knowledge/gen-stack`; Registry `agentxm`.
**Diagnostic evidence:** Both failed commands exited `3`; the exact-version
view reported code `not_found` and suggested checking the name or passing
`--type`; the versions-list command exited `0`.
**Hypothesis:** The current `view` surface supports extension-level metadata
and a versions list but not a version-qualified extension selector.

Evidence: The command help documents `axm view <extension> [<field>]` and the
optional `versions` field, while the exact-version selector was rejected as an
unknown extension identity.
