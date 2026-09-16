---
id: 2026-09-16T214850Z-8wh946
subject: axm-cli-interactions
key: lint-skill-cli-incompatible
observed_at: "2026-09-16T21:48:50Z"
session: 27f43628-ab23-444e-96a8-8d6e4bbd8a99
kind: observation
status: open
---

**Expected:** `axm lint --json` would report `ok: true` or only package findings, so the ownership of `skills/spec` could be confirmed before editing it.
**Observed:** The result was `ok: false` with the error `workspace/axm-skill-compatible`: the bundled official AXM skill 0.29.4 declares `>=0.29.0 <0.30.0`, and the running CLI is 0.31.1. The only other findings were four `project-outputs-not-shadowed` warnings for `axm` projections, and none concerned `skills/spec`.
**Impact:** Neutral for this task. Ownership was confirmed from `axm.json` (`"spec": "workspace"`) and the `.claude/skills/spec` symlink to `skills/spec/src`. The workspace lint stays failing until the skill is refreshed, which could hide new errors.
**Outcome:** Editing `skills/spec` went ahead. The compatibility recovery was not applied, because it is outside the task's authority.
**Recovery:** not needed
**Detected by:** Structured `axm lint --json` output during preflight before editing a managed skill.
**Observed factors:** axm 0.31.1; a prior note in this subject recorded axm 0.29.4 on 2026-09-15; project scope; `axm.json` has uncommitted changes adding `spec`.
**Diagnostic evidence:** ruleId `workspace/axm-skill-compatible`; reasonCode `cli-version-incompatible`; cliVersion 0.31.1; skillVersion 0.29.4; source `bundled:@agentxm/skills/axm@0.29.4`; recovery nextAction `axm skills install @agentxm/skills/axm --bundled --preview`; exit status unavailable, because output was piped through `head`.
**Hypothesis:** The CLI was upgraded without reinstalling the bundled skill.

Evidence: the `axm lint --json` result fields above, from one run in this session.
