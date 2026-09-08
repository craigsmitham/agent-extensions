---
id: 2026-09-08T155437Z-k3d8
subject: axm-cli-interactions
key: strict-lint-blocks-skeleton-bundle
observed_at: "2026-09-08T15:54:37Z"
session: 01UzzaTW9g4F9GJ58suYN17H
kind: blocked
status: open
---

**Expected:** A deliberately content-free knowledge bundle skeleton, created by
`axm knowledge new` and conformant with OKF v0.2, to be committable. The bundle
passed the OKF validator with 0 errors and `axm lint` reported `ok: true`.
**Observed:** The repository pre-commit gate runs `axm lint --view git-index
--strict`, which treats the `knowledge/empty-bundle` warning as failing. The
commit was rejected. `axm lint --help` documents no per-rule waiver, suppression,
or acknowledgement flag, so a bundle that `axm knowledge new` can create cannot
be committed in this repository until it holds at least one concept.
**Impact:** The commit was blocked. Resolved by authoring one concept document
(`src/overview.md`) that the requested skeleton had deliberately excluded, which
widened the change beyond what was asked. One extra commit attempt.
**Recovery:** Added a concept document to the bundle. The empty-bundle finding
cleared. Task did not complete, for an unrelated reason recorded separately.
**Detected by:** Pre-commit hook output; `axm lint` JSON result with
`summary.exitCategory: "warnings"` and `ok: false`.
**Observed factors:** axm 0.28.11; skill compatibility `compatible`; gate at
`scripts/check-public-safety.sh` invoking `axm lint --view git-index --strict`;
bundle created minutes earlier by `axm knowledge new` in the same session.
**Diagnostic evidence:** tool version 0.28.11; command surface `axm lint --view
git-index --strict --json`; ruleId `knowledge/empty-bundle`; severity `warning`;
message "Knowledge bundle contains no concept documents to discover.";
`summary.exitCategory` `warnings`; `ok` false; process exit status not supplied,
because the hook printed the JSON result rather than propagating the status to
the transcript.
**Hypothesis:** `axm knowledge new` and `axm lint --strict` may disagree about
whether a freshly scaffolded bundle is a valid intermediate state.
**Suggests:** A per-rule acknowledgement, or exempting a bundle whose manifest
was created in the same change, would let a skeleton land before its content.
