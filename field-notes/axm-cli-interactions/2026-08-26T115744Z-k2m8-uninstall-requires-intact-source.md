---
id: 2026-08-26T115744Z-k2m8
subject: axm-cli-interactions
key: uninstall-requires-intact-source
observed_at: "2026-08-26T11:57:44Z"
session: codex-j6p2
kind: workaround
status: open
---

**Expected:** AXM could unregister retired workspace packages after their
maintained content had moved to a replacement package.
**Observed:** Pack uninstall preview first blocked when the two retired pack
manifests were absent. After restoring their manifests, pack removal succeeded,
but knowledge uninstall apply failed validation while each bundle's `src/`
content was absent and rolled back.
**Impact:** Four retirement commands required restoration scaffolding and retry;
two knowledge applies failed before the successful recovery.
**Recovery:** Restored the four manifests, uninstalled both packs, added a
temporary valid root concept to each retired knowledge bundle, uninstalled both
knowledge identities, and removed the temporary scaffolding. The requested
local retirement completed.
**Detected by:** Structured AXM preview/apply results and process exit statuses.
**Observed factors:** AXM CLI `0.28.1`; compatible AXM skill `0.28.1`; project
workspace; canonical package content had already moved into Gen Stack; retired
package manifests or bundle roots were absent during the failing attempts.
**Diagnostic evidence:** Initial pack preview exited `6`, returned outcome
`blocked`, mode `preview`, cause code `conflict`, reference
`packs/uninstall/desired-state-graph-complete`, one blocked unit, and named both
missing pack manifests. Each knowledge apply exited `9`, returned outcome
`failed`, mode `apply`, failure code `validation`, message `Failed to inspect
Open Knowledge Format bundle (validation)`, one failed unit, disposition
`restored`, and restored `axm.json` and `axm-lock.yaml` as applicable.
**Hypothesis:** Workspace uninstall resolves and validates the currently
registered source before removing its desired-state identity.
**Suggests:** Document that workspace package retirement must unregister the
package while its manifest and valid source root are still intact.

Evidence: Restoring only the manifests made both pack previews and applies
succeed. Restoring a minimal valid `src/index.md` made both knowledge previews
and applies succeed with the same candidate identities that had failed.
