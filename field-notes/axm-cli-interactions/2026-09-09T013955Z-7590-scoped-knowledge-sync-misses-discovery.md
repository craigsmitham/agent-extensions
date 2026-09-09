---
id: 2026-09-09T013955Z-7590
subject: axm-cli-interactions
key: scoped-knowledge-sync-misses-discovery
observed_at: "2026-09-09T01:39:55.545019+00:00"
session: 817f4ef5253c
kind: workaround
status: open
---

**Expected:** After changing the product-engineering knowledge manifest description,
a scoped sync preview would reveal any materialization needed for that package,
based on help describing the extension argument as a root to reconcile.
**Observed:** Scoped preview reported the package up to date while AGENTS.md still
contained the previous description. Workspace-wide preview found one stale
Knowledge discovery region.
**Impact:** Updating this bundle's discovery text required one additional preview
and a workspace-wide sync. Time cost not measured.
**Recovery:** Workspace-wide preview showed only AGENTS.md knowledge discovery;
`axm sync --json` applied that one change successfully.
**Detected by:** Comparing the manifest description with the generated discovery
row and the two preview results.
**Observed factors:** AXM 0.28.11; project-authored
`@craigsmitham/knowledge/product-engineering` version 2.0.0.
**Diagnostic evidence:** All three commands exited 0. Scoped
`axm sync @craigsmitham/knowledge/product-engineering --preview --json`:
`ok=true`, `result.outcome=no-op`, `counts.total=0`, `units=[]`.
Workspace `axm sync --preview --json`: `result.outcome=previewed`,
`counts.total=1`, unit `knowledge:discovery`, state `ready`, artifact `AGENTS.md`,
managed region `knowledge:discovery-region`. Apply: `result.outcome=applied`,
`counts.committed=1`, unit `knowledge:discovery` state `committed`,
footprint only `AGENTS.md`. Progress event records were inspected separately
from final result fields; no failure diagnostic was supplied.
**Hypothesis:** Scoped knowledge sync may exclude shared discovery regeneration;
implementation cause unknown.
