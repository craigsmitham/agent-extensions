---
id: 2026-08-17T140623Z-50cf67fa
subject: axm-cli-interactions
key: upgrade-github-api-504
observed_at: "2026-08-17T14:06:23Z"
session: 0d115892
kind: friction
status: open
---

**Expected:** `axm upgrade` would complete the release-preflight requirement to use the latest AXM CLI before updating and publishing extensions.
**Observed:** The release lookup failed with HTTP 504 and AXM reported that the GitHub API was temporarily unavailable; the installed CLI remained at 0.27.5.
**Impact:** The CLI self-upgrade did not complete, but the public Registry update preview remained available; delay was under one minute.
**Recovery:** Continued with the narrowly scoped official-skill update and left the CLI upgrade for retry before publication.
**Detected by:** The `axm upgrade` human-readable error and the unchanged `axm --version` output.
**Observed factors:** The immediately following Registry-backed `axm update ... --preview --json` succeeded with one ready step and no warnings.
**Hypothesis:** The GitHub release endpoint or its proxy returned a transient gateway timeout independent of Registry availability.
**Suggests:** Preserve the retry instruction, and consider a bounded automatic retry for transient GitHub 5xx responses during upgrade preflight.

Evidence: `axm upgrade` returned `GitHub API is temporarily unavailable (status 504)` on 2026-08-17; `axm --version` remained `0.27.5`.
