---
id: 2026-08-28T211737Z-52061543
subject: axm-cli-interactions
key: knowledge-publish-timeout-blocked-pack
observed_at: "2026-08-28T21:17:37Z"
session: 90e3397d
kind: workaround
status: open
---

**Expected:** The admitted idempotent continuation would publish the four
remaining release candidates and return a successful terminal result.
**Observed:** AXM published `review 1.0.0` and `investigate 0.3.0`, but the
Registry request for `knowledge/gen-stack 2.0.0` timed out and
`packs/gen-stack 7.0.0` was blocked by that failed dependency.
**Impact:** The release closure remained incomplete and required another
bounded Registry mutation for the failed knowledge package and its blocked
pack.
**Recovery:** Use AXM's returned continuation command for exactly
`@craigsmitham/knowledge/gen-stack` and `@craigsmitham/packs/gen-stack` with
`--on-existing verify`, then perform exact-version Registry readback.
**Detected by:** The terminal `publish-result-v3` execution outcomes and exit
status.
**Observed factors:** AXM CLI 0.28.1; 17 selected packages; 13 verified
existing; two published; one failed; one blocked; exit status 16.
**Diagnostic evidence:** Knowledge outcome reason `upload_failed`; cause code
`timeout`; class `external`; retryable `true`; pack reason
`blocked_by_dependency`; blocked by `@craigsmitham/knowledge/gen-stack`.
**Hypothesis:** unknown

Evidence: The complete terminal result named both successful publications,
the retryable timeout, the blocked dependent, and the exact two-package
continuation command.
