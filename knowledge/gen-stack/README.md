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

Version `0.6.0` keeps software work-item guidance in the top-level
`src/work-items/` collection and removes redundant intent-to-feedback and
change-signal reconciliation concepts. OODA and Requirement-impact guidance
remain in `src/control-loop/`; reusable Process authoring guidance remains in
`src/processes/`. The clean `gen-stack` application profile remains at
`src/profile/`.

## License

The bundle is licensed under CC-BY-SA-4.0. This preserves the reciprocal
license previously declared by the consolidated software-architecture and
software-engineering knowledge packages. Referenced sources retain their own
rights; citations identify influence and provenance rather than relicensing
source material.
