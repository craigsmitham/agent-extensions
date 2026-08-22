---
id: 2026-08-21T235040Z-k7p3
subject: axm-cli-interactions
key: knowledge-lint-yaml-portability
observed_at: "2026-08-21T23:50:40Z"
session: s-k7p3
kind: gap
status: open
---

**Expected:** `axm knowledge lint` validation of YAML frontmatter would identify
syntax that a general-purpose YAML parser could not read.
**Observed:** AXM reported the bundle valid with zero diagnostics, while Ruby
Psych rejected an inline `generated` mapping whose unquoted timestamp contains
colons.
**Impact:** The evaluation needed one additional parser probe to distinguish
AXM acceptance from YAML portability; elapsed time was not measured.
**Recovery:** Continued with AXM's result and recorded the portability question
separately; the evaluation remains in progress.
**Detected by:** Parsing all concept frontmatter with Ruby 2.6 Psych after the
AXM lint completed.
**Observed factors:** AXM skill metadata targets CLI 0.27.x; the bundle uses OKF
0.2; 19 guide documents use the inline timestamp form.
**Hypothesis:** AXM and Ruby Psych accept different YAML syntax subsets or
versions.

Evidence: `axm knowledge lint --path
./.axm/extensions/@craigsmitham/knowledge/software-architecture --json` exited
0 with `valid: true` and no diagnostics. Ruby Psych raised
`Psych::SyntaxError` at the first inline mapping, whose form was
`generated: { by: codex/gpt-5.6, at: 2026-08-21T22:12:04Z }`.
