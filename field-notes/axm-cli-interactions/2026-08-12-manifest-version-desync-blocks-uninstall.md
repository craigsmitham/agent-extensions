---
subject: axm-cli-interactions
key: manifest-version-desync-blocks-uninstall
date: 2026-08-12
kind: gap
status: open
---

**Expected:** After `axm version @craigsmitham/skills/craft-effect-v4 set 0.1.0`
reported `Updated skill ... 0.0.1 -> 0.1.0`, the workspace version state would be
consistent and unrelated commands would keep working.

**Actual:** `axm version` updated only `skill.json`. The lockfile and
`trust.json` stayed at `0.0.1`. Every subsequent
`axm uninstall @craigsmitham/skills/effect-v4-<name>` then failed with
`Cannot decide pack retention because the desired pack graph is incomplete.
(conflict)` — a message naming neither the version, the manifest, nor the skill
that was actually mismatched. The uninstall printed a full `removed:` file plan
and `✔ Processed Uninstall skill` before failing, and exited 0, so a loop that
checked output or exit status recorded 20 successes while nothing was removed.

**Gap:** Manifest version is writable through `axm version`, but no command
observed here reconciles the lockfile for a workspace-authored package.
`axm install` refuses with `Cannot resolve pack dependencies from non-registry
source (usage)`, `axm lint --fix` applied 0 fixes, and `axm packs repair
--accept-current` failed with the version conflict itself. The only reachable
consistent state was reverting the manifest to `0.0.1`. The downstream error
surfaces at an unrelated command and does not name the desynced package.

**Suggests:** Make `axm version` update the lockfile and trust baseline for
workspace-authored packages in the same operation, or fail closed when it
cannot. Failing that, have the pack-retention conflict name the package and
versions that disagree, and make `axm uninstall` exit non-zero when plan
execution fails.

Evidence:
- AXM 0.26.6, workspace `/Users/craig/Code/craigsmitham/agent-extensions`,
  project scope.
- `axm version @craigsmitham/skills/craft-effect-v4 set 0.1.0` →
  `✔ Updated skill @craigsmitham/skills/craft-effect-v4 0.0.1 -> 0.1.0`.
- `.axm/axm-lock.yaml` `craft-effect-v4.version` remained `0.0.1`;
  `.axm/trust.json` `skill:craft-effect-v4.resolvedVersion` remained `0.0.1`.
- `axm uninstall @craigsmitham/skills/effect-v4-config --yes` →
  `✔ Processed Uninstall skill`, then `✖ Plan execution failed`, then
  `● effect-v4-config: Cannot decide pack retention because the desired pack
  graph is incomplete. (conflict)`; shell exit status `0`; package directory
  still present.
- `axm packs repair @craigsmitham/packs/effect-v4 --accept-current` →
  `✖ Pack dependency @craigsmitham/skills/craft-effect-v4 requires ^0.1.0, but
  trusted workspace state has 0.0.1. (conflict)`.
- After reverting `skill.json` to `0.0.1`, the identical uninstall succeeded:
  `✔ Uninstalled skill effect-v4-config for 5 agents`.
- Whether a documented command reconciles workspace lockfile versions is
  unknown; `axm help basic-usage` and the `axm` skill quick reference were not
  exhaustively searched for one.
