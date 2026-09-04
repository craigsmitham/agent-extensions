---
id: 2026-09-04T145530Z-p4t9
subject: axm-cli-interactions
key: workspace-strict-lint-blocks-preflight
observed_at: "2026-09-04T14:55:30Z"
session: 2ea7960b-9b16-49b3-af43-6c38406a731b
kind: gap
status: open
---

**Expected:** `docs/publishing.md` presents `scripts/check-public-safety.sh`
with no arguments as "this publishing preflight validates the complete working
tree" and directs the reader to "run the local safety gate" and review its
findings before publishing. A clean workspace was therefore expected to reach
the gate's custom validators and pass.
**Observed:** The no-argument workspace view exited 1 at
`axm lint --view workspace --strict`, reporting "10 issues. 10 need manual
attention." — all warnings with ruleId `workspace/managed-file-unowned` and
message "Agent skill artifact has no AXM ownership proof." on `./skills/audit-
docs`, `./skills/author-docs`, `./skills/author-okf`, `./skills/checklist-
design`, `./skills/engineer-requirements`, `./skills/field-notes`,
`./skills/improve-whatever`, `./skills/manage-work-items`, `./skills/research`,
and `./skills/temporal-dates`. Because strict lint precedes them, no custom
validator ran. The same script with `--view git-index` — the mode the tracked
pre-commit hook and CI use — exited 0 and printed "Public extension safety
checks passed for the git-index view."
**Impact:** The documented publish preflight produced no usable verdict, and its
package-inventory, secret-scan, symlink, manifest, and license validators were
never exercised in the workspace view. Confidence for the release had to be
taken from the git-index view instead. Nine of the ten flagged paths are tracked
repository packages, so the failure is not attributable solely to local
untracked work. One extra script run and one script read were spent
distinguishing the two views. Elapsed time not measured.
**Recovery:** Progress was restored by relying on `scripts/check-public-
safety.sh --view git-index`, which is authoritative for the commit and for CI.
The commit proceeded and its pre-commit hook passed. The workspace-view failure
was not resolved.
**Detected by:** Running the exact command `docs/publishing.md` prescribes for
publishing preflight and comparing its exit status against the `--view
git-index` run of the same script.
**Observed factors:** `./skills/audit-docs` is entirely untracked (0 files in
`git ls-files skills/audit-docs`) and is absent from the gate's own approved
29-package `expected` inventory, so the workspace view sees content the
git-index view cannot. The other nine flagged directories are tracked and are
listed in that inventory. `axm lint --json` without `--strict` returned ok=true
with summary errors 0, warnings 10, exitCategory "warnings". AXM 0.28.5;
`axmSkillCompatibility` reported status "compatible" (CLI 0.28.5, skill 0.28.1,
range ">=0.28.0 <0.29.0", recovery action "none"). The workspace had just been
migrated to lockfileVersion 7.
**Diagnostic evidence:** tool `axm` 0.28.5; command surface `scripts/check-
public-safety.sh` (no arguments) wrapping `axm lint --view workspace --strict`;
exit status 1. Rule `workspace/managed-file-unowned`, group "workspace", kind
"advisory", severity "warning", 10 occurrences. Contrasting run: same script
`--view git-index`, exit status 0. Lint summary object: `{"total": 10, "errors":
0, "warnings": 10, "infos": 0, "exitCategory": "warnings"}`. Request or
correlation ID: not supplied. No mutation was involved and nothing was retried.
**Hypothesis:** The two views disagree because ownership proof for
workspace-authored skills is established by state the git-index snapshot
materializes but the live working tree does not carry, so the same tracked
packages read as unowned in place; `docs/publishing.md` meanwhile describes the
workspace view as the preflight without noting that only the git-index view is
expected to pass.
**Suggests:** Either `docs/publishing.md` should name `--view git-index` as the
preflight command, or the publishing guidance should state which warnings are
expected in the workspace view, as it already does for
`workspace/authored-content-unpublished`.

Evidence: The workspace view stopped at strict lint and never printed "Public
extension safety checks passed", while the git-index view printed that line
after "Knowledge validation passed for 1 bundle". The gate's `expected` array in
`scripts/check-public-safety.sh` lists nine `skills/` entries and does not
include `skills/audit-docs`.
