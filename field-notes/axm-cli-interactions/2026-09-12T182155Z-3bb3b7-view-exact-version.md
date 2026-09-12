---
id: 2026-09-12T182155Z-3bb3b7
subject: axm-cli-interactions
key: view-exact-version
observed_at: "2026-09-12T18:21:55.976893+00:00"
session: 2c6f8701
kind: gap
status: open
---

**Expected:** The AXM skill requires exact-version Registry readback after publishing.
**Observed:** AXM 0.29.4 `axm view @craigsmitham/rules/use-effect-v4@0.2.0 --json` returned not_found after successful publication.
**Impact:** One failed read and one additional versions-list read during release verification.
**Recovery:** `axm view @craigsmitham/rules/use-effect-v4 versions --json` succeeded and included 0.2.0; publication completed.
**Detected by:** CLI result.
**Observed factors:** View help documents an extension handle and versions field, without an exact-version selector example.
**Diagnostic evidence:** Failed read exit status 3; stdout ok=false, code=not_found, title=Not Found, detail=No extension named "@craigsmitham/rules/use-effect-v4@0.2.0" was found. Stderr emitted matching error and a login suggestion. Recovery exit status 0, versions=[0.2.0, 0.1.1, 0.1.0].
**Hypothesis:** Exact-version selector syntax is unsupported by view.
