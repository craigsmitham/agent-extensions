---
id: 2026-08-23T031017Z-f1ebb8
subject: axm-cli-interactions
key: publish-recovery-registry-failure
observed_at: "2026-08-23T03:10:17Z"
session: 0efd7f2b-d94e-46f7-9d15-270734a73e53
kind: blocked
status: open
---

**Expected:** The human-authorized recovery command returned by the preceding partial publish should publish or verify all 6 remaining items.
**Observed:** The command exited 10 after publishing 3 releases and verifying 1 existing release; the `field-notes` upload failed with Registry HTTP 500 and the `improve-whatever` upload timed out.
**Impact:** Two skill releases remain unpublished and require another separately authorized recovery invocation.
**Recovery:** AXM returned a narrower recovery command for the 2 failed skills. It was preserved but not run because AXM's mutation-retry guidance prohibits an outer automatic retry loop; the task did not fully complete.
**Detected by:** The fixed `ok: false` JSON result and process exit 10.
**Observed factors:** Identity probe succeeded for the default registry; publication-set preflight was admitted; both failed uploads reported `retryable: true`, `maxAttempts: 1`, and `retryStoppedBy: replay-unsafe`.
**Hypothesis:** unknown

Evidence: `counts` reported `selected: 6`, `published: 3`, `alreadyPublished: 1`, `blocked: 0`, `failed: 2`, and `pending: 0`. Published items were `@craigsmitham/skills/author-architecture-docs@3.1.0`, `@craigsmitham/skills/setup-architecture-docs@0.5.0`, and `@craigsmitham/packs/software-architecture@0.6.0`; `@craigsmitham/skills/audit-docs@0.1.2` was verified existing. Remaining items were `@craigsmitham/skills/field-notes@0.2.2` and `@craigsmitham/skills/improve-whatever@0.0.8`.
