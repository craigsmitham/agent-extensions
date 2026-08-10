# Synthetic invoice repository

At `e555`, `billing/invoice-number.ts::allocate` obtains the next tenant-scoped
sequence value in the invoice transaction. The uniqueness constraint is
`(tenant_id, invoice_number)`. Unit, concurrency, and rollback tests cover the
flow. The diff from `d444` to `e555` changes only `docs-site/` and
`tools/image-optimizer/`; definitions, callers, schema, configuration,
dependencies, deployment, and invoice tests are unchanged.
