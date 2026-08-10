# Accepted specification against a non-Git source export

Specification status: Accepted on 2026-08-09T20:00:00Z for the scope below.
Planning evidence is `partner-service-export-v12`, version 12, captured
2026-08-10T09:30:00Z. The export is authoritative for this plan and contains no
Git branch, commit, or worktree metadata.

- O1: An authenticated partner can read its own current integration status.
- B1: A configured partner receives `200` with `active`, `paused`, or `error`.
- B2: An authenticated partner without a configuration receives `404`.
- B3: A partner cannot distinguish another partner's configuration from absence.
- B4: Repository unavailability returns the existing `503 service_unavailable`
  response without configuration or partner details.
- D1: Add the endpoint to the existing partner HTTP boundary.
- D2: Reuse the existing partner identity and repository capabilities.
- C1: `GET /partner/status` derives partner identity from `PartnerPrincipal` only.
- C2: `PartnerRepository.findStatus(partnerId)` is the authoritative lookup.
- C3: Responses use the existing `PartnerStatusJson` encoder.
- C4: Endpoint telemetry uses `partner_status_request_total` with exactly
  `success`, `not_found`, and `repository_error`; it records no partner identifier.
- S1: Repository-backed status behavior through existing service tests.
- S2: Authenticated HTTP behavior and privacy-preserving not-found mapping.

Verified export evidence:

- `app/partner/http.ts#registerPartnerRoutes(router, service, metrics)` owns all
  partner routes. Existing routes call `requirePartnerPrincipal` before service
  invocation, map `PartnerNotFound` to the shared `notFoundJson`, map
  `RepositoryUnavailable` to `serviceUnavailableJson`, and increment one
  route-owned outcome counter. The new route and counter follow this verified
  ownership convention.
- `app/partner/service.ts#PartnerService` is constructed with
  `PartnerRepository`. Its existing query methods pass only the principal's
  `partnerId` to the repository and propagate the two tagged failures unchanged;
  `getStatus(principal)` is proposed with the same boundary.
- `app/partner/repository.ts#PartnerRepository.findStatus(partnerId)` already
  returns `PartnerStatus | PartnerNotFound | RepositoryUnavailable`; no repository
  interface change is required.
- `app/partner/status-json.ts#PartnerStatusJson.encode` already encodes only the
  accepted `active`, `paused`, and `error` values.
- `test/partner/service.spec.ts` owns service query tests and fixtures;
  `test/partner/http.spec.ts` owns authenticated route, shared-error-mapping, and
  counter assertions. Both expose the required existing doubles.
- Existing public endpoint security contracts use one file per route under
  `test/security/contracts/`; `test/security/contracts/partner-status.spec.ts` is
  a proposed addition grounded in that verified convention.
- `docs/public-api.md` has a Partner section, and `package.json` defines
  `pnpm test` as the complete unit, HTTP, and security-contract suite.

RP1 (`delivery-policy-v3`, included in the export): every public endpoint change
must update `docs/public-api.md`, pass `pnpm test`, and add or update the owning
security-contract test under `test/security/contracts/`. These are repository
delivery obligations, not new product behavior.
