---
id: 2026-09-02T143340Z-k7m2
subject: axm-cli-interactions
key: scoped-knowledge-sync-omits-discovery
observed_at: "2026-09-02T14:33:40Z"
session: k7m2
kind: gap
status: open
---

**Expected:** After changing a workspace-authored Knowledge manifest
description, `axm sync --type knowledge --preview --json` would include the
stale Knowledge discovery region already reported by workspace lint.
**Observed:** The type-scoped preview returned `no-op`, while the immediately
preceding workspace preview reported `knowledge:discovery` ready to update
`AGENTS.md`.
**Impact:** The bounded type-scoped command could not converge the changed
Knowledge discovery projection; a workspace-wide sync was required and its
other units had to be reviewed.
**Recovery:** Use the retained workspace-wide preview, apply its three
determined units, inspect the resulting files, and re-run convergence checks.
The task remains in progress.
**Detected by:** Comparing the structured results of `axm sync --preview
--json` and `axm sync --type knowledge --preview --json`.
**Observed factors:** AXM CLI 0.28.4; compatible bundled AXM skill 0.28.1;
workspace-authored `@craigsmitham/knowledge/software-engineering` description
changed; the workspace preview identified `knowledge:discovery` as stale.
**Diagnostic evidence:** type-scoped outcome `no-op`, zero units; workspace
preview outcome `previewed`, with a `knowledge:discovery` unit whose artifact
was `AGENTS.md`.
**Hypothesis:** unknown

Evidence: The two preview results were produced consecutively against the same
working tree without an intervening mutation.
