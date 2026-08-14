---
subject: axm-cli-interactions
key: pack-release-partially-publishes-after-clean-preview
date: 2026-08-14
kind: gap
status: open
---

**Expected:** Applying the exact dependency-inclusive pack selection accepted by publish preview should publish the new knowledge, skill, and pack in dependency order without leaving a partial release.
**Actual:** AXM published the knowledge bundle, then reported an unspecified Registry `internal` error for the skill and blocked the pack, leaving one of three selected artifacts published.
**Gap:** Preflight did not detect the skill failure, and apply did not preserve all-or-nothing release state across the selected pack graph.
**Suggests:** Make dependency-inclusive pack publication atomic, or return a stable typed failure with a verified retry command that tolerates successfully published earlier jobs.

Evidence: AXM CLI 0.27.3 previewed three pending public artifacts successfully. The identical apply exited 10 after publishing `@craigsmitham/knowledge/effect-v4@0.1.0`; `@craigsmitham/skills/craft-effect-v4@0.0.1` failed with `An unexpected error occurred. (internal)`, and `@craigsmitham/packs/effect-v4@0.2.0` was `blocked by earlier job failure`.
