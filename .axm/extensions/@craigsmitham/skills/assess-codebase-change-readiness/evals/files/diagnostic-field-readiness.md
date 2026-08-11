# Synthetic diagnostic-field change case

Assessment snapshot: source export `diag-service-v7`, captured
2026-07-02T10:30:00Z. This is not a Git checkout.

## Accepted contract and risk

The service owner accepted:

- O1: internal timeout diagnostics identify the owning subsystem.
- B1: `TimeoutDiagnostic` includes a required `subsystem` field populated from
  the existing internal enum.
- B2: external error text, status, telemetry cardinality, and retry behavior do
  not change.
- C1: the field remains inside the process and contains no user input or secret.

Impact is limited to internal test and debug output. There is no schema,
network, authorization, persistence, configuration, migration, rollout, or
runtime topology change.

## Current evidence and work

- Export v7 shows `src/diagnostics/timeout.ts:TimeoutDiagnostic` and all three
  constructors.
- P1 updates the type and three constructors, then updates focused unit tests.
- Completion evidence: typecheck; focused constructor tests; external-error
  snapshot test; telemetry label-set test; existing retry-decision test rerun
  against all three timeout constructors.
- Repository instructions require typecheck and focused tests for this area; no
  separate change approval or deployment document is required.
