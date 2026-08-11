# Synthetic notification-retry contradiction

Assessment snapshot: repository revision `n31`, observed
2026-08-04T11:00:00Z. No relevant drift is reported.

The product and service owners accepted both of these sources for the same
notification type and release at `n31`; neither source declares precedence:

- Contract A, C4: a failed notification receives at most three total delivery
  attempts, after which it becomes terminal.
- Contract B, B7: a failed notification retries with backoff without an attempt
  limit until its 24-hour expiry.

Both sources agree that duplicate sends are forbidden, authorization is
unchanged, expiry is 24 hours, and operators can inspect attempt history.

Current worker, scheduler, persistence, and test anchors are verified. The plan
implements the three-attempt limit and cites only Contract A. Apart from that
choice, it preserves the 24-hour expiry, duplicate-send prohibition,
authorization, and attempt history with traced worker, scheduler, persistence,
contract, authorization, idempotency, expiry, and operator-history tests. Each
test has an executable command and observable assertion at `n31`.

No authority has reconciled the incompatible accepted retry-limit rules.
