---
id: 2026-08-26T232235Z-q7d4
subject: axm-cli-interactions
key: bulk-publish-preview-integrity-drift
observed_at: "2026-08-26T23:22:35Z"
session: w3p9
kind: blocked
status: open
---

**Expected:** `axm publish --preview --json --non-interactive` would produce an actionable publication set for every workspace-authored extension, as directed by `axm help publish`.
**Observed:** The preview selected 26 authored extensions, failed 16 with immutable-version integrity drift, blocked the other 10 during authoritative preflight, and returned no available publication set.
**Impact:** Publishing all workspace-authored extensions was prevented; no Registry upload occurred. The delay was not measured.
**Recovery:** Not yet restored at capture time; the workflow continued with the supported version lifecycle.
**Detected by:** Structured preview result and process exit status.
**Observed factors:** AXM CLI 0.28.1; project scope; Registry `agentxm`; owner `@craigsmitham`; preview mode; `--non-interactive`; workspace lint was clean and skill compatibility was compatible.
**Diagnostic evidence:** Command exit status `6`; result `ok: false`; contract `publish-result-v3`; selection counts `considered: 28`, `included: 26`, `unmanaged: 1`; result counts `selected: 26`, `published: 0`, `alreadyPublished: 0`, `blocked: 10`, `failed: 16`, `unknown: 0`; failure reason `integrity_drift`; error code `conflict`; error class `user`; retryable `false`; affected identities were `@craigsmitham/skills/field-notes@0.2.2`, `@craigsmitham/skills/improve-whatever@0.0.8`, `@craigsmitham/skills/question@0.1.2`, `@craigsmitham/skills/temporal-dates@0.1.0`, `@craigsmitham/subagents/researcher@0.0.1`, `@craigsmitham/rules/field-notes@0.2.2`, `@craigsmitham/rules/use-effect-v4@0.1.0`, `@craigsmitham/knowledge/field-notes@0.2.1`, `@craigsmitham/knowledge/workflow-automation@0.2.0`, `@craigsmitham/knowledge/effect-v4@0.5.1`, `@craigsmitham/knowledge/knowledge-management@0.1.0`, `@craigsmitham/knowledge/product-management@0.1.0`, `@craigsmitham/knowledge/strategy@0.2.1`, `@craigsmitham/packs/effect-v4@0.6.0`, `@craigsmitham/packs/field-notes@0.2.0`, and `@craigsmitham/packs/qrspi@0.1.0`.
**Hypothesis:** The local package archives changed without corresponding version increments.

Evidence: The authoritative preview returned one `integrity_drift` failure for each listed immutable version and reported all remaining candidates as `blocked_by_preflight`; no upload was attempted.
