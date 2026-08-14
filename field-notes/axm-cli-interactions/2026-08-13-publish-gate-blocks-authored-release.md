---
subject: axm-cli-interactions
key: publish-gate-blocks-authored-release
date: 2026-08-13
kind: blocked
status: dropped
---

**Dropped:** The repository intentionally applies a complete-workspace public-safety gate; the obsolete authored-content lint predicates described here were removed by the v4 workspace model.

**Expected:** `scripts/check-public-safety.sh` would permit an exact new-package
release after package lint passed, while leaving the documented
`workspace/authored-content-unpublished` advisory visible.

**Actual:** the script stopped at `axm lint --view workspace --strict` because
the four newly scaffolded and edited Knowledge packages were also reported as
`workspace/knowledge-state-valid` errors with `locally-modified` state. Three
unrelated pre-existing pack dependency-version findings also blocked the exact
Knowledge release.

**Gap:** the repository guide describes unpublished authored content as an
expected informational pre-publication state, but the complete-workspace strict
gate rejects the same authored packages and unrelated workspace findings before
an exact package selection can be preflighted.

**Suggests:** make the public release gate able to validate an exact intended
package selection, or ensure newly authored content does not also produce a
strict invalid-state error before its first publication.

Evidence: AXM 0.26.7; clean bundle-level `axm knowledge lint` for
`knowledge-management`, `software-architecture`, `product-management`, and
`strategy`; failure reproduced by `scripts/check-public-safety.sh` in the public
extension workspace on 2026-08-13.
