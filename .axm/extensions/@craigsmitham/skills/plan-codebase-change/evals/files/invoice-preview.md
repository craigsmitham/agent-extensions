# Accepted specification and planning snapshot: invoice preview

Specification status: Accepted by the synthetic product and architecture owners
at revision `i100` on 2026-08-09T15:00:00Z. Planning snapshot `i100` is identical.

## Accepted identifiers

- O1: An authorized billing clerk can preview a draft invoice without persisting
  or sending it.
- B1: A valid draft returns line items, tax, and total in the existing money JSON
  representation.
- B2: Missing, non-draft, and unauthorized invoices all return the already
  established not-found response; no invoice facts are disclosed.
- B3: A tax-calculation failure returns the existing calculation-unavailable
  response and records the existing safe error metric.
- D1: Add the endpoint to the invoice HTTP boundary.
- D2: Put preview orchestration in the invoice application service.
- D3: Reuse `TaxCalculator`; do not duplicate tax rules.
- D4: Keep rendering pure and independent of persistence and delivery.
- C1: `POST /invoices/:id/preview` is authorized before invoice state is exposed.
- C2: Preview performs no writes and emits no delivery event.
- C3: `InvoiceService.preview` owns lookup, draft-state validation, calculation,
  and rendering orchestration.
- C4: `TaxCalculator.calculateDraft` remains the authoritative tax interface.
- C5: `InvoicePreviewJson` uses the existing `MoneyJson` encoding.
- C6: Failure telemetry contains error category and request correlation only.
- S1: Application-service preview succeeds and fails through existing test doubles.
- S2: The HTTP endpoint exposes B1-B3 through the existing auth and error mapping.
- S3: The composed endpoint passes API-contract and non-persistence verification.

## Verified repository evidence

- `src/invoices/http.ts` owns invoice routes through `registerInvoiceRoutes`.
- `src/invoices/service.ts` owns `InvoiceService`; `preview` is proposed there.
- `src/tax/calculator.ts` exports `TaxCalculator.calculateDraft`.
- `src/http/money-json.ts` exports `MoneyJson`.
- `test/invoices/service.test.ts` and `test/invoices/http.test.ts` are existing
  behavior surfaces; `test/contracts/invoices.test.ts` owns invoice API contracts.
- New response type files conventionally live beside their owning HTTP module, so
  `src/invoices/preview-json.ts` is a proposed addition grounded in that convention.
- RP1 (`CONTRIBUTING.md`): changed HTTP behavior must update `docs/api/invoices.md`,
  pass `npm run check`, and pass the owning unit and contract test suites.

No relevant configuration, dependency, deployment, or runtime drift exists.
