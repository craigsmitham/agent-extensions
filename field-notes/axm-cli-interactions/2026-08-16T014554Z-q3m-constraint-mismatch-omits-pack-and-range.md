---
id: 2026-08-16T014554Z-q3m
subject: axm-cli-interactions
key: constraint-mismatch-omits-pack-and-range
observed_at: "2026-08-16T01:45:54Z"
session: 6faf0876-0105-4599-bf75-e87b41b17574
kind: gap
status: open
---

**Expected:** After bumping a workspace-authored knowledge bundle from 0.2.1 to
0.3.0, `axm lint` findings would name the constraint that no longer matched, or
`axm sync` would reconcile it, since `axm help knowledge` documents bumping the
manifest version as the normal pre-publish step.
**Observed:** `axm lint` reported `workspace/desired-state-reconcilable` and
`workspace/knowledge-state-valid` as `canonical state constraint-mismatch`
without naming the constraint holder or the range. `axm sync --preview` listed
the step as `ready` with `previous version=none; proposed version=0.3.0;
reason=constraint-mismatch`; applying it printed `Already up to date — 2
workspace items` and the two lint findings persisted unchanged.
**Impact:** Roughly ten extra commands to locate the cause: reverted the bump to
confirm it was the trigger, re-bumped via `axm version`, read `axm help
workspace-state`, inspected `.axm/axm-lock.yaml`, then grepped `.axm` and read
`.axm/extensions/@craigsmitham/packs/software-engineering/pack.json` to find the
`^0.2.0` dependency pin. The authoring task itself completed.
**Recovery:** Widened the pack dependency to `^0.3.0` and ran `axm version
@craigsmitham/packs/software-engineering minor`; `axm lint` then reported no
findings and `axm sync` reported materialization up to date.
**Detected by:** `axm lint` failing after a manifest version bump that
`axm sync` claimed to have applied.
**Observed factors:** Bundle settings entry is a bare `workspace:` source with
no version constraint. `.axm/axm-lock.yaml` holds no row for the bundle, and
`axm help workspace-state` states that workspace-authored state does not belong
in the lockfile. The pack `@craigsmitham/packs/software-engineering` lists the
bundle in `dependencies` at `^0.2.0`. `axm lint` was clean before the bump and
clean again after the pack range was widened. Hand-editing the version and
using `axm version` produced the same findings.
**Hypothesis:** The finding is computed from the pack manifest's dependency
range but rendered without the depending pack or the range, and `axm sync`
treats the closure as ready and then as already materialized rather than
blocking on the unsatisfiable constraint.
**Suggests:** Include the depending pack and the unsatisfied range in the
`constraint-mismatch` message.

Evidence: `axm lint` output text `knowledge
'@craigsmitham/knowledge/software-engineering' has canonical state
constraint-mismatch.`; `axm sync --preview --json` candidate
`212bd762ab6e76e228834ff72677b543e1200c4c1339873c5868f492b8b5be42` with
`readyCount: 2`, `blockedCount: 0`, `errorCount: 0`; pack manifest dependency
`"@craigsmitham/knowledge/software-engineering": "^0.2.0"`.
