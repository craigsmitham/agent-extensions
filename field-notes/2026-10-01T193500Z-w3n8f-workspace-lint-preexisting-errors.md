---
observed_at: "2026-10-01T19:35:00Z"
session: "c5511fc0-57ce-4efd-886d-b1e81f0325a4"
area: "axm lint"
---

# Workspace lint failed on errors unrelated to the change

## Context
Validating the effect-v4 knowledge bundle after refreshing it for Effect 4.0.0.
The working tree was clean before the refresh, and the edits touched only
`knowledge/effect-v4/`.

## Friction
Workspace `axm lint` exited 1 with three errors unrelated to the bundle, so it
could not show whether the change passed.

## Cost / impact
One extra command to locate a bundle-scoped validator. One more after
`axm knowledge lint knowledge/effect-v4` returned `not_found` because the
bundle needed `--path`.

## Outcome
`axm knowledge lint --path knowledge/effect-v4` passed. The workspace errors
were left unchanged.

## Evidence
- `workspace/projection-ownership-valid` (×2): "AXM cannot safely update its
  section in AGENTS.md: Managed region source ownership conflicts"
- `workspace/axm-skill-compatible`: "AXM CLI 0.37.0 is outside the official AXM
  skill range >=0.32.0 <0.33.0"
- `3 errors and 5 warnings in 5 locations · exit 1`

## Existing context
Earlier field notes in this repo record a stale bundled AXM skill reached
through the commit hook.
