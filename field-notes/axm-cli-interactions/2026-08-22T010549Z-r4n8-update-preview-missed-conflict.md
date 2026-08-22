---
id: 2026-08-22T010549Z-r4n8
subject: axm-cli-interactions
key: update-preview-missed-conflict
observed_at: "2026-08-22T01:05:49Z"
session: s8d4q1
kind: gap
status: open
---

**Expected:** Applying an update immediately after a ready, warning-free preview against unchanged workspace state should execute the previewed plan.
**Observed:** `axm update @agentxm/packs/agent-engineering --preview --json --non-interactive` reported one ready step and no warnings or errors, while the following apply failed before changing files with two `constraint-conflict` problems.
**Impact:** The update sequence required one retry after removing the deprecated packs that own the conflicting constraints.
**Recovery:** Reordered the migration to uninstall the legacy packs before retrying the replacement-pack update; task completion was not yet known at capture time.
**Detected by:** Comparing the preview result with the immediately following apply result and Git status.
**Observed factors:** AXM CLI 0.27.15; project scope; preview candidate `9e4d44b9dbbcf788b26b62eb43527109b1978bc078a7d1e3d54014cf20be2b5b`; apply candidate `4835a1e97d68eac940942149290bed03a632863c8fb5f642d482d3352a160ad5`; deprecated context-, harness-, and skill-engineering packs were still installed; Git status showed no AXM-managed changes after failure.
**Hypothesis:** Preview validation did not account for constraints contributed by other installed packs, while apply validation did.

Evidence: Preview returned `outcome: previewed`, `readyCount: 1`, and `errorCount: 0`; apply returned `outcome: failed`, `errorCode: conflict`, and `constraint-conflict; constraint-conflict`; the failed step reported zero applied changes.
