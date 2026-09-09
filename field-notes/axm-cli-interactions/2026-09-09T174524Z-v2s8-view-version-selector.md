---
id: 2026-09-09T174524Z-v2s8
subject: axm-cli-interactions
key: view-version-selector
observed_at: "2026-09-09T17:45:24.557247+00:00"
session: release-r7c2
kind: workaround
status: open
---

**Expected:** Verify the exact published release required by the AXM skill using a version-qualified Registry view.
**Observed:** After successful publication, axm view @craigsmitham/knowledge/product-engineering@2.1.0 --json treated the version-qualified identity as an extension name and returned not_found.
**Impact:** One failed read and one alternative read-only verification; elapsed delay not measured.
**Recovery:** axm publish @craigsmitham/knowledge/product-engineering --preview --on-existing verify --json verified the locally selected 2.1.0 archive against the published version, without upload.
**Detected by:** Complete structured results and process exits.
**Observed factors:** AXM 0.28.12; view help documents an extension argument but no version flag. Publication had succeeded for the exact identity.
**Diagnostic evidence:** View exit 3, ok false, code not_found; suggestion to check name/type/FQN. Verification exit 0, ok true, participation verified-existing, version 2.1.0, status success, reason version_already_published, alreadyPublished 1, failed 0, blocked 0. Archive integrity matched the publication preview.
**Hypothesis:** The view selector does not support a version suffix.
