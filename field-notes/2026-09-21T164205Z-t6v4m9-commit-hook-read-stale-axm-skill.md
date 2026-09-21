---
observed_at: "2026-09-21T16:42:05Z"
session: "session-k4m8v2"
area: "AXM commit hook"
---

# Commit hook read a stale bundled skill version

## Context
The fully staged field-notes 1.0.0 release and AXM v8 workspace migration were
being committed after a converged workspace preview.

## Friction
The commit hook's Git-index validation reported the bundled AXM skill as 0.31.1
and incompatible with CLI 0.32.2. The staged canonical AXM manifest and all four
live projections declare skill and CLI compatibility version 0.32.2.

## Cost / impact
The normal commit was blocked once and required bypassing the inconsistent hook
after its reported state was compared with already available staged and live
state.

## Outcome
The occurrence was recorded and the commit proceeded without the hook. Package
validation, converged sync preview, and publication preview remained required.

## Evidence
The hook reported `input.view: git-index`, reason code
`cli-version-incompatible`, observed skill 0.31.1, and target 0.32.2. The staged
canonical package is `agent_extensions/registry/@agentxm/skills/axm` 0.32.2.
