---
id: 2026-09-08T115825Z-2176
subject: axm-cli-interactions
key: authored-skill-ownership-warning
observed_at: "2026-09-08T11:58:25.914552+00:00"
session: 844b5bbd2f6c
kind: gap
status: open
---

**Expected:** A workspace-authored skill with current configured projections has
consistent ownership reporting across lint and show.
**Observed:** `axm lint --json` warned that `skills/author-okf` has no AXM ownership
proof, while `axm skills show author-okf --json` reported workspace source,
enabled project scope, version 0.1.8, and current status for all five configured agents.
**Impact:** One additional show call was used to resolve the apparent conflict;
no authoring work was blocked.
**Recovery:** Used the manifest, desired workspace entry, and show result to
resolve the canonical authoring source; left ownership state unchanged.
**Detected by:** Preflight during author-okf revision.
**Observed factors:** AXM 0.28.11; compatible skill 0.28.1. Lint also listed nine
other ownership warnings.
**Diagnostic evidence:** Both commands exited 0 with `ok: true`.
Lint rule `workspace/managed-file-unowned`, severity `warning`, authority
`skills/author-okf`; summary 0 errors, 10 warnings.
**Hypothesis:** Unknown.
