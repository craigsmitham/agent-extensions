# Product Docs

Grow and maintain a product's documentation, chiefly its system's
specification: what the system does, whom and what it serves, and why. The
skill keeps that account in one place that people and agents can find, trust,
and change as the system changes, so that every requirement stays connected to
whom it serves.

The documentation lives in `product/` at the repository root, as an OKF v0.2
bundle that follows the [Product docs profile](src/references/profile.md).
`product/business/` holds the direction and intent the product serves, and
`product/spec/` specifies its system. How the system works, such as
architecture, implementation, and operations, stays in your design and
operations records; the specification links to them.

## Use it when

- Starting a specification for a new or existing system.
- Adding or changing what the system does, such as features, use cases,
  requirements, business rules, required levels of quality, or the data it
  keeps.
- Recording whom the system serves: its users, the jobs it helps with, the
  opportunity and objectives behind it, where it focuses now, and the
  mission, vision, and principles it follows.
- Checking whether a change, including design, dependency, or operations work,
  affects what the specification binds.
- Reviewing specification documents against the profile's rules.

Not for architecture or design documents, task planning, or release
roadmaps.

## Examples

```text
$product-docs create a spec for this repository
$product-docs add a requirement that reservations of unavailable equipment are rejected
$product-docs does moving search to a new index affect anything the spec requires?
$product-docs review product/spec/features/equipment-search/
```

## What to expect

- Only `product/spec/system.md` is required. The skill adds other documents when
  there is content for them.
- It does not invent objectives, measures, or decisions. What is unknown is
  recorded under **Open questions** for you to settle.
- When the system's behavior and the specification disagree, it asks which
  is right rather than changing either.

## License

MIT.
