---
id: 2026-08-17T150629Z-k3f7
subject: axm-cli-interactions
key: outdated-subcommand-missing
observed_at: "2026-08-17T15:06:29Z"
session: 550e2604
kind: gap
status: open
---

**Expected:** `axm outdated` would list extensions with available updates; the
axm skill's quick reference table documents it as "Show extensions with
available updates | `axm outdated`".
**Observed:** `axm outdated` exited with code 2 and "Unknown subcommand
\"outdated\" for \"axm\""; the printed command list has no equivalent
subcommand.
**Impact:** One failed invocation while checking whether effect pack
dependencies were current; work rerouted through the lockfile and
`axm view <fqn> versions` per dependency. Extra steps: 1 failed command plus
manual per-dependency version comparison; elapsed time not measured.
**Recovery:** Compared workspace manifest versions against
`axm view @craigsmitham/knowledge/effect-v4 versions` and
`axm view @craigsmitham/skills/craft-effect-v4 versions` output; task
completed.
**Detected by:** CLI error output on direct invocation.
**Observed factors:** Skill doc at `~/.claude/skills/axm` (loaded via the axm
skill this session) lists `axm outdated` and `axm install`/`axm update`
without a type prefix; the CLI's top-level command list includes `install`,
`update`, and `view` but no `outdated`.
**Hypothesis:** Skill quick reference documents a subcommand that was renamed
or not yet shipped in the installed CLI version.
**Suggests:** Align the axm skill quick reference with the installed CLI's
actual subcommand set.

Evidence: `axm outdated` → exit 2, "Unknown subcommand \"outdated\" for
\"axm\"" (2026-08-17, this workspace); `axm view @craigsmitham/packs/effect-v4
versions --json` succeeded in the same session, showing the CLI itself was
operational.
