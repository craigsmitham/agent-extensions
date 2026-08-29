---
id: 2026-08-29T182416Z-c8q4
subject: axm-cli-interactions
key: workspace-lint-unrelated-projection-drift
observed_at: "2026-08-29T18:24:16Z"
session: codex-c8q4
kind: gap
status: open
---

**Expected:** `axm lint --json` would provide a clean or target-relevant preflight for creating the bounded `checklist-design` skill package.
**Observed:** The command exited `1` with two workspace-level `workspace/projections-current` errors for the managed `AGENTS.md#knowledge` and `subagent:researcher` projections; neither finding named the new skill target.
**Impact:** The AXM preflight could not serve as a clean baseline for the bounded creation, so the existing projection drift had to be preserved and separated from target validation. No retry occurred; elapsed cost was not measured.
**Recovery:** Progress continued by retaining the structured findings and consulting live AXM creation guidance; the original task was still in progress at capture time.
**Detected by:** The complete structured result from `axm lint --json`.
**Observed factors:** AXM CLI `0.28.2`; AXM skill `0.28.1`; compatibility status `compatible`; two error-severity advisory findings; summary exit category `errors`.
**Diagnostic evidence:** Process exit status `1`; rule `workspace/projections-current`; affected artifacts `AGENTS.md#knowledge` and `subagent:researcher`; recovery action for skill compatibility `none`.
**Hypothesis:** The workspace-wide lint surface reports projection drift independently of the exact package being authored.

Evidence: The retained JSON result reported `ok: false`, compatibility `compatible`, exactly two findings, and no `checklist-design` identity.
