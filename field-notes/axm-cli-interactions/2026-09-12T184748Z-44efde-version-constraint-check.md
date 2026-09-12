---
id: 2026-09-12T184748Z-44efde
subject: axm-cli-interactions
key: version-constraint-check
observed_at: "2026-09-12T18:47:48.635731+00:00"
session: 2c6f8701
kind: observation
status: open
---

**Expected:** A successful AXM version update would leave the rule usable by its workspace pack.
**Observed:** AXM 0.29.4 accepted a minor bump of field-notes from 0.2.3 to 0.3.0; scoped sync preview then rejected the pack's ^0.2.0 constraint.
**Impact:** Required one version correction and another preview.
**Outcome:** Version 0.2.4 fits the existing pack; scoped sync succeeded.
**Recovery:** Set the version to 0.2.4, previewed, then synced the rule.
**Detected by:** Structured CLI result.
**Observed factors:** packs/field-notes/pack.json requires ^0.2.0.
**Diagnostic evidence:** Version result ok=true, outcome=applied. Sync preview exit status 6; stdout ok=false, code=conflict, detail included fact=workspace/extension-constraints-satisfied, authority=desired-state-graph:workspace, observed version=0.3.0, reason=candidate-violates-constraints. Stderr carried the same conflict. Corrected preview and sync exited 0.
**Hypothesis:** Version mutation and sync validate different constraints.
