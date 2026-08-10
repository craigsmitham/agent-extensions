# Accepted-label specification and snapshot: webhook redelivery

Specification status: Accepted at revision `w410` on 2026-08-09T16:00:00Z.
Planning snapshot: `w410`; all listed paths and symbols are verified.

- O1: Operators can request redelivery of a failed webhook event.
- B1: An authorized request for a failed event enqueues one redelivery and returns
  the accepted operation identifier.
- B2: Duplicate requests after a redelivery has completed return the existing
  operation identifier without another delivery.
- D1: The existing operations endpoint owns the request.
- D2: The existing delivery queue owns execution.
- C1: `POST /operations/webhooks/:id/redeliver` owns authorization and lookup.
- C2: `WebhookRedeliveryQueue.enqueue` accepts the event and operation IDs.
- C3: Retry schedule is 1, 5, and 15 minutes after a failed attempt.
- S1: Endpoint-to-queue redelivery for a failed, idle event.
- S2: Worker retry and completed-operation idempotency.

Verified anchors are `src/operations/webhooks.ts`,
`src/webhooks/redelivery-queue.ts`, `src/webhooks/redelivery-worker.ts`, and their
same-directory tests.

Material gap: the specification never decides what an operator observes or what
state changes when the event is already in flight. Plausible outcomes include
joining the active operation, rejecting the request, or scheduling another
operation. The outcome affects API semantics, persisted operation state, and
delivery duplication risk. No accepted exclusion removes this case from O1.
