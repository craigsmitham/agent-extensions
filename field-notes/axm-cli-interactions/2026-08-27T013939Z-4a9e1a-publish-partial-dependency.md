---
id: 2026-08-27T013939Z-4a9e1a
subject: axm-cli-interactions
key: publish-partial-dependency
observed_at: "2026-08-27T01:39:39Z"
session: 6ff134
kind: gap
status: open
---

**Expected:** `axm publish` should apply the admitted three-package Gen Stack publication set or return complete failure details for any refused item.
**Observed:** The apply result was `ok: false` with `execution.status: partial`: `@craigsmitham/skills/gen-stack@1.10.0` published, `@craigsmitham/knowledge/gen-stack@0.19.0` failed, and `@craigsmitham/packs/gen-stack@2.11.0` was blocked by the failed knowledge dependency. The knowledge failure detail was unavailable because the retained tool output was truncated.
**Impact:** The knowledge and pack releases were delayed and required an exact Registry readback plus the CLI-supplied recovery step; elapsed recovery time was not measured.
**Recovery:** AXM supplied `axm publish --on-existing verify --json --yes @craigsmitham/knowledge/gen-stack @craigsmitham/packs/gen-stack`; recovery outcome was pending at capture time.
**Detected by:** The structured publish result reported `ok: false`, a partial execution, and counts of one published, one failed, and one blocked.
**Observed factors:** AXM CLI 0.28.1; explicit project-workspace selection; Registry `agentxm`; warning-free archive previews immediately preceded apply; the CLI reported that the OS keychain was unavailable and used its restricted credential file.
**Diagnostic evidence:** Contract `publish-result-v3`; process exit status unavailable — output was not retained; skill integrity `sha512-zq3dshe7wAgwJYhrT/bsfJf2zckHxUgf8IcNv7rFd6HHYOIF5iyQpci9SHnzKHEFgsPct1d5USahgMnOq2nufg==`; knowledge failure code, response status, and request identifier unavailable — output was not retained; pack reason `blocked_by_dependency`; remaining items `@craigsmitham/knowledge/gen-stack`, `@craigsmitham/packs/gen-stack`.
**Hypothesis:** unknown

Evidence: One direct AXM Registry mutation admitted three exact candidates but completed only the independent skill before a knowledge failure blocked the dependent pack; AXM itself identified a replay-safe continuation using existing-version verification.
