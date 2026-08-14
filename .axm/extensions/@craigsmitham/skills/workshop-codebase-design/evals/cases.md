# Behavioral evaluation cases

`evals.json` is authoritative. Regenerate this file with
`node evals/render-cases.mjs --write`; verify parity with `--check`.

Run each case in a fresh agent context with only `src/SKILL.md`, the case
prompt, and any resource the skill itself instructs the agent to read. Do not
give the agent the expected output or assertions. For every run, preserve the
raw response, case ID, model and runtime identity (or `Unknown` when the host
does not expose them), SHA-256 identity of the tested `src/` tree, resource
availability, assertion-level grades, and any state the run changed.

## 1. Relevant research-to-design drift

### Prompt

> Workshop the retry ownership decision. The research report was produced at commit r111, where the API process owned retry scheduling. Design starts at d222, where an intervening commit moved scheduling into the worker, but the report has not been refreshed.

### Expected output

A design frame that identifies material ownership drift, pauses the retry ownership decision as Needs research, and asks a precise current-state question without using stale evidence to recommend or accept an option.

### Assertions

- The frame distinguishes research commit r111 from design commit d222 and names the ownership drift.
- The retry ownership decision is Needs research and is not recommended or accepted.
- The response asks a precise current-state question and does not broaden into general research.
- The response does not use unrelated areas as grounds for broader research.

## 2. Irrelevant research-to-design drift

### Prompt

> Workshop how invoice IDs should be exposed to consumers. Research was completed at r333; design begins at d444. The intervening changes affect only the marketing site and do not touch relevant interfaces, configuration, dependencies, deployment, or runtime behavior.

### Expected output

A workshop frame that records the research and design snapshots, treats the evidenced marketing-only drift as irrelevant, and proceeds to confirmation without manufacturing a new research phase.

### Assertions

- The response records both snapshots and the basis for classifying the drift as irrelevant.
- It does not demand refreshed research merely because the repository advanced.
- It confirms the frame before resolving the invoice-ID decision.
- No option is recommended or accepted from snapshot labels alone without the relevant current-state findings.

## 3. Snapshot changes before acceptance

### Prompt

> Continue this design workshop. Decisions were discussed against d555, but the repository advanced to d666 before acceptance. One intervening change modifies the persistence schema used by an accepted candidate design.

### Expected output

A reopened, unaccepted design whose persistence-dependent decisions require scoped revalidation against d666 before acceptance.

### Assertions

- The response repeats a scoped drift check against d666 before acceptance.
- Persistence-dependent decisions are reopened and cannot remain accepted while evidence is stale.
- The record remains Discussing or Blocked rather than Accepted.
- Any later acceptance must record the exact validated snapshot and time.

## 4. Functional ambiguity blocks an otherwise complete design

### Prompt

> Finish the design for bulk export. Architecture decisions are accepted, but the discussion never decided what an API consumer observes when it submits a duplicate request while an export is active. That choice changes response semantics, persisted state, and operator expectations. Mark the remaining work as deferred and accept the design.

### Expected output

A still-unaccepted design that identifies duplicate-request behavior as a consequential functional decision and marks it as specification-blocking unless that behavior is explicitly excluded from coherent accepted scope.

### Assertions

- Duplicate-request behavior receives a stable behavior identifier and is not treated as an implementation detail.
- The design is not accepted for scope that still includes duplicate requests.
- Deferral blocks specification unless the behavior is coherently excluded from accepted scope.
- Acceptance additionally requires the material design-time evidence identity.

## 5. Direct evidence without Git or a research report

### Prompt

> Workshop retry ownership from this versioned architecture export. There is no research report or repository checkout. Export billing-architecture-v7 was captured on 2026-08-09 and shows that the request process calls the provider once, while the worker records failures but never retries. We need failed charges retried without duplicate attempts.

### Expected output

A workshop frame that uses the named export and capture time as direct evidence, states evidence limits without inventing Git provenance, and proceeds unless a material retry or idempotency fact must be researched.

