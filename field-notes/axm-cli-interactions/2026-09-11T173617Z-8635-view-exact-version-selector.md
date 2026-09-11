---
id: 2026-09-11T173617Z-8635
subject: axm-cli-interactions
key: view-exact-version-selector
observed_at: "2026-09-11T17:36:17.383371+00:00"
session: 01a09180-7995-7971-8c44-c53ec4e5ca0c
kind: workaround
status: open
---

**Expected:** Verify the exact published version after the AXM publication workflow, as required by the installed AXM skill.
**Observed:** `axm view @craigsmitham/knowledge/effect-v4@1.0.4 --json` exited 3 with `not_found` immediately after publication succeeded. Its error treated the version-qualified selector as the extension name.
**Impact:** Exact-version verification required an unversioned metadata read and a publication verification preview; no upload was repeated.
**Recovery:** `axm view @craigsmitham/knowledge/effect-v4 --json` listed public version 1.0.4. `axm publish @craigsmitham/knowledge/effect-v4 --preview --on-existing verify --json` exited 0 and verified the local 1.0.4 archive against the published version.
**Detected by:** Post-publication readback.
**Observed factors:** AXM 0.28.12; workspace-authored knowledge package 1.0.4; authenticated publisher matched the package owner.
**Diagnostic evidence:** View: exit 3, ok false, code `not_found`, title `Not Found`. Verification preview: exit 0, ok true, participation `verified-existing`, action `skip`, reason `version_already_published`, status `success`, counts alreadyPublished 1, failed 0, blocked 0, pending 0. SHA-512 integrity matched the preflight and successful upload.
**Hypothesis:** unknown
