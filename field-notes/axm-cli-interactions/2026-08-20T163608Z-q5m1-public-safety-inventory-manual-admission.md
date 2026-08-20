---
id: 2026-08-20T163608Z-q5m1
subject: axm-cli-interactions
key: public-safety-inventory-manual-admission
observed_at: "2026-08-20T16:36:08Z"
session: q7d2f9
kind: gap
status: open
---

**Expected:** Following the documented publishing gate would identify any required admission step before the full public-safety check.
**Observed:** `scripts/check-public-safety.sh` rejected three newly authored public packages because its private `expected` array still contained the prior 25-package inventory; the publishing guide names the check but not this admission surface.
**Impact:** The release gate stopped once and required locating and updating an additional repository-maintained inventory. Delay was not measured.
**Recovery:** Add the reviewed package paths to the approved inventory, rerun the gate, and continue the requested release.
**Detected by:** The workspace public-safety check after AXM lint passed.
**Observed factors:** The actual inventory differed only by `packs/qrspi`, `skills/question`, and `skills/research`; the check printed the three additions in its diff.
**Hypothesis:** The explicit inventory is an intentional admission control whose maintenance step is not documented in the publishing workflow.

Evidence: `scripts/check-public-safety.sh` compares discovered `@craigsmitham` manifests with a shell array and exits when they differ; the array contained 25 package paths before this release.
