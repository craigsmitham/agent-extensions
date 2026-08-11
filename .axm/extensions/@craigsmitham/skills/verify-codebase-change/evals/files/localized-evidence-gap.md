# Synthetic localized-evidence verification case

Accepted contract `indexed-events-v1`, accepted by the data-service owner at
revision `events-r40`:

- B1: event lookup returns the same records and ordering.
- C1: the new index is created concurrently and is used by the lookup query.
- C2: the migration must hold no write lock longer than 200 milliseconds on a
  production-like dataset.
- RP1: typecheck, query-result equivalence tests, and migration checks are
  required.

Implementation identity: patch `events-index-p3` against `events-r40`, observed
2026-07-11T18:30:00Z. Inspection of the complete patch shows a concurrent index
migration and the intended query plan. Typecheck, query-result equivalence, and
isolated migration tests pass at that patch identity.

No production-like migration run or lock-duration measurement was captured.
The available isolated test uses 100 rows and cannot establish C2. Code,
comparison boundary, and all other cited evidence remain accessible, so the
missing measurement affects C2 rather than the defensibility of the assessment
as a whole.
