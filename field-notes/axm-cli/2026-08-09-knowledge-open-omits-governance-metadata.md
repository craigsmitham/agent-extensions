---
subject: axm-cli
key: knowledge-open-omits-governance-metadata
date: 2026-08-09
kind: gap
status: open
---

**Expected:** Opening an OKF concept for a context-governance audit would expose
its lifecycle and provenance metadata along with its searchable metadata and
body.
**Actual:** `axm knowledge open ... --json` returned the title, type,
description, tags, relative path, and body but omitted `sources`, `generated`,
`verified`, `status`, and `stale_after`.
**Gap:** A consumer can select and read a concept through AXM but must bypass
that route and inspect canonical Markdown before evaluating its provenance,
freshness, or verification state.
**Suggests:** Include OKF governance fields in concept-open output, or provide
an option that returns the complete parsed frontmatter.

Evidence: `axm knowledge open harness-engineering
practices/context-gardening --json` on 2026-08-09 returned `result.concept`
without the lifecycle and provenance fields present in the canonical concept.
