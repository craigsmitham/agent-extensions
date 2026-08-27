---
id: 2026-08-27T001954Z-n6p4
subject: axm-cli-interactions
key: bulk-publish-partial-dependency-block
observed_at: "2026-08-27T00:19:54Z"
session: g1b7
kind: workaround
status: open
---

**Expected:** The admitted 26-item publication set would publish the three pending Gen Stack releases after authoritative preview passed with no blocked or failed items.
**Observed:** The apply published the skill, failed the knowledge upload, blocked the dependent pack, and returned a partial result.
**Impact:** Knowledge `0.18.0` and pack `2.10.0` remained unpublished and required bounded recovery; elapsed delay was not measured.
**Recovery:** Registry readback confirmed skill `1.9.0` and the absence of the two newer versions; explicit dependency-first publication remained to run at capture time.
**Detected by:** Structured apply result, process exit status, and exact registry readback.
**Observed factors:** AXM CLI 0.28.1; Registry `agentxm`; project scope; owner `@craigsmitham`; 26 selected items; 23 verified existing versions; public visibility; existing-version policy `verify`.
**Diagnostic evidence:** Command exit status `16`; result `ok: false`; mode `apply`; counts `selected: 26`, `published: 1`, `alreadyPublished: 23`, `blocked: 1`, `failed: 1`, `pending: 0`, `unknown: 0`; successful identity `@craigsmitham/skills/gen-stack@1.9.0`; failed identity `@craigsmitham/knowledge/gen-stack@0.18.0`, action `error`, reason `upload_failed`; blocked identity `@craigsmitham/packs/gen-stack@2.10.0`, action `error`, reason `blocked_by_dependency`; direct upload failure detail unavailable — reduced output did not retain it; registry latest versions after apply were skill `1.9.0`, knowledge `0.17.1`, and pack `2.9.1`.
**Hypothesis:** unknown

Evidence: The admitted preview had three pending items and no blockers; apply published only the skill, while registry readback showed the knowledge and dependency-bound pack still at their prior versions.
