---
subject: axm-cli-interactions
key: adopt-reports-applied-no-effect
date: 2026-08-12
kind: blocked
status: dropped
---

**Dropped:** Superseded by the AXM v4 authority model; the trust-derived wrong-origin state and its adopt recovery no longer govern workspace reconciliation.

**Expected:** `axm status` reported `canonical-wrong-origin` on four skills and
named `axm adopt <fqn> --preview` as the recovery, so running the adopt should
have cleared the finding and unblocked the pre-commit public-safety gate.
**Actual:** every adopt run reported success — `"ok": true`,
`"outcome": "applied"`, `"appliedCount": 1`, exit 0 — while changing nothing.
No file under `.axm` was modified, and a fresh `axm status` reported the same
four findings with the same recovery command.
**Gap:** the command's success report is not evidence that the recorded state
changed. There is no output distinguishing "adopted" from "nothing to do", so
the only way to learn the recovery had failed was to re-run `status` and
compare, then check file mtimes.
**Suggests:** make adopt report what it wrote (or that it wrote nothing), and
fail rather than report `applied` when the finding it recovers still holds
afterwards.

Evidence: AXM CLI 0.26.6, skill 0.26.6, workspace
`/Users/craig/Code/craigsmitham/agent-extensions`. Affected skills:
`conduct-codebase-research`, `frame-codebase-research`, `refine-work`,
`workshop-codebase-design`. Ran adopt six times across those four (once with
`--json`). `find .axm -newermt '-3 minutes' -type f` returned nothing after the
batch. `git diff -- .axm/trust.json` contained no added line naming any of the
four. `scripts/check-public-safety.sh --view git-index` reported the same four
blocking findings before and after. The workspace also had an unrelated
`packs/effect-v4` conflict blocking `axm sync` at the time, and
`workshop-codebase-design` had uncommitted edits; whether either affects adopt
is unknown.
