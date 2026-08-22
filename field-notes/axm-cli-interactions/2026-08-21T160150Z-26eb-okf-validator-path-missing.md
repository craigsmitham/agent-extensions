---
id: 2026-08-21T160150Z-26eb
subject: axm-cli-interactions
key: okf-validator-path-missing
observed_at: "2026-08-21T16:01:50Z"
session: dd6874ad9ab2e95f
kind: workaround
status: open
---

**Expected:** The `author-okf` skill's required command,
`python3 scripts/validate_okf.py <bundle> --summary`, would inventory the
existing bundle before revision.
**Observed:** Python reported that `scripts/validate_okf.py` does not exist in
this workspace.
**Impact:** One validation attempt failed and the reference inventory did not
run in the same command; elapsed cost was not measured.
**Recovery:** Use AXM's documented `axm knowledge lint --path <package>` for
bundle validation and run the reference inventory separately; the original
task continued.
**Detected by:** Non-zero exit from the skill-prescribed validator command.
**Observed factors:** The active workspace is an AXM knowledge-package
repository; `axm help knowledge` documents `axm knowledge lint`, while the
repository has no `scripts/validate_okf.py` at its root.
**Hypothesis:** The portable skill assumes its validator script is available
relative to the active workspace rather than relative to the skill package.

Evidence: Python printed `can't open file
'/Users/craig/Code/craigsmitham/agent-extensions/scripts/validate_okf.py': [Errno
2] No such file or directory`.
