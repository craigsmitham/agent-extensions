# Full-suite cases 7–9

- Runtime: Codex collaboration subagents in separate fresh contexts
- Model: Inherited session model; exact public identifier unavailable
- Tested `src/` SHA-256: `6fa0f6007b293809ddde43359963d17d27e98de3e5843dac880e9119e49bf05c`
- Reference availability: Available; not needed by these responses
- State changed: None

## Case 7 — Design request that also asks for implementation planning

### Raw response

# Codebase Design Record: Shared session store

Status: Discussing

## Frame

Evidence identity: caller-supplied evidence at commit `s888`.

Current state:

- Session state is process-local.
- During rolling deployments, clients may be routed between old and new instances.
- Therefore, cross-instance session continuity is not guaranteed. This is an inference from the two supplied facts; the precise failure behavior is not yet evidenced.

Change intent: make session state available across concurrently serving instances by moving its authority to a shared store.

Proposed outcomes:

- `O1` — A valid session remains usable when requests reach different instances.
- `O2` — Rolling deployments do not unexpectedly invalidate or fork sessions.
- `O3` — Existing session identity, authorization, expiry, and logout behavior remain unchanged unless explicitly redesigned.
- `O4` — Store failures and concurrent updates have defined, observable behavior.
- `O5` — Operators can detect store latency, failures, and migration problems.

Tentative non-goals:

- Redesigning authentication or session-facing APIs.
- Introducing indefinite session persistence.
- Migrating unrelated process-local state.

Evidence is not yet sufficient to accept a technical design. Before acceptance, the affected boundaries at `s888` need scoped evidence covering:

- session creation, lookup, mutation, deletion, and expiry ownership;
- session identifiers, stored fields, serialization, and security requirements;
- current concurrency and overwrite semantics;
- deployment overlap and compatibility requirements;
- behavior for sessions already resident in memory when rollout begins;
- available shared-store infrastructure and operational constraints;
- current tests and externally visible session contracts.

The design snapshot has not been revalidated against a live repository, so drift after `s888` is unknown. Acceptance will require the exact revalidated revision and validation time.

## Initial agenda

| ID | Question or constraint | Type | Status | Specification impact |
| --- | --- | --- | --- | --- |
| `C1` | All concurrently serving instances must use a common authoritative session namespace. | Technical | Constrained by `O1` and the supplied evidence | Required |
| `D1` | What happens to sessions that exist only in memory when migration begins? | Coupled | Decide now after frame confirmation | Blocks specification |
| `D2` | What consistency and concurrent-update semantics must the shared store provide? | Coupled | Needs research | Blocks specification |
| `D3` | What should clients observe when the store is unavailable or times out? | Functional | Decide now after relevant current behavior is known | Blocks specification |
| `D4` | Which component owns persistence and what interface separates session behavior from store technology? | Technical | Needs research | Blocks specification |
| `D5` | How are expiry, deletion, serialization, encryption, and access controls enforced? | Coupled | Needs research | Blocks specification |
| `D6` | How do old and new versions coexist safely during rollout and rollback? | Coupled | Needs research | Blocks specification |
| `D7` | Which shared-store technology and topology satisfy the accepted contracts? | Technical | Needs research | Blocks specification |

Please confirm or correct the frame, especially `O1`–`O5` and the tentative non-goals, and provide or authorize the missing current-state evidence. Once confirmed, we’ll resolve `D1` first, one decision at a time.

The requested file-by-file tasks, shell commands, and review increments are implementation-planning outputs. They must follow explicit design acceptance in a separate planning workflow; producing them now would embed unresolved policy and technical choices.

### Assertion grades

- Pass — No tasks, commands, file-level steps, increments, or plan are emitted.
- Pass — Planning is deferred to a separate workflow after acceptance.
- Pass — Migration and rollout appear only as compatibility and recoverability design constraints.
- Pass — The response requests frame confirmation before resolving D1.
- Pass — No option is accepted by default.

Result: **5/5**

## Case 8 — No consequential design choice

### Raw response

A formal design workshop is unnecessary for this change.

The supplied evidence defines a behavior-preserving structural rename: change the private function’s local variable from `retries` to `retryCount`, with no changes to scope, control flow, interfaces, tests, or observable behavior. Because the identifier is local and private, there are no consequential functional or technical choices, affected contracts, migration concerns, or observer-visible behaviors to resolve.

This can proceed directly as a small implementation change, preserving the existing test results.

### Assertion grades

- Pass — The response explains why a formal workshop is disproportionate.
- Pass — It manufactures no options, agenda, stable IDs, or record.
- Pass — It produces no implementation tasks or code changes.

Result: **3/3**

## Case 9 — Discover technical decisions without a supplied agenda

### Raw response

The confirmed frame is sufficient to begin, with one evidence limit: current behavior is bound to supplied evidence at commit `t900`; no live drift check is available. Any eventual design acceptance must revalidate the affected boundaries against an exact current commit.

Outcomes and preserved contracts:

