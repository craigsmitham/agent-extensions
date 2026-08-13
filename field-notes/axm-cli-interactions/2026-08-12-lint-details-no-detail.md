---
subject: axm-cli-interactions
key: lint-details-no-detail
date: 2026-08-12
kind: gap
status: open
---

**Expected:** `axm lint` ended with `Next: Show detailed lint output · axm lint
--details`, so `--details` should have explained each `canonical state
wrong-origin` finding well enough to act on it.
**Actual:** `axm lint --details` printed the same four finding lines as the plain
run, with no added cause, path, or recovery. The actionable information came
only from `axm status`, which named the problem `canonical-wrong-origin` and gave
`axm adopt <fqn> --preview` as recovery.
**Gap:** the `--details` affordance is advertised as the next step for
understanding a finding, but for `workspace/desired-state-reconcilable` it adds
nothing, so the suggested path costs a round trip before landing on `axm status`.
**Suggests:** either have `--details` render the per-extension local state and
recovery for this rule, or make the `Next` hint point at `axm status` for
`workspace/*` findings.

Evidence: AXM CLI 0.26.6, skill 0.26.6, workspace
`/Users/craig/Code/craigsmitham/agent-extensions`. Plain `axm lint` reported
"1 issue. 1 needs manual attention." against `./.axm/settings.json` with four
related findings (`conduct-codebase-research`, `frame-codebase-research`,
`refine-work`, `workshop-codebase-design`). `axm lint --details` reproduced those
four lines and the `Next` block only. `axm lint --json` also carried no cause
beyond the same message strings. Four skills had locally edited canonical content
at the time.
