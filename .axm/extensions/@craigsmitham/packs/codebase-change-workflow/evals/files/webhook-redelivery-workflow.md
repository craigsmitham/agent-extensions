# Synthetic webhook redelivery workflow

All names, revisions, and behavior in this fixture are synthetic.

## Source request

At 2026-08-01T10:00:00Z on deployment `w090`, a partner observed that transient
HTTP 503 responses permanently failed webhook deliveries. The report was filed
at 2026-08-02T09:00:00Z. Desired outcome: retry transient failures without
duplicating successful deliveries, while preserving the current public delivery
identifier and terminal failure visibility. A proposed worker retry loop is an
unverified implementation preference.

## Repository evidence at `w100`

- `src/webhooks/accept.ts::acceptWebhook` validates the request, creates one
  delivery row with a stable delivery key, and enqueues its row ID.
- `src/webhooks/worker.ts::deliverWebhook` loads the row and calls the partner.
  A 2xx response sets `delivered`; every other response or transport error sets
  `failed`. No retry is scheduled.
- `src/webhooks/delivery-store.ts` enforces uniqueness on the delivery key but
  has no attempt records or retry transition.
- `src/webhooks/status-api.ts` exposes `pending`, `delivered`, and `failed`.
- Worker tests cover one successful attempt and one terminal failure. Integration
  tests verify that duplicate accepts return the existing delivery identifier.
- Metrics count terminal outcomes but not attempts or retry exhaustion.
- Between `w090` and `w100`, the only relevant change renamed the queue; behavior
  and persistence contracts did not change. This is sufficient to relate the
  report to current behavior but not to reproduce the partner's environment.

## Accepted decision options for the workshop

The evaluator supplies these choices only after the workshop presents the
corresponding decision:

- The worker owns retry policy and scheduling.
- A delivery permits three total attempts at 0, 30, and 120 seconds.
- Attempt uniqueness is `(delivery_key, attempt_number)`; a delivered row never
  transitions again.
- Consumers observe `retrying` after a retryable failure and `failed` only after
  exhaustion or a non-retryable response.
- Retryable outcomes are transport errors, HTTP 408, 429, and 5xx. Other 4xx
  responses are terminal.
- Metrics count attempts, scheduled retries, exhaustion, and suppressed duplicate
  attempts. Rollback disables new scheduling but preserves readable attempt rows.

## Planning evidence at `w110`

Only `docs/webhooks.md` changed after `w100`; implementation anchors, tests,
configuration, dependencies, deployment behavior, and runtime contracts are
unchanged. Proposed attempt storage belongs beside `delivery-store.ts` by the
repository's existing persistence convention.
