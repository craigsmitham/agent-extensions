# Effect v4

This pack installs two members:

- `@craigsmitham/rules/use-effect-v4` — directs agents working with Effect to
  use Effect v4 APIs and conventions rather than carrying v3 patterns forward.
- `@craigsmitham/knowledge/effect-v4` — a standalone OKF 0.2 bundle of
  twenty-four concise checklists for design, implementation, maintenance, and
  review.

The checklists were last reviewed and updated against **Effect 4.0.6**. See the
[bundle
index](https://github.com/craigsmitham/agent-extensions/blob/main/knowledge/effect-v4/src/index.md)
for the complete topic list and the major-version policy.

The former `@craigsmitham/skills/craft-effect-v4` routing skill is not part of
this pack. Consult a topic checklist directly when it is useful.

## Checklist maintenance

Before revising a checklist, inspect current Effect v4 source and tests plus
representative v4 applications or libraries that exercise the topic. Record
each reference's role, declared Effect version, and reviewed commit. Prefer
small excerpts with relevant tests; verify the specific behavior before moving
a source pin. The reference selection reviewed on 2026-10-27 is:

- [Effect](https://github.com/Effect-TS/effect) — released API contracts,
  regression tests, and idiomatic examples; 4.0.6.
- [opencode](https://github.com/anomalyco/opencode) — application services,
  Bun test harness, and concurrency tests; catalog 4.0.1. Its
  [HTTP recorder](https://github.com/anomalyco/opencode/tree/432d870b02683d2e40e895ddc70d437189b25276/packages/http-recorder)
  supplies the current client-decoration reference.
- [LiveStore](https://github.com/livestorejs/livestore) — worker ownership and
  interoperability; catalog 4.0.3. Its Effect facade is project-specific.
- [Alchemy](https://github.com/alchemy-run/alchemy) — infrastructure service
  implementations and platform adapters; catalog ^4.0.5, overrides 4.0.5.
  Distinguish presentation demos and native async Workers from Effect service
  style examples.
- [effect-local](https://github.com/lucas-barake/effect-local) — protocol
  boundaries and replica ownership; development 4.0.0, library peer ~4.0.0.
- [dfx](https://github.com/tim-smart/dfx) — library services and untraced
  functions; development ^4.0.5, peer ^4.0.0.

The standalone [effect-http-recorder](https://github.com/anomalyco/effect-http-recorder)
repository is historical beta.83 evidence. Prefer the integrated opencode
package for current examples. A repository's use of a pattern does not make
every detail a general convention: retain the bundle's clock, schema,
cancellation, and observability requirements, and justify custom facades or
layer graphs by a concrete repeated need.

Keep each topic to five through ten independently judgeable items. Link to API
detail and extended guidance rather than turning a checklist back into a guide.
