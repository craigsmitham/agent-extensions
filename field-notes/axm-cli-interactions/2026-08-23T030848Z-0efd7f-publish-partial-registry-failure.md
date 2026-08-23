---
id: 2026-08-23T030848Z-0efd7f
subject: axm-cli-interactions
key: publish-partial-registry-failure
observed_at: "2026-08-23T03:08:48Z"
session: 0efd7f2b-d94e-46f7-9d15-270734a73e53
kind: blocked
status: open
---

**Expected:** `axm publish --yes --json --non-interactive` should publish or verify every admitted workspace-authored extension after successful identity and selection preflight.
**Observed:** The command exited 16 after publishing 3 releases and verifying 23 existing releases; 5 uploads failed with Registry `internal` or `timeout` responses, and 1 dependent pack was blocked.
**Impact:** The requested bulk publish completed only partially. Six selected items remain unpublished or blocked and require a separate human-authorized recovery invocation.
**Recovery:** AXM returned an exact recovery command for the 5 failed skills and the blocked pack. It was preserved but not run because AXM's mutation-retry guidance prohibits an outer automatic retry loop; the task did not fully complete.
**Detected by:** The fixed `ok: false` JSON result and process exit 16.
**Observed factors:** Identity probe succeeded for the default registry; publication-set preflight was admitted; upload execution returned retryable failures with `maxAttempts: 1` and `retryStoppedBy: replay-unsafe`.
**Hypothesis:** unknown

Evidence: `counts` reported `selected: 32`, `published: 3`, `alreadyPublished: 23`, `blocked: 1`, `failed: 5`, and `pending: 0`. The remaining items were `@craigsmitham/skills/audit-docs`, `@craigsmitham/skills/author-architecture-docs`, `@craigsmitham/skills/field-notes`, `@craigsmitham/skills/improve-whatever`, `@craigsmitham/skills/setup-architecture-docs`, and `@craigsmitham/packs/software-architecture`.
