---
id: 2026-08-17T140539Z-7d2bfa91
subject: ci-cd-workflows
key: gh-fix-ci-gh-version-drift
observed_at: "2026-08-17T14:05:39Z"
session: 0d115892
kind: friction
status: open
---

**Expected:** The installed `gh-fix-ci` inspection script would tolerate GitHub CLI field drift and return the failing PR check details.
**Observed:** With GitHub CLI 2.45.0, the script called `gh pr checks --json`; that command rejected the unknown flag and printed usage instead of inspecting the failure.
**Impact:** The failed workflow had to be inspected manually with `gh run view --log-failed`; delay was under one minute.
**Recovery:** Used the skill's documented manual fallback to retrieve the Actions run metadata and failed-job log.
**Detected by:** The inspection script's stderr and nonzero exit status.
**Observed factors:** `gh auth status` succeeded with repository and workflow scopes; the failing check was a GitHub Actions run.
**Hypothesis:** The compatibility fallback handles changing JSON fields but does not detect GitHub CLI releases that predate `gh pr checks --json` entirely.
**Suggests:** Detect support for `gh pr checks --json` and fall back to PR metadata plus `gh run view` when the flag is unavailable.

Evidence: `inspect_pr_checks.py --repo . --pr 6 --json` failed with `unknown flag: --json` under `gh version 2.45.0` on 2026-08-17.
