# Product-quality criteria

Ten `reporting-review` checklists for judging desired qualities of the software
product. Select them through [Reviewing a codebase](../reviewing-a-codebase.md),
apply the shared [cross-cutting concern model](../cross-cutting-concerns.md), and
keep inspection procedures and supporting-artifact verdicts outside these
lists. A `reporting-review` checklist records a judgment and its evidence
against each item rather than an action to perform; [Reviewing a
codebase](../reviewing-a-codebase.md) gives the working definition and the
assessment states.

- [Suitability quality criteria](suitability.md) - Use when assessing whether the product's capability set is complete and appropriate for its intended stakeholder needs and operating context.
- [Correctness quality criteria](correctness.md) - Use when assessing whether product behavior conforms to applicable contracts and preserves declared invariants across relevant conditions and transitions.
- [Reliability quality criteria](reliability.md) - Use when assessing whether required service remains dependable through time, demand, faults, interruption, degradation, and recovery.
- [Security quality criteria](security.md) - Use when assessing whether the product preserves authorized protection of information, identity, authority, and operation against relevant threats.
- [Safety quality criteria](safety.md) - Use when assessing whether the product keeps the risk of unacceptable harm within declared tolerances across use, misuse, failure, and integration.
- [Efficiency quality criteria](efficiency.md) - Use when assessing whether required behavior meets applicable time, capacity, resource, and cost constraints under representative workloads.
- [Usability quality criteria](usability.md) - Use when assessing whether intended users can understand and operate the product to accomplish relevant goals with acceptable effort and error risk.
- [Compatibility quality criteria](compatibility.md) - Use when assessing whether the product can coexist and exchange meaning with required systems and environments without unacceptable interference.
- [Evolvability quality criteria](evolvability.md) - Use when assessing whether the product can accommodate required change over its lifetime without disproportionate risk, delay, or cost.
- [Intelligibility quality criteria](intelligibility.md) - Use when assessing whether qualified maintainers can form an accurate, coherent, and appropriately bounded mental model of the product.

## Judging a product, not sustaining one

These lists judge a codebase against a declared claim on the evidence available
at a stated revision. Three of them name outcomes that a running system must
also be sustained against, and [How to run it](../../../operations/) owns that
side. The split is by question, not by subject.

| Outcome | Judged here as | Sustained there as |
| --- | --- | --- |
| Reliability | Whether the product supports a stated dependability claim on available evidence | Capacity, resilience, graceful degradation, and recovery under live demand |
| Security | Whether the product preserves authorized protection against declared threats | Access, secrets, patching, and audit for a running system |
| Efficiency | Whether required behavior meets its declared time, capacity, resource, and cost envelope | Ownership, on-call load, and retiring systems that still run |

A verdict here is a bounded judgment at a revision, not a statement about
production. A healthy production record is not a passing review, and a passing
review is not evidence that the live system holds.
