# Synthetic webhook-replay change case

Assessment snapshot: repository revision `r84`, observed 2026-07-01T15:00:00Z.
No relevant drift is reported from accepted design snapshot `r84`.

## Accepted contract

Accepted by the product and service owners at `r84`:

- O1: an operator can safely replay a failed webhook delivery.
- B1: an eligible failed delivery creates one replay and returns its replay ID.
- B2: repeated requests with the same idempotency key return the existing replay.
- B3: replay must never create a concurrent attempt while the original delivery
  is in flight.
- C1: `POST /deliveries/{id}/replays` accepts an idempotency key.
- C2: terminal failed deliveries are eligible; successful deliveries are not.
- S1: endpoint, service, persistence, authorization, and contract tests compose
  as one operator-visible slice.

The contract does not define the response, state transition, or retry semantics
when the original delivery is in flight.

## Current-state evidence

- `src/deliveries/replay.ts:createReplay` owns replay creation.
- `src/deliveries/model.ts:DeliveryState` includes `sending`, `failed`, and
  `delivered`.
- Existing authorization and idempotency tests are named and executable at r84.

## Implementation plan

- P1 covers O1/B1-B3/C1-C2/S1 at the verified anchors.
- P1 states: “Use the simplest missing policy: return 409 for `sending`; add a
  contract test.” No accepted source is cited for this behavior.
- Completion evidence includes unit, contract, authorization, and concurrency
  tests. No migration or deployment topology change is involved.
