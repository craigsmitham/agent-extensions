---
subject: axm-cli-interactions
key: ignored-claude-concept-omitted-from-index
date: 2026-08-14
kind: gap
status: open
---

**Expected:** Staging a complete authored Knowledge package should include every concept that AXM validated and published from the workspace.
**Actual:** The workspace safety gate passed and AXM published the package, but the Git-index gate reported that `platforms/index.md` linked to a missing `claude.md` concept because the repository's `**/CLAUDE.md` ignore pattern also matched the lowercase concept filename.
**Gap:** The workspace and Git-index views selected different package contents without an earlier warning that a canonical authored file was ignored by Git.
**Suggests:** Make the publishing gate identify authored package files excluded by Git before publication, or narrow the repository ignore rule so ordinary lowercase concept files are not excluded.

Evidence: AXM CLI 0.27.4 and the workspace safety gate reported no findings before publication. After `git add -A`, `scripts/check-public-safety.sh --view git-index` reported `knowledge/stale-index-entry` for `src/platforms/index.md:9`; `git check-ignore -v` attributed the omission to `.gitignore:2` and `**/CLAUDE.md`.
