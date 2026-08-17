---
id: 2026-08-17T191254Z-q8m2
subject: axm-cli-interactions
key: upgrade-rate-limit
observed_at: "2026-08-17T19:12:54Z"
session: codex-q8m2
kind: blocked
status: open
---

**Expected:** `axm upgrade` should resolve the current release so the repository's pre-commit release gate can refresh the CLI and installed AXM skill.
**Observed:** The command exited nonzero with `GitHub API rate limit prevented release resolution (rate_limit)`; the subsequent chained skill update and sync preview did not run.
**Impact:** One release-gate command failed and the skill refresh plus reconciliation preview had to be invoked separately; elapsed delay was not measured.
**Recovery:** Progress continued by checking the installed CLI version and running the remaining refresh and preview steps separately; final completion was pending at capture time.
**Detected by:** The AXM command's stderr diagnostic and nonzero exit.
**Observed factors:** The installed CLI reported version `0.27.8` immediately after the failed command, while the installed AXM skill declared `0.27.7`.
**Hypothesis:** unknown

Evidence: `axm upgrade` emitted the `rate_limit` diagnostic on 2026-08-17, and the following `axm --version` output was `0.27.8`.
