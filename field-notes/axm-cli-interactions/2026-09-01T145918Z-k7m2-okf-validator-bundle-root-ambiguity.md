---
id: 2026-09-01T145918Z-k7m2
subject: axm-cli-interactions
key: okf-validator-bundle-root-ambiguity
observed_at: "2026-09-01T14:59:18Z"
session: 01a05abb-9d2a-75e1-91b9-5d7f5fe344fb
kind: gap
status: open
---

**Expected:** The author-OKF instruction to run its validator over the bundle
root would validate the `knowledge/software-engineering` package whose manifest
declares `bundleRoot: src`.
**Observed:** `python3 .agents/skills/author-okf/scripts/validate_okf.py
knowledge/software-engineering --info --summary` exited 1, treated `README.md`
as a concept without frontmatter, treated `src/index.md` as a nested index with
forbidden frontmatter, and reported that `knowledge/software-engineering/index.md`
was missing. In the same validation pass, `axm knowledge lint --path
./knowledge/software-engineering` exited 0.
**Impact:** The standalone OKF validation required one corrected invocation;
the initial output could be mistaken for bundle conformance failures.
**Recovery:** Validate the declared OKF content root at
`knowledge/software-engineering/src`; final task status was not yet known when
captured.
**Detected by:** The standalone validator's complete diagnostic output and
nonzero process exit status.
**Observed factors:** AXM CLI version 0.28.2; author-OKF skill version in the
workspace; package manifest `bundleRoot` is `src`; no mutation was retried.
**Diagnostic evidence:** Exit status 1; findings `frontmatter-missing` on
`README.md`, `index-frontmatter` on `src/index.md`, and
`discovery-root-missing` for the package root. The AXM knowledge linter reported
“Knowledge validation passed for 1 bundle.”
**Hypothesis:** The standalone validator consumes an OKF content root directly
and does not resolve `bundleRoot` from a surrounding AXM knowledge manifest.
**Suggests:** Clarify the author-OKF validation example for packaged bundles or
teach the validator to resolve a manifest-declared content root.

Evidence: The two validators were run against the same authored package during
one pre-publication validation pass; only the target path interpretation
differed.
