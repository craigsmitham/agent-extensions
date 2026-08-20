---
id: 2026-08-20T164013Z-h7p2
subject: axm-cli-interactions
key: safety-fixture-drops-case-folded-file
observed_at: "2026-08-20T16:40:13Z"
session: q7d2f9
kind: gap
status: open
---

**Expected:** The public-safety integration fixture would reproduce every tracked file from the Git tree it archives.
**Observed:** On a case-insensitive filesystem, the fixture's fresh `git add -A` omitted tracked `platforms/claude.md` because `.gitignore` contains `**/CLAUDE.md`; Git-index lint then reported the existing link as stale.
**Impact:** The integration suite stopped twice after the release gate had passed, requiring inspection of the generated fixture. Delay was not measured.
**Recovery:** Force-add the archived tree when initializing the fixture so tracked ignored files remain represented, then rerun the suite.
**Detected by:** Comparing the visible fixture files with `git ls-files` after strict AXM lint reported `claude.md` missing.
**Observed factors:** The file existed in the fixture worktree but was absent from its index; `git check-ignore -v` identified `.gitignore:2`; the source repository already tracked the file.
**Hypothesis:** The fixture assumed a fresh add was equivalent to restoring a Git tree, which is false for tracked paths that also match ignore rules.

Evidence: `git -C <fixture> ls-files` omitted only `platforms/claude.md` from that directory while `git -C <fixture> check-ignore -v` matched it to `**/CLAUDE.md`.
