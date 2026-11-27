---
okf_version: "0.2"
---
# Software engineering

Start with the decision facing the team. A test or production observation can send a change back to design, and the examples below can be used independently.

| Work on a change | Where to start |
| --- | --- |
| Understand the need | Use [Jobs to Be Done](business-analysis/foundations/jobs-to-be-done.md) to understand the progress someone seeks. Use [Shape Up](project-management/foundations/shape-up.md) to bound the investment. |
| Describe what should change | [Selecting a specification method](requirements-engineering/authoring/selecting-a-specification-method.md) helps express behavior, constraints, and acceptance conditions. |
| Design and build | [Buxton on design](architecture-and-design/foundations/buxton-design.md) covers exploring alternatives. Use [domain-driven design](architecture-and-design/foundations/domain-driven-design.md) when concepts or interfaces need clearer boundaries. |
| Get feedback while implementing | Turn an agreed example into an [executable specification](software-testing/patterns/executable-specifications.md). Choose [which components to exercise](software-testing/patterns/evidence-matched-test-world.md) so the test can expose the failure that matters. |
| Integrate and release | Trace the decisions in [Delivering a software change](release-engineering/foundations/delivering-a-software-change.md). For teams shipping from main, use the [direct-to-main delivery guide](release-engineering/guides/direct-to-main-delivery.md) to place checks and handle concurrent changes. |
| Confirm the result in production | Follow the change through exposure and observed behavior using the [delivery job map](release-engineering/foundations/delivering-a-software-change.md). If users are affected by a failure, use [incident policy and records](software-operations/foundations/incident-policy-and-records.md) to coordinate recovery. |

## Browse by discipline

- [Business analysis](business-analysis/index.md)
- [Requirements engineering](requirements-engineering/index.md)
- [Architecture and design](architecture-and-design/index.md)
- [Software testing](software-testing/index.md)
- [Release engineering](release-engineering/index.md)
- [Software operations](software-operations/index.md)
- [Project management](project-management/index.md)
