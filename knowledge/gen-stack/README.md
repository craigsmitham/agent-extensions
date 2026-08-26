# Gen Stack

Opinionated software-change guidance combining OODA control with
human-oriented Intent, canonical Requirements, Architecture, Compilation,
Implementation, Evaluations, and operational learning.

## Scope

This bundle is the canonical knowledge authority used by the `gen-stack` pack.
It contains the complete Intent, Requirements, Architecture, work-item,
Implementation, Evaluation, and adaptive-control guidance formerly distributed
across the `gen-stack`, `software-architecture`, and `software-engineering`
knowledge packages. Its central rule is **one authority, many witnesses**:
accepted Requirements own desired-state obligations, while architecture,
implementations, tests, evaluations, and runtime observations retain their
different roles and may intentionally represent the same predicate.

The authority and transformation model is influenced by Chad Fowler's
[The Generative Stack](https://chadfowler.com/regenerative-software/3miwhqqvwxc2x/)
and the surrounding Regenerative Software series. The adaptive control model
applies John R. Boyd's OODA semantics from
[The Essence of Winning and Losing](https://www.coljohnboyd.com/documents/1995-06-28__Boyd_John_R__The_Essence_of_Winning_and_Losing__PPT-PDF.pdf).
The documents here are an original synthesis for this extension family; they
do not reproduce Fowler's or Boyd's text or diagrams.

## Use

Install the complete method through:

```bash
axm install @craigsmitham/packs/gen-stack
```

Open `src/index.md` to browse the bundle or use AXM Knowledge concept search.

Version `0.7.0` adds the Evaluation explainer and general, Surface, and C4
design guides; defines Evaluation Roles, Suites, and Reports; and requires the
governed System Evaluation Approach in the draft `gen-stack` application
profile. Concrete Definitions, Suites, Executions, Results, and Reports remain
repository-native. OODA and Requirement-impact guidance remains in
`src/control-loop/`; reusable Process authoring guidance remains in
`src/processes/`.

## License

The bundle is licensed under CC-BY-SA-4.0. This preserves the reciprocal
license previously declared by the consolidated software-architecture and
software-engineering knowledge packages. Referenced sources retain their own
rights; citations identify influence and provenance rather than relicensing
source material.
