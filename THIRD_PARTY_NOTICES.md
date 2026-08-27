# Third-party notices

## Diátaxis documentation framework

The `docs` package family is inspired by and, where its concept provenance says
so, adapts material from the
[Diátaxis documentation framework](https://diataxis.fr/) by Daniele Procida.
The upstream source is available at
[`evildmp/diataxis-documentation-framework`](https://github.com/evildmp/diataxis-documentation-framework)
under the Creative Commons Attribution-ShareAlike 4.0 International license.
The package concept files identify their specific sources and indicate that the
material has been reorganized, summarized, and adapted for agent use.

## Open Knowledge Format

`author-okf/src/references/SPEC.md` is a vendored copy of the
[Open Knowledge Format v0.2 specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
from GoogleCloudPlatform's `knowledge-catalog` repository, pinned in the file's
header to upstream commit `3fcbb9f828c2f23d109c855ee403c3a4c81f3a96` and
retrieved on 2026-07-27. The upstream work is licensed under Apache-2.0. A
vendor header was added; the specification body is otherwise unchanged from
that pinned revision.

## Effect

The Effect v4 extensions describe public APIs and patterns from
[`Effect-TS/effect`](https://github.com/Effect-TS/effect), which is licensed
under MIT. The extensions are original guidance and examples rather than a
vendored copy of the Effect source.

## JavaScript Temporal

`temporal-dates` describes the public JavaScript Temporal API and links readers
to authoritative public references. It does not vendor the TC39 specification
or MDN documentation.

## Management and architecture sources

The `gen-stack`, `knowledge-management`, `product-management`, and `strategy`
bundles synthesize ideas from public
sources identified in each concept's provenance metadata. These include the
FAIR Guiding Principles, W3C PROV, KCS, ISO/IEC/IEEE 42010, D. L. Parnas's work
on modular decomposition, Kent Beck's writing and interviews on YAGNI and Tidy
First, Martin Fowler's writing on YAGNI and preparatory refactoring, the Agile
Alliance's simple-design guidance, Sandi Metz's writing on premature
abstraction, public agent-engineering guidance from Anthropic and OpenAI,
Silicon Valley Product Group's product-model writing, Roger L. Martin's Playing
to Win writing, and Harvard Business School's value-stick materials. The
bundles and related rule packages contain original summaries and applications;
they do not vendor those sources or reproduce their proprietary templates.

Gen Stack `0.3.0` consolidates the original guidance previously published in
the `software-architecture` and `software-engineering` knowledge packages. The
merged package preserves their source-level attribution and CC-BY-SA-4.0
reciprocal licensing; the former published package versions retain their
original identities and licenses.

The `gen-stack` bundle and pack are explicitly influenced by Chad Fowler's
[The Generative Stack](https://chadfowler.com/regenerative-software/3miwhqqvwxc2x/)
and the surrounding Regenerative Software series. They contain an original
software-change method and terminology for authority, Requirements,
evaluations, and bounded regeneration; they do not vendor Fowler's prose or
diagrams. Individual concepts identify the source claims they use.

The `gen-stack` bundle and pack also adapt the Observe, Orient, Decide, and Act
control semantics from John R. Boyd's
[The Essence of Winning and Losing](https://www.coljohnboyd.com/documents/1995-06-28__Boyd_John_R__The_Essence_of_Winning_and_Losing__PPT-PDF.pdf).
They apply OODA as an original software-change control model and do not vendor
Boyd's briefing or diagram.

The Gen Stack Shape guidance and skill are conceptually influenced by Ryan
Singer and Basecamp's public [Shape Up](https://basecamp.com/shapeup/)
guidance, including appetite, boundaries, risks, pitches, and breadboarding.
They adapt those ideas into an original Gen Stack change-intent and repository-
impact workflow; they do not vendor Shape Up prose, diagrams, or templates.
