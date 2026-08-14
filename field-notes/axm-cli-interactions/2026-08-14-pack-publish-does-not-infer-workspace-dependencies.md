---
subject: axm-cli-interactions
key: pack-publish-does-not-infer-workspace-dependencies
date: 2026-08-14
kind: gap
status: open
---

**Expected:** `axm help packs` says publishing an authored pack publishes included workspace-authored dependencies first, so previewing the authored `effect-v4` pack should include its new authored skill and knowledge dependencies.
**Actual:** `axm publish @craigsmitham/packs/effect-v4 --preview --visibility public --json` rejected the pack because the new knowledge dependency did not yet exist in the Registry.
**Gap:** Dependency inclusion is opt-in through the pack-specific `--include-dependencies` flag, but the lifecycle guidance describes it as the default and generic publish help does not expose that flag.
**Suggests:** Align the documented default with CLI behavior, or surface the required pack dependency flag and a recovery suggestion in generic publish help and failure output.

Evidence: With the workspace-authored pack at 0.2.0 and both declared workspace dependencies present, AXM CLI 0.27.3 exited 9 during preview and reported `Dependency @craigsmitham/knowledge/effect-v4 requests range "^0.1.0", but that extension does not exist in the registry.`
