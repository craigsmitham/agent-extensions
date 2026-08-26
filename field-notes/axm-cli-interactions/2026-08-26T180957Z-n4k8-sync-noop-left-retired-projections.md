---
id: 2026-08-26T180957Z-n4k8
subject: axm-cli-interactions
key: sync-noop-left-retired-projections
observed_at: "2026-08-26T18:09:57Z"
session: q7m2
kind: workaround
status: open
---

**Expected:** After direct intent and pack membership for `reconcile-gen-stack` were removed, AXM sync should remove or identify every agent projection for that retired package.
**Observed:** `axm sync --preview --fail-on-change --json` exited `0` with `outcome: no-op`, but four symlinks remained under `.agents/skills`, `.claude/skills`, `.cursor/skills`, and `.github/skills`, each targeting the removed `skills/reconcile-gen-stack/src` path.
**Impact:** The requested extension removal required four additional exact-path cleanup operations after AXM reported convergence.
**Recovery:** Removed the four stale projection symlinks directly after confirming their targets and retained the canonical package deletion.
**Detected by:** Exact post-removal filesystem verification after AXM lint and sync reported a clean, converged workspace.
**Observed factors:** AXM CLI `0.28.1`; project scope; source authority had been removed from `axm.json` and `packs/gen-stack/pack.json`; canonical package path no longer existed.
**Diagnostic evidence:** Sync process exit `0`; result outcome `no-op`; counts total `0`, failed `0`, blocked `0`; affected projections `.agents/skills/reconcile-gen-stack`, `.claude/skills/reconcile-gen-stack`, `.cursor/skills/reconcile-gen-stack`, and `.github/skills/reconcile-gen-stack`.
**Hypothesis:** AXM convergence did not classify retained project-authored projection symlinks as cleanup candidates after source deletion.
