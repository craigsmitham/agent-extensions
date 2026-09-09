---
id: 2026-09-09T022128Z-c7n4
subject: axm-cli-interactions
key: authored-roots-unowned-workspace-lint
observed_at: "2026-09-09T02:21:28Z"
session: maintenance-release-f2k9
kind: gap
status: open
---

**Expected:** The public release gate recognizes the nine configured workspace-authored skill packages as canonical source.
**Observed:** Workspace strict lint reports each skills/<name> package as an unowned agent artifact, while strict Git-index lint reports zero findings. Sync is no-op; lint --fix retains the warnings.
**Impact:** The workspace-view safety gate exits 1 before other checks. Additional inspection and use of the exact Git-index gate were required; total delay not measured.
**Recovery:** Strict Git-index lint exits 0. The complete staged-content safety gate remains the commit check; no rule was disabled.
**Detected by:** Safety gate and structured lint outputs.
**Observed factors:** CLI 0.28.12; nine authored manifests match workspace declarations; inspected author-docs package has skill.json and src/SKILL.md, no root SKILL.md. Output observation scans all resolved agent skill containers and classifies directory entries without ownership markers as unowned.
**Diagnostic evidence:** workspace summary errors 0, warnings 9; all ruleIds `workspace/managed-file-unowned`, paths `./skills/<name>`; lint --fix outcome ok with same nine warnings; Git-index strict summary errors 0, warnings 0, exitCategory clean.
**Hypothesis:** Agent-container discovery includes the authored root in workspace view without distinguishing package directories from agent projections.
