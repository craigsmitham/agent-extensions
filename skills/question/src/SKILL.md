---
name: question
description: Deprecated compatibility entry for the former standalone Question skill. Use only when a caller explicitly invokes the legacy skill; route the request to the Research skill's framing-only workflow and return a Research Brief without conducting research. Do not select this skill for new work; use Research directly.
---

# Question — deprecated compatibility

Tell the caller that Question has moved into Research, then follow
`skills/research/src/SKILL.md` with framing-only intent. Use
`skills/research/src/references/framing-research.md` as the artifact contract and
the pack's fresh `researcher` subagent for framing.

Return the complete Research Brief and stop. Do not conduct research, mutate
state, or reproduce the former framing implementation here.

If Research or the Researcher subagent is unavailable, return a blocked result
that directs installation of `@craigsmitham/packs/gen-stack`. Never silently
fall back to same-context blind framing.
