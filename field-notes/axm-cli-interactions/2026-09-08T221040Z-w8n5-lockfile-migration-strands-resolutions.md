---
id: 2026-09-08T221040Z-w8n5
subject: axm-cli-interactions
key: lockfile-migration-strands-resolutions
observed_at: "2026-09-08T22:10:40Z"
session: 01BJvgpqyTJjsDzUYBVeWEct
kind: gap
status: open
---

**Expected:** `axm install @craigsmitham/skills/spot-spew` in a workspace whose
`axm-lock.yaml` declared `lockfileVersion: 6` failed with "declares version 6,
but this AXM supports version 7", and its own guidance said: "Preserve the
incompatible lockfile outside its authoritative path, review the desired
workspace intent, then remove the incompatible file", then `axm sync --preview`
and `axm sync`. Following those four steps was expected to leave a reconciled
workspace.
**Observed:** `axm sync --preview` previewed 6 items and reported success, but
`axm sync` failed: "Desired state cannot be enumerated completely; fix pack and
declaration problems first: @craigsmitham/packs/docs: The configured external
Pack has no matching accepted resolution." One unit `failed` with "effects were
restored" and five were `blocked by earlier step failure`. Re-running `axm sync`
reproduced the same failure. `axm lint --json` then reported `ok: false` with 12
errors — 10 `workspace/desired-state-reconcilable` and 2
`workspace/skills-lockfile-aligned` — covering every configured skill and pack
except the one installed afterwards.
**Impact:** The workspace `vineyard-software/vineyard-software-internal` was
left with no accepted resolution for 2 skills and 4 packs between the lockfile
removal and the recovery — a state worse than the original blocked-but-committed
one. Three extra commands (`sync`, `sync`, `lint`) and one preview were spent
before recovery. The requested spot-spew install itself succeeded. Elapsed cost
not measured.
**Recovery:** Bare `axm install` (documented as "or reinstall configured
extensions") resolved all 8 configured extensions and wrote a
`lockfileVersion: 7` lockfile. `axm lint` then returned `ok: true` with only
`workspace/managed-file-unowned` warnings, and
`axm sync --preview --fail-on-change` reported converged. The task completed.
**Detected by:** The `✖ Failed to sync 6 workspace items` line and the
subsequent `axm lint --json` `ok: false` result with error-severity findings.
**Observed factors:** axm 0.28.11 (with `AXM_UPDATE_AVAILABLE latest=0.28.12`
banner); target workspace declared 3 skills and 4 packs, all registry-sourced
from `@craigsmitham`, with `packs/software-engineering` pinned at `@2.1.1`; the
workspace Git tree was clean and the lockfile was tracked; the v6 lockfile had
been copied aside before removal.
**Diagnostic evidence:** tool version 0.28.11; command surface `axm sync`;
affected artifacts `@craigsmitham/packs/docs`, `@craigsmitham/packs/field-notes`,
`@craigsmitham/packs/effect-v4`, `@craigsmitham/packs/software-engineering`,
`@craigsmitham/skills/author-okf`, `@craigsmitham/skills/improve-whatever`;
error class `conflict`; lint rule IDs `workspace/desired-state-reconcilable` and
`workspace/skills-lockfile-aligned`; request or correlation ID not supplied;
retryability not supplied — a second identical `axm sync` reproduced the
failure; recovery command `axm install`.
**Hypothesis:** unknown — `sync` may reconcile against accepted resolutions
without being able to create them, so a workspace with external sources and no
lockfile cannot be recovered by `sync` alone; not investigated.
**Suggests:** The recovery guidance printed with the lockfile-version error
names `axm sync --preview` and `axm sync` but not `axm install`, which was the
command that actually restored resolution.

Evidence: the lockfile-version error and its printed recovery steps, the
`axm sync` failure text with its failed and blocked units, the `axm lint --json`
error findings, and the bare `axm install` run plus the converged
`sync --preview --fail-on-change` and `ok: true` lint that followed it.