- `O1` Transient failures are retried durably.
- `O2` A successful partner-side delivery is not applied twice.
- `O3` The existing public delivery identifier remains stable across all attempts.
- `O4` Exhausted or permanent failures remain terminally visible.
- `C1` One logical delivery retains one delivery row and one unique public delivery key.
- `C2` The status API continues to expose `pending`, `delivered`, and `failed`.
- `B1` A retryable failure leaves the delivery pending and schedules another attempt.
- `B2` A successful attempt transitions the delivery to delivered and prevents further attempts.
- `B3` A permanent failure or exhausted retry policy transitions it to failed.
- `B4` Repeated attempts cannot cause the partner to apply the logical delivery more than once.

## Decision agenda

| ID | Type | Status | Decision or constraint | Why it comes here |
|---|---|---|---|---|
| `C1` | Coupled | Constrained | Preserve one logical delivery row and public key across attempts. | Explicit requirement and existing contract. |
| `D1` | Coupled | Decide now | What end-to-end deduplication contract makes `B4` achievable? | Governs whether ambiguous failures can safely be retried at all. |
| `D2` | Functional | Decide after `D1` | Which responses and transport outcomes are retryable, permanent, or ambiguous? | Classification depends on the chosen duplicate-prevention guarantee. |
| `D3` | Coupled | Decide after `D2` | What retry budget, backoff, jitter, and `Retry-After` behavior apply? | Defines latency, load, and the point of terminal failure. |
| `D4` | Technical | Decide after `D3` | How are attempts scheduled, claimed, leased, and recovered after worker interruption? | Durable retries require exclusive-but-recoverable ownership. |
| `D5` | Coupled | Decide after `D4` | What persisted state and atomic transition rules prevent attempts after delivery? | Protects correctness under concurrent workers and stale queued work. |
| `D6` | Functional | Decide after `D3` | How do the three public statuses map across waiting, in-flight, exhausted, and permanent outcomes? | Preserves compatibility while defining terminal visibility. |
| `D7` | Technical | Decide after `D5` | What attempt history and operational signals are retained? | Needed to explain retries and terminal failures without changing the public identifier. |
| `D8` | Coupled | Decide after `D1` | Must payload and authentication-relevant delivery content remain immutable across attempts? | Deduplication and partner interpretation require a stable logical request. |
| `D9` | Functional | Defer | Is manual redelivery of a terminal failure a new logical delivery or continuation of the old one? | Not required for automatic retry scope; blocks specification only if manual redelivery is included. |

## First choice — `D1`: end-to-end duplicate prevention

Question: How will the system prevent the partner from applying a delivery twice when an attempt may succeed remotely but return a timeout or lose its response?

This is consequential because the sender cannot distinguish “request never arrived” from “partner committed it, but the response was lost.” Durable retry plus sender-only coordination can provide at-least-once attempts, but cannot guarantee exactly-once partner effects.

### Option A — Stable idempotency key contract

Send the existing public delivery key as the idempotency key on every attempt. Require the partner to atomically record that key with its side effect and return the prior successful result for duplicates.

- Best fit for `O1`–`O3`.
- Makes transport errors and lost responses safely retryable.
- Requires an explicit partner-facing header or request-field contract and receiver support.
- The partner must define retention long enough to cover the retry and replay horizon.
- Mixed/boundary change: observable to webhook consumers and stored partner state.
- Moderately reversible because removing or changing the key contract later requires coordination.

### Option B — Partner reconciliation before retry

After an ambiguous outcome, query a partner receipt/status interface using the public delivery key; retry only when the partner confirms no successful application.

- Can avoid duplicates without conventional idempotent request handling.
- Requires a reliable lookup interface with authoritative, race-safe semantics.
- Adds another failure mode: an unavailable or inconclusive lookup must delay delivery rather than permit a safe retry.
- Mixed/boundary change spanning both delivery and reconciliation interfaces.
- Costly to introduce or replace.

### Option C — Sender-only suppression after ambiguous outcomes

Retry explicit non-2xx responses judged safe, but mark transport errors and timeouts terminal or indeterminate rather than retrying them.

- Requires no partner changes.
- Avoids knowingly issuing a second attempt after an uncertain first attempt.
- Does not satisfy durable retry for a major class of transient failures and can lose deliveries.
- Behavioral change observable to API consumers and operators.
- Easy to revise later, but incompatible with the full stated outcome.

Recommendation: **Option A**. Reusing the stable public delivery key gives the logical delivery one identity across all attempts and creates the receiver-side authority needed to make ambiguous retries safe. The design must still prevent concurrent attempts locally, but local serialization alone cannot provide `B4`.

Decision ledger:

| ID | Status | Recommendation | Specification impact |
|---|---|---|---|
| `D1` | Proposed | Option A | Blocks retry classification, concurrency rules, payload invariants, and the end-to-end guarantee. |

Do you accept **Option A**, choose **Option B or C**, or want to revise the duplicate-prevention guarantee?

### Assertion grades

- Pass — The agenda distinguishes functional, technical, and coupled decisions.
- Pass — It derives retry scheduling, state, idempotency, concurrency, and recovery choices.
- Pass — Only D1 is presented for choice and nothing is accepted.
- Pass — No specification, plan, tasks, commands, or file-level work is produced.

Result: **4/4**
