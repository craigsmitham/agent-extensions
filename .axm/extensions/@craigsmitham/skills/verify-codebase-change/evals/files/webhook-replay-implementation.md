# Synthetic webhook-replay verification case

Accepted contract `replay-contract-v2`, accepted by product and service owners
at repository revision `r84`:

- O1: an operator can safely replay a failed webhook delivery.
- B1: an eligible failed delivery creates one replay and returns its replay ID.
- B2: duplicate idempotency keys return the existing replay.
- B3: replay must never create a concurrent attempt while the original delivery
  is in flight.
- C1: successful and unknown deliveries are ineligible.
- RP1: endpoint changes require authorization and contract tests.

Implementation snapshot: patch `replay-patch-6` applied to revision `r84`,
observed 2026-07-08T16:00:00Z. The patch comparison contains only the listed
endpoint, service, persistence, and test changes.

Relevant implementation:

```ts
if (delivery.state === "delivered") return ineligible()
return replayStore.createOrFind(delivery.id, idempotencyKey)
```

The state enum includes `sending`, `failed`, and `delivered`. Therefore the
implementation calls `createOrFind` for both `sending` and `failed`.

Reported checks all pass: typecheck, authorization tests, duplicate-key tests,
failed-delivery contract test, delivered-delivery contract test, and unknown-ID
contract test. No test or runtime observation exercises `sending`.

The implementation plan proposed an internal `replay_attempt_total` metric, but
the accepted contract and repository obligations do not require it. The patch
does not add that metric. No deployment or migration change is in scope.
