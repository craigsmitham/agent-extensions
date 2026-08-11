# Synthetic implementation evidence at `w120`

Implementation occurred outside the workflow pack. Snapshot `w120` is a clean
repository revision based on planning snapshot `w110`; the comparison contains
only the planned webhook attempt storage, worker policy, scheduling,
observability, documentation, and tests.

The worker's response classifier at `w120` is:

```ts
if (status === 408 || status >= 500) return "retryable"
if (status >= 400) return "terminal"
return "delivered"
```

Transport failures use a separate accepted retryable branch. Because the second
condition includes 429, the worker records it as terminal and does not schedule
another attempt.

Recorded checks at `w120` all pass: typecheck; worker unit tests for 408, 500,
503, 400, and 404; attempt-uniqueness integration tests; delivery-state contract
tests; retry-exhaustion tests; rollback-readability tests; and documentation
validation. No test or runtime observation exercises HTTP 429.

All other accepted retry, idempotency, state, metrics, rollback, and preserved
identifier obligations have attributable implementation and passing evidence at
`w120`. No unplanned surfaces are reported.
