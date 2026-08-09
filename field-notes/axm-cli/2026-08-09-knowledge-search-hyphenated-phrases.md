---
subject: axm-cli
key: knowledge-search-hyphenated-phrases
date: 2026-08-09
kind: workaround
status: open
---

**Expected:** A natural multiword query would find a concept whose body and tags contain the same terms, including a hyphenated form.
**Actual:** `axm knowledge search "specification source of truth" --json` and `axm knowledge search "spec as source" --json` returned zero items, while `axm knowledge search "source-of-truth" --json` returned the spec-driven development concept.
**Gap:** Search token or phrase matching makes common unhyphenated wording miss content indexed with a hyphenated term, and the help does not explain the matching semantics.
**Suggests:** Normalize hyphenated and whitespace-separated terms equivalently, or document the query syntax and matching behavior in `axm knowledge search --help`.

Evidence: All commands exited 0 in the project workspace; the zero-result responses reported `"count": 0`, while the hyphenated query reported the concept `domains/software-engineering/practices/spec-driven-development`.
