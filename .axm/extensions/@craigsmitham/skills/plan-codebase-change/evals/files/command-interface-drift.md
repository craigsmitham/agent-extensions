# Accepted specification with planning-time drift

Specification snapshot: `s200`, accepted on 2026-08-08T12:00:00Z.
Planning snapshot: `p230`, observed on 2026-08-10T12:00:00Z.

Accepted identifiers:

- O1: Administrators can archive one expired workspace from the CLI.
- B1: A valid archive command marks the workspace archived and prints its ID.
- B2: Invalid workspace IDs are rejected before any persistence call.
- D1: Extend the `workspace archive` command owned by the legacy command registry.
- D2: Keep ID validation in the command adapter before invoking the service.
- C1: `WorkspaceArchiveService.archive` owns the state transition and remains
  present with unchanged semantics at `p230`.
- C2: `src/cli/commands.ts#registerWorkspaceCommands` owns parsing and dispatch.
- C3: `src/cli/commands.ts#parseWorkspaceId` owns validation.
- S1: Extend the command registry and its adapter tests.
- S2: Compose the adapter with `WorkspaceArchiveService` in the CLI integration test.
- S3: Verify the unchanged service transition independently.

Verified drift from `s200` to `p230`:

- `src/cli/commands.ts` and both named symbols were removed.
- Commands now use generated descriptors under `src/commands/descriptors/`.
- Workspace-ID validation moved into a shared runtime decoder after dispatch.
- The accepted design never considered generated descriptors or post-dispatch
  validation, so rebinding C2/C3 would choose new ownership and failure timing.
- `WorkspaceArchiveService.archive` and its tests did not change; C1/S3 remain
  current and independently verifiable.
