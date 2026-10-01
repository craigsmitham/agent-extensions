---
observed_at: "2026-10-01T20:59:50Z"
session: "b01e62f6-b833-4016-9b51-91ceacb70af1"
area: "pre-commit public safety hook"
---

# Commit hook blocked by workspace errors outside the change

## Context
Committing the effect-v4 knowledge bundle refresh (1.0.6) before publishing it.
The staged changes touched only `knowledge/effect-v4/` and one field note.
`axm knowledge lint --path knowledge/effect-v4` passed.

## Friction
`.githooks/pre-commit` runs `scripts/check-public-safety.sh --view git-index`.
Its `axm sync --preview` step reported `blocked: 1`, so the commit was
rejected even though the blocking unit concerned `AGENTS.md`, not the staged
bundle.

## Cost / impact
The commit and the publish that follows it were halted pending a user decision.
Reading the hook output needed three extra commands because it printed about
57 KB of JSON.

## Outcome
Nothing was committed and the changes remain staged. The user was asked how to
proceed.

## Evidence
- Blocked unit: "Knowledge discovery; instruction files (unavailable)" —
  "AXM cannot safely update its section in AGENTS.md: Managed region source
  ownership conflicts"
- `axm lint` also reports `workspace/axm-skill-compatible`: CLI 0.38.0 is
  outside the bundled AXM skill range >=0.32.0 <0.33.0.

## Existing context
The same workspace errors were recorded earlier today in
`2026-10-01T193500Z-w3n8f-workspace-lint-preexisting-errors.md`.
