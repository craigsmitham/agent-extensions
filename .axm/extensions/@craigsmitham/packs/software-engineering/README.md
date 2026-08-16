# Software engineering

Software engineering judgment for architecture documentation and
evidence-timed change. This pack keeps YAGNI and Tidy First as distinct,
concise rules while placing their rationale, boundaries, and examples beside
portable architecture guidance in a shared knowledge bundle.

## Included extensions

| Extension | Role |
| --- | --- |
| `@craigsmitham/knowledge/software-engineering` | Architecture documentation, functional and quality concerns, changeability, invariants, YAGNI, Tidy First, and paired explainers and guides for software work items |
| `@craigsmitham/rules/yagni` | Questions speculative capability, structure, process, and scope throughout the SDLC |
| `@craigsmitham/rules/tidy-first` | Questions whether a small behavior-preserving preparation should precede an authorized behavior change |

The rules are not standalone: each links to a document in the bundled
knowledge package. The knowledge package remains useful on its own.

## Install

```bash
axm install @craigsmitham/packs/software-engineering
```

## Usage

The rules remain available as lightweight decision prompts. Follow their links
when the decision needs the fuller model, constraints, or examples. The
knowledge bundle also provides tool-neutral explainers and authoring guides for
an intentionally small architecture corpus, operational incident records,
software defect reports, and feature requests.

## Evaluation cases

Use these cases when validating the effective instruction surface:

| Case | Expected decision |
| --- | --- |
| One provider is requested and no second variation is active | Do not build an unused provider framework |
| Current structure materially obstructs an authorized behavior change | Consider the smallest behavior-preserving preparation, then make the behavior change separately |
| Urgent restoration makes preparatory work too costly | Change behavior directly; tidy after, later, or never |
| A public compatibility boundary will soon become costly to reverse | Treat compatibility as a current constraint while deferring unrelated extension points |
| The task is read-only research, diagnosis, or review | Neither rule authorizes a structural or behavioral change |

## License

The pack's own metadata and README are licensed under MIT. Each member retains
the license declared in its manifest. See the repository for source attribution
and provenance.
