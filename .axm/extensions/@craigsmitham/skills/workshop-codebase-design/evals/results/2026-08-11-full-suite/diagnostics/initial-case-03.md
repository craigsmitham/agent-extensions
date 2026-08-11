# Case 3 — Snapshot changes before acceptance

- Runtime: Codex collaboration subagent
- Model: Inherited session model; exact public identifier unavailable
- Tested `src/` SHA-256: `9635ad7ea8154f3ffdd4b3134217c1da152988deef7c04aef4bc78a2b66db3dd`
- Reference availability: Available; not needed by the response
- State changed: None

## Prompt

> Continue this design workshop. Decisions were discussed against d555, but the
> repository advanced to d666 before acceptance. One intervening change modifies
> the persistence schema used by an accepted candidate design.

## Raw response

The design cannot be accepted against `d666` yet. The persistence-schema change is material drift: it affects stored data, compatibility, migration, and potentially rollback behavior.

## Workshop frame

- Evidence snapshot used for discussion: `d555`
- Current design snapshot: `d666`
- Relevant drift: an intervening change modified the persistence schema required by the selected candidate
- Classification: mixed/boundary change, observable to data consumers, older versions, and operators
- Evidence limit: the `d666` schema contract, invariants, and migration behavior have not been supplied
- Unrelated accepted decisions remain accepted; only this decision and anything depending on it are reopened

## Decision-ledger update

### D1 — Retain the selected persistence design under `d666`?

- Status: `Needs research`
- Type: Coupled
- Previous basis: evidence at `d555`
- Affected boundaries: persisted representation, readers and writers, existing stored data, version compatibility, migration, rollback, and recovery
- Specification impact: **Blocks specification** of the persistence-dependent scope
- Reason: its constraining evidence changed before design acceptance, so the earlier selection cannot safely be carried forward or marked `Superseded` without revalidation

The precise current-state question is:

> At `d666`, what persistence schema, invariants, read/write ownership, migration requirements, and mixed-version or rollback guarantees apply, and does the previously selected candidate satisfy them for both existing and newly written data?

Please confirm or correct this frame and provide scoped `d666` evidence answering that question—such as the schema change, its compatibility or migration contract, and relevant verification evidence. Once supplied, we can reassess D1, present viable alternatives if the candidate no longer fits, and request an explicit choice. Until then, the record remains `Discussing`, with design acceptance and specification readiness blocked by D1.

## Grade

- Pass — The response requires scoped revalidation against `d666` before acceptance.
- Pass — Persistence-dependent decisions are reopened while unrelated decisions remain intact.
- Pass — The record remains `Discussing` rather than `Accepted`.
- Pass — Later acceptance necessarily depends on the revalidated `d666` evidence identity.

Result: **4/4**
