---
id: 2026-08-17T134951Z-k7q2
subject: axm-cli-interactions
key: upgrade-github-rate-limit
observed_at: "2026-08-17T13:49:51Z"
session: 565ef42a
kind: workaround
status: open
---

**Expected:** `axm upgrade` updates the CLI, as prescribed by
docs/publishing.md ("Upgrade AXM immediately before release work").
**Observed:** `axm upgrade` exited with "GitHub API rate limit prevented
release resolution (rate_limit)" and advised waiting for the reset.
**Impact:** CLI stayed at 0.27.7; the prescribed pre-release upgrade step could
not complete. No retry attempted; not measured beyond one failed invocation.
**Recovery:** Continued with CLI 0.27.7. `axm update @agentxm/skills/axm
--ignore-release-age` succeeded and cleared the `workspace/axm-skill-compatible`
lint finding, so `axm lint` reports no findings.
**Detected by:** Non-zero-looking error banner in `axm upgrade` output during a
release-readiness pass.
**Observed factors:** Unauthenticated GitHub API access from this machine;
first `axm upgrade` invocation in the session; `axm --version` 0.27.7 before
and after.
**Hypothesis:** GitHub API rate limiting on unauthenticated release lookups.

Evidence: `axm upgrade` output "GitHub API rate limit prevented release
resolution (rate_limit) / Next: Wait for the rate limit to reset and try
again." followed by successful `axm update @agentxm/skills/axm
--ignore-release-age` and a clean `axm lint` in the same session.
