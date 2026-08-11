# Synthetic invoice-delivery drift case

The delivery contract was accepted and planned at repository revision `i100`.
The readiness assessment observes revision `i124` on
2026-08-05T13:00:00Z.

## Accepted contract

- O1: an authorized operator can request delivery of a finalized invoice.
- B1: one request schedules one idempotent delivery and returns its identifier.
- B2: repeated requests return the existing delivery.
- C1: the existing invoice-view authorization policy governs the request.

## Plan at i100

P1 changes `src/invoices/delivery-service.ts:schedule`, publishes to the
`invoice-delivery` queue, and adds service, authorization, and idempotency tests.

## Reported current drift at i124

- `delivery-service.ts:schedule` no longer exists.
- Commit evidence states invoice delivery ownership moved to a dispatch module.
- The `invoice-delivery` queue was replaced, but the available evidence does not
  establish the replacement queue's delivery, deduplication, or transaction
  semantics.
- The invoice-view authorization policy and its tests are unchanged and verified
  at `i124`.

No current dispatch owner, symbol, or queue contract is supplied.
