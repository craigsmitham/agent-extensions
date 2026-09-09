# agent-extensions

Public, reusable agent extensions maintained by
[@craigsmitham](https://github.com/craigsmitham) and managed with
[AXM](https://axm.sh).

This repository is the authoritative source for the packages below. Personal,
machine-specific, and private operational extensions are maintained separately
and are not published from this repository.

## Packs

| Pack | Purpose | Install |
| --- | --- | --- |
| `effect-v4` | Effect v4 guidance: a rule requiring v4 conventions plus a knowledge bundle of twenty-four concise topic checklists | `axm install @craigsmitham/packs/effect-v4` |
| `docs` | Portable documentation craft plus distinct authoring/remediation and read-only audit skills | `axm install @craigsmitham/packs/docs` |
| `field-notes` | Observe how work actually goes within declared subjects, then triage recurring obstacles into verified improvements | `axm install @craigsmitham/packs/field-notes` |
| `research` | Fresh-context, read-only research framing and evidence gathering with inspectable uncertainty | `axm install @craigsmitham/packs/research` |
| `software-engineering` | Evidence-backed codebase review and coherent repository execution-surface craft, sourced from the `product-engineering` bundle | `axm install @craigsmitham/packs/software-engineering` |
| `work-management` | Consistent Operational Incident Records, Defect Reports, and Changes across repositories and trackers, sourced from the `product-engineering` bundle | `axm install @craigsmitham/packs/work-management` |

## Standalone knowledge

| Bundle | Purpose | Install |
| --- | --- | --- |
| `knowledge-management` | Durable knowledge authority, lifecycle, discovery, provenance, and maintenance across human and executable sources | `axm install @craigsmitham/knowledge/knowledge-management` |
| `product-engineering` | An opinionated product-development lifecycle from strategy through operations and maintenance, with shared conceptual foundations | `axm install @craigsmitham/knowledge/product-engineering` |

The `strategy`, `product-management`, `requirements-engineering`,
`software-engineering`, `work-management`, and `workflow-automation` bundles
were retired into `product-engineering`. Surviving concepts live under the
section that owns the question they answer, and each carries a `pe-` section
tag, because a query can be scoped to a bundle but not to a folder. Not all of
them survived. The `workflow-automation` and `strategy` concepts have since
been dropped rather than absorbed, because they summarized public sources that
are better read at the source: "Where to play" now holds its question, its
scope, and its boundaries and nothing else, and delivery automation is once
again claimed scope that has not been written.

## Standalone skills

| Skill | Purpose | Install |
| --- | --- | --- |
| `temporal-dates` | JavaScript Temporal type selection, API usage, interoperability, and pitfalls | `axm install @craigsmitham/skills/temporal-dates` |
| `author-okf` | Author and validate Open Knowledge Format v0.2 bundles | `axm install @craigsmitham/skills/author-okf` |
| `improve-whatever` | Evidence-based evaluation through the lens of Philippians 4:8–9 | `axm install @craigsmitham/skills/improve-whatever` |
| `spot-spew` | Spot avoidable maintenance burden from custom or non-idiomatic code and weigh replacing it with adopted capabilities | `axm install @craigsmitham/skills/spot-spew` |

## Layout

Canonical packages live under:

```text
├── knowledge/
├── packs/
├── rules/
├── subagents/
└── skills/
```

Agent-specific skill directories are AXM-managed projections. Author canonical
content under the root package directories above, not through those
projections. Acquired packages live under `agent_extensions/<source-key>/`.

## Contributing and publishing

Read [AGENTS.md](./AGENTS.md) before changing or adding an extension. Public
content must be portable, rights-cleared, intentionally safe to disclose, and
free of private dependencies or real sensitive data.

Follow [How to review and publish public extensions](./docs/publishing.md) for
the complete commit and release gate. For a catalog-wide registry preflight:

```bash
axm publish --authored --owner @craigsmitham --preview --json
```

## Licensing

Package licenses are declared in each extension manifest and summarized in
[LICENSE.md](./LICENSE.md). The [licensing policy](./docs/licensing.md) defines
the prospective defaults and package-boundary rules. Third-party material and
attribution are recorded in [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).
