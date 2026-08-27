---
id: 2026-08-26T232541Z-m4r8
subject: axm-cli-interactions
key: bulk-publish-partial-recovery
observed_at: "2026-08-26T23:25:41Z"
session: w3p9
kind: workaround
status: open
---

**Expected:** The admitted 26-item publication set would complete after `axm publish --on-existing verify --yes --json --non-interactive` passed authoritative preflight.
**Observed:** The apply published 20 items, failed four items, blocked two dependent packs, and returned an explicit six-item recovery command.
**Impact:** Six selected extensions were not published in the first apply and required one additional bounded Registry operation; elapsed delay was not measured.
**Recovery:** AXM supplied `axm publish --on-existing verify --json --non-interactive --yes @craigsmitham/skills/field-notes @craigsmitham/skills/gen-stack @craigsmitham/knowledge/workflow-automation @craigsmitham/knowledge/gen-stack @craigsmitham/packs/field-notes @craigsmitham/packs/gen-stack`; recovery had not yet run at capture time.
**Detected by:** Structured apply result and process exit status.
**Observed factors:** AXM CLI 0.28.1; Registry `agentxm`; project scope; owner `@craigsmitham`; 26-item admitted publication set; public visibility preserved; existing-version policy `verify`.
**Diagnostic evidence:** Command exit status `10`; result `ok: false`; contract `publish-result-v3`; mode `apply`; counts `selected: 26`, `published: 20`, `alreadyPublished: 0`, `blocked: 2`, `failed: 4`, `unknown: 0`; failed identities `@craigsmitham/skills/field-notes@0.2.3`, `@craigsmitham/skills/gen-stack@1.8.0`, `@craigsmitham/knowledge/workflow-automation@0.2.1`, and `@craigsmitham/knowledge/gen-stack@0.17.0`; blocked identities `@craigsmitham/packs/field-notes@0.2.1` and `@craigsmitham/packs/gen-stack@2.9.0`; direct failure details unavailable — output was not retained; recovery listed the same six remaining items and both blocked dependents.
**Hypothesis:** unknown

Evidence: The apply result reported 20 successful publications, four failed items, two dependency-blocked packs, and a specific `--on-existing verify` recovery command for only the remaining closure.
