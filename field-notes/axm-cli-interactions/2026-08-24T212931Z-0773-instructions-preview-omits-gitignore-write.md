---
id: 2026-08-24T212931Z-0773
subject: axm-cli-interactions
key: instructions-preview-omits-gitignore-write
observed_at: "2026-08-24T21:29:31Z"
session: unknown
kind: gap
status: open
---

**Expected:** `axm instructions enable --preview --json` would enumerate every
artifact that the identical apply command would write.
**Observed:** Preview listed only `.axm/settings.json`; apply also rewrote
`.gitignore` to add the managed exact-path alias region.
**Impact:** The `.gitignore` mutation could not be reviewed from the preview and
had to be discovered through a post-apply Git diff.
**Recovery:** Inspected the applied diff, confirmed it contained the intended
exact alias entry, and continued the migration.
**Detected by:** Compared the complete preview result with `git diff` after
apply.
**Observed factors:** AXM CLI 0.27.17; project instruction-file management was
already enabled; the legacy recursive ignore region was present and the current
managed alias region was absent.
**Diagnostic evidence:** Preview candidate
`ec3d07ea4937bd48ea3ed7ac947691b65ac9bb4c2352e5e391a76616fbd786de` exited
0 with one ready `.axm/settings.json` step; apply exited 0 and added the
instruction-aliases region to `.gitignore`.
**Hypothesis:** The preview artifact model represents the configuration
transition but omits files reconciled as side effects.
**Suggests:** Include every reconciled artifact and its change in the preview
plan.

Evidence: The before/after diff added the managed
`/CLAUDE.md` ignore entry and its AXM region markers even though `.gitignore`
was absent from the preview result.
