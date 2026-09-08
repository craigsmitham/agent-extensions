---
id: 2026-09-08T164200Z-p9r4
subject: axm-cli-interactions
key: uninstall-leaves-workspace-source
observed_at: "2026-09-08T16:42:00Z"
session: 017WPEnCqQnxuukAMrcPSRXm
kind: gap
status: open
---

**Expected:** `axm uninstall @craigsmitham/knowledge/product-management` to
remove the workspace-authored bundle, or to name the canonical path it was
leaving behind. `axm uninstall --help` states "Remove an extension from the
workspace", and `--preview` states "Show what would be removed without making
changes".
**Observed:** The preview returned `outcome: previewed` with a single unit
`product-management` in state `ready`, five `agentOutcomes` entries all
`not-applicable` / `workspace-owned`, and no `path`, `removedPaths`, or
`changes` field naming any artifact. The applied run returned
`outcome: applied` with `counts.committed: 1`. Afterward `axm.json` no longer
listed `product-management` under `knowledge` and the generated `AGENTS.md`
knowledge region had been updated, but `knowledge/product-management/` still
contained `knowledge.json`, `README.md`, `src/index.md`, `src/log.md`, and
`src/value-and-demand/index.md`.
**Impact:** Two extra verification steps (reading `axm.json` and listing the
directory) to establish what the command had done, then one manual
`git rm -r knowledge/product-management` to finish the retirement. Task
completed.
**Recovery:** Listed the directory, then deleted the retained source with
`git rm -r -q knowledge/product-management`. A later `axm lint --json` returned
10 findings, all pre-existing `workspace/managed-file-unowned` warnings on
`skills/*`, and `axm sync --preview --fail-on-change --json` returned
`outcome: no-op`.
**Detected by:** Listing `knowledge/product-management` after the applied
uninstall reported success, as part of verifying the retirement.
**Observed factors:** axm 0.28.11; skill compatibility `compatible` against
declared range `>=0.28.0 <0.29.0`; bundle was workspace-authored
(`"product-management": "workspace"` in `axm.json`), not installed from the
registry; the same command updated the generated instruction-file knowledge
region without a separate `axm sync`; second observed occurrence of this key,
after `2026-09-08T155704Z-m7q2` on the `strategy` bundle in another session.
**Diagnostic evidence:** tool version 0.28.11; command surface
`axm uninstall @craigsmitham/knowledge/product-management --non-interactive
--json`; contract `plan-result-v3`; candidateId
`e305fad2a86b26910189046e3bd0043e82c6b98e8e622b52b4e91b2b47c45e2d` (preview);
outcome `applied`; counts `{total:1, committed:1, failed:0, blocked:0}`; unit
`product-management` state `committed`, message not supplied; process exit
status 0.
**Hypothesis:** Uninstall appears to scope itself to desired state and
projections for a workspace-authored package, leaving canonical source to
another command or to manual deletion, without that boundary appearing in the
result.
**Suggests:** Naming the retained canonical path in the uninstall result for a
workspace-authored package, or pointing at the command that removes it.
