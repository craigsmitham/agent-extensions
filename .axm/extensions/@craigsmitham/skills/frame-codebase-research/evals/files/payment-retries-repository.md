# Synthetic repository description: Payments Service

This fixture is entirely synthetic. Treat it as the available repository for the
evaluation prompt.

- Repository: `example/payments-service`
- Branch: `main`
- Commit: `d00df26`
- Worktree: clean
- Current release tag: `2.6`
- Reported affected release tag: `2.4`

High-level structure discovered without tracing implementation:

- `src/payments/retry-worker.ts` exposes the retry worker entry point.
- `src/payments/charge-provider.ts` defines the external charge boundary.
- `src/payments/attempt-store.ts` owns persisted payment-attempt state.
- `config/retry-policy.yaml` configures retry timing.
- `tests/payments/retry-worker.test.ts` names retry behavior.

The fixture establishes only anchors. It does not state which files changed,
whether the symptom reproduces, or what caused or fixed it.
