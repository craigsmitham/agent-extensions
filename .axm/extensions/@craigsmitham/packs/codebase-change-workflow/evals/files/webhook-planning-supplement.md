# Withheld planning evidence at `w110`

Reveal this synthetic evidence only after the first planning attempt states the
precise response-class reachability question.

`src/webhooks/partner-client.ts` follows redirects up to its configured limit.
Informational 1xx responses are handled inside the HTTP client and are never
returned to `deliverWebhook`. If the redirect limit is exhausted, the client
returns `TransportFailure(kind=redirect_limit)`, which reaches the worker through
the already accepted transport-error branch. Therefore every outcome observable
at the worker boundary is covered by C13; this evidence changes no accepted
classification or behavior.
