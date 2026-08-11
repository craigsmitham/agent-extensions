---
subject: axm-cli-interactions
key: skills-new-reorders-settings
date: 2026-08-11
kind: gap
status: open
---

**Expected:** `axm skills new prune-work` should add the new skill declaration
while preserving unrelated `.axm/settings.json` structure.
**Actual:** The command moved the unchanged top-level `lint` block from before
`skills` to after `packs`, creating an unrelated ordering diff.
**Gap:** The resulting JSON is semantically equivalent, but the mutation adds
review noise outside the requested skill declaration.
**Suggests:** Preserve existing top-level key order when rewriting settings, or
make the canonical ordering explicit and apply it through a dedicated formatter.

Evidence: In a clean worktree, `axm skills new prune-work --owner
@craigsmitham --yes --non-interactive --json` with AXM 0.25.8 added
`skills.prune-work` and also relocated the unchanged `lint.rules` object.
