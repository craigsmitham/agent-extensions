---
id: 2026-09-08T121500Z-q7w2
subject: axm-cli-interactions
key: unauthenticated-preview-masks-integrity-drift
observed_at: "2026-09-08T12:15:00+00:00"
session: 40e135ca36b6
kind: gap
status: open
---

**Expected:** `axm publish --type knowledge --preview` reports the same
per-version preflight outcome regardless of authentication state, since the
documented purpose of `--preview` is to preflight without uploading.
**Observed:** Run unauthenticated, the command exited 0 and listed
`@craigsmitham/knowledge/knowledge-management@0.1.1` under
"9 versions already published and integrity-verified", planning a single
publish of `software-engineering`. The identical command run after
`axm login --device-code` exited 0 but reported
"1 extension failed preflight" with
"Immutable-version integrity drift for @craigsmitham/knowledge/knowledge-management@0.1.1 (conflict)"
and only 8 versions verified.
**Impact:** The first preview understated the release plan by one bundle. Had
the version bump been scoped to that first plan, `knowledge-management` would
have been left at a version whose local content no longer matches the published
archive. One extra preview run was needed after authenticating; no work was
lost and publishing completed.
**Recovery:** Re-ran the preview after authenticating, treated the drifted
bundle as requiring a bump regardless of content changes, and bumped all ten
bundles before publishing. All 10 versions published and integrity-verified.
**Detected by:** Comparing preview output before and after `axm login` while
preparing a release.
**Observed factors:** AXM 0.28.11. First run: no registry session
(`axm whoami` reported `auth_required`). Second run: authenticated as
@craigsmitham with scopes `account:read, extensions:read`. Same working tree,
same command, same flags, runs about 4 minutes apart. The unauthenticated run
did print "Authoritative publication set (unavailable)" and a registry
authentication warning.
**Diagnostic evidence:** Both runs exited 0. Unauthenticated run:
"9 versions already published and integrity-verified", 2 planned changes.
Authenticated run: "1 extension failed preflight", "1 extension not attempted",
error class `conflict`, remediation
`axm version @craigsmitham/knowledge/knowledge-management patch`.
**Hypothesis:** Unknown. The "(unavailable)" marker on the authoritative
publication set suggests the unauthenticated path substitutes a local
assumption for registry-side integrity verification, but reports the result
using the same "integrity-verified" wording as a real check.
**Suggests:** Distinguish "not checked — unauthenticated" from
"integrity-verified" in preview output.
