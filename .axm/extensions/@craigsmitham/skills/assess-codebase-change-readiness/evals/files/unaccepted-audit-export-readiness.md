# Synthetic audit-export change case

Assessment snapshot: repository revision `a210`, observed
2026-08-01T09:00:00Z. No relevant drift is reported.

## Draft contract

The change contract is complete but has status `Draft`. Repository governance
names the product owner as the required acceptance authority, and the product
owner has not accepted or rejected it.

- O1: compliance operators can export one audit case as CSV.
- B1: an authorized operator receives exactly the events in the selected case.
- B2: unauthorized callers receive the existing forbidden response.
- C1: export generation does not persist another copy of event data.

## Current evidence and plan

- The endpoint, authorization policy, query owner, and CSV encoder are verified
  at `a210`.
- P1 traces O1/B1/B2/C1 through the endpoint, query, encoder, and focused tests.
- Verification methods include authorization tests, CSV contract tests, and a
  persistence-write assertion.
- No product, technical, or planning gap is otherwise reported.
