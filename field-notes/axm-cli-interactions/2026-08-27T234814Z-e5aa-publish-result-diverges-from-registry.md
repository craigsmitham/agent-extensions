---
id: 2026-08-27T234814Z-e5aa
subject: axm-cli-interactions
key: publish-result-diverges-from-registry
observed_at: "2026-08-27T23:48:14Z"
session: unknown
kind: gap
status: open
---

**Expected:** One admitted 18-package `axm publish` operation would report each
persisted Registry upload as successful and block only packages whose exact
dependencies were absent.
**Observed:** AXM 0.28.1 exited 16 and reported 13 published, three failed, and
two dependency-blocked. Exact Registry readback then showed the supposedly
failed `@craigsmitham/skills/quick-change@0.1.0` present and public, while
`@craigsmitham/skills/research@3.0.0`,
`@craigsmitham/knowledge/gen-stack@0.25.0`, and both packs remained absent.
**Impact:** The release became partially applied and required 18 exact Registry
reads plus a narrowed recovery preflight before consumer updates could proceed.
**Recovery:** Stopped broad retries, used `axm view` for exact-version readback,
and limited the next candidate to the verified-missing dependencies and packs.
Task completion was pending at capture time.
**Detected by:** Comparing the structured publish outcomes with immediate
`axm view <handle> --json` results.
**Observed factors:** CLI and workspace skill version 0.28.1; publisher
`@craigsmitham`; target `registry.agentxm.ai`; preview status `admitted`; all 18
archives public and warning-free; apply result `unknown: 0`.
**Diagnostic evidence:** Publish exit status 16; counts `published: 13`,
`failed: 3`, `blocked: 2`; failure reason `upload_failed` for Quick Change,
Research, and Gen Stack Knowledge; block reason `blocked_by_dependency` for Gen
Stack and QRSPI packs. Further failure detail is unavailable — output was
reduced before retention. Registry readback timestamps established Quick Change
0.1.0 at `2026-08-27T23:47:16.604Z` and did not list the other failed versions.
**Hypothesis:** At least one upload completed server-side after the client
classified its response as failed; the reason for the other upload failures is
unknown.

Evidence: The exact apply result and exact-version Registry metadata disagree
for Quick Change 0.1.0, while both independently show a partial release.
