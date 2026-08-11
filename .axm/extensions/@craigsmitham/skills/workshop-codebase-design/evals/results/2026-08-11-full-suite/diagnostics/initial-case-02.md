# Case 2 — Irrelevant research-to-design drift

- Runtime: Codex collaboration subagent
- Model: Inherited session model; exact public identifier unavailable
- Tested `src/` SHA-256: `9635ad7ea8154f3ffdd4b3134217c1da152988deef7c04aef4bc78a2b66db3dd`
- Reference availability: Available; not needed by the response
- State changed: None

## Prompt

> Workshop how invoice IDs should be exposed to consumers. Research was
> completed at r333; design begins at d444. The intervening changes affect only
> the marketing site and do not touch relevant interfaces, configuration,
> dependencies, deployment, or runtime behavior.

## Raw response

## Workshop frame

- Change intent: decide how invoice IDs are exposed to external consumers.
- Evidence snapshot: completed research at `r333`.
- Design snapshot: `d444`.
- Relevant drift: none. The intervening marketing-only changes do not affect invoice interfaces, configuration, dependencies, deployment, or runtime behavior, so the relevant `r333` evidence remains applicable at `d444`.
- Current evidence limit: the research findings themselves were not supplied. I cannot yet identify existing ID types, consumer surfaces, compatibility obligations, or persistence constraints.
- Status: `Discussing`.
- Specification readiness: blocked pending the existing research evidence.

Initial agenda:

| ID | Question | Type | Status | Specification impact |
| --- | --- | --- | --- | --- |
| D1 | Which invoice identifier and semantics should each consumer-facing boundary expose? | Coupled | Needs research evidence | Blocks specification |
| D2 | Must existing identifiers remain accepted or returned during migration? | Coupled | Needs research evidence | Blocks specification |

Please confirm this frame and provide the `r333` report or its relevant findings—especially the current identifiers, affected consumer interfaces, persisted references, and compatibility constraints. Then we can resolve D1 first with two or three viable options and an explicit recommendation.

## Grade

- Pass — The response records both snapshots and the marketing-only basis for irrelevant drift.
- Pass — It does not require refreshed research merely because the revision advanced.
- Pass — It requests frame confirmation before resolving the decision.
- Pass — It recommends or accepts no option from snapshot labels alone.

Result: **4/4**
