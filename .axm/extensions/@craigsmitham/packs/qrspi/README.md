# QRSPI

Provides a two-stage workflow for independent research. It first turns a subject
into a small set of high-value, evidence-seeking questions prioritized around
consequential uncertainty, then executes that brief as a consistent,
question-by-question evidence report.

## Included extensions

| Extension | Role |
| --- | --- |
| `@craigsmitham/skills/question` | Select relevant concerns and produce a Research Brief with prioritized, stable question IDs, including hypothesis-neutral blind checks |
| `@craigsmitham/skills/research` | Execute a Research Brief and return a stable report with citations, counterevidence, confidence, implications, and gaps |

## Install

```bash
axm packs install @craigsmitham/packs/qrspi
```

## Usage

```text
/question Frame the five research questions most likely to change our decision
about this proposal. Treat the prior analysis as originating material and keep
the independent frame blind to its findings.

/research Execute the resulting Research Brief in standard mode.
```

The pack supports research framing and execution. It does not make the resulting
decision unless the caller explicitly requests and authorizes that outcome.

## License

The pack's own metadata and README are licensed under MIT. Its member retains
the license declared in its manifest.
