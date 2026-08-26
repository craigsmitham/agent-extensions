---
id: 2026-08-26T152746Z-m4q8
subject: axm-cli-interactions
key: okf-validator-package-root-contract
observed_at: "2026-08-26T15:27:46Z"
session: s8f3k2
kind: gap
status: open
---

**Expected:** The Author OKF skill's `python3 scripts/validate_okf.py <bundle>` command should accept the project-authored Knowledge package root `knowledge/gen-stack`, whose manifest declares `bundleRoot: src`.
**Observed:** The validator treated `knowledge/gen-stack` itself as the OKF content root, reported package `README.md` as a concept missing frontmatter, reported `src/index.md` as an illegal nested index with frontmatter, and claimed the root `index.md` was missing.
**Impact:** The initial type-inventory validation produced two false errors and required one corrected invocation against `knowledge/gen-stack/src`; no content was changed.
**Recovery:** Use `python3 skills/author-okf/src/scripts/validate_okf.py knowledge/gen-stack/src --summary` for this package layout.
**Detected by:** The validator's structured file paths contradicted `knowledge.json.bundleRoot` and the AXM Knowledge package layout.
**Observed factors:** AXM 0.28.1; project-authored Knowledge package; `knowledge.json` declares `bundleRoot: src`; initial command exited `1`.
**Diagnostic evidence:** command `python3 skills/author-okf/src/scripts/validate_okf.py knowledge/gen-stack --summary`; exit status `1`; errors `README.md [frontmatter-missing]`, `src/index.md [index-frontmatter]`, and warning `index.md [discovery-root-missing]`.
**Hypothesis:** The standalone validator accepts an OKF content root and does not resolve an AXM Knowledge package manifest automatically, while the skill labels its argument as the bundle root.
**Suggests:** Clarify the skill command as `<bundleRoot directory>` or teach the validator to resolve `knowledge.json.bundleRoot` from an AXM Knowledge package root.

Evidence: The package manifest was read before the invocation and explicitly identifies `src` as the content root; the original exit status and diagnostics were retained.