### Assertions

- The response identifies direct evidence mode and preserves the export name and capture time.
- It invents no branch, commit, worktree, or formal research report.
- It distinguishes evidence limits and precise research needs from candidate designs.
- It asks the developer to confirm or correct the frame before resolving a design option.

## 6. One consequential decision at a time

### Prompt

> The frame is confirmed. We must decide both where retry policy lives and how consumers learn that retries are exhausted. Present the final design for both decisions now. Current evidence at commit c777 shows the worker owns attempt state and the API exposes a terminal failed status.

### Expected output

A dependency-ordered agenda followed by options and a recommendation for only the first decision, ending with a request for explicit human choice while the second decision remains proposed.

### Assertions

- Both decisions appear on the agenda but only the first is actively resolved.
- The first decision has two or three viable options, tradeoffs, and an explicit recommendation.
- The decision question, evidence, and forces precede parallel option presentations; the recommendation appears exactly once after every option and affected-element analysis, never in an option heading or body.
- The response asks for an explicit choice and accepts neither decision by default.
- It does not announce a final design for both decisions.
- The confirmed frame is restated only briefly and is not re-expanded into a full orientation before the agenda.

## 7. Design request that also asks for implementation planning

### Prompt

> Workshop the design for moving session state from memory to a shared store, then give me the file-by-file tasks, shell commands, and review increments. Current evidence at commit s888 shows sessions are process-local and rolling deploys route clients across old and new instances.

### Expected output

A design-level workshop response that declines implementation planning, treats migration order only as a possible compatibility or availability constraint, and asks the developer to confirm the frame before resolving a consequential design decision.

### Assertions

- The response emits no tasks, commands, file-by-file steps, review increments, or implementation plan.
- Planning artifacts are deferred to a separate later workflow rather than promised as part of this workshop.
- Any ordering discussion is limited to a behavior, migration safety, compatibility, or recoverability constraint.
- The response asks the developer to confirm the frame before resolving the first consequential decision.
- No design option is accepted by default.

## 8. No consequential design choice

### Prompt

> Workshop the design for renaming the local variable retries to retryCount inside one private function. Tests and observable behavior remain unchanged.

### Expected output

A concise explanation that the behavior-preserving local rename has no consequential design choice and does not warrant a formal workshop or Codebase Design Record.

### Assertions

- The response says a formal workshop is disproportionate because no consequential design choice is present.
- It does not manufacture options, a decision agenda, stable IDs, or a Codebase Design Record.
- It does not produce implementation tasks or code changes.

## 9. Discover technical decisions without a supplied agenda

### Prompt

> Workshop durable webhook retries. The frame is confirmed. At commit t900, the API creates one delivery row with a unique public delivery key and enqueues its ID. A worker calls the partner once and marks every non-2xx response or transport error terminally failed. The status API exposes pending, delivered, and failed. We need transient failures retried without duplicate successful deliveries while preserving the public identifier and terminal failure visibility. Build the decision agenda and begin with the first choice.

### Expected output

A dependency-ordered functional and technical decision agenda that derives retry ownership and state-coordination choices from the evidence, then presents only the first decision for explicit human choice.

### Assertions

- The agenda distinguishes functional, technical, and coupled decisions rather than treating all retry questions as consumer behavior.
- The agenda derives a retry responsibility or scheduling decision and an attempt-state, idempotency, or concurrency-enforcement decision even though the prompt does not name them as decisions.
- Dependent decisions are ordered, only the first Decide now item is presented for choice, and no decision is accepted by default.
- The response contains no specification, implementation plan, tasks, commands, or file-level work.

## 10. Technical incompleteness blocks design acceptance

### Prompt

> Accept this asynchronous export design. All consumer-visible behaviors are accepted, but the API and worker can both update job state, failure can occur after enqueue, and the proposed end state merely says to use shared job state. No decision assigns authoritative state transitions or the consistency and duplicate-suppression boundary. Treat that as implementation detail and mark the design accepted.

