---
id: 2026-08-16T020501Z-w9d
subject: axm-cli-interactions
key: sync-half-applies-pack-upgrade-then-fails
observed_at: "2026-08-16T02:00:12Z"
session: 6faf0876-0105-4599-bf75-e87b41b17574
kind: blocked
status: open
---

**Expected:** `axm sync` would reconcile the workspace or block without writing,
per `axm help workspace-state`: "A handled failure or interruption restores
protected targets," and "Sync may resolve a desired external extension once when
no accepted row exists. After acceptance, reinstall and sync use that exact
identity; only update may advance it."
**Observed:** `axm sync` advanced accepted resolution for
`@agentxm/packs/agent-engineering` from 0.2.0 to 0.3.0 and its members
`prompt-engineering` and `harness-engineering` from 0.1.1 to 0.2.0 in
`.axm/axm-lock.yaml`, then failed: `Plan execution failed` /
`@agentxm/packs/agent-engineering: Pack transition left its desired member graph
incomplete (internal)`. The lockfile retained the advanced versions and
integrity hashes; no canonical content changed. `axm lint` went from `No
findings` to three findings and stayed there.
**Impact:** Blocked the documented pre-release step
`axm update @agentxm/skills/axm --ignore-release-age`, which reported
`Blocker: incomplete-graph` with `relevantProblems:
["pack-manifest-content-mismatch"]` and applied nothing. Release work stopped
until the workspace was restored; that step was never completed. Six extra
commands to diagnose and recover.
**Recovery:** `git checkout -- .axm/axm-lock.yaml` restored the committed
accepted resolution and `axm lint` returned `No findings`. Publishing then
proceeded with the AXM CLI at its current version 0.27.5 and the workspace AXM
skill left un-updated.
**Detected by:** `axm lint` failing immediately after `axm sync` reported
`Plan execution failed`.
**Observed factors:** `axm lint` reported `No findings` immediately before the
`axm update` attempt. `axm upgrade` reported AXM already up to date at 0.27.5
(Homebrew). The failing pack and its members are registry packages owned by
`@agentxm`, unrelated to the packages being released. `axm sync --preview`
listed all three items as `ready` with `blockedCount: 0` and `errorCount: 0`
before the failing apply. `git status` showed `.axm/axm-lock.yaml` as the only
generated file modified by the failed apply.
**Hypothesis:** The pack transition writes accepted resolution before validating
the resulting member graph, and its rollback path does not restore the lockfile
when the transition fails with this internal error.
**Suggests:** unknown.

Evidence: lockfile diff advancing `@agentxm/packs/agent-engineering`
`resolvedVersion: 0.2.0 -> 0.3.0` with `manifestContentIdentity`
`32a036f7... -> eacb9507...`, plus `prompt-engineering` and
`harness-engineering` `0.1.1 -> 0.2.0`; `axm lint` finding text `Pack
'@agentxm/packs/agent-engineering' does not currently form a reconcilable
desired-state route.`
