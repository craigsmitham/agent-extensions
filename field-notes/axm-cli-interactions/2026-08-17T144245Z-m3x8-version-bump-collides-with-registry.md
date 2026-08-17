---
id: 2026-08-17T144245Z-m3x8
subject: axm-cli-interactions
key: version-bump-collides-with-registry
observed_at: "2026-08-17T14:42:45Z"
session: 565ef42a
kind: workaround
status: open
---

**Expected:** `axm version <fqn> patch` from the workspace manifest version
produces a publishable version, per the docs/publishing.md flow (bump, then
preview, then publish).
**Observed:** `axm publish ... --preview` failed preflight with "version 0.0.3
is already published for @craigsmitham/skills/craft-effect-v4. Published
versions are immutable." The workspace manifest was at 0.0.2 while the
registry already had 0.0.3 (`axm view ... versions`: 0.0.1–0.0.3), so the
local patch bump landed on a taken version. The knowledge bundle had the same
drift (workspace 0.1.0, registry 0.1.1) but its minor bump to 0.2.0 happened
to clear it.
**Impact:** One failed publish preview; one extra version bump and a pack
dependency-constraint edit to recover. Not measured beyond that.
**Recovery:** Bumped the skill again to 0.0.4, updated the pack constraint
`^0.0.3` → `^0.0.4` (pre-1.0 caret is an exact pin at 0.0.x), re-previewed.
Task continued.
**Detected by:** `execution.outcomes[].reason: version_exists` in the
`--preview --json` output; confirmed with `axm view <fqn> versions`.
**Observed factors:** Workspace manifests (skill 0.0.2, knowledge 0.1.0)
behind the registry's published latest (0.0.3, 0.1.1) at session start;
`axm version` computes from the local manifest only; `axm lint` and
`axm outdated` had reported no findings about the drift.
**Hypothesis:** A previous release bumped and published without the manifest
change landing back in this repository's main branch, and `axm version` does
not consult the registry when computing the next version.
**Suggests:** A registry-aware warning in `axm version` (or a lint rule) when
the computed version is already published for the selector.

Evidence: preview JSON `execution.outcomes` for
@craigsmitham/skills/craft-effect-v4 with `reason: version_exists` and the
conflict message quoted above; `axm view @craigsmitham/skills/craft-effect-v4
versions` listing 0.0.3/0.0.2/0.0.1; git history showing skill.json at 0.0.2
on main (`5a83a4d`).
