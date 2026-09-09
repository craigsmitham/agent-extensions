# Proposal: a shared rental-product case for product engineering

Status: implemented in the local documentation on 2026-09-09. The original
analysis and proposal below are retained as the decision history. The authored
[Northbank case](../knowledge/product-engineering/src/northbank-equipment.md)
and its linked worked examples now supply the context across the explainers
and selected lifecycle guidance. All business decisions remain fictional.

## Implementation evidence — 2026-09-09

The accepted direction is implemented locally. The five new concepts remain
fictional worked explanations, not a running example application or a release
of the managed package.

| Accepted element | Current implementation evidence |
| --- | --- |
| Shared business, actors, service vocabulary, episodes, and numerical scopes | [Northbank Equipment](../knowledge/product-engineering/src/northbank-equipment.md) |
| Tactical DDD/code responsibilities, consistency, tests, and migration | [Allocation change](../knowledge/product-engineering/src/engineering/northbank-allocation-change.md), linked from DDD and use cases |
| Tooling, CI/CD, infrastructure, task contracts, replacement and retention | [Engineering-system change](../knowledge/product-engineering/src/engineering/northbank-engineering-system.md), linked from strategy and task-interface guidance |
| Accepted obligation, witness authority, and later impact analysis | [Commitment specimens](../knowledge/product-engineering/src/solution/requirements/authoring/northbank-commitment-requirements.md), connected to development, authoring, review, lifecycle, and adaptation guidance |
| Incident, defect, corrective Change, recovery, and maintenance | [Receipt records](../knowledge/product-engineering/src/delivery/work-items/northbank-receipt-incident.md), connected to JTBD, maintenance strategies, and work-item guidance |
| Other conceptual connections | All twenty foundation explainers use the relevant Northbank context; value/demand, outcomes, care, testing, and codebase-review guidance include scoped applications |
| Related map views | Contractor digital-coordination SVG and engineering-capability SVG in the Wardley explainer; both rendered and visually inspected |
| Discovery and local readability | Root/section indexes and reading routes preserve existing locations; all five new concept titles are returned by AXM's bundle-scoped query |
| Format and references | OKF validator: 87 concepts, zero errors and warnings; 948 local link/anchor checks resolve; no unreachable non-log Markdown documents |
| Managed state | AXM lint: zero errors and nine pre-existing skill ownership advisories; sync preview reports no changes |

Whitespace validation passed. The source comparisons used the saved pre-edit
working tree, preserving the user's preceding discovery revisions. No real
customer research, production test results, or human verification attestations
were invented. General architecture, construction, release, and operating
guidance remains explicitly incomplete where the bundle had not written it.

The following sections retain the original proposal and assessment snapshot.

## Recommendation

Keep equipment rental and develop it into **Northbank Equipment: making and
keeping dependable equipment commitments**. Northbank is a fictional regional
rental business with an existing software product, depot operations, suppliers,
and an engineering system that must evolve together.

Use one stable business context, several connected episodes, and explicit
alternative scenarios. The central question is how Northbank helps contractors
keep work moving while sustaining a viable business. Reservation confirmation
is one intervention within that question. Application code, infrastructure,
developer tooling, CI/CD, support, training, and retirement all contribute to
the case.

The example should let a reader start from either direction:

- A business choice reaches customer experience, domain rules, implementation,
  verification, release, operation, and evidence about the original choice.
- A code smell, failed build, incident, or costly workaround prompts an
  investigation into the responsibility, obligation, and purpose it serves.

The desired result is a reusable setting in which each concept makes a
different consequential distinction. It is not a prescribed combination of
all the methods explained in the bundle.

## Analysis scope, evidence, and disposition

This assessment concerns example suitability, conceptual connections, and
coverage of the requested product-engineering use case. The audience is the
authors and maintainers of this bundle, and practitioners learning across its
concepts. It is not a general audit of every claim, source, link, or schema.

The observation is the working tree on 2026-09-09, including the user's revised
and untracked explainers, over Git HEAD
`31a7316a6ca7dfeb25d22d350ebe901d9be0ef7b`. HEAD alone does not identify the
reviewed content. The 108 files under `knowledge/product-engineering/src`
had aggregate SHA-256
`ef94509b77e3b4d465b997bd3179ef93dc991e558ceeb84f7989136bf083630b`
when inspected. This digest concatenates sorted relative paths, NUL, file
bytes, and NUL. There are 107 Markdown files and one SVG.

Coverage combines a path/title census with purposeful content and journey
sampling. The census covered the following populations, including indexes:

| Area | Markdown files | Content examined for this proposal |
| --- | ---: | --- |
| Foundations | 22 | Example passages, key distinctions, comparison material, and connections across all 20 substantive explainers |
| Requirements and solution | 30 | Index routes; authority and maturity; one authority; classification; conflict resolution; stateful and quantitative obligations; external conformance; impact analysis |
| Engineering | 18 | Index routes; test admission and levels; specification authority; task interfaces and adoption example; quality pillars, cross-cutting records, and test-suite assessment |
| Delivery | 26 | Index routes; work-item taxonomy; verification; evidence and provenance |
| Problem | 3 | Both substantive concepts: value and demand, outcomes and evidence |
| Maintenance | 2 | Existing-product understanding, care, invoice-service example, and links to intervention strategies |
| Strategy and operations | 2 | Scope, responsibilities, and acknowledged coverage gaps |
| Root | 4 | Bundle index, overview, and revised reading routes; log inventoried |

