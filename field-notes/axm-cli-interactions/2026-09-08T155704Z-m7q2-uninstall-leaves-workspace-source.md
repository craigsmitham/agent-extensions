---
id: 2026-09-08T155704Z-m7q2
subject: axm-cli-interactions
key: uninstall-leaves-workspace-source
observed_at: "2026-09-08T15:57:04Z"
session: 016aZdMPUK1ArBTBDJKRkdGj
kind: gap
status: open
---

**Expected:** `axm uninstall @craigsmitham/knowledge/strategy` to report which
paths it would remove, and for the preview to distinguish removing the
`axm.json` desired-state entry from removing the workspace-authored canonical
source at `knowledge/strategy/`. `axm uninstall --help` states "Remove an
extension from the workspace" and `--preview` states "Show what would be
removed without making changes".
**Observed:** The preview returned `outcome: previewed`, `atomicity.declared:
closure-atomic`, and a single unit `strategy` in state `ready` with
`message: null` and no path, `removedPaths`, or `changes` field naming any
artifact. The applied run returned `outcome: applied` with
`counts.committed: 1`. Afterward `axm.json` no longer listed `strategy` under
`knowledge`, but `knowledge/strategy/` still contained `knowledge.json`,
`README.md`, `src/index.md`, and `src/log.md`.
**Impact:** Two extra verification steps (reading `axm.json` and listing the
directory) to determine what the command had actually done, then one manual
`git rm -r knowledge/strategy` to finish the removal. Task completed.
**Recovery:** Read `axm.json` and `ls knowledge/strategy` to establish observed
state, then deleted the source directory with `git rm -r -q knowledge/strategy`.
A later `axm lint --json` returned 10 findings, all pre-existing
`workspace/managed-file-unowned` warnings on `skills/*`, and none for the
removed bundle.
**Detected by:** Listing `knowledge/strategy` after the applied uninstall
reported success, as part of verifying the retirement.
**Observed factors:** axm 0.28.11; skill compatibility `compatible` against
declared range `>=0.28.0 <0.29.0`; bundle was workspace-authored
(`"strategy": "workspace"` in `axm.json`), not installed from the registry;
preview reported per-agent projection outcomes as `not-applicable` with
`reasonCode: workspace-owned`; the same command did update the generated
`AGENTS.md` knowledge region without a separate `axm sync`.
**Diagnostic evidence:** tool version 0.28.11; command surface
`axm uninstall @craigsmitham/knowledge/strategy --non-interactive --json`;
contract `plan-result-v3`; candidateId
`9e740a2492baa11830d29f6dc34be3e6225b8a6c135a91059a53b5d403df768f`;
outcome `applied`; counts `{total:1, committed:1, failed:0, blocked:0}`; unit
`strategy` state `committed`, message not supplied; process exit status not
supplied, because the pipeline replaced it with the formatter status.
**Hypothesis:** Uninstall may deliberately scope itself to desired state and
projections for a workspace-authored package, leaving canonical source to
`demote` or manual deletion, without that boundary appearing in the result.
**Suggests:** Naming the retained canonical path in the uninstall result for a
workspace-authored package, or pointing at `demote` when source authority
remains after the entry is removed.
