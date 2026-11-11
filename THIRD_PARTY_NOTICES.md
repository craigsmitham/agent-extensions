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

## Pattern descriptions and collections

The `docs` knowledge bundle summarizes and adapts guidance from these works,
each published under Creative Commons Attribution-ShareAlike 4.0 International:

- Rebecca Wirfs-Brock and Christian Kohls,
  [Elephants, Patterns, and Heuristics](https://wirfs-brock.com/rebecca/papers/ElephantsPatternsAndHeuristics/)
  (2019, revised 2021).
- Lise B. Hvatum and Rebecca Wirfs-Brock,
  [Exploring the Generative Nature of Patterns](https://wirfs-brock.com/rebecca/papers/explrgenpat2023/)
  (2023).
- Rebecca Wirfs-Brock and Lise Hvatum,
  [Who Will Read My Patterns?](https://wirfs-brock.com/rebecca/papers/whowillread/)
  (2019, revised 2021).
- Lise B. Hvatum and Rebecca Wirfs-Brock,
  [Pattern Stories and Sequences for the Backlog](https://wirfs-brock.com/rebecca/papers/magicbacklog2017/)
  (2017).

The bundle reorganizes these ideas into documentation patterns, authoring and
review guidance, and original synthetic examples. The adapted guidance and
the existing docs package family retain `CC-BY-SA-4.0`; concept provenance
identifies the sources and bounds the claims attributed to them.

The bundle also discusses Alistair Cockburn's
[2023 PLoP talk](https://alistaircockburn.com/Talk%202023-10%20PLOP%2030%20yrs%20patterns.pdf),
Wirfs-Brock and Christian Kohls's
[Pattern Smells, Get Rid of Them](https://wirfs-brock.com/rebecca/papers/patternsmells/),
Kohls and Wirfs-Brock's
[Constructive Feedback Using Pattern Smells](https://wirfs-brock.com/rebecca/papers/constructivefeedback/),
and Wirfs-Brock and Lise Hvatum's
[The Value of Pattern Collections](https://wirfs-brock.com/rebecca/papers/valueofpatterncollections/).
The latter three are identified as 2026 preprints. These sources are cited in
original explanatory prose; their slides, figures, full texts, and templates
are not reproduced or vendored. Their source rights are not relicensed by
this repository. Chris Richardson's Microservices.io and Gregor Hohpe and
Bobby Woolf's Enterprise Integration Patterns are credited as observed
documentation examples, without reproducing their descriptions. The source
review for these pattern entries was refreshed on 2026-11-11.

## Checklist patterns

The docs bundle's checklist patterns reorganize and rewrite Craig Smitham's
earlier checklist-design guidance, whose 0.1.10 release used MIT. Concept
provenance pins that source revision. The new documentation belongs to the
existing `CC-BY-SA-4.0` docs bundle; earlier releases retain their license.

The concepts cite Degani and Wiener's NASA checklist study, Conroy and
colleagues' AAPM checklist guidance, PRISMA reporting guidance, Moore and
colleagues' process-evaluation guidance, the BetterBirth trial, software
inspection research, Shao and colleagues' regulated-learning meta-analysis,
Green and colleagues' test-enhanced-learning review, and Kalyuga and
colleagues' expertise-reversal review. These sources inform original summaries
and illustrative examples. Their full texts, checklists, figures, and templates
are not reproduced or vendored, and their source rights are not relicensed by
this repository. Domain-specific evidence is distinguished from the bundle's
generalized design guidance.

## Open Knowledge Format

`skills/okf/src/references/SPEC.md` is a vendored copy of the
[Open Knowledge Format v0.2 specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md)
from GoogleCloudPlatform's `open-knowledge-format` repository, pinned in the file's
header to upstream commit `ad30107c31c06aec8a7d5636e0d1058118604e6f` and
retrieved on 2026-10-30. The upstream work is licensed under Apache-2.0; its license
is included at `skills/okf/src/references/LICENSE-OKF.txt`. A
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

## Codebase renewal

The `codebase-renewal` pack contains original explanatory prose inspired by
Peter Drucker's renewal practices, with a software-engineering mapping to its
six standalone members. Its [package README](packs/codebase-renewal/README.md)
links the Drucker Institute reading and the members' source discussions. No
source text or code is vendored; the pack metadata and README use MIT, and each
member retains its own declared license.

## Repository reconciliation

The `reconcile` skill contains original instructions and explanatory prose
about duplication, divergence, and appropriate independence among repository
content. No third-party text or code is vendored; the package uses MIT.

## Software improvement

The `improve` skill contains original guidance inspired by Peter Drucker's
continuing improvement, SWEBOK's maintenance guidance, the public abstract of
ISO/IEC 25010:2023, Basili, Caldiera, and Rombach's Goal Question Metric work,
and Google's engineering practices. Its [package README](skills/improve/README.md)
links the sources and explains their contributions. No source text or code is
vendored; the package's original instructions and explanatory prose use MIT.

## Software experimentation

The `experiment` skill contains original guidance inspired by Peter Drucker's
systematic innovation, James Shore and Shane Warden's spike solutions,
Barry O'Reilly's hypothesis-driven development, and Microsoft Research's
trustworthy experimentation work. Its [package README](skills/experiment/README.md)
links the sources and explains their contributions and limits. No source text
or code is vendored; the package's original instructions and explanatory prose
use MIT.

## Software pruning

The `prune` skill contains original guidance inspired by David Parnas's work on
software contraction, SWEBOK's maintenance and retirement guidance, and Martin
Fowler's refactoring work. Its [package README](skills/prune/README.md) links
the sources and explains their contributions. No source text or code is
vendored; the package's original instructions and explanatory prose use MIT.

## Software alignment

The `align` skill contains original guidance inspired by W3C's specification
guidelines, IETF RFCs 2119 and 8174, SEI's architecture conformance work, and
NASA's requirements management and product verification guidance. Its
[package README](skills/align/README.md) links the sources and explains their
contributions. No source text or code is vendored; the package's original
instructions and explanatory prose use MIT.

## Software generalization

The `generalize` skill contains original guidance inspired by Bertrand Meyer,
David Musser and Alexander Stepanov, David Parnas, John Ousterhout, Martin
Fowler, and Sandi Metz. Its [package README](skills/generalize/README.md)
links the sources and explains each contribution. No source text or code is
vendored; the package's original instructions and explanatory prose use MIT.

## Software-engineering discipline migration

The `software-engineering-foundations` and discipline knowledge bundles retain
existing product-engineering material and its source attribution. The migration
map in `docs/software-engineering-migration.json` identifies the original
revision, moved concepts, and passages extracted from existing organizational
pages. These bundles synthesize ideas from public sources identified in each
concept’s provenance metadata. These include public
agent-engineering guidance from Anthropic and OpenAI, Silicon Valley Product
Group's product-model writing,
Roger L. Martin's Playing to Win writing, and Harvard Business School's
value-stick materials. The `product-engineering` bundle also absorbed the
retired `software-engineering` and `work-management` bundles, adding sources
such as ISO/IEC/IEEE and NIST standards, published Google engineering material,
Martin Fowler's and Kent Beck's public writing on testing, the DORA research
program, and public build-tool and browser-automation documentation. The
bundle contains original summaries and applications; it does not vendor those
sources or reproduce their proprietary templates.

The migrated foundations also cite Google SRE material, NASA and
DOE maintenance guidance, Parnas's software-aging work, Bill Buxton's design
work, Fred Brooks's essays, Ryan Singer's Shape Up, Glen Alleman's project
management writing, and Peter Drucker's business and renewal writing. Each
concept records its specific sources and distinguishes original applications
from the source authors' claims.

Every name above is credited because a file that survives in the repository
today cites it. Sources cited only by retired concepts are omitted.
