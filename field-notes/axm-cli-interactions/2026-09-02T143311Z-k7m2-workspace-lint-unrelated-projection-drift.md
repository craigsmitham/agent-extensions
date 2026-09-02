---
id: 2026-09-02T143311Z-k7m2
subject: axm-cli-interactions
key: workspace-lint-unrelated-projection-drift
observed_at: "2026-09-02T14:33:11Z"
session: k7m2
kind: gap
status: open
---

**Expected:** `axm lint --json` in a fresh, clean checkout would report only
drift caused by the software-engineering knowledge changes in progress.
**Observed:** Lint also reported a missing `CLAUDE.md` instruction target and a
stale `workspace:@craigsmitham/subagents/researcher` projection.
**Impact:** The workspace-wide lint result could not serve as a clean validation
of the bounded knowledge and pack change; one scoped validation and later
convergence step were required.
**Recovery:** Continue with the already-passing package-scoped knowledge lint,
then run the normal AXM synchronization and revalidate the complete candidate.
The task remains in progress.
**Detected by:** `axm lint --json` exited nonzero after the authored knowledge
package passed `axm knowledge lint --path knowledge/software-engineering --json`.
**Observed factors:** AXM CLI 0.28.4; compatible bundled AXM skill 0.28.1; clean
checkout before the bounded authoring work; lint reported two errors and one
warning.
**Diagnostic evidence:** exit category `errors`; rules
`workspace/projections-current` for `subagent:researcher` and
`workspace/instructions-target-current` for `CLAUDE.md`; the AGENTS knowledge
projection was also stale after the intended manifest-description change.
**Hypothesis:** unknown

Evidence: The unrelated instruction and subagent findings were both present in
the retained structured lint result and are outside the two knowledge guides
and software-engineering pack being authored.
