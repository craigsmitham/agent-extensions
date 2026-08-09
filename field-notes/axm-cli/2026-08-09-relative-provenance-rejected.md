---
subject: axm-cli
key: relative-provenance-rejected
date: 2026-08-09
kind: gap
status: open
---

**Expected:** An OKF concept source could use a bundle-relative path, as the
active OKF authoring guidance explicitly permits relative path-valued
`sources[].resource` fields.
**Actual:** `axm knowledge lint --path
./.axm/extensions/@craigsmitham/knowledge/harness-engineering` rejected
`../explainers/agent-skills.md` and `../explainers/instruction-files.md` with
"sources[0].resource is required and must be a safe absolute URI."
**Gap:** The AXM Knowledge profile rejects a provenance form permitted by the
OKF guidance used to author the bundle.
**Suggests:** Document the stricter AXM profile in `axm help knowledge`, or
accept safe bundle-relative provenance paths consistently with OKF.

Evidence: command exited 1 on 2026-08-09; affected paths were
`guides/agent-skills.md` and `guides/instruction-files.md`.
