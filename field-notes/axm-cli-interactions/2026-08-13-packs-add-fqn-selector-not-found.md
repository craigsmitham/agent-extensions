---
subject: axm-cli-interactions
key: packs-add-fqn-selector-not-found
date: 2026-08-13
kind: workaround
status: open
---

**Expected:** The recovery command suggested by `axm lint` and the safety gate,
`axm packs add @craigsmitham/packs/codebase-change-workflow @craigsmitham/skills/workshop-codebase-design --replace-existing`,
should resolve the `canonical-constraint-mismatch` finding it was suggested for.
**Actual:** That exact command failed with `Pack '@craigsmitham/packs/codebase-change-workflow' not found (not_found)` and suggested creating a pack. Rerunning with the bare pack name, `axm packs add codebase-change-workflow ...`, succeeded and updated the constraint.
**Gap:** `axm packs add` does not accept the owner-qualified pack FQN that the tool's own recovery suggestion emits, so the suggested command is not runnable as printed.
**Suggests:** Make `axm packs add` accept the FQN selector, or emit the bare-name form in lint and safety-gate recovery suggestions; verify suggested recovery commands reach their postcondition when run verbatim.

Evidence: Repository `agent-extensions`, worktree on `main` ahead of commit `377c561` with local edits, 2026-08-13, AXM CLI 0.26.7 with `@agentxm/skills/axm@0.26.7`. The FQN form exited non-zero with code `not_found`; the bare-name form in the same session reported `Added 1 extension to pack codebase-change-workflow` and modified `.axm/extensions/@craigsmitham/packs/codebase-change-workflow/pack.json`.
