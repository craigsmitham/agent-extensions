---
id: 2026-08-29T212245Z-p6k3
subject: axm-cli-interactions
key: publish-partial-result-unretained
observed_at: "2026-08-29T21:22:45Z"
session: unknown
kind: gap
status: open
---

**Expected:** An admitted 12-package `axm publish` selection would return a
retained terminal result and make every selected exact version available for
Registry readback.
**Observed:** The command's output exceeded the retained tool window, so its
exit status and structured terminal result were unavailable. After the process
ended, exact-version Registry reads found 10 selected versions and did not find
`@craigsmitham/knowledge/work-management@0.1.1` or
`@craigsmitham/packs/work-management@0.2.1`.
**Impact:** Publication verification required 12 separate Registry reads and a
fresh bounded preflight for the two absent versions.
**Recovery:** Check that no publisher remains active, preview only the two
absent versions, publish that bounded selection if admitted, and read both
exact versions back from the Registry.
**Detected by:** Post-mutation `axm view <identity> versions --json` reads.
**Observed factors:** The original 12-package preview reported an admitted
publication set with 12 pending candidates. No publisher process remained at
readback time. Each version-list read exited 0.
**Diagnostic evidence:** Original publish exit status and structured output:
unavailable — output was not retained. Missing version lists contained
`work-management` knowledge `0.1.0` and pack versions `0.2.0`, `0.1.2`,
`0.1.0`, and `0.0.1`.
**Hypothesis:** unknown

Evidence: The admitted candidate count, completed process check, and exact
Registry version lists establish the partial observable state without replaying
the original mutation.
