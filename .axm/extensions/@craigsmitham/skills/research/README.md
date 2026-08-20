# Research

Executes a bounded research brief and returns a consistent, evidence-backed
report organized around the brief's questions. It is designed for people who
need to understand the result quickly, inspect the evidence behind any answer,
and see which uncertainty still matters.

Every question keeps a stable identifier from the input brief through a summary
dashboard and detailed finding. The report includes citations, counterevidence,
confidence, decision implications, evidence that could change each answer, and
an actionable gap list.

## Use it when

- You have a research brief or explicit questions ready to investigate.
- You need current evidence gathered and synthesized rather than questions
  merely framed.
- You want a stable report shape across rapid, standard, and deep research.

Do not use it to define the initial research questions, create a survey or
interview guide, or make a decision the brief did not authorize.

## Install

```bash
axm skills install @craigsmitham/skills/research
```

It is also included in `@craigsmitham/packs/qrspi`.

## Example

```text
/research Execute this Research Brief in rapid mode. Preserve the question IDs,
use evidence current through today, and stop after two hours: ...
```

## Output

The report always contains research context, an executive synthesis, a question
dashboard, one detailed finding per question, cross-question synthesis,
emergent findings, unresolved gaps, and a source-and-method register.

## License

MIT
