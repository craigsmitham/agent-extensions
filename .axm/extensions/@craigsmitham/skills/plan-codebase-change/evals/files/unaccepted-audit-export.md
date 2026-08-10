# Draft specification: audit export

Specification status: Draft. It has not been accepted by any product or
architecture owner. Snapshot `a900` was captured on 2026-08-10T10:00:00Z and the
listed anchors are verified.

- O1: An auditor can export the current audit search as CSV.
- B1: An authorized request returns the filtered records in current sort order.
- B2: An empty result returns a header-only CSV.
- C1: `AuditSearchService` remains the source of filtering and ordering.
- C2: `AuditCsvEncoder` escapes spreadsheet-formula prefixes.
- C3: Export authorization matches audit-search authorization.
- S1: Compose search, encoding, authorization, and endpoint verification.

Verified anchors are `src/audit/search.ts`, `src/audit/http.ts`,
`src/audit/csv.ts`, and their owning tests. No drift is known. Completeness of
the draft does not constitute acceptance.
