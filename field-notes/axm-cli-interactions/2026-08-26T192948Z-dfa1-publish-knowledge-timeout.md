---
id: 2026-08-26T192948Z-dfa1
subject: axm-cli-interactions
key: publish-knowledge-timeout
observed_at: "2026-08-26T19:29:48Z"
session: q7m2
kind: workaround
status: open
---

**Expected:** The admitted three-item Gen Stack publication would upload the
unified skill and knowledge bundle, then publish the dependency-resolved pack.
**Observed:** The skill upload succeeded, the knowledge upload exceeded the
registry deadline after one replay-unsafe attempt, and the pack was blocked by
the failed knowledge dependency.
**Impact:** Publication completed for one of three selected items and required
one bounded recovery command for the remaining knowledge bundle and pack.
**Recovery:** AXM supplied an exact recovery using `--on-existing verify` for
the remaining knowledge and pack identities so any ambiguous prior upload is
verified rather than overwritten.
**Detected by:** AXM `publish-result-v3` structured execution output.
**Observed factors:** AXM CLI `0.28.1`; registry `agentxm`; authenticated public
owner `@craigsmitham`; preview status `admitted`; exact selection contained
`@craigsmitham/skills/gen-stack@1.0.0`,
`@craigsmitham/knowledge/gen-stack@0.10.0`, and
`@craigsmitham/packs/gen-stack@2.0.0`.
**Diagnostic evidence:** Overall result `ok=false`, execution status `partial`;
skill status `success`; knowledge failure code `timeout`, class `external`,
`retryable=true`, `attemptCount=1`, `maxAttempts=1`,
`retryStoppedBy=replay-unsafe`; pack status `blocked`, reason
`blocked_by_dependency`; recovery remaining items are the knowledge bundle and
pack.
**Hypothesis:** The larger knowledge archive exceeded the registry request
deadline while the smaller skill archive completed.
