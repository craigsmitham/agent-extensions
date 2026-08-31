---
id: 2026-08-31T192958Z-m4q8
subject: axm-cli-interactions
key: exact-version-view-not-found
observed_at: "2026-08-31T19:29:58Z"
session: unknown
kind: gap
status: open
---

**Expected:** The Registry-mutation verification guidance could be followed by reading the exact published selector `@craigsmitham/skills/audit-docs@0.1.3` through `axm view`.
**Observed:** The identity-level view listed version `0.1.3`, but `axm view @craigsmitham/skills/audit-docs@0.1.3 --json` returned `not_found` and treated the versioned selector as an extension name.
**Impact:** Exact-version readback was unavailable through the documented metadata-view command; deprecation verification must remain identity-level. One unsupported read was attempted.
**Recovery:** Preserved the identity-level version list and continued with identity-level deprecation and readback; no mutation was rerun.
**Detected by:** Comparing the successful identity result with the immediately following structured exact-selector error.
**Observed factors:** AXM CLI version 0.28.2; public Registry identity; version `0.1.3` was present in the successful `versions` array.
**Diagnostic evidence:** Error code `not_found`; detail `No extension named "@craigsmitham/skills/audit-docs@0.1.3" was found`; per-command process exit status unavailable because the shell invocation continued to a later successful read.
**Hypothesis:** `axm view` accepts only unversioned extension identities even though Registry-mutation guidance requires exact-version readback.
**Suggests:** Support exact-version selectors in `axm view`, or define a different exact-version verification command in lifecycle guidance.

Evidence: The same command sequence returned the unversioned identity with latest version `0.1.3`, then rejected the exact-version selector with a structured `not_found` result.
