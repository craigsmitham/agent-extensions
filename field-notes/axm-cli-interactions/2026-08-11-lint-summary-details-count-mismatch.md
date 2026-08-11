---
subject: axm-cli-interactions
key: lint-summary-details-count-mismatch
date: 2026-08-11
kind: gap
status: open
---

**Expected:** `axm lint` and `axm lint --details` should report the same set and
count of current findings because `--details` is presented as the expanded view
of the summary.
**Actual:** `axm lint` reported one issue for
`workshop-codebase-design`; the immediately following `axm lint --details`
reported three unpublished-content infos for `assess-codebase-change-readiness`,
`verify-codebase-change`, and `workshop-codebase-design`.
**Gap:** The summary omitted two findings that the detailed view considered
current in the same worktree.
**Suggests:** Derive summary and detailed output from the same finding set, or
explain any intentional filtering in the summary.

Evidence: AXM CLI `0.25.8`, project scope, repository `main` at
`a881a71aceac6d5d866ceca3be38cff5a632492e`, commands run consecutively on
2026-08-11 with no intervening filesystem mutation.