The primary local authorities are the [overview](../knowledge/product-engineering/src/overview.md),
[reading routes](../knowledge/product-engineering/src/reading-product-engineering.md),
subject concepts, and the repository's coherence instruction. This assessment
does not revalidate the external scholarship behind the methods. It does not
cover other knowledge bundles, skills, or a real rental implementation.

[AXM-1773](https://linear.app/agentxm/issue/AXM-1773/decompose-agentxmcore-into-ddd-grouped-packages-and-retire-custom)
was read as a granularity reference. Its proposed decomposition, enforcement,
retirement ledger, and migration sequence demonstrate the kinds of decisions
the case should expose. Its measurements and estimates belong to that issue;
they are not Northbank facts, validated outcomes, or universal architecture rules.

**Disposition: targeted expansion of the shared case.** Preserve the conceptual
organization and revised discovery routes. Replacing the business domain would
discard useful material without addressing the main gap: connected examples
of sufficient depth across the product and engineering system.

### Strengths to preserve

The rental scenario already connects economic value, strategic alternatives,
customer behavior, design exploration, commitments, domain models, project
evidence, measures, and maintenance. The DDD explainer already distinguishes
the promise from the asset assignment. The Wardley example explicitly declares
its digital scope and physical omissions. The reading routes make questions,
rather than a mandatory process, the organizing connection.

The deeper guidance has particularly valuable boundaries: requirements versus
witnesses; product quality versus engineering-system capability; task meaning
versus pipeline orchestration; and incident restoration versus correction and
closure. The revised case must make these boundaries observable.

### Findings relative to the requested expanded use

These are editorial gaps against the new ambition, not findings that the
existing examples are inaccurate. Medium severity means a recurring gap in
the desired learning journey; it does not imply a production defect.

**EX-01 — The running case does not yet reach a reviewable engineering change**

- Severity: Medium.
- Confidence: High within the reviewed example passages.
- Condition: Rental modeling and landscape examples explain choices, but do
  not yet connect them through a concrete file-level change, enforcement,
  verification, and migration of an existing engineering system.
- Evidence: [DDD: model refinement](../knowledge/product-engineering/src/foundations/domain-driven-design.md#model-refinement-and-evolution)
  describes separating commitments and allocations;
  [Wardley: equipment-rental example](../knowledge/product-engineering/src/foundations/wardley-mapping/wardley-mapping.md#an-equipment-rental-example)
  deliberately scopes digital coordination;
  [task-interface adoption](../knowledge/product-engineering/src/engineering/adopting-a-repository-task-interface.md#worked-example)
  has a useful separate four-inventory example.
- Impact: Readers must invent the connection to tactical responsibilities,
  tooling, CI/CD, and infrastructure themselves.
- Expected state: At least one bounded change can be followed from purpose to
  owned rule, file/module, technical mechanism, evidence, rollout, and outcome.
- Recommendation: Add a commitment/allocation change and an engineering-system
  simplification episode with concrete artifacts and different proof obligations.
- Route: Shared-case authoring, followed by selected foundation and engineering
  example revisions.

**EX-02 — Related examples need a shared context with explicit branches**

- Severity: Medium.
- Confidence: High.
- Condition: The examples deliberately use different situations and local
  assumptions; they do not yet constitute one consistent case history.
- Evidence: [JTBD](../knowledge/product-engineering/src/foundations/jobs-to-be-done.md#running-example-coordinating-a-service-incident)
  uses incident coordination; [maintenance](../knowledge/product-engineering/src/maintenance/maintenance-and-the-life-of-software-products.md#maintenance-makes-continuity-possible)
  uses an invoice service; [renewal](../knowledge/product-engineering/src/foundations/drucker-organizational-renewal.md)
  uses a library. Shape Up excludes automatic substitution from its bounded
  project; Alleman's example narrows a two-depot pilot to one; the KPI definition
  measures a two-depot population.
- Impact: Treating every passage as the same episode would silently change
  scope, certainty, or chronology when readers follow cross-references.
- Expected state: Stable shared facts, identified episodes, and clearly marked
  alternatives make each passage intelligible independently and in sequence.
- Recommendation: Establish the Northbank baseline and episode boundaries
  below; preserve counterexamples and source-authored illustrations.
- Route: Case-context authoring and coordinated example updates, preserving
  current concept locations and links.

**EX-03 — The expanded case must distinguish illustration from missing guidance**

- Severity: Medium.
- Confidence: High.
- Condition: The bundle explicitly leaves architecture/construction, release
  flow/automation, and operational procedures unwritten while the requested
  case needs artifacts in all those areas.
- Evidence: Current [engineering](../knowledge/product-engineering/src/engineering/index.md),
  [delivery](../knowledge/product-engineering/src/delivery/index.md), and
  [operations](../knowledge/product-engineering/src/operations/index.md) indexes.
- Impact: A sufficiently detailed case could accidentally be presented as
  complete general guidance or obscure the acknowledged coverage gaps.
- Expected state: Concrete fictional choices illustrate existing concepts;
  the indexes continue to describe actual coverage accurately.
- Recommendation: Label case-specific decisions and their assumptions, link
  to existing conceptual owners, and leave new general guides as separate work.
- Route: Editorial scope control during the example update.

## Proposed business and product context

### Stable facts

Northbank operates two depots, **Central** and **Riverside**, in one regional
service area. It owns a fleet, uses maintenance suppliers, and occasionally
sources replacement equipment from partner depots. Its existing service
combines a contractor portal, a staff console, assisted phone bookings,
physical preparation, delivery or collection, support, and billing.

The focal audience is small contractors whose crews must coordinate equipment
with a scheduled job start. A business owner or administrator may arrange and
pay for the rental; a site supervisor coordinates the work; an operator uses
the equipment. These roles can be held by the same person, but their goals
must not be assumed identical. Depot staff, dispatchers, repair suppliers,
support colleagues, developers, and responders have their own work and needs.

Customer alternatives include owning equipment, borrowing, using another
rental provider, rescheduling the job, and purchasing a service with an
operator included. Flexible pickup renters provide a contrasting segment.
Neither comparison is a claim about an actual market.

The strategic hypothesis is that dependable fulfillment and recovery can earn
repeat preference and a sufficient premium to cover reserves, staff effort,
delivery, and support. Higher utilization can conflict with reserve capacity;
faster confirmation can conflict with trustworthy promises. Better worker
scheduling and supplier coordination may create value for those participants
as well as the company. No gain is assumed to have been demonstrated.

### The product problem

Northbank grew from one depot and software organized around a particular
machine assigned to a booking. Across two depots, staff compensate for stale
records, breakdowns, and ambiguous confirmation through calls and spreadsheets.
The portal can appear reassuring before the underlying commitment is secure.

The recurring conceptual insight is:

> A customer buys access to an agreed capability for a period under agreed
> terms. A physical machine is one means of fulfilling that commitment.

This is a proposed model for the selected offering, not a universal rental
rule. Some customers may require a named machine or prohibit substitution.
Those are useful contrasting cases. A change in the internal model does not
authorize changing an existing customer's agreement.

Use the following working vocabulary consistently, while showing where the
legacy system fails to preserve it:

| Term | Proposed meaning in the case |
| --- | --- |
| Request | The customer's desired capability, period, site constraints, and decision deadline; no equipment promise yet |
| Offer | Proposed price, terms, capability, and period; acceptance and securing capacity still have stated conditions |
| Hold | Temporarily secured capacity with an explicit expiry and owner |
| Confirmed reservation | Northbank's recorded commitment under accepted terms, after required capacity and deposit conditions are established |
| Allocation | Assignment of a particular asset to fulfill the reservation; separately changeable within the agreed terms |
| Ready for handover | Fleet/depot judgment under its release process, distinct from whether the asset can be promised for a future period |
| At risk | Evidence threatens fulfillment and requires recovery; it does not erase the commitment or silently redefine it as pending |
| Withdrawal | Explicitly recorded withdrawal under the accepted policy, with customer communication and applicable consequences |
| Fulfilled | The agreed service has actually been supplied, assessed separately from issuing or reading a confirmation |

The simplified pilot may use staff control to secure capacity; the later
allocation design uses software enforcement. Neither may let silence mean
confirmation. Withdrawal policy and its consequences need an explicit
fictional acceptance decision; the ability to withdraw is not permission to
advertise unconditional fulfillment.

### People and decision responsibilities

Use three collaborating responsibility groups: booking/product experience,
depot systems/integrations, and platform/operations. Do not infer one bounded
context per group or one deployment per team. A designer and two engineers can
form the bounded team in the Shape Up episode without describing the whole
organization's staffing.

Product and depot leadership decide service scope and business obligations.
Design and engineering contribute alternatives and feasibility evidence.
Technical owners decide implementation within those obligations. Responders
hold explicitly assigned coordination roles during incidents. These are
fictional arrangements chosen to expose contribution, authority, and learning.

## Existing product and engineering system

Give the case enough concrete structure to inspect without inventing an entire
production company:

| Surface or dependency | Baseline responsibility | Useful tension |
| --- | --- | --- |
| Contractor portal | Request equipment, inspect status, manage a reservation, obtain invoices/receipts | A reassuring status can conceal uncertainty; mobile use and keyboard access matter |
| Depot console | Prepare equipment, confirm capacity, arrange collection/delivery, manage exceptions | Local knowledge and urgent overrides can bypass software assumptions |
| Shared application package | Booking, fleet integration, payment coordination, identity, documents, technical helpers | Mixed meanings and dependencies make a small rule change span unrelated modules |
| Fleet product | Equipment catalog, condition/inspection records, depot location | Fresh reads do not establish atomic reservation capability |
| Payment provider | Deposit authorization and payment records | Decline, success, and unknown outcome require different handling |
| Database | Northbank reservation and allocation state, operation history, durable work | Transaction boundaries and ownership determine what can be promised |
| Queue and document workers | Render and deliver receipts; retry recoverable work | Safe replay and worker failure differ from losing or duplicating financial effects |
| Identity and messaging providers | Authentication and communication delivery | Authentication does not decide Northbank's substitution authority; delivery does not prove comprehension |
| Build/task runner, package manager, compiler, linter | Construct and check the software | Custom checks may duplicate established capabilities or enforce a distinct rule |
| CI/CD and deployment configuration | Invoke tasks, create artifacts, deploy versions, sequence migrations | Passing source checks does not identify what was deployed or establish recovery |
| Telemetry, support records, and measures | Observe technical behavior and customer consequences | Missing telemetry, proxies, and cohort changes can make conclusions misleading |

Use technology-neutral responsibilities and small TypeScript-shaped examples.
Commands, provider versions, and framework recipes belong in an explicitly
bounded implementation companion if later needed. The portable explanation
must survive changing the runner, framework, cloud, and tracker.

The fictional baseline can include this representative layout:

```text
apps/contractor-portal/
apps/depot-console/
packages/application/src/
  booking/booking-service.ts
  fleet/availability.ts
  auth/staff-actions.ts
  billing/render-receipt.ts
  notifications/reservation-status.ts
  ids.ts
  runtime/
scripts/check-boundaries.*
scripts/verify.*
deployment/
```

Here `available` is overloaded, staff-access code contains substitution policy,
receipt rendering can reach payment mutation, and several entrypoints maintain
their own check lists. These are invented conditions to investigate. They are
not findings from a real codebase.

## Episodes and chronology

Use these labels as editorial anchors, not mandatory document identifiers or a
new lifecycle taxonomy. Each passage names the scope it assumes.

| Episode | Situation and proposed detail | What remains open |
| --- | --- | --- |
| A — Choose a dependable service | Investigate failed first rentals; compare dependable fulfillment with economical flexible pickup; examine customer, staff, and supplier value | Demand, causal effect on repeat use, and full economics |
| B — Make confirmation understandable | Compare a calendar, guided request, and suggested appointments; shape staff confirmation, current status, and a neutral notification linking to it | Whether dependable confirmation is feasible within the bounded operating arrangement |
| C — Learn what the commitment requires | An inventory experiment shows the assumed API cannot prevent competing allocations; reconsider the two-depot project; choose a controlled one-depot pilot | Later automation, second-depot rollout, and whether the pilot benefits customers |
| D — Separate commitment from allocation | A later investment makes allocation ownership explicit and supports policy-governed replacement while preserving customer terms | Partner capacity, multi-machine reservations, and automated cross-depot recovery |
| E — Simplify the engineering system | Review boundaries and task semantics; extract owned responsibilities; verify established alternatives; retire redundant checks and plumbing | Mechanisms whose guarantees are not yet replaced; actual reduction in maintenance burden |
| F — Observe performance and respond | After an explicitly separate two-depot rollout, inspect confirmation measures; investigate a receipt-worker incident and coordination failures | Outcome attribution, permanent correction, and whether current intervention policies remain suitable |
| G — Renew or retire | Reconsider an old invoice export, extend a successful depot practice, and investigate demand for operated services | New offering, changed competencies, migration responsibilities, and whether to enter the new business |

Episodes are connected but do not imply a strict project sequence. Engineering
care and incident response continue during discovery and delivery. E can start
from an independent maintenance concern. F can reveal a reason to reopen A.

Preserve the existing six-week illustration with explicit distinctions:

- Shape Up's six weeks is an appetite for a designer and two engineers. The
  bounded confirmation proposal excludes automated substitution, inter-depot
  transfers, and an inventory replacement.
- Alleman's six-week, $120,000 two-depot commitment is a separate management
  scenario. Its week-three evidence and revised seven-to-nine-week,
  $140,000–$180,000 forecast explain reconsideration. The selected one-depot
  pilot does not deliver the original scope.
- These can be compared as alternative views/scenarios around B/C; do not
  claim that an appetite, estimate, budget, and baseline mean the same thing
  or that both methods must be adopted.
- D and the later two-depot measurement period require new decisions. They
  are not scope silently smuggled into the original confirmation bet.

## The detailed DDD and code episode

### Model and boundaries

Use **Rental Operations** for commitments, substitution, and allocation;
**Fleet Readiness** for condition and release for handover; **Billing** for
invoices and payment meaning; and **Identity/Access** for identity and access
facts. Distinguish Northbank's models from provider interfaces. The actual
context map must show current entanglement before the proposed separation.

Within Rental Operations, use:

- `Reservation`: identity, agreed capability/period/terms, and commitment state.
- `RentalPeriod`, `CapabilityRequirement`, and `Money`: values with relevant
  behavior and explicit units or currency.
- `AssetSchedule`: allocations and holds for one asset within a stated horizon.
- `SubstitutionPolicy`: whether a candidate satisfies the agreed constraints.
- `ReplaceAllocation`: application coordination, permission checks, persistence,
  and recovery for one replacement request.
- `AllocationReplaced`: a committed internal occurrence, translated separately
  if another context needs an integration contract.

Begin D with a single reservation line and a Northbank-owned asset at one
depot. The broader model may support multiple lines; the worked transaction
does not claim to solve multi-machine or partner allocation.

The promise, physical readiness, payment attempt, and document job each need
their own state. Avoid one universal `status` field. A confirmation can become
at risk or be withdrawn under the accepted policy; historical confirmation
must remain distinguishable from current state and actual fulfillment.

### Rules to make reviewable

Propose the following specimen rules, with acceptance explicitly located
inside the fictional episode:

1. An asset has no overlapping active allocations or unexpired holds within
   the declared scheduling scope.
2. An authorized replacement preserves reservation identity, agreed period,
   price, and capability constraints. A candidate outside the agreed terms
   requires a new customer decision.
3. A failed replacement cannot leave the reservation pointing to an allocation
   that was not secured. Existing allocation state is preserved on failure;
   that does not mean a broken original machine remains fit for use.
4. Repeating the same replacement request produces no second replacement or
   duplicate business effect; reusing its identity with different inputs is
   rejected. Its retention and retry horizon are explicit.
5. Fleet readiness is checked under its own handover responsibility. An
   allocation record is not an inspection certificate or proof of future
   physical readiness.
6. A receipt job can be retried without creating another charge. Financial
   records remain owned by Billing.

Do not supply invented engineering safety thresholds. Equipment constraints
in this case are agreed fictional inputs used to explain modeling; an actual
equipment decision needs its governing domain authority.

### Concrete code and ownership changes

| Baseline responsibility | Proposed owner and representative file | Reason and evidence needed |
| --- | --- | --- |
| Substitution decision inside `auth/staff-actions.ts` | `rental-operations/substitution-policy.ts` | Domain policy survives changing identity provider; independent policy examples expose unacceptable candidates |
| One Boolean in `fleet/availability.ts` | Fleet readiness translation and Rental Operations reservable-capacity query | The same machine can be ready now but committed tomorrow; each meaning has a distinct source |
| `booking-service.ts` changes machine IDs directly | `rental-operations/replace-allocation.ts` and `asset-schedule.ts` | Concurrency, failure, and replay evidence establish allocation behavior |
| All identifiers in `ids.ts` | Generic identifier mechanism plus IDs owned with their concepts | A reusable mechanism no longer defines every domain's vocabulary |
| Receipt rendering reaches payment mutations | Billing supplies committed document data; document worker renders it | Duplicate delivery/replay cannot initiate another financial action |
| Feature policy and cross-context composition inside low-level helpers | Owned policy plus explicit application composition | Dependency direction is justified by responsibilities and interfaces |

Keep packages named for meaning. Classifications can be annotations used in
the discussion. A bounded context may contain several modules/packages; a
package is not thereby a bounded context or deployment. Do not turn
core/supporting/generic classifications into automatic dependency tiers.

For the bounded local-storage version, an intentionally explicit pseudocode
outline would be:

```text
replaceAllocation(request):
  establish actor permission and obtain candidate capability evidence
  begin Rental Operations transaction
    check durable request identity and prior result
    load reservation and both affected schedules under concurrency control
    validate expected revision, commitment state, and substitution constraints
    secure replacement and release former allocation as one atomic change
    record new assignment, request result, and pending publication
  commit
  publish committed occurrence through the durable publication path
```

This version deliberately allows one transaction across the reservation and
affected schedules within one owned persistence boundary. Explain that choice
and its contention costs rather than implying the one-aggregate-per-transaction
heuristic mechanically solves the invariant. The eventual authoring must make
locking/constraint behavior, lock ordering, conflict handling, and retry scope
concrete before claiming concurrency protection.

Provider calls stay outside that transaction. A partner reservation or payment
authorization needs a separate durable attempt/reconciliation model. A timeout
is an unknown outcome; it does not prove the provider failed or authorize a
second charge. A capacity hold's expiry and an uncertain authorization must be
resolved together before confirmation. These are a useful advanced use-case
branch, not hidden prerequisites of the small replacement example.

### Strategic classification and evolutionary assumptions

Make these separate judgments available for discussion. The placements below
are invented starting assumptions for Northbank's case, not market research.
They can change in a later episode when the premises change.

| Subject at the stated granularity | DDD judgment for Northbank | Assumed Wardley placement and implication |
| --- | --- | --- |
| Deciding acceptable substitutions and recovery priorities | Core: this knowledge is hypothesized to support Northbank's distinctive promise | Custom: local terms, site constraints, and recovery choices require tailored work; invest in learning and explicit policy |
| Routine fleet catalog and condition recordkeeping | Generic where established models meet the relevant need | Product: assume several mature offerings; examine integration and data fitness before adopting or replacing |
| Northbank's depot handover coordination | Supporting where local procedures are necessary but not a source of advantage | Custom for the local coordination activity; simplify or adapt proportionately |
| Standard invoicing and deposit authorization | Generic under the case's conventional commercial terms | Product/service provision assumed available; preserve agreement and reconcile uncertain outcomes through owned integration |
| Automatic recovery recommendation experiment | Strategic role remains a hypothesis; novelty alone does not make it core | Genesis: usefulness under unusual constraints has not been demonstrated; a small experiment precedes reliance |
| Build and dependency enforcement | Engineering-system capability, not a DDD subdomain classification | Product capabilities assumed available in adopted tools; demonstrate replacement of the custom approximation |
| Compute and durable storage provision | Technical dependencies, not business subdomains merely because they are reusable | Utility provision assumed available; evaluate required semantics, operation, and cost |

The distinctiveness of a whole fulfillment capability does not mean every
algorithm or mechanism inside it deserves custom construction. For example,
routine scheduling machinery may be reusable while the policy governing which
commitment to protect remains specialized. Conversely, moving a component to a
folder named `generic` says nothing about market maturity or business meaning.

## Tooling, CI/CD, infrastructure, and migration

The engineering-system episode should be as specific as the domain episode.
Use three representative changes and one deliberate retention:

| Decision | Proposed example detail | Completion evidence |
| --- | --- | --- |
| Replace simulated boundaries | Split a tangled responsibility before extraction; define owned public interfaces; use established package, compiler, and lint capabilities where they cover the chosen policy | Representative forbidden imports and cycles are rejected through supported consumption paths; legitimate consumers still build; the retired checker has no unique remaining obligation |
| Unify task meaning | Two scripts, a hook, and CI maintain four validation inventories; CI omits a new allocation-integration check | One resolved membership authority; supported invocations include the required check; deliberately failing that check fails the intended workflow |
| Replace obsolete runtime plumbing | A custom telemetry drain implementation can be replaced if the adopted runtime facility demonstrably preserves shutdown delivery under the deployed worker model | Fault/shutdown experiment for that runtime; behavior and resource cost recorded; no assumption that a provider feature name establishes equivalence |
| Retain a distinct domain obligation | Keep verification of substitution constraints and access restrictions | Generic tooling cannot establish the domain judgment; its test/analysis remains with the owning rule |

Use deletion as an outcome of demonstrated replacement, not as a success
metric by itself. Some adapters, coordination, and technical mechanisms remain
necessary. AXM-1773's proposed principle that only domain code should be bespoke
should not become an unqualified rule in the portable case.

Give the fictional repository separate task intentions for fast source
validation, integration evidence, artifact construction, migration rehearsal,
and deployed smoke checks. Explain inputs, dependencies, output artifacts,
cache meaning, and freshness. A cached build result cannot establish today's
provider health. A hook may intentionally run a smaller task; it must not
misrepresent that task as the full release assessment.

CI/CD supplies triggers, sequencing, privileges, artifact promotion, and
handling of results. The task contract supplies the meaning of each invoked
operation. Include an artifact identity linked to source, configuration, and
results so the deployed object can be distinguished from a passing source
revision. Do not prescribe a new runner or cloud product in the foundation text.

For infrastructure, choose a transactional store for the bounded allocation
design, durable jobs/publication for post-commit work, and replaceable document
workers. Show ownership of schemas, credentials, queue retry behavior,
deployment configuration, recovery, and costs. A provider substitution must
consider behavior, data migration, operational burden, and price; a market
category is insufficient evidence of fit.

The migration must be part of the worked change:

1. Inventory existing promises and actual writers, including depot procedures
   and provider integrations. Observe current behavior without blessing every
   legacy behavior as correct.
2. Resolve policy ownership and dependency cycles before splitting packages.
3. Introduce the new representation and backfill only what the old records
   support. A named-machine agreement cannot be silently widened to allow
   capability substitution. Keep ambiguous records for explicit resolution.
4. Move a bounded depot/cohort to one authoritative allocation writer;
   reconcile holds and assignments. A second writer cannot remain capable of
   allocating the same inventory outside the new protection.
5. Exercise behavior, deployed permissions, queue recovery, and customer/staff
   understanding before expanding the cohort.
6. Retire obsolete paths, scripts, data access, and configuration after their
   obligations and consumers are accounted for.

Rollback must address data and commitments as well as application code. Once
new records or external effects exist, reverting a binary alone may be
insufficient. State when to stop writes, reconcile, roll forward, or restore
compatible readers. Do not sell a modular monolith as an automatic need for
distributed services.

## Evidence, measures, and operating care

### Distinct evidence for distinct claims

| Claim | Smallest useful example evidence | What it does not prove |
| --- | --- | --- |
| Candidate meets agreed substitution rules | Plain input/output examples of the policy | Concurrent allocation or physical fitness at handover |
| Competing requests cannot allocate the same asset | Concurrent requests through the application interface against the real persistence mechanism | Partner-provider atomicity or customer value |
| Replacement is atomic and replay-safe | Conflict, interrupted operation, and retry scenarios observing durable results | Exactly-once delivery by a queue |
| Receipt retry has no second financial effect | Durable job/replay evidence with a payment boundary that would expose an unintended call | Every real payment-provider failure mode |
| Current confirmation is understandable and operable | Scenario evaluation with contractors/depot staff; targeted real-browser interaction/accessibility evidence | Full accessibility conformance or dependable equipment delivery |
| Required validation participates in CI | Resolved task inspection and an observable failure propagated by the workflow | Runtime correctness by virtue of task inclusion |
| Release preserves existing commitments | Migration rehearsal on representative histories and deployed checks of the identified artifact | Safe migration for histories excluded from the rehearsal |
| The service helps contractors | Observed fulfillment, crew disruption, customer accounts, and repeat-use evidence with cohort context | Causal attribution from one improved percentage |

An authoritative example can execute at any suitable test level. If an accepted
requirement already states the rule, the example is its synchronized witness.
If the example text is chosen as the requirement, identify that authority and
avoid adding a second independent statement. Characterization of existing
behavior remains evidence about what happens until an acceptance decision
establishes what ought to happen.

### Preserve the current numerical illustrations with explicit scope

Use the KPI definition already in the bundle: distinct routine requests at two
depots, submitted at least one hour before the recorded dispatch deadline;
numerator confirmed before and still valid at that deadline; cancellations
remain in the denominator under the declared rule. Retain the illustrative
82% baseline, 89% observed value, and 92% target. Locate this in the later
two-depot episode, with comparable definitions and separate depot counts.
There is no claim that the one-depot pilot generated those results.

Pair that measure with actual fulfillment, post-confirmation withdrawal,
customer-reported crew disruption, and cost/margin inquiry. No causal
improvement or realistic market benchmark is asserted by the invented numbers.

Retain the separate confirmation-read SLI: an authorized client's attempt
receives the authorized current state within two seconds; the illustrative SLO
is 99.9% over 28 days. Currentness needs reconciled evidence, not just an HTTP
success. Keep unknown and missing telemetry visible. The million-attempt,
900-bad-attempt calculation is an arithmetic exhibit, not asserted traffic
for the two-depot pilot. Its 99.91% result and 90% consumed error budget do not
establish fulfillment performance or an SLA breach.

Likewise, the value-stick amounts, employee surplus amounts, forecast ranges,
and worker-headroom calculation stay labeled numerical exhibits with their
own assumptions. Do not combine them into an invented company financial model.

### Receipt-worker and incident episode

Keep the new maintenance examples' baseline: durable receipt jobs, replay that
cannot charge again, and sufficient spare processing capacity. Accepting an
isolated worker failure can preserve the service under those assumptions.
Contrast that with a scenario where a receipt is required immediately for
collection and only one worker is available. Label the changed premise.

Use runtime-state accumulation for scheduled, condition-based, and predictive
intervention comparisons. Rising memory is first an observation; diagnosis
and a forecast require additional evidence. A six-hour headroom estimate is a
conditional projection; the time required to drain, replace, warm, and verify
the worker determines whether it is useful.

In a separate incident branch, changed receipt workloads defeat spare capacity
and coordination spans the three responsibility groups. The engineering
manager intervenes after conflicting instructions. This places the existing
JTBD case inside Northbank while preserving its main distinction: the manager
may seek confidence and reduced personal intervention, while responders need
to coordinate a response. Training, responsibility changes, a managed service,
and software remain competing responses.

The Operational Incident Record preserves impact, control, chronology,
restoration, and follow-up. A Defect Report preserves the evidence and
expectation concerning resource retention. A corrective Change records the
bounded modification and its verification. Restarting may restore operation;
it neither confirms root cause nor closes every linked record. A known issue
can also be investigated before operational impact warrants an incident.

### Renewal and continuity

Place the long-lived invoice-export example inside Northbank Billing. Customers
and support staff have learned practices around its outputs. A new format or
provider must account for those dependencies, discover who still uses the old
export, and provide an appropriate transition. Preserving bytes and preserving
use can demand different actions.

For Drucker's four disciplines, use concurrent Northbank choices: retire an
unproductive legacy export after consumer migration, improve current
confirmation, extend a demonstrably successful depot practice, and investigate
an operated-equipment offering. Keep the library illustration as an optional
contrast showing applicability beyond commercial software.

The operated-service branch changes the business assumption that customers
can turn equipment access into productive work themselves. It could require
different competencies and model boundaries. It must remain a new opportunity
under examination, not a feature automatically added to the rental roadmap.

## How the case supports the body of knowledge

### Foundations

| Concept | Proposed use of the case |
| --- | --- |
| Jobs to Be Done | Contractor choice supplies the main cross-bundle connection; retain incident coordination as a Northbank secondary inquiry to distinguish buyer progress, performer goals, and alternatives |
| Value-based strategy | Show customer, employee, and supplier exchanges; preserve numerical exhibits and the reserve-capacity/cost tension |
| Playing to Win | Compare dependable contractor service and economical flexible pickup; make mutually constraining capabilities and management systems visible |
| Cagan product strategy | Focus on failed first rentals; give a team a problem; show an integration-capacity conflict and evidence reopening the retention hypothesis |
| Wardley mapping | Map fulfillment dependencies and changing provision; separately map the engineering team's ability to change and release safely |
| Strategy perspectives | Follow the same investment through value, advantage, landscape, team focus, assumptions, and renewal without merging their answers |
| Drucker's theory of the business | Operated-service demand challenges the equipment-access assumption; distinguish a broken execution path from a weakening business theory |
| Drucker's organizational renewal | Concurrent abandonment, improvement, extension of success, and exploration; identify who bears transition costs |
| Buxton design | Calendar, guided request, and suggested offers; sketches expose pending state, competing requests, and customer effort before visual polish |
| Use cases | Reserve equipment, replace an allocation, cancel a confirmed reservation, and recover an uncertain authorization; keep goal levels and boundaries visible |
| Domain-driven design | Discover promise versus assignment, readiness versus reservability; classify subdomains; map contexts; trace one rule into code and transactional behavior |
| Brooks's architect role | Make “confirmed” coherent across portal, staff console, notifications, and recovery; preserve decision responsibility with implementation feedback |
| Shape Up | Bounded staff-confirmation bet with explicit no-gos and phone fallback; scope reduction does not weaken the selected essential promise |
| Alleman | Demonstrated capability, integration evidence, resource constraints, revised forecasts, and authorized scope change; distinguish accomplishment from customer benefit |
| KPIs | Stable populations and definitions; compare target, observation, guardrails, and interpretation; make denominator changes consequential |
| SLIs/SLOs/SLAs | Distinguish reading current state, receiving a commitment, and actual fulfillment; define measurement and agreement boundaries |
| Maintenance strategies | Choose by function, failure mode, consequence, evidence, and intervention burden |
| Run-to-failure maintenance | Replaceable receipt worker with durable work and spare capacity; altered dependencies change acceptability |
| Preventive maintenance | Demonstrated accumulation supports time/use-based draining; contrast scheduled inspection with scheduled replacement |
| Condition-based and predictive maintenance | Observation, diagnosis, forecast, warning time, and post-intervention evidence remain distinct |

### Lifecycle guidance and deeper subtrees

| Area | Shared specimen or connection |
| --- | --- |
| Value and demand; outcomes and evidence | Offering/audience/need/job/proposition relationships; observed choice and fulfillment without assuming causality |
| Requirement development | Sales, depot, contractor, support, and provider accounts disagree; preserve candidates and assign the actual decision |
| Requirement authority and authoring | One substitution rule, one quality obligation, a provider-interface obligation, and a migration obligation; use prose, decision table, state model, and executable example where each helps |
| Requirement review and lifecycle | Inspect conflicting promises; distinguish unclear wording from unresolved policy; trace a change in substitution rights through old bookings, data, tests, staff procedure, and measurement |
| Requirement/work-item host adaptation | Represent the same identities and relationships in a document and a tracker example; keep host behavior distinct from portable meaning |
| Narrow, cross-boundary, and browser verification | Policy examples, real-store concurrency, provider uncertainty, artifact/deployment checks, and observable user interaction; each test earns its own claim |
| Specification authority and test-suite quality | Accepted behavior versus characterization; readable intent versus binding code; fixtures that preserve the failure being assessed |
| Repository task interface | The four-inventory example, explicit prerequisites, cache/freshness, caller roles, and one supported meaning per task |
| Codebase review | Start from a snapshot and claim context; assess product outcomes using source, configuration, data, tests, and evidence without substituting mechanism presence for a verdict |
| Work-item roles and common guides | A linked incident, defect report, corrective Change, and separately proposed simplification Change; evidence, decisions, delivery, verification, and closure remain independent |
| Maintenance and care | Invoice compatibility, tacit support knowledge, consumer migration, useful continuity, and justified retirement |
| Delivery and operations scope | Concrete release/recovery artifacts illustrate responsibilities; general workflow and operational guides remain acknowledged gaps |

The codebase-review episode can exercise all ten candidate quality questions
without turning them into ten mandatory findings: appropriate capability
(suitability), allocation rules (correctness), recovery (reliability), account
and staff boundaries (security), harmful substitution consequences (safety),
workload/cost bounds (efficiency), usable status (usability), fleet/payment
meaning (compatibility), representative change (evolvability), and accurate
maintainer understanding (intelligibility). Real-world safety evidence is not
supplied by the fictional capability examples; a review must record its limit.

Use the existing cross-cutting records to connect the engineering system:
claim context scopes the review; specification states intent; structure
localizes responsibility; lifecycle integrity covers artifact/migration
identity; risk describes consequences; assurance selects methods; feedback
connects observations to action; evidence bounds the resulting claims.
Pipeline throughput and test-suite quality retain their own assessment
subjects rather than becoming extra product-quality pillars.

## Maps, artifacts, and discovery

Use several connected views with explicit correspondence, not one overloaded
diagram:

1. A service/actor view includes contractors, depot work, equipment, transport,
   suppliers, and software.
2. A product Wardley map anchors on keeping the contractor's work moving.
   Include the physical dependencies omitted from the current digital map
   when making a whole-service claim. Leave evolutionary placement unresolved
   where the fictional market assumptions have not been specified.
3. An engineering Wardley map anchors on the team's need to change and release
   dependably; it includes tests, build, packages, deployment, compute, and
   telemetry. Its user and scope differ from the contractor view.
4. Current/proposed DDD context maps describe meaning and relationships.
5. Module and task graphs describe imports and execution dependencies.
6. A deployment/data-flow view locates persistence, processes, queues, and
   external effects.

For each consequential element, state how it corresponds to another view.
A Wardley component can be realized by multiple modules or a purchased service;
a module may support several capabilities. Strategic importance, evolution,
model boundary, dependency direction, and deployment are independent judgments.

The minimum shared artifact set for authoring is:

- A concise case context with stable facts and the episode/alternative map.
- A service promise and small vocabulary of deliberately distinguished terms.
- A strategic choice comparison and the two scoped Wardley views.
- One candidate-experience comparison and bounded project/pitch variant.
- A small current/proposed context and module example with representative code.
- A few linked obligation, executable-example, and evidence specimens.
- One task-contract/CI change and one migration/recovery record.
- A measure definition with a small fictional result exhibit.
- A linked incident/defect/change record set and a retirement decision.

Do not build a second tracking system, executable demo product, or universal
metadata schema just to maintain the example. Blank reusable templates remain
blank; place filled specimens beside the explanations that benefit from them.

For publication, propose a root-level cross-lifecycle concept titled
**Northbank Equipment: a product-engineering case**, linked from the reading
guide and bundle index. Keep its main job to establish context and routes.
Detailed treatments stay with the concept that explains them. This proposal
file is an editorial planning artifact outside the managed knowledge source.

Each local example needs only four things: its episode, the minimum premises,
the decision/distinction under discussion, and a useful next question. It
must remain readable when retrieved independently. Cross-references should
explain the conceptual move, for example:

> The allocation test checks whether competing requests preserve the accepted
> rule. To examine whether the resulting service reduces crew disruption,
> continue to Outcomes and evidence.

Maintain one owner for shared case facts, while allowing bounded local
recaps. Local alternatives state what premise changes. Keep assumptions,
proposals, fictional acceptance decisions, implementation states, and
illustrative results separate. Source-authored examples and contrary cases
remain when they teach something the Northbank case cannot.

## Proposed update sequence and completion criteria

1. Establish the stable case context, episode boundaries, and scope of the
   numerical exhibits. Resolve the confirmation/commitment vocabulary before
   expanding its use.
2. Develop D and E in enough detail to test the design of the case: one
   domain-rule-to-code change and one tooling/CI/infrastructure change, each
   with evidence and migration. If either needs too much machinery to teach
   its point, simplify the specimen before revising the whole corpus.
3. Update DDD, Wardley, use cases, and the linked requirements/verification/task
   examples as one coherent group. Preserve source attribution and distinguish
   explanatory synthesis from the methods' own claims.
4. Update value, strategy, design, architectural responsibility, and project
   examples, preserving the stated alternatives and scope exclusions.
5. Align KPI, service-level, maintenance, incident, and renewal episodes; then
   connect selected lifecycle guides to the same specimens.
6. Revisit the new reading routes and local cross-references after the examples
   exist. Preserve question-led entry and current concept locations; update
   indexes/descriptions only where their canonical content actually changes.

The update is ready for review when a reader can follow a business claim down
to one technical obligation and bounded result, and follow one technical
observation back to an ownership or product decision. The review should also
confirm coherent scope/timing, explicit alternatives, local readability,
correct authority relationships, and no claim that an illustrative artifact
fills an unwritten guide. Normal link, metadata, and package validation applies
when the managed docs are actually changed.

This proposal is based on repository evidence and editorial analysis. It has
not been tested with readers or implemented as a case application. The next
work is the coordinated documentation update using this case, with the
concrete choices above as its proposed starting point.
