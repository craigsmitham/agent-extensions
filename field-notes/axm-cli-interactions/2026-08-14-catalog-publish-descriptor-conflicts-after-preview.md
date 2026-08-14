---
subject: axm-cli-interactions
key: catalog-publish-descriptor-conflicts-after-preview
date: 2026-08-14
kind: gap
status: open
---

**Expected:** Applying the exact catalog-wide selection accepted by publish preview should publish every pending artifact or reject the selection before uploading any artifact.
**Actual:** AXM published two knowledge bundles, then failed nine pending artifacts because their publication descriptors had changed after preview, returned an untyped internal error for another bundle, and blocked five packs.
**Gap:** A clean preview did not remain applicable to the immediately following identical publish, and apply left the catalog in a partial release state.
**Suggests:** Bind apply to the reviewed preview descriptor and make the selected publication atomic, or refresh dependent descriptors after each successful job and return a typed idempotent retry plan.

Evidence: AXM CLI 0.27.4 previewed 45 authored public packages with 28 already published, 17 pending, and no failures or blocks. The identical `--authored --owner @craigsmitham --visibility public --on-existing verify` apply published `knowledge/context-engineering@0.1.0` and `knowledge/eval-engineering@0.1.0`, then reported 15 failures: nine `publication descriptor changed after preview` conflicts, one Registry `internal` error for `knowledge/prompt-engineering@0.1.0`, and five packs blocked by earlier job failure.
