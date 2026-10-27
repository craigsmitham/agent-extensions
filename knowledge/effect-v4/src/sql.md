---
type: Checklist
title: SQL
description: Evaluate whether database access has explicit client, schema, statement, transaction, retry, telemetry, and testing boundaries.
tags: [effect, effect-v4, sql, transaction, schema, repository, database]
status: stable
sources:
  - id: effect-sql
    resource: https://github.com/Effect-TS/effect/blob/effect%404.0.6/ai-docs/src/40_sql/10_basics.ts
    title: Effect 4.0.6 SQL basics
  - id: effect-sql-client
    resource: https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/effect/src/sql/SqlClient.ts
    title: Effect 4.0.6 SqlClient source
  - id: effect-sql-error
    resource: https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/effect/src/sql/SqlError.ts
    title: Effect 4.0.6 SqlError source
  - id: effect-pg-client
    resource: https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/sql/pg/src/PgClient.ts
    title: Effect 4.0.6 native PostgreSQL client
  - id: effect-pg-types
    resource: https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/sql/pg/src/PgTypes.ts
    title: Effect 4.0.6 PostgreSQL binary codecs
  - id: effect-sqlite-do-client
    resource: https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/sql/sqlite-do/src/SqliteClient.ts
    title: Effect 4.0.6 Durable Object SQLite client
  - id: effect-sql-tests
    resource: https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/effect/test/sql/SqlClient.test.ts
    title: Effect 4.0.6 post-commit regression tests
generated: { by: codex/gpt-6, at: 2026-10-27T18:45:50Z }
---

# SQL

- [ ] Provide the dialect-specific client layer at the infrastructure edge and
  configure prepared statements for the deployed pooler; expose database
  behavior through repositories or domain services.[^effect-pg-client]
- [ ] Use parameterized statement construction; never concatenate untrusted
  values into SQL text.
- [ ] Decode selected rows and encode statement inputs with schemas matching
  the driver's actual scalar and JSON representations.[^effect-pg-types]
- [ ] Keep `SqlError` and its reason available until the owning repository,
  service, handler, or scheduler can translate or recover correctly.
- [ ] Enclose every statement that must commit or roll back together in one
  transaction owned by the operation with that atomicity requirement.
- [ ] Confirm the dialect client supports the transaction shape relied on:
  nesting and savepoint release, concurrent sibling transactions, and
  asynchronous work inside the transaction.[^effect-sqlite-do-client]
- [ ] Retry only known retryable reasons such as serialization or deadlock
  failures, around the complete repeat-safe transaction, with a bound.
- [ ] Keep credentials and sensitive parameters out of telemetry; control
  whether raw query text is recorded in spans or diagnostics.
- [ ] Defer commit-dependent notifications with `SqlClient.afterCommit` only
  where the dialect supports it; `sqlite-do` runs callbacks immediately.
  Persist delivery-critical work in the transaction because callbacks can be
  lost on process exit or an unknown commit outcome.[^effect-sql-client]
- [ ] Run integration tests against the supported dialect for constraints,
  transactions, concurrency, schema decoding, retries, and post-commit behavior
  under nested rollback and commit failure.[^effect-sql-tests]

## Resources

- [SQL basics](https://github.com/Effect-TS/effect/blob/effect%404.0.6/ai-docs/src/40_sql/10_basics.ts)
- [SqlClient source](https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/effect/src/sql/SqlClient.ts)
- [SqlError source](https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/effect/src/sql/SqlError.ts)
- [Native PostgreSQL client and pool configuration](https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/sql/pg/src/PgClient.ts)
- [Durable Object SQLite transactions](https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/sql/sqlite-do/src/SqliteClient.ts)
- [PostgreSQL parameter and result codecs](https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/sql/pg/src/PgTypes.ts)

[^effect-pg-types]: Effect PostgreSQL binary codecs.
[^effect-pg-client]: Effect native PostgreSQL client.
[^effect-sqlite-do-client]: Effect Durable Object SQLite client.
[^effect-sql-client]: Effect SqlClient post-commit callback contract and limitations.

[^effect-sql-tests]: [Effect post-commit regression tests](https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/effect/test/sql/SqlClient.test.ts).
