---
name: effect-v4-schema-boundaries
description: Designs Effect v4 Schema boundaries between unknown, encoded, and domain values. Use when JSON or external input is cast, validation is duplicated or ad hoc, wire and domain representations differ, constructors bypass invariants, or output is encoded manually—even without current Schema usage. Skip data already trusted and kept inside a validated boundary.
---

# Effect v4 Schema boundaries

Decode once at ingress, use trusted domain values internally, and encode at egress.

## Establish the boundary

- Treat network, storage, environment, form, and parsed JSON values as `unknown`.
- Use an unknown decoder at the first trusted boundary; never cast external data into the domain type.
- Use a schema's `make` or `makeEffect` for already-typed construction when type-side validation is still required, not as a substitute for decoding unknown input.
- Use Effectful decoding when transformations or validation require services or asynchronous work.

## Own representation changes

- Let a schema transformation define the relationship between encoded and domain representations.
- Keep wire compatibility decisions at adapters; do not leak encoded shapes through the domain.
- Encode through the same schema used to define the boundary.
- Choose strictness deliberately for extra fields, coercion, defaults, and optionality.

## Keep one source of truth

- Reuse schema-derived types and constructors instead of parallel interfaces, predicates, and validators.
- Preserve structured schema issues long enough to produce useful path-aware diagnostics.
- Map parse failures to domain or protocol errors only where that vocabulary belongs.
- Test round trips and representative invalid inputs, especially at transformations.

Do not validate repeatedly after a value has crossed a trustworthy boundary.
