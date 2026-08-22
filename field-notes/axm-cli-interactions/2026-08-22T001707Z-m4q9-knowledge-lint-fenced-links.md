---
id: 2026-08-22T001707Z-m4q9
subject: axm-cli-interactions
key: knowledge-lint-fenced-links
observed_at: "2026-08-22T00:17:07Z"
session: s-k7p3
kind: workaround
status: open
---

**Expected:** `axm knowledge lint` would ignore Markdown links inside fenced
code because they are example source text rather than links in the containing
concept.
**Observed:** AXM reported 19 broken or escaping links from fenced Markdown
examples in one concept, including links whose targets exist only in the
synthetic example corpus.
**Impact:** The reference corpus had to be moved from fenced examples to a
physical nested fixture before bundle validation could continue; elapsed time
was not measured.
**Recovery:** Replaced the fenced file bodies with linked fixture files and
continued validation.
**Detected by:** Running `axm knowledge lint --path` with JSON output after
adding the reference concept.
**Observed factors:** The enclosing document used `markdown` fenced code
blocks; AXM reported the source lines within those fences as link diagnostics.
**Hypothesis:** The knowledge linter's link extraction does not exclude fenced
code blocks.
**Suggests:** Link validation could ignore Markdown syntax inside fenced code
blocks.

Evidence: the lint completed with `valid: true` and emitted 19 link warnings;
18 pointed into fenced corpus file bodies and one pointed to the profile's
literal placeholder link.
