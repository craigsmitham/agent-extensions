---
subject: axm-cli-interactions
key: knowledge-query-type-filter
date: 2026-08-15
kind: workaround
status: open
---

**Expected:** `axm knowledge concepts query --type Pattern` would filter
concepts by their required OKF `type` frontmatter.
**Actual:** The command rejected `--type`; filtering frontmatter requires the
more general `--property /type=Pattern` syntax.
**Gap:** A central concept discriminator has no named query flag, although
other common discriminators such as `--status` and `--tag` do.
**Suggests:** Add a `--type` alias for the `/type` property filter or include a
type-filter example in query help.

Evidence: `axm knowledge concepts query --bundle
@craigsmitham/knowledge/docs --type Pattern` printed “Unrecognized flag:
--type”; command help listed `--property` as the frontmatter filter.
