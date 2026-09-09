# Software engineering

Evidence-backed guidance for reviewing software quality, designing tests at
the narrowest effective level through cross-boundary and browser-dependent
worlds, giving decided behavior an authoritative specification, and shaping
coherent repository execution surfaces. This pack installs one standalone
knowledge bundle and introduces no rules, skills, subagents, hooks, or MCP
servers, so this README is the only routing a reader gets.

## Included extension

| Extension | Role |
| --- | --- |
| `@craigsmitham/knowledge/product-engineering` | The How to build it section holds outcome-centered codebase review, cross-cutting quality concerns, test-suite quality and test-architecture guidance, executable-specification authority and lifecycle, and execution-surface craft |

The `software-engineering` bundle was retired into `product-engineering`, where
its concepts live under `src/engineering/` and carry the `pe-engineering` tag.
Installing this pack therefore brings the whole product-engineering body of
knowledge, not the engineering section alone.

## Where to start

| To do this | Read |
| --- | --- |
| Run a review of an existing codebase | `src/engineering/codebase-review/reviewing-a-codebase.md` |
| Decide which quality outcome a finding belongs to | `src/engineering/codebase-review/software-quality-pillars.md` |
| Place a concern that runs through every pillar | `src/engineering/codebase-review/cross-cutting-concerns.md` |
| Judge a test suite rather than the product | `src/engineering/codebase-review/supporting/test-suite-quality.md` |
| Choose a test level, or give a decided rule a specification | The eleven concepts at the top of `src/engineering/` |

Review is organized as ten product-quality pillars and eight cross-cutting
records. Per-outcome criteria lists and standalone review aids were retired;
the guidance they carried now sits inside the three files above.

## Install

```bash
axm packs install @craigsmitham/packs/software-engineering
```

## Use it for

- Reviewing a codebase against ten product-quality pillars and eight
  cross-cutting concern records, with each finding admitted against a pillar
  and its evidence method chosen without overclaiming.
- Assessing test-suite quality separately from product testability.
- Admitting a test deliberately, proving each behavior once at the cheapest
  trustworthy level, and substituting collaborators through explicit seams.
- Designing the smallest representative cross-boundary or end-to-end test
  world for a material integration risk.
- Deciding when interface evidence requires a real browser and choosing a
  focused scope, matrix, and observation contract.
- Deciding which rules earn an authoritative, human-readable specification,
  keeping incidental mechanics out of its text, and keeping it trustworthy
  once accepted.
- Designing task graphs, script surfaces, caching intent, and invocation
  contracts shared by humans, agents, and CI.

The knowledge bundle remains useful and installable on its own. It also holds
the five questions either side of How to build it: three of them carry
concepts, and two carry scope and boundaries only.

## License

The pack metadata and README are MIT-licensed. The included knowledge bundle
retains the license declared in its own manifest.
