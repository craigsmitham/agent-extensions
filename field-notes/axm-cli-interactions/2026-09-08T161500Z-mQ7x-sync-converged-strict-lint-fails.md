---
id: 2026-09-08T161500Z-mQ7x
subject: axm-cli-interactions
key: sync-converged-strict-lint-fails
observed_at: "2026-09-08T16:15:00Z"
session: session_01MpxZvoWtUGtiYk8xQRiNa9
kind: workaround
status: open
---

**Expected:** `scripts/check-public-safety.sh` asserts a converged workspace
with `axm sync --preview --json` and then runs `axm lint --view workspace
--strict`, so a workspace that sync reports as converged was expected to pass
the strict lint that immediately follows it.
**Observed:** `axm sync --non-interactive` exited 0 with "Synced 1 workspace
item" and `axm sync --preview --json` returned `outcome: "no-op"` with
`counts.failed = 0` and `counts.blocked = 0`, while `axm lint --view workspace
--strict` on the same tree exited 1 with 10 `workspace/managed-file-unowned`
warnings, one per workspace-authored skill directory (`./skills/audit-docs`
through `./skills/temporal-dates`), including nine this session never touched.
`axm lint --view git-index --strict` on the same repository reported "No
findings" and exited 0.
**Impact:** The public-safety gate exits 1 before reaching any of the checks
this task needed verified. Determining whether the failure belonged to this
session's changes took three extra commands and one improvised snapshot run;
not measured beyond that. No package content was affected.
**Recovery:** Materialized the pristine Git index with
`scripts/materialize-git-index.sh` into a scratch directory and ran `axm lint
--view workspace --strict` there; it produced the same 10 warnings and exit 1,
establishing the finding as pre-existing rather than introduced. Reran the
gate from a scratch copy of the script with that one lint line allowed to
fail, which then reported "Public extension safety checks passed for the
workspace view." The task completed with the gate's remaining checks verified
and the strict-lint failure reported rather than forced.
**Detected by:** Non-zero exit status from `bash scripts/check-public-safety.sh`
and the warning list printed above the failure.
**Observed factors:** axm 0.28.11; workspace scope; `axm.json` declares agents
claude-code, codex, cursor, github-copilot-cli, and zed with
`instructionFiles.gitignoreAliases: true`; the repository keeps canonical
skills at `skills/<name>` and projections under `.claude/skills` and
`.agents/skills`; `axm-lock.yaml` records only registry-acquired packages, so
no workspace skill has a lockfile entry; the warnings also appear in a
materialized index snapshot that contains no projections at all.
**Diagnostic evidence:** exit status 1 from `axm lint --view workspace
--strict` and from `bash scripts/check-public-safety.sh`; exit status 0 from
`axm lint --view git-index --strict`; finding `ruleId:
workspace/managed-file-unowned`, `severity: warning`, `kind: advisory`,
`observed: "Agent skill artifact has no AXM ownership proof."`, `expected:
"Agent-directory artifacts have a resolvable AXM ownership proof."`,
`authority: skills/<name>`; retryability: not supplied; suggested recovery:
not supplied.
**Hypothesis:** The ownership rule treats the repository's root `skills/`
directory as an agent projection directory and looks for an ownership proof
that workspace-authored canonical packages never carry, and the rule is
evaluated only in the workspace view, which is why the git-index view is
clean. Sync does not evaluate that rule, so the two commands disagree about
the same tree.
**Suggests:** Either have the rule recognize a canonical workspace package
root as its own authority, or have `axm sync` surface the same advisory it
leaves behind, so a gate that pairs the two commands does not receive
contradictory verdicts.
