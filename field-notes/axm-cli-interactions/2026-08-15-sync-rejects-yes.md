---
subject: axm-cli-interactions
key: sync-rejects-yes
date: 2026-08-15
kind: workaround
status: open
---

**Expected:** After previewing a workspace mutation, `axm sync --yes` would
apply it using the same confirmation flag accepted by `axm packs add`.
**Actual:** `axm sync --yes` rejected `--yes` as unrecognized; rerunning
`axm sync` applied the previewed change without an additional confirmation.
**Gap:** Mutating AXM commands expose different confirmation interfaces, and
the applicable interface is not apparent from the preview output.
**Suggests:** Give mutation commands a consistent apply flag, or make preview
output name the exact apply command.

Evidence: In the same workspace session, `axm packs add ... --yes` succeeded;
`axm sync --preview` reported one ready workspace item; `axm sync --yes`
printed the sync usage and an “Unrecognized flag” error; plain `axm sync`
then materialized the one Knowledge discovery update.
