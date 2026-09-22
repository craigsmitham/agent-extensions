---
observed_at: "2026-09-22T21:17:09Z"
session: "d5eee53f-00be-47e2-b34b-0c7a9aaa8468"
area: "local Effect source clones"
---

# Archived effect-smol clone lacked the rc release tags

## Context
Diffing Effect `4.0.0-rc.115` against `4.0.0-rc.117` to review the effect-v4
knowledge bundle, starting from the local clone `~/Code/Effect-TS/effect-smol`.

## Friction
`git log effect@4.0.0-rc.115..effect@4.0.0-rc.117` failed in effect-smol. The
upstream repository is archived (latest commit "Update readme with archive
notice"; newest tag `effect@4.0.0-beta.98`) and has no rc tags. Effect v4 work
and the bundle's source pins are in `Effect-TS/effect`.

## Cost / impact
Three extra commands (fetch, tag listing, remote inspection) before switching
clones.

## Outcome
Grepped the bundle's pin URLs, switched to `~/Code/Effect-TS/effect`, fetched
tags, and continued.

## Evidence
`fatal: ambiguous argument 'effect@4.0.0-rc.115..effect@4.0.0-rc.117': unknown revision or path not in the working tree.`
