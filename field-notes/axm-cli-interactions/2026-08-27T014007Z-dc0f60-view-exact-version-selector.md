---
id: 2026-08-27T014007Z-dc0f60
subject: axm-cli-interactions
key: view-exact-version-selector
observed_at: "2026-08-27T01:40:07Z"
session: 6ff134
kind: workaround
status: open
---

**Expected:** The AXM Registry-mutation workflow's required exact-version readback could use an exact version in the `axm view` extension selector.
**Observed:** `axm view` treated each `@owner/type/name@version` value as the extension name and returned `not_found`; its help documents only an unversioned extension argument plus fields such as `versions`.
**Impact:** Three read-only commands failed and exact-version verification required a second command shape; elapsed delay was not measured.
**Recovery:** Query each unversioned FQN with the `versions` field and verify that the intended exact version is present.
**Detected by:** All three structured results returned exit status `3`, `ok: false`, and code `not_found`.
**Observed factors:** AXM CLI 0.28.1; public Registry reads; fully-qualified skill, knowledge, and pack identities.
**Diagnostic evidence:** Failed selectors `@craigsmitham/skills/gen-stack@1.10.0`, `@craigsmitham/knowledge/gen-stack@0.19.0`, and `@craigsmitham/packs/gen-stack@2.11.0`; error code `not_found`; suggestion `Check the name, pass --type, or use a fully-qualified name.`
**Hypothesis:** The `view` command does not implement version-qualified selectors even though Registry mutation verification requires exact-version evidence.

Evidence: Three distinct extension types produced the same exit status, error code, and name-resolution behavior from the documented `view` command.
