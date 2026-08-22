---
id: 2026-08-21T163231Z-869c05
subject: axm-cli-interactions
key: knowledge-lint-links-in-fenced-examples
observed_at: "2026-08-21T16:32:31Z"
session: unknown
kind: workaround
status: open
---

**Expected:** Markdown links inside fenced synthetic examples would remain
literal example content rather than be validated as links from the containing
Knowledge concept.
**Observed:** `axm knowledge lint` reported eight missing-path warnings and four
escaping-link warnings for links inside two `markdown` fenced blocks.
**Impact:** Strict workspace lint failed with 12 warnings, requiring one rewrite
of otherwise valid synthetic example content.
**Recovery:** Replace Markdown link syntax in the fenced examples with
backticked paths and state that an implementation should render those paths as
links; validation can then complete.
**Detected by:** `axm knowledge lint --path
.axm/extensions/@craigsmitham/knowledge/software-architecture` and `axm lint
--strict --json`.
**Observed factors:** AXM 0.27.15; the affected links were inside fenced blocks
tagged `markdown`; the targets intentionally described a synthetic repository
outside the Knowledge bundle.
**Hypothesis:** The Knowledge link extractor evaluates Markdown link syntax
without excluding fenced code content.
**Suggests:** Exclude fenced code from authored-link validation or document how
authors should represent synthetic Markdown links in examples.

Evidence: The bundle lint output identified lines 301–309 as missing bundle
paths and lines 374–377 as escaping links, all within fenced example blocks.