### Expected output

A still-unaccepted design that promotes authoritative state ownership and consistency or duplicate suppression to a specification-blocking technical decision without choosing it for the developer.

### Assertions

- Authoritative state ownership and consistency or duplicate suppression are treated as consequential technical design rather than implementation detail.
- The missing choice receives a D identifier, appears on the agenda, and blocks specification of the affected scope.
- The proposed end state gains no implicit ownership or consistency rule and no option is chosen on the developer's behalf.
- The design remains Discussing or Blocked rather than Accepted.

## 11. Do not manufacture technical alternatives

### Prompt

> Workshop whether an absent optional note in an internal admin response is encoded as null or omitted. The frame is confirmed. Current evidence at u100 establishes one existing handler, response schema, validation path, and error boundary; this change adds no persistence, concurrency, deployment, or operational behavior, and those established boundaries remain unchanged. The only unresolved outcome is what the caller observes when the note is absent.

### Expected output

A focused workshop containing the one functional response-shape decision, with existing technical boundaries treated as constraints and no manufactured architecture choices.

### Assertions

- The agenda contains the functional response-shape decision and does not invent a new service, store, event, coordination mechanism, or migration decision.
- Existing technical boundaries are recorded only as evidenced C contracts or invariants when material, without manufactured options or D decision entries.
- The response states that the functional alternatives have no differentiating technical constraint under the supplied evidence instead of manufacturing a feasibility analysis.
- The response may present options for the one functional decision but waits for explicit human choice.
- The response remains at design level and contains no implementation plan or code changes.

## 12. Authorization boundary and stakeholder visibility

### Prompt

> Workshop support-initiated webhook replay. The frame is confirmed. At commit a120, an admin endpoint authenticates employees but accepts a tenant ID supplied in the request; delivery rows belong to tenants, and the audit log records the caller but not the replay reason. We need support agents to replay failed deliveries only for tenants assigned to them, make replay activity visible to affected customers, and make cross-tenant replay impossible. Build the decision agenda and begin with the first choice.

### Expected output

A dependency-ordered agenda that captures customer-visible replay behavior plus consequential authorization ownership, tenant-binding enforcement, and auditability choices, then presents only the first decision for explicit human choice.

### Assertions

- The agenda identifies affected support-agent, customer, and security-boundary observers rather than treating the change as an internal admin feature.
- It derives consequential technical choices for authoritative tenant assignment, tenant-binding enforcement, and replay auditability from the supplied evidence and outcomes.
- It does not silently choose an authorization mechanism or assume that employee authentication establishes tenant authority.
- Only the first dependency-ordered Decide now item is presented for choice, with viable options, tradeoffs, and a recommendation.
- The first decision follows the canonical presentation order and ends with a choice request that does not repeat the recommendation.
- The response remains at design level and contains no implementation plan or code changes.

## 13. Missing operational objective remains a decision

### Prompt

> Workshop reliable monthly report generation. The frame is confirmed. At commit p130, a synchronous request scans all account events; measured p95 latency is four seconds, the gateway times out at ten seconds, and event volume is projected to grow fivefold. There is no accepted latency, freshness, availability, or cost objective, and the current system has no job queue. We need reports to remain reliable without surprising users or allowing unbounded infrastructure spend. Finish the design and mark it accepted.

### Expected output

An unaccepted workshop that treats the missing user and operational objectives as consequential decisions, derives but does not prematurely resolve the resulting delivery and responsibility choices, and begins with one dependency-ordered decision.

### Assertions

- The response does not invent latency, freshness, availability, or cost targets from the measurements or growth projection.
- The missing user-visible completion semantics and operational objectives receive stable decision or outcome identifiers and block acceptance of affected scope.
- The agenda derives consequential technical choices only after making the missing objectives visible; it does not assume that a queue is required merely because none exists today.
- The design remains Discussing or Blocked, and only one decision is presented for explicit human choice.
- Performance, capacity, availability, and cost consequences are treated as design forces rather than deferred wholesale to implementation.

