---
id: 2026-08-29T194645Z-r7n2
subject: axm-cli-interactions
key: scoped-knowledge-sync-omits-discovery
observed_at: "2026-08-29T19:46:45Z"
session: c4m7p2
kind: workaround
status: open
---

**Expected:** Syncing the exact workspace knowledge package after changing its
canonical description would reconcile the generated knowledge-discovery entry.
**Observed:** `axm sync @craigsmitham/knowledge/effect-v4 --preview --json
--non-interactive` returned a no-op with exit status 0, while the subsequent
workspace-wide preview reported one ready `knowledge:discovery` update to
`AGENTS.md`.
**Impact:** One scoped preview and one scoped apply produced no change, requiring
an additional workspace-wide preview and apply; elapsed cost was not measured.
**Recovery:** The workspace-wide sync identified the exact managed discovery
region and restored progress.
**Detected by:** The generated Effect v4 discovery description remained
different from `knowledge/effect-v4/knowledge.json.description` after the
scoped sync.
**Observed factors:** AXM CLI version 0.28.2; the canonical package was
workspace-authored; both scoped commands exited successfully and reported
`outcome: no-op`.
**Diagnostic evidence:** Scoped plan totals were zero. The workspace-wide
preview reported candidate
`8d744a87f1e42b91053734e37aa2ef695c13bdc15a225845857e660be73aa54c`,
one ready unit with id `knowledge:discovery`, and no warnings or blocked
units.
**Hypothesis:** Scoped knowledge synchronization does not include the
workspace-level discovery projection even when that projection consumes the
selected package's metadata.

Evidence: The canonical description changed to “Checklists to consult when
designing, implementing, maintaining, or reviewing Effect v4 TypeScript”; the
scoped result was a no-op, and the immediately following workspace result
planned an `AGENTS.md#knowledge` update.
