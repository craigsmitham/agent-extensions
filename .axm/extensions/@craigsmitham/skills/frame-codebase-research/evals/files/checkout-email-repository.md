# Synthetic repository description: Commerce App

This fixture is entirely synthetic. Treat it as the available repository for the
evaluation prompt.

- Repository: `example/commerce-app`
- Branch: `main`
- Commit: `c0ffee1`
- Worktree: clean
- Relevant deployment: `commerce-eu` release `2026.08.1`

High-level structure discovered without tracing implementation:

- `services/checkout/complete-order.ts` exposes `completeOrder`.
- `services/notifications/order-confirmation.ts` exposes
  `requestOrderConfirmation`.
- `workers/email-dispatch.ts` contains the confirmation-email worker entry point.
- `config/regions/eu.yaml` contains EU-specific checkout and notification values.
- `tests/checkout/order-confirmation.test.ts` names the checkout-to-confirmation
  behavior.

No runtime logs, affected order identifiers, provider records, or implementation
trace are included.