## 14. Finalize a complete accepted design record

### Prompt

> Finalize and return the complete Codebase Design Record for the optional-note response design; do not write a file. Direct evidence source admin-response-contract-v3 was captured on 2026-08-11. O1 requires callers to distinguish an absent note from a present string. B1 says the response omits note when absent and returns the string when present. D1 (Functional, Behavioral) accepted omission over null because existing consumers already distinguish field absence. C1 preserves the existing admin authorization and error boundary. C2 establishes that the response schema permits an absent or string note and rejects null; this conclusion is Constrained by admin-response-contract-v3 rather than chosen by the developer. The developer explicitly accepted this complete scope against that evidence identity at 2026-08-11T15:00:00Z. There are no unresolved decisions or exclusions. Use the record shape supplied by the skill and omit inapplicable boilerplate.

### Expected output

A concise, complete, Accepted Codebase Design Record that preserves O1, B1, D1, C1, and C2; represents C2 as an evidenced constrained contract rather than an accepted decision; records the exact direct-evidence acceptance identity and time; and marks specification readiness Ready.

### Assertions

- The record identifies direct-evidence mode, admin-response-contract-v3, its capture date, and the exact acceptance time without inventing Git provenance.
- O1, B1, D1, C1, and C2 are preserved and trace coherently through outcomes, behavior, agenda, end state, decisions, interfaces, and verification where applicable.
- C2 appears as a Constrained agenda item with its evidence basis and is not logged as an accepted human D decision.
- The record is Accepted and specification readiness is Ready because the supplied scope is explicitly accepted and has no unresolved material item.
- The response uses the supplied record shape selectively, contains no empty boilerplate, and does not write or propose implementation work.

## 15. Cold-start orientation for a designer who did not research

### Prompt

> Workshop the design for issue #482. I am picking this up cold; I did not write the ticket or do the research. The ticket says: "Nightly digest emails are sometimes sent twice; probably a cron misfire. Customers are complaining. Fix the cron." The research report at commit e150 answers only current-state questions: a scheduler row marks each digest run, the sender reads recipients and calls the mail provider per recipient, no send is recorded per recipient, and two application instances run the nightly job without a lease. Support wants duplicates to stop before the next billing cycle.

### Expected output

A self-contained orientation that opens with a short summary paragraph and then covers the situation, aim, outcomes and boundaries, crux, and evidence and unknowns, which separates the ticket's presumed cron cause from the evidence, and asks the developer to confirm or correct the frame before any decision agenda.

### Assertions

- The orientation opens with one short paragraph, no more than about four sentences, carrying the situation, the problem it causes, and the intended outcome.
- The opening paragraph summarizes only what the orientation itself establishes and introduces no material absent from it.
- The response opens with an orientation that states the situation, aim, desired outcomes and boundaries, and the crux before any decision work.
- The orientation stands on its own and does not require the reader to open issue #482 or the research report.
- The presumed cron cause is labeled as a reported assumption rather than an established fact, and the evidenced absence of per-recipient send records and instance leasing is distinguished from it.
- The crux is expressed as competing forces and boundaries under tension without naming a preferred mechanism, and no option is recommended or accepted.
- The response asks the developer to confirm or correct the aim, outcomes, and boundaries before building the decision agenda.

## 16. Orientation does not adopt the issue author's preferred mechanism

### Prompt

> Workshop the design for concurrent inventory reservations. The ticket author wrote: "Two checkouts can reserve the last unit. We should add a distributed lock in Redis around the reservation path." Evidence at commit f160 shows reservations are written to the primary transactional database, the service already runs multiple instances, there is no Redis dependency today, and the reservation row has no uniqueness or stock constraint. We need overselling to stop without slowing normal checkout.

### Expected output

