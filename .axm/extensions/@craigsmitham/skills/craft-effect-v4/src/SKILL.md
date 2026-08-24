---
name: craft-effect-v4
description: >
  Routes Effect v4 TypeScript work to opinionated guides on data modeling,
  services and layers, errors, schemas, configuration, resource safety,
  concurrency, streams, platform integration, testing, and observability. Use
  when designing TypeScript architecture or writing or reviewing TypeScript in
  an Effect codebase, and when designs or code involve service boundaries, raw
  `process.env` reads, thrown or `unknown` errors, unvalidated JSON casts,
  `Promise.all`, detached promises, `try/finally` cleanup, homemade caches,
  per-key client or connection maps, scattered `fetch` calls, `console.log`
  telemetry, or direct `node:fs` use — even where Effect is absent but
  warranted. Not for Effect v3 conventions or codebases that deliberately use
  another runtime model.
compatibility: Effect v4 prereleases; guides target 4.0.0-rc.111 and require installed-version verification
---

# Craft Effect v4

Route Effect v4 work to the smallest relevant part of
`@craigsmitham/knowledge/effect-v4`.

## Compatibility gate

Apply this gate before inspecting files or opening the v4 knowledge bundle. If
the request says the codebase deliberately uses Effect v3 and migration is not
authorized, do not apply or offer v4 APIs. State that the v3/v4 boundary makes
the requested rewrite incompatible with scope, keep migration out of scope,
and stop.

1. Confirm the codebase targets Effect v4 and inspect its exact installed
   version. v3 conventions do not carry forward, and these guides do not
   describe them. The bundle targets `4.0.0-rc.111`; Effect v4 is
   still prerelease software, so verify consequential API claims against the
   installed version's public source and tests whenever the versions differ.
2. Read
   `.axm/extensions/@craigsmitham/knowledge/effect-v4/src/index.md` and open
   only the guides its symptom map routes to. The index is the canonical route;
   do not recreate that map in this skill or load the whole bundle.
3. Follow the selected guides and repository-local requirements. Open the
   guides they cross-link only when the requested scope needs them.

During a design or architecture workflow, use the guides to establish
version-matched capability semantics, constraints, and feasibility evidence for
the options under consideration. Supply that evidence to the active workflow;
do not choose consequential alternatives for the developer. Do not infer that
Effect availability alone makes its use a binding architectural rule.

When feasibility depends on a guide's API claim, or that claim conflicts with
the installed Effect version, inspect current public Effect v4 source and tests
before acting, and report the drift.
