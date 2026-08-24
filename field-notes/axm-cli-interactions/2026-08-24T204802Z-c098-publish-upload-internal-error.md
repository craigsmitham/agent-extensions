---
id: 2026-08-24T204802Z-c098
subject: axm-cli-interactions
key: publish-upload-internal-error
observed_at: "2026-08-24T20:48:02Z"
session: 2E16E51B-DF14-4C75-811E-079918D2A447
kind: blocked
status: open
---

**Expected:** `axm publish --yes --json --non-interactive` would upload the six releases accepted by the immediately preceding preview.
**Observed:** Four releases published, `@craigsmitham/subagents/researcher@0.0.1` failed with `upload_failed` and `An unexpected error occurred. (internal)`, and one release was blocked.
**Impact:** The requested catalog publication remained incomplete with two releases pending; one read-only reconciliation preview was required to establish Registry state.
**Recovery:** A subsequent preview verified 31 published versions and identified `@craigsmitham/subagents/researcher@0.0.1` and `@craigsmitham/packs/qrspi@0.1.0` as the only pending releases. No outer mutation retry was attempted.
**Detected by:** The publish result returned `ok: false`, `published: 4`, `blocked: 1`, and `failed: 1`.
**Observed factors:** Authentication and the complete preflight succeeded immediately before upload; the failure response exposed no Registry correlation identifier in the selected JSON fields.
**Hypothesis:** unknown

Evidence: The mutation result named the researcher subagent and the stable `upload_failed` reason. The following preview returned `ok: true`, 31 already published, two pending, and zero blocked or failed entries.
