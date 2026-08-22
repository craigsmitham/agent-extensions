---
id: 2026-08-22T234934Z-w8m2
subject: axm-cli-interactions
key: fork-projects-package-root
observed_at: "2026-08-22T23:49:34Z"
session: codex-v3p9
kind: workaround
status: open
---

**Expected:** Enabling a forked Agent Skill would project each agent-native skill link to the package's `src/` directory, where `SKILL.md` is discoverable.
**Observed:** `axm fork` followed by `axm skills enable` created four links to the canonical package root; each lacked `SKILL.md`, while `axm skills show`, `axm lint`, and `axm sync --preview` reported the projections current.
**Impact:** The successor skill was not agent-discoverable until four projected links were corrected manually, despite all AXM checks passing.
**Recovery:** Retargeted the four tracked projections to the canonical package's `src/` directory; each then resolved `SKILL.md`, and `axm sync --preview` remained a no-op.
**Detected by:** Final diff review compared the old and new symlink targets, followed by direct `SKILL.md` existence checks.
**Observed factors:** AXM CLI and installed AXM skill version 0.27.15; project scope; workspace-authored skill forked from another workspace-authored skill; five configured agents with four shared projection paths.
**Hypothesis:** The fork or enable path materializes the canonical package root instead of the skill runtime payload and current-state checks do not validate the target suffix.
**Suggests:** Project `src/` for forked skills and validate that every enabled skill projection exposes a root `SKILL.md`.

Evidence: The generated target omitted `/src`, all four root `SKILL.md` checks failed, comparable managed skills targeted `/src`, and the corrected links passed the same checks without reconciliation drift.
