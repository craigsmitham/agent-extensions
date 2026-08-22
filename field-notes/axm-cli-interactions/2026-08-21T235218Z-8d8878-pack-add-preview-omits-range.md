---
id: 2026-08-21T235218Z-8d8878
subject: axm-cli-interactions
key: pack-add-preview-omits-range
observed_at: "2026-08-21T23:52:18Z"
session: codex-8d8878
kind: workaround
status: open
---

**Expected:** `axm packs add --preview --json` would show the exact dependency
range it planned to write, because the command was being used to raise an
existing pack member's lower bound.
**Observed:** The preview reported one ready manifest update but exposed no
before/after dependency range; previews for four different existing members
also returned the same candidate ID.
**Impact:** One member update had to be applied and the manifest inspected
before the range-writing behavior could be confirmed; one extra mutation and
inspection step affected this pack update.
**Recovery:** Applied the knowledge member update, confirmed that the lower
bound changed from `>=1.0.0` to `>=1.1.0`, then applied the remaining member
updates. The original work continued.
**Detected by:** Comparing the JSON preview output with the pack manifest.
**Observed factors:** AXM 0.27.x; project-workspace authored pack; each member
already existed in the pack; JSON and non-interactive preview mode.
**Hypothesis:** The pack-add preview describes the manifest operation but does
not currently serialize field-level dependency changes.
**Suggests:** Include the previous and proposed dependency ranges in preview
step details for existing pack members.

Evidence: The preview step contained only `label: software-architecture`,
`status: ready`, while the applied knowledge update changed the manifest floor
to `@craigsmitham/knowledge/software-architecture: >=1.1.0`.