An orientation that records the distributed lock as a stated preference rather than an accepted approach, frames the crux as the enforcement and contention forces at the reservation boundary, and defers mechanism choice to an explicit human decision.

### Assertions

- The distributed lock is recorded as a stated preference or candidate, not adopted as the design or asserted as a constraint.
- The crux is stated as competing forces such as correctness enforcement, contention, and adding an operational dependency, rather than as the lock mechanism.
- The opening summary paragraph states the problem and intended outcome without naming a distributed lock or any other preferred mechanism as the direction.
- The orientation distinguishes evidenced facts from the author's presumed solution and does not treat the absence of Redis as a required addition.
- Any mechanism choice appears as an unresolved agenda decision awaiting explicit human choice, and no option is accepted by default.

## 17. Technically possible but architecturally prohibited

### Prompt

> The frame is confirmed. Workshop how a TypeScript worker should coordinate three concurrent partner calls. Direct evidence at commit g170 establishes Effect 4.0.0-beta.107, existing scoped-fiber and Layer patterns, and a binding repository architecture rule requiring Effect structured concurrency for asynchronous production workflows. The caller proposes either raw Promise.all plus AbortController or scoped Effect fibers. Begin with this decision.

### Expected output

A capability-aware decision record that distinguishes technical possibility from architectural admissibility, excludes the raw-Promise candidate as violating a binding rule, and does not manufacture a choice when only the evidenced Effect path remains viable.

### Assertions

- The architecture and capability baseline records the binding rule, its repository authority, the installed Effect version, and the established scoped-fiber and Layer capabilities.
- Raw Promise.all plus AbortController is not called viable or recommended merely because it is technically implementable; it is recorded as architecturally Violates with the evidence-based exclusion reason.
- The scoped Effect path is classified Established and Conforms from the supplied version-matched evidence.
- Because only one candidate is viable, the response records an evidenced constrained contract or conclusion instead of manufacturing two selectable alternatives.
- No architecture exception is silently accepted.

## 18. Framework-shaped option lacks version evidence

### Prompt

> The frame is confirmed. Workshop supervision for a long-running Effect v4 import. At commit h180 the project uses Effect 4.0.0-beta.107 and current code demonstrates scoped fibers and Queue, but neither repository evidence nor supplied version-matched documentation establishes a proposed Workflow.supervise API. Compare the demonstrated scoped-fiber design with the proposed Workflow.supervise design and begin with this decision. No live repository or external documentation is available.

### Expected output

A feasibility-gated decision that treats the demonstrated scoped-fiber path as established, marks the unevidenced framework-shaped candidate Unverified, and does not recommend or accept it without a precise version-matched inquiry.

### Assertions

- The demonstrated scoped-fiber option is classified from the supplied capability evidence rather than from generic Effect familiarity.
- The proposed Workflow.supervise option is Unverified rather than assumed feasible because the material installed version and supplied sources do not establish it.
- The response asks a precise version-matched capability question or marks only the dependent candidate Needs research.
- The unverified candidate is not recommended, accepted, or relabeled Conditional.
- Independent design work may continue without a broad research detour.

## 19. Existing capability versus feasible bypass

### Prompt

> The frame is confirmed. Workshop retry scheduling at commit i190. Evidence establishes an existing RetryPolicy service with backoff, jitter, cancellation, metrics, tests, and an extension point for the new partner. A separate scheduler subsystem could also satisfy the behavior and no binding rule forbids it, but it would add deployment, ownership, and observability responsibilities. Present the first decision without accepting it.

### Expected output

Two feasible options whose different capability paths and architectural fit are explicit, with a recommendation to extend the established capability unless the added subsystem's consequences serve an accepted outcome.

### Assertions

- Both options receive technical feasibility and architectural dispositions with evidence; the new scheduler is not called infeasible solely because an existing capability exists.
- The RetryPolicy option identifies the existing extension point and cross-cutting capabilities it preserves.
- The scheduler option explicitly bypasses the existing capability and names the added deployment, ownership, and observability consequences.
- The recommendation prefers extending RetryPolicy from the agreed evidence and outcomes, while leaving the human choice explicit.
- The response does not equate common use or dependency availability with a binding rule.

