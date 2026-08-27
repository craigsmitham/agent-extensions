---
id: 2026-08-26T232618Z-t6k2
subject: axm-cli-interactions
key: publish-recovery-partial
observed_at: "2026-08-26T23:26:18Z"
session: w3p9
kind: workaround
status: open
---

**Expected:** The AXM-supplied six-item recovery command would finish all items left by the initial partial publication.
**Observed:** The recovery published three items and verified one existing item, but `@craigsmitham/knowledge/gen-stack@0.17.0` failed again and blocked `@craigsmitham/packs/gen-stack@2.9.0`.
**Impact:** Two extensions remained unpublished and required another bounded Registry operation; elapsed delay was not measured.
**Recovery:** AXM supplied `axm publish --on-existing verify --json --non-interactive --yes @craigsmitham/knowledge/gen-stack @craigsmitham/packs/gen-stack`; recovery had not yet run at capture time.
**Detected by:** Structured recovery result and process exit status.
**Observed factors:** AXM CLI 0.28.1; Registry `agentxm`; project scope; explicit six-item selection; existing-version policy `verify`; public visibility preserved.
**Diagnostic evidence:** Command exit status `16`; result `ok: false`; contract `publish-result-v3`; mode `apply`; counts `selected: 6`, `published: 3`, `alreadyPublished: 1`, `blocked: 1`, `failed: 1`, `unknown: 0`; failed identity `@craigsmitham/knowledge/gen-stack@0.17.0`; blocked identity `@craigsmitham/packs/gen-stack@2.9.0`; direct failure details unavailable — output was not retained; recovery listed the same two remaining items and the pack as a blocked dependent.
**Hypothesis:** unknown

Evidence: The recovery result advanced four of six selected items and returned a narrower `--on-existing verify` recovery command for the remaining dependency closure.
