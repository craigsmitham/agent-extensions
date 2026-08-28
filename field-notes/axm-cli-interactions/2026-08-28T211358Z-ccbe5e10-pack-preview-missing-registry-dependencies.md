---
id: 2026-08-28T211358Z-ccbe5e10
subject: axm-cli-interactions
key: pack-preview-missing-registry-dependencies
observed_at: "2026-08-28T21:13:58Z"
session: 90e3397d
kind: blocked
status: open
---

**Expected:** The exact 13-package Gen Stack release selection would pass
authoritative Registry preflight because its unchanged direct dependencies had
already been versioned in the repository.
**Observed:** `axm publish --preview --json` selected the intended 13 packages
but blocked the complete publication set because no installable Registry
version satisfied `@craigsmitham/skills/investigate >=0.3.0` or
`@craigsmitham/skills/research >=3.0.2`.
**Impact:** Publication did not start; one additional preview of the pack's
workspace-authored dependency closure was required.
**Recovery:** No mutation was attempted. Continue with the same explicit
selection plus `--include-dependencies --on-existing verify`, then require a
clean authoritative preview before upload.
**Detected by:** The retained structured publish-preview result and exit
status.
**Observed factors:** AXM CLI 0.28.1; public project workspace; explicit
13-package selection; dependency inclusion `explicit`; exit status 9; all 13
selected packages reported blocked.
**Diagnostic evidence:** Failure code `validation`; class `user`; retryable
`false`; the pack reported `pack/dependency-version-resolvable` blockers for
`investigate` and `research`; the result suggested publishing satisfying
versions of those two skills.
**Hypothesis:** The required dependency versions are authored in the workspace
but have not yet been published.

Evidence: The preview selected 13 packages, published none, and returned the
two exact unsatisfied dependency identities and ranges without uploading an
archive.
