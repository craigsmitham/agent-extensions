# Effect v4 reference implementation review

Reviewed and adopted 2026-10-27. **Status: adopted in source-reviewed candidate
checklists.** All recommendations below are implemented alongside the Effect
4.0.6 refresh in local knowledge version 1.0.7 and pack version 1.0.1.

## Outcome

Keep the existing emphasis on explicit boundaries, typed failures, scoped
resources, injectable services, and observable tests. Improve the guidance in
four places: reusable Effect functions, test-runner neutrality, concurrency
test synchronization, and service identity. Refresh the reference selection
policy before importing more application conventions.

These conventions are inferred from source examples and current upstream
guidance, not evidence that one style improves defect rates. Keep the existing
checklists as `reporting-review` candidates with their current completion,
exception, maintenance, and field-validation protocol.

## Scope and snapshots

Audience: maintainers of this repository's Effect extensions. Local baseline:
`96b4888df4a2b325ba86f6fc0b0f8bc9402e4b2a`, followed by the working-tree 4.0.6
refresh. Public repository default-branch heads were resolved on 2026-10-27
and source reads were pinned to those commits. Dependency declarations below
describe the sampled manifests/catalogs; they are not claims that installations
or tests were run at those versions.

| Repository | Snapshot | Declared Effect baseline | Evidence sampled and appropriate use |
| --- | --- | --- | --- |
| Effect | [`41f6738`](https://github.com/Effect-TS/effect/tree/41f673823010b390e23213f820ba5dc6bf9af783), `main` | 4.0.6 | `ai-docs` function, service, layer, and testing examples; released 4.0.6 contracts and selected regressions are the API authority. |
| opencode | [`432d870`](https://github.com/anomalyco/opencode/tree/432d870b02683d2e40e895ddc70d437189b25276), `dev` | catalog 4.0.1 | Instance service, location service map, keyed mutex and tests, Bun Effect harness, layer graph, integrated HTTP recorder. Useful application and test boundaries; custom graph machinery is local. |
| LiveStore | [`aafda20`](https://github.com/livestorejs/livestore/tree/aafda2024137edb59795f9711c5a877c09450eba), `main` | catalog 4.0.3 | Webmesh worker, Effect facade, and selected helper implementations. Useful worker ownership and interoperability examples, with project-specific wrappers. |
| Alchemy | [`59fd117`](https://github.com/alchemy-run/alchemy/tree/59fd1170ee559b47c59aab437ba701a7b05b8497), `main` | catalog ^4.0.5; overrides 4.0.5 | Local state store, Links service/KV implementation, native Worker and integration test. Distinguish framework internals, presentation demos, and native platform examples. |
| effect-local | [`4ad7067`](https://github.com/lucas-barake/effect-local/tree/4ad70672bb7e4d5199546b4f33845d3d5e8cca23), `main` | development 4.0.0; library peer ~4.0.0 | SyncClient adapter, browser replica owner, chat login, time formatting, and connection tests. Useful typed protocol boundaries and explicit ownership. |
| dfx | [`dee64e7`](https://github.com/tim-smart/dfx/tree/dee64e7daae7d810f991f5d6f73308e09b417e75), `main` | development ^4.0.5; peer ^4.0.0 | Discord REST service, shard lifecycle excerpts, and ordering test. Useful library service construction and untraced functions; protocol retry machinery is specialized. |
| effect-http-recorder | [`89e1b85`](https://github.com/anomalyco/effect-http-recorder/tree/89e1b85f7caa12ad076b8f9b65c804f89c60ecd0), `dev` | 4.0.0-beta.83 | HTTP service decoration and test support. Historical conceptual reference; its latest commit remains 2026-07-07 and imports `effect/unstable/http`. |

Method: purposeful source sampling, not a repository census. Read service
contracts, representative implementations, test harnesses, and relevant test
cases; inspect long implementation files in bounded excerpts. Compare each
candidate with our checklists and the released API. Examples show a pattern
exists; a manifest version does not prove every file follows it correctly.

## Adopted convention changes

### 1. Distinguish reusable functions from Effect values

**Priority: high. Confidence: high.** Before adoption, our checklists explained
boundaries and wrappers but omitted function-construction style. Upstream
explicitly recommends
`Effect.fn` or `Effect.fnUntraced` for reusable generator functions. The
[current function guide](https://github.com/Effect-TS/effect/blob/41f673823010b390e23213f820ba5dc6bf9af783/ai-docs/src/01_effect/01_basics/02_effect-fn.ts)
distinguishes a named tracing boundary from an untraced library helper.
[dfx REST helpers](https://github.com/tim-smart/dfx/blob/dee64e7daae7d810f991f5d6f73308e09b417e75/src/DiscordREST.ts)
and [effect-local login](https://github.com/lucas-barake/effect-local/blob/4ad70672bb7e4d5199546b4f33845d3d5e8cca23/examples/chat/shared/src/session.ts)
provide examples of both choices.

Adopted principle in the service/wrapping guidance:

> For reusable generator functions, use `Effect.fn("Operation.name")` at a
> meaningful tracing boundary or `Effect.fnUntraced` when no span is needed.
> Keep pure helpers ordinary functions and one-off programs as Effect values.

Keep function post-processing with the constructor's supported combinator
arguments. Do not require tracing for every helper, replace concise existing
combinators mechanically, or confuse `const make = Effect.gen(...)` with a
function that merely returns `Effect.gen(...)`.

### 2. Specify test-harness behavior without mandating Vitest

**Priority: high. Confidence: high.** The first item in
[Testing](../knowledge/effect-v4/src/testing.md) previously required
`@effect/vitest`. That is a useful default for a Vitest repository but too broad
as portable guidance. [opencode's Bun harness](https://github.com/anomalyco/opencode/blob/432d870b02683d2e40e895ddc70d437189b25276/packages/core/test/lib/effect.ts)
supplies scopes, layers, TestClock, TestConsole, failure reporting, and a guard
against unexpected fetch traffic. [effect-local's tests](https://github.com/lucas-barake/effect-local/blob/4ad70672bb7e4d5199546b4f33845d3d5e8cca23/examples/chat/test/connection.test.ts)
use `@effect/vitest` directly.

Adopted harness contract:

> Run Effect tests through a harness that reports failed exits, owns test
> scopes and fibers, and supplies controlled services; prefer `@effect/vitest`
> when the repository uses Vitest.

Add explicit offline substitution where network access is outside the test's
contract. The observed opencode guard covers its fetch path, not every possible
socket or SDK. A custom harness should demonstrate failure propagation,
interruption, finalization, and clock behavior before being treated as
equivalent. This is a targeted correction to the current checklist, not a
recommendation that repositories build their own runners.

### 3. Synchronize concurrency tests on events

**Priority: medium. Confidence: high.** Before adoption, the checks required
deterministic time and cancellation coverage but did not say how tests know a
worker reached the relevant state. [opencode's keyed-mutex tests](https://github.com/anomalyco/opencode/blob/432d870b02683d2e40e895ddc70d437189b25276/packages/core/test/effect/keyed-mutex.test.ts)
use Deferred signals for holder start and release, then verify the interrupted
waiter leaves the holder's entry alive. They still use a scheduler yield in
places; the example supports explicit signals, not a claim of a perfect
universal test recipe.

Adopted in Testing and Async coordination:

> Establish worker readiness and release points with explicit signals; advance
> TestClock for time policy, and assert the observable outcome after joining or
> interrupting the worker.

Use this to displace guessed sleeps, not to require internal instrumentation
or assertions about incidental scheduler order. Keep distinct-key progress,
same-key exclusion, and cleanup as observable contracts.

### 4. Make service identity explicit; keep layer placement flexible

**Priority: medium. Confidence: high for identity, moderate for style.** The
[upstream service guide](https://github.com/Effect-TS/effect/blob/41f673823010b390e23213f820ba5dc6bf9af783/ai-docs/src/01_effect/03_services/01_service.ts)
uses an explicit `Context.Service` interface and a package/path identifier.
[opencode's Instance contract](https://github.com/anomalyco/opencode/blob/432d870b02683d2e40e895ddc70d437189b25276/packages/core/src/instance/service.ts)
and dfx also namespace identifiers. Our service checklist previously named a
service tag without making that identity convention concrete.

Adopted service identity contract:

> Give each service a stable, collision-resistant `Context.Service` identifier
> and a public interface that exposes the capability rather than its adapter.

Keep public layer inputs, outputs, and construction failures inspectable.
Static `.layer` members, separately exported layers, and dependency-open layer
factories all appear in the sample. Prefer consistency within a module or
repository; the evidence does not justify one universal placement or naming
scheme. Our existing composition and lifetime checks already express the
important behavior.

## Improve reference selection

**Priority: high. Confidence: high.** A reference should name its role and
version, not imply endorsement of every pattern in the repository.

- For current HTTP recording examples, prefer opencode's
  [`@opencode/http-recorder` package](https://github.com/anomalyco/opencode/blob/432d870b02683d2e40e895ddc70d437189b25276/packages/http-recorder/package.json)
  and [current recorder implementation](https://github.com/anomalyco/opencode/blob/432d870b02683d2e40e895ddc70d437189b25276/packages/http-recorder/src/http/recorder.ts).
  The standalone repository remains useful historical evidence but is pinned
  to beta.83 and has obsolete import paths. Replace the checklist's applied
  source only after checking the precise behavior it supports.
- Label Alchemy's
  [`cloudflare-worker-async`](https://github.com/alchemy-run/alchemy/blob/59fd1170ee559b47c59aab437ba701a7b05b8497/examples/cloudflare-worker-async/src/worker.ts)
  as a native platform-boundary example. It is not an Effect service style
  reference. Its latest implementation uses ordinary async handlers.
- Prefer small, behavior-specific excerpts with pinned commits and relevant
  tests. Do not automatically move historical source citations to a new HEAD
  merely because the repository remains active.

## Practices to retain or decline

Retain schema decoding at external boundaries, narrow error translation,
service substitution, scoped background work, and bounded resource ownership.
The samples provide concrete applications of these existing requirements.

Do not import opencode's
[LayerNode graph](https://github.com/anomalyco/opencode/blob/432d870b02683d2e40e895ddc70d437189b25276/packages/util/src/effect/layer-node.ts)
or LiveStore's
[Effect facade](https://github.com/livestorejs/livestore/blob/aafda2024137edb59795f9711c5a877c09450eba/packages/@livestore/utils/src/effect/mod.ts)
as general conventions. They support local composition and migration needs;
our evidence does not show those needs in ordinary consumers. Keep public
Effect APIs as the baseline and justify wrappers by a concrete repeated need.

Do not weaken clock or schema guidance to match demos. Alchemy's
[LinksKV example](https://github.com/alchemy-run/alchemy/blob/59fd1170ee559b47c59aab437ba701a7b05b8497/demos/effect-prezzy/app/src/LinksKV.ts)
illustrates interchangeable layers and bounded traversal, but also uses
`Date.now()` and typed JSON retrieval without an explicit schema decode in that
function. Those choices do not override our deterministic-time and boundary
validation requirements.

Likewise, effect-local's SyncClient translates some interruption-only causes
to protocol availability errors. Treat that as a protocol-owned decision to
inspect, not a general license to turn cancellation into a retryable error.
LiveStore's webmesh sample includes a dynamic span name; retain our stable-name
guidance rather than copying every detail of an otherwise useful example.

## Adoption record and validation limits

| Recommendation | Implementation |
| --- | --- |
| Reusable functions and deliberate tracing | [Services and layers](../knowledge/effect-v4/src/services-and-layers.md), [Wrapping foreign APIs](../knowledge/effect-v4/src/wrapping.md) |
| Runner-neutral harness, offline substitution, custom-harness checks | [Testing](../knowledge/effect-v4/src/testing.md) |
| Explicit concurrency synchronization | [Testing](../knowledge/effect-v4/src/testing.md), [Async coordination](../knowledge/effect-v4/src/async-coordination.md) |
| Service identity and flexible layer placement | [Services and layers](../knowledge/effect-v4/src/services-and-layers.md) |
| Current recorder and qualified native Worker references | [HTTP client](../knowledge/effect-v4/src/http-client.md), [Cloudflare Workers](../knowledge/effect-v4/src/cloudflare-workers.md) |
| Reference roles, versions, pinned evidence, and limits on importing local machinery | [Bundle maintenance](../knowledge/effect-v4/src/index.md#maintaining-this-bundle), [Pack maintenance](../packs/effect-v4/README.md#checklist-maintenance) |

All recommendations are adopted. The checklists retain five through ten items;
extended rationale stays in this review. Existing clock, schema, cancellation,
and observability requirements remain the authority when examples differ.

The package owner remains `@craigsmitham`. Revisit these conventions when the
installed Effect release changes, a reference migrates, or observed use exposes
misinterpretation. Validate candidate wording against representative examples
and compare reviewers using it with current practice for missed defects,
agreement, time, and unsupported completion. Reject or revise a convention if
it adds ceremony without improving the intended review decision.

No upstream suites, application builds, benchmarks, or user studies were run.
This review does not rank entire repositories or establish runtime correctness,
performance gains, usability, or checklist effectiveness. It excludes a broad
survey of AI, RPC, workflow, GraphQL, and event-log architecture.
