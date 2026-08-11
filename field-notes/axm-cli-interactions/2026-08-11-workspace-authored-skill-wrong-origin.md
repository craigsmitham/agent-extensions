---
subject: axm-cli-interactions
key: workspace-authored-skill-wrong-origin
date: 2026-08-11
kind: gap
status: open
---

**Expected:** `axm lint --strict --details` should recognize the edited
`@craigsmitham/skills/workshop-codebase-design` canonical package as
workspace-authored because project settings declare its workspace source.
**Actual:** Lint reported `workspace/desired-state-reconcilable` with canonical
state `wrong-origin` and directed the user to `axm status`.
**Gap:** The finding did not identify the observed competing origin or how an
ordinary canonical-source edit caused the origin classification to change.
**Suggests:** Include the declared and observed origins plus the safe
reconciliation action in the detailed or JSON finding.

Evidence: The failure occurred after editing only canonical package content and
evaluation artifacts. `axm lint --json` reported one error at
`.axm/settings.json`, with no warnings or informational findings.
