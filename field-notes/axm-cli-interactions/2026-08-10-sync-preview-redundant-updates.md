---
subject: axm-cli-interactions
key: sync-preview-redundant-updates
date: 2026-08-10
kind: gap
status: open
---

**Expected:** `axm help skills` says workspace-authored skill contents are
symlinked into configured agent directories and that `axm sync` is unnecessary
after editing canonical `src/SKILL.md` files.
**Actual:** After editing two canonical skills, `axm sync --preview --json`
proposed `updated` projection steps for both even though `readlink` showed every
projection already pointed to the corresponding canonical `src/` directory.
**Gap:** The preview presents an apparently redundant materialization action
without explaining what state, if any, differs beyond the symlinked content.
**Suggests:** Suppress no-op projection updates for healthy symlinks or explain
the non-content state that the proposed sync would update.

Evidence: `axm sync --preview --json` returned two `ready` steps with
`reason=locally-modified`; `readlink` for the `.agents`, `.claude`, `.cursor`, and
`.github` projections returned the expected relative canonical `src/` target.
