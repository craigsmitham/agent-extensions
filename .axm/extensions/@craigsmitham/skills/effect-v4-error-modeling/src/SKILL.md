---
name: effect-v4-error-modeling
description: Models Effect v4 failures and recovery boundaries. Use when code throws, catches `unknown`, collapses failures into strings, recovers broadly, retries indiscriminately, or mixes expected failures with defects or interruption—even without an existing Effect error channel. Skip impossible internal states that should remain defects and straightforward propagation of errors already normalized at a sound boundary.
---

# Effect v4 error modeling

Keep expected failure, defects, and interruption semantically distinct.

## Classify first

- Put anticipated, actionable failures in the typed error channel.
- Use small tagged errors with the context a caller needs to decide, recover, report, or retry.
- Treat violated invariants and programmer mistakes as defects.
- Treat interruption as lifecycle control flow, not a business error.

Do not expose raw `unknown`, third-party exceptions, or transport errors beyond their ownership boundary. Translate them once while preserving useful cause or metadata.

## Recover deliberately

- Recover by tag at the layer that owns the fallback decision.
- Catch a full `Cause` only when the code truly handles failures, defects, and interruption.
- Preserve unhandled cases; do not turn every failure into a default value.
- Retry only failures known to be transient, with an explicit schedule and termination policy.
- Convert to defects with `orDie` only when failure is genuinely impossible after composition.

## Design the public channel

- Prefer domain meaning over implementation detail: `CustomerNotFound` is more useful than a database driver's exception.
- Keep variants discriminable and payloads stable.
- Map errors at subsystem boundaries rather than repeatedly throughout business logic.
- Test typed failure, defect, and interruption paths separately when each matters.

Avoid a single catch-all application error that removes the distinctions Effect can enforce.
