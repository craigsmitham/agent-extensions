---
id: 2026-08-27T234415Z-22d7
subject: axm-cli-interactions
key: publish-authored-flag
observed_at: "2026-08-27T23:44:15Z"
session: unknown
kind: gap
status: open
---

**Expected:** `docs/publishing.md` documents `axm publish --authored --owner
@craigsmitham --preview --json` as the catalog-wide release preflight.
**Observed:** AXM 0.28.1 `axm publish --help` does not expose an `--authored`
flag; publication already selects workspace-authored extensions and exposes the
`--owner` filter.
**Impact:** The documented command could not be used as written; release
selection required one help lookup and a syntax adjustment.
**Recovery:** Used the authoritative 0.28.1 help and retained the documented
publisher boundary with `--owner @craigsmitham`.
**Detected by:** Comparing the repository publishing guide with live
`axm publish --help` output during release preflight.
**Observed factors:** The workspace AXM skill and CLI both report version
0.28.1 and compatible status.
**Diagnostic evidence:** Command `axm publish --help`; exit status 0; available
selection flags included `--owner`, `--type`, and `--exclude`; `--authored` was
absent.
**Hypothesis:** The guide retained syntax from an earlier CLI contract.

Evidence: `docs/publishing.md` contains the `--authored` example, while the
installed AXM 0.28.1 help describes publication as workspace-authored-only and
omits that flag.
