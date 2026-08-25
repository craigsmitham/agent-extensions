---
id: 2026-08-25T205051Z-v3h6
subject: axm-cli-interactions
key: version-apply-flag-rejected
observed_at: "2026-08-25T20:50:51Z"
session: s8f2n
kind: friction
status: open
---

**Expected:** After previewing a version mutation, the same non-interactive apply convention used by other AXM lifecycle commands would apply it.
**Observed:** `axm version ... --yes --json` rejected `--yes` as an unrecognized flag.
**Impact:** The version sequence required one read-only help lookup and one corrected invocation.
**Recovery:** Read `axm version --help`, then applied the already-previewed exact version without `--yes`.
**Detected by:** Versioning the Gen Stack migration packages.
**Observed factors:** Clean local `agentxm/axm` main checkout; CLI reported `0.27.18`; project lockfile version `6`; exact target versions had already been previewed.
**Diagnostic evidence:** Process exit status `2`; error code `usage`; detail `Unrecognized flag: --yes in command axm version`.
**Hypothesis:** Apply confirmation conventions vary between AXM lifecycle commands and are not discoverable from the preview result.

Evidence: The failed command changed no files. The corrected exact-version commands completed with `outcome: applied` and committed one manifest change each.
