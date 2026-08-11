# Synthetic diagnostic-field verification case

Accepted contract `diagnostic-field-v1`, accepted by the service owner against
source export `diag-service-v7`:

- O1: internal timeout diagnostics identify the owning subsystem.
- B1: `TimeoutDiagnostic` has a required `subsystem` value from the existing
  internal enum.
- B2: all three constructors populate it.
- B3: external error text, status, telemetry labels, and retry behavior remain
  unchanged.
- C1: no user input or secret enters the field.
- RP1: typecheck and focused tests are required.

Implementation identity: patch `diag-field-p2` against export
`diag-service-v7`, observed 2026-07-09T09:15:00Z. This is a non-Git source and no
branch or commit is supplied. The comparison archive contains the complete patch
and the captured check record below.

Inspected patch artifact `diag-field-p2`:

```diff
 export interface TimeoutDiagnostic {
   readonly kind: "timeout"
   readonly elapsedMs: number
+  readonly subsystem: Subsystem
 }

+const withSubsystem = (
+  subsystem: Subsystem,
+  diagnostic: Omit<TimeoutDiagnostic, "subsystem">
+): TimeoutDiagnostic => ({ ...diagnostic, subsystem })

-export const connectTimeout = timeout("connect")
-export const scheduleTimeout = timeout("schedule")
-export const storageTimeout = timeout("storage")
+export const connectTimeout = withSubsystem("transport", timeout("connect"))
+export const scheduleTimeout = withSubsystem("scheduler", timeout("schedule"))
+export const storageTimeout = withSubsystem("storage", timeout("storage"))
```

`Subsystem` is the existing closed internal enum with values `transport`,
`scheduler`, and `storage`. The three shown constructors are the only
constructors in the base export. Their subsystem arguments are constants; no
caller or user input reaches the helper. The complete comparison contains no
change to external serialization, retry logic, telemetry construction, schema,
configuration, persistence, or network interfaces.

Captured check record `diag-field-p2/checks/run-17`, produced in the isolated
CI environment `diag-ci-node22` at 2026-07-09T09:22:31Z:

```text
pnpm typecheck                                      PASS
pnpm test timeout-diagnostic.constructors          PASS (3 cases)
pnpm test external-error.snapshot                  PASS (8 cases)
pnpm test timeout-retry.behavior                    PASS (12 cases)
pnpm test telemetry-label-set                      PASS (6 cases)
tracked or generated files changed by checks       none
```

The patch artifact was inspected for this verification fixture. The CI record
is attributable to the patch identity but is a captured result, not an
independently rerun observation.

The plan proposed direct constructor edits in `timeout.ts`; the patch instead
adds `diagnostic-context.ts` for the helper. Repository evidence imposes no file
placement rule for internal helpers.
