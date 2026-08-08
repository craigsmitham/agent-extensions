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
| `effect-v4` | Effect v4 patterns for types, services, failures, resources, schemas, concurrency, streams, testing, and observability | `axm install @craigsmitham/packs/effect-v4` |
| `docs` | Diátaxis-oriented documentation knowledge plus authoring and review skills | `axm install @craigsmitham/packs/docs` |

## Standalone skills

| Skill | Purpose | Install |
| --- | --- | --- |
| `temporal-dates` | JavaScript Temporal type selection, API usage, interoperability, and pitfalls | `axm install @craigsmitham/skills/temporal-dates` |
| `okf-author` | Author and validate Open Knowledge Format v0.2 bundles | `axm install @craigsmitham/skills/okf-author` |
| `eval-whatever` | Evidence-based evaluation through the lens of Philippians 4:8–9 | `axm install @craigsmitham/skills/eval-whatever` |

## Layout

Canonical packages live under:

```text
.axm/extensions/@craigsmitham/
├── knowledge/
├── packs/
└── skills/
```

Agent-specific skill directories are AXM-managed projections. Author canonical
content under `.axm/extensions`, not through those projections.

## Contributing and publishing

Read [AGENTS.md](./AGENTS.md) before changing or adding an extension. Public
content must be portable, rights-cleared, intentionally safe to disclose, and
free of private dependencies or real sensitive data.

Run the local gate before committing:

```bash
scripts/check-public-safety.sh
```

Preflight registry publication before uploading anything:

```bash
axm publish --authored --owner @craigsmitham --preview --json
```

## Licensing

Package licenses are declared in each extension manifest and summarized in
[LICENSE.md](./LICENSE.md). Third-party material and attribution are recorded
in [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).