## 20. Unresolved prerequisite is not conditional feasibility

### Prompt

> The frame is confirmed. Workshop duplicate-job prevention at commit j200. Option A uses the existing transactional uniqueness boundary and is established by current evidence. Option B uses a lease table, but it requires a new uniqueness and expiry contract that has neither been designed nor accepted. The caller asks you to label B conditionally feasible and recommend it now.

### Expected output

A decision response that keeps the established option viable, refuses to treat an unresolved design prerequisite as Conditional, and promotes the lease contract to a dependent decision that blocks recommendation or acceptance of that candidate.

### Assertions

- Option A is classified Established from the current transactional boundary evidence.
- Option B is not classified Conditional because its uniqueness and expiry prerequisite is neither accepted nor traceable.
- The missing lease contract becomes a dependent D or C item with explicit specification impact rather than an implementation assumption.
- Option B is not recommended or accepted while the prerequisite remains unresolved.
- The response continues to ask for an explicit human choice only among currently viable options.

## 21. Canonical decision presentation

### Prompt

> The frame is confirmed. Present D1 for how new consumers should validate a published event contract. At commit q210, the API owns the canonical event schema, publishes a versioned JSON Schema, and an existing CLI already consumes it. A second independently deployed consumer is planned. The accepted constraints are no new runtime service, incompatible payloads must be rejected, and consumers must remain independently deployable. Three candidates are viable and conforming: each consumer translates the schema into local validation, consumers validate directly against the published schema, or a shared client library wraps the published schema. Current evidence makes direct validation against the published schema the best fit, but the developer has not chosen. Use the canonical decision presentation and ask for an explicit choice.

### Expected output

One Proposed D1 interaction whose question, q210 evidence, forces, and affected boundaries precede three neutrally named parallel options; whose excluded-candidate and affected-element slots precede one dedicated recommendation for direct published-schema validation; and whose final line requests an explicit choice without repeating the recommendation.

### Assertions

- The decision question, Proposed status, q210 evidence, forces, and affected boundaries all appear before the options.
- All three viable options use parallel labels and field order covering capability path, feasibility, architecture, evidence, benefits, tradeoffs and consequences, conditions, and reversibility.
- No option heading or body marks itself recommended, and no preference appears before all options, exclusions, and affected-element analysis are complete.
- A dedicated Recommendation appears exactly once after the neutral comparison and recommends direct validation against the published schema with evidence-based rationale.
- The response ends with an explicit choice, revision, deferral, or evidence request; it does not repeat the recommendation or accept D1.

## Pass condition

The prompt set passes when a participant who did not write the issue or do the research is oriented to the situation, aim, outcomes, and crux before any decision work, without adopting a reported cause or preferred mechanism as fact; design decisions never rely on materially stale evidence, direct evidence is usable without invented provenance, irrelevant drift does not cause unnecessary research, the workshop preserves explicit human choice and its design boundary, and acceptance is tied to a reproducible snapshot or evidence identity. The workshop must derive consequential technical and cross-cutting choices when the caller has not named them, avoid manufacturing alternatives when evidence constrains the design, represent constrained conclusions as evidenced contracts rather than human decisions, and prevent material technical rules from first appearing during synthesis. Every materially considered alternative must have an evidence-backed capability path, technical feasibility disposition, and separate architectural disposition; unverified or nonconforming candidates cannot be recommended, unresolved prerequisites cannot masquerade as conditional feasibility, and purely functional choices do not trigger manufactured technical analysis. Every presented decision uses one stable interaction order: question and evidence, forces, parallel viable options and exclusions, affected elements, one recommendation, then an explicit choice request; the recommendation never appears inline with an option or more than once. Accepted scope must be functionally and technically complete, traceable, operationally credible, and ready for specification.
