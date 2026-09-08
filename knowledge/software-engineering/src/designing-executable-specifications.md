---
type: Guide
title: Designing executable specifications
description: Use when intended behavior needs an authoritative, human-readable, continuously verified statement that non-authors can dispute; choose which rules earn a specification, keep incidental mechanics out of the specification text, and bind automation below the readable layer.
tags:
  [
    testing,
    executable-specifications,
    specification-by-example,
    bdd,
    acceptance-testing,
    gherkin,
    living-documentation,
    test-architecture,
    characterization-testing,
    spec-driven-development,
  ]
status: draft
sources:
  - id: north-introducing-bdd
    resource: https://dannorth.net/introducing-bdd/
    title: Introducing BDD
  - id: fowler-spec-by-example
    resource: https://martinfowler.com/bliki/SpecificationByExample.html
    title: Specification by Example
  - id: fowler-business-readable
    resource: https://martinfowler.com/bliki/BusinessReadableDSL.html
    title: Business Readable DSL
  - id: fowler-given-when-then
    resource: https://martinfowler.com/bliki/GivenWhenThen.html
    title: Given When Then
  - id: adzic-spec-by-example
    resource: https://www.manning.com/books/specification-by-example
    title: Specification by Example — How Successful Teams Deliver the Right Software
  - id: cucumber-better-gherkin
    resource: https://cucumber.io/docs/bdd/better-gherkin/
    title: Cucumber — Writing Better Gherkin
  - id: cucumber-brief
    resource: https://cucumber.io/blog/bdd/keep-your-scenarios-brief/
    title: Keep Your Scenarios BRIEF
  - id: cucumber-antipatterns
    resource: https://cucumber.io/blog/bdd/cucumber-anti-patterns-part-two/
    title: Cucumber Anti-Patterns
  - id: keogh-criteria-scenarios
    resource: https://lizkeogh.com/2011/06/20/acceptance-criteria-vs-scenarios/
    title: Acceptance Criteria vs. Scenarios
  - id: farley-four-layer
    resource: https://www.adamsanderson.co.uk/blog/2025-02-22-acceptance-tests-and-playwright/
    title: Building Acceptance Tests Using a Four-Layer Model
  - id: bdd-quality-study
    resource: https://pmc.ncbi.nlm.nih.gov/articles/PMC7251619/
    title: Characterising the Quality of Behaviour Driven Development Specifications
  - id: martraire-living-docs
    resource: https://hilton.org.uk/blog/living-documentation-principles
    title: Principles of Living Documentation
  - id: pact-intro
    resource: https://docs.pact.io/
    title: Pact — Contract Testing
  - id: characterization-tests
    resource: https://understandlegacycode.com/blog/characterization-tests-or-approval-tests/
    title: Regression, Characterization, and Approval Tests
generated: { by: claude/opus-5, at: 2026-09-08T11:45:02Z }
---

# Designing executable specifications

Use this guide when a behavior needs a statement of intent that people who do
not read the code can read and dispute, and that fails automatically when the
system stops honoring it.

An executable specification is defined by **authority and audience**, not by
test level, notation, or framework. Its text is what intended behavior means;
code and automation conform to it. That axis is orthogonal to the level ladder:
a specification may execute as a unit test, and a browser end-to-end test may
be no specification at all. Choose the level with the [narrowest effective
test](choosing-the-narrowest-effective-test.md),
[cross-boundary](designing-cross-boundary-and-end-to-end-tests.md), and
[browser-dependent](choosing-browser-dependent-interface-tests.md) guides; use
this guide to decide which behaviors earn a specification and what its text may
contain.[^north-introducing-bdd][^fowler-spec-by-example]

A specification is not a contract suite. A contract suite is the comprehensive
test of a consumer-facing module interface; a specification states a rule
someone could have decided differently. One suite may be both, but the two
properties are earned separately.

## Desired outcomes

- **Disputable rules** — each specification states a rule a stakeholder could
  reasonably disagree with, not a mechanism.
- **Text as authority** — implementation and automation change to match the
  specification, never the reverse.
- **Readable without the code** — domain language, named actors, concrete data.
- **Automation below the text** — binding layers absorb interface and
  implementation change without edits to a specification.
- **Continuous validation** — the set runs on every change, so its claims stay
  warranted rather than aspirational.

## Admit a specification deliberately

A specification carries a readable layer, a binding layer, and an obligation to
keep both honest — a cost most tests should not pay. Admit one only when all
four hold:

1. **It is a rule, not a mechanism** — the behavior was decided, and a
   different decision was available.
2. **Someone outside the author has standing** — a stakeholder, another team, a
   regulator, or a downstream consumer can contradict it.
3. **It outlives the implementation** — the rule survives a rewrite of whatever
   enforces it today.
4. **No existing specification owns it** — no other already states the rule.

Acceptance criteria are abstract rules; specifications are the concrete
examples drawn from them. Do not write an example for every criterion — when
examples follow from one in seconds of conversation, leave it as a
criterion.[^keogh-criteria-scenarios] Examples illustrate rules rather than
enumerating behavior, so a set of them is deliberately incomplete and cannot
alone establish correctness.[^fowler-spec-by-example]

## Write the specification text

Each specification states one rule and shows it with real data:[^cucumber-brief]

- **Business language** — words from the domain the rule belongs to.
- **Real data** — names, amounts, dates; placeholders hide what real values
  expose.
- **Intention revealing** — what the actor is achieving, not how.
- **Essential** — anything not carrying the rule is incidental; remove it.
- **Focused** — one rule per example; a second rule is a second example.
- **Brief** — most examples fit in five lines or fewer.

Name the actor: first-person "I" hides which party acts and
observes.[^cucumber-antipatterns] Keep the phases distinct — context, one
triggering event, observable outcome; two unrelated events mean two
specifications.[^fowler-given-when-then]

Apply one test before accepting wording: **will this text need to change if the
implementation changes?** If yes, mechanics have leaked in and belong in the
binding layer.[^cucumber-better-gherkin] The opposite failure is as common — an
example with no concrete values restates the rule instead of illustrating
it.[^cucumber-antipatterns]

## Keep these out of the specification text

| Kept out | Where it belongs |
| --- | --- |
| Interface mechanics: field entry, clicks, navigation, selectors | Binding layer |
| Boundary sweeps, validation matrices, combinatorial tables | Unit or property-based tests |
| Incidental setup: credentials, sign-in steps, dates the rule does not depend on | Binding layer |
| Wire formats, status codes, payload shape | Contract suite or narrow integration test |
| Stored rows, log output, call counts | Narrow test through an explicit seam |
| Behavior discovered by reading existing code | Characterization test, named as such |
| Rules no one outside the author could dispute | An ordinary test, with no specification ceremony |

Two exclusions matter most because they masquerade as thoroughness.
**Parameterized expansion** multiplies cases cheaply and is the common cause of
bloated suites; use an example table only where each row is a distinct rule a
reader needs.[^cucumber-antipatterns] **Retroactive specifications** — written
afterward to record what the code already does — assert actual rather than
intended behavior; that is a characterization or approval test, often valuable
but carrying no authority over intent.[^characterization-tests]

## Worked example

A refund rule, first written as a recorded interface walkthrough:

```gherkin
Scenario: Refund
  Given I am on the login page
  And I sign in as "user1@test.com" with password "Passw0rd!"
  And I navigate to "/account/membership"
  When I click "Cancel membership"
  And I click "Confirm"
  Then I should see "Your refund is being processed"
  And the refunds table contains a row with status "PENDING"
  And the response status is 200
```

The reader learns how to drive the sign-in form, and cannot learn what a member
is entitled to. The same behavior as a specification:

```gherkin
Rule: An annual membership is refunded in full if cancelled within 14 days

  Example: Priya cancels inside the refund window
    Given Priya bought an annual membership for £120 on 1 March
    When she cancels it on 14 March
    Then she is refunded £120

  Example: Priya cancels after the refund window
    Given Priya bought an annual membership for £120 on 1 March
    When she cancels it on 20 March
    Then she is refunded £0
```

| Removed | Reason | New home |
| --- | --- | --- |
| Sign-in steps and credentials | Incidental to the rule | Binding layer |
| Page paths, button labels, message text | Implementation mechanics | Protocol driver |
| `refunds` table row assertion | Storage detail, not the promise | Narrow integration test |
| Response status `200` | Transport detail | Contract suite |

The examples sit either side of the window without adjudicating its edge. Day
14 itself is a boundary question: prove it in a narrower test rather than
growing the specification into a coverage matrix.

## Separate the specification from its automation

Automate validation without changing the specification; when automation is
awkward, change the automation.[^adzic-spec-by-example] Four layers keep that
possible:[^farley-four-layer]

| Layer | Contains | Changes when |
| --- | --- | --- |
| **Specification** | The rule and its examples, in domain language | The rule changes |
| **Domain actions** | A small vocabulary of domain operations and observations | The domain vocabulary changes |
| **Protocol drivers** | How an operation is performed against one interface: HTTP, in-process, browser | An interface changes |
| **System** | The subject under test | — |

Bind at the lowest layer that still exercises the rule; driving every
specification through a browser makes the suite slow and brittle and pins the
practice to the top of the ladder.[^cucumber-antipatterns] Where a rule must
hold across several interfaces, add a protocol driver rather than a second
specification. Maintain the middle layers as deliberately as the text: organize
domain actions by domain concept rather than by feature file, reuse existing
phrasing instead of coining synonyms, keep the domain vocabulary small and free
of technical terms, and hold one level of abstraction across a
suite.[^bdd-quality-study]

## Choose a notation, not a framework

Gherkin is one notation. Table-driven examples, a plain test DSL with
domain-named cases, and a shared contract suite can each be executable
specifications, and a Gherkin file can easily fail to be one. Choose by who
must read the text: the value is that it is business-*readable*, not
business-*writable*.[^fowler-business-readable] Neighboring forms add what
examples cannot. **Property-based tests** assert an
invariant over generated inputs — the right home for variation kept out of the
specification text, and poor stakeholder documentation. **Consumer-driven
contracts** specify an integration as concrete request and response pairs;
assert only fields actually consumed, since over-specifying couples the
consumer to provider internals.[^pact-intro] **Formal specifications** check
state spaces examples cannot reach, and do not replace a readable set.

## Keep specifications authoritative

A specification that does not run continuously is documentation with no
warrant. Run the set on every change and publish its readable output where the
people who own the rules can reach it; documentation earns trust by being
automatically checked, not carefully maintained.[^martraire-living-docs]
When one fails, decide which side is wrong before changing either: the
implementation stopped honoring the rule, the rule changed and the text should
change deliberately with its owner, or the text never stated the rule
correctly. Never edit a specification to match observed behavior to make a
suite green — that converts it into a characterization test still labeled as
intent. Retire specifications whose rule is gone, rewrite ones kept only
because they were once written, and declare who owns each set's
text.[^cucumber-antipatterns]

## Specify behavior for generated change

When code is cheap to regenerate, the executable specification is what holds
intent stable across regenerations, and the gate a generated change must pass:
its text is readable by a reviewer who did not write the change, and its
failure is attributable to a named rule. The admission rules do not relax under
generation. The characteristic failure is volume — many generated examples,
none disputed by anyone, encoding the current implementation rather than a
decision. Treat a specification proposed alongside an implementation as
unreviewed until someone with standing over the rule has read it, and keep
authored intent separate from generated coverage.

## Completion check

- [ ] It states one decided rule that someone outside the author can dispute,
      and no other specification already states it.
- [ ] The text uses domain language, a named actor, and concrete real data.
- [ ] The text would survive a change of implementation or interface.
- [ ] Mechanics, incidental setup, storage, and transport details are absent,
      and variation and boundary coverage live in narrower tests.
- [ ] Automation binds through domain actions and a protocol driver, at the
      lowest layer that exercises the rule.
- [ ] The set runs continuously and its output reaches the rules' owners.
- [ ] Any test recording existing behavior is labeled a characterization test.

[^north-introducing-bdd]: North, [Introducing BDD](https://dannorth.net/introducing-bdd/), recounts replacing "test" with "behaviour" to give analysts, testers, developers, and the business one vocabulary for intent.
[^fowler-spec-by-example]: Fowler, [Specification by Example](https://martinfowler.com/bliki/SpecificationByExample.html), describes concrete examples as both specification and test, and warns that examples are inherently incomplete and cannot stand alone.
[^fowler-business-readable]: Fowler, [Business Readable DSL](https://martinfowler.com/bliki/BusinessReadableDSL.html), argues the value lies in business people reading the text, and that making it business-writable raises cost sharply.
[^fowler-given-when-then]: Fowler, [Given When Then](https://martinfowler.com/bliki/GivenWhenThen.html), sets out context, event, and outcome, and notes that frameworks execute "given" clauses as setup rather than description.
[^adzic-spec-by-example]: Adzic, [Specification by Example](https://www.manning.com/books/specification-by-example), presents the process patterns of illustrating with examples, refining the specification, automating validation without changing specifications, validating frequently, and evolving a living documentation system.
[^cucumber-better-gherkin]: Cucumber, [Writing Better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/), contrasts declarative and imperative styles and offers the test of whether wording must change when the implementation does.
[^cucumber-brief]: Cucumber, [Keep Your Scenarios BRIEF](https://cucumber.io/blog/bdd/keep-your-scenarios-brief/), gives business language, real data, intention revealing, essential, focused, and brief as the qualities of a readable example.
[^cucumber-antipatterns]: Cucumber, [Cucumber Anti-Patterns](https://cucumber.io/blog/bdd/cucumber-anti-patterns-part-two/), catalogs testing through the UI, first-person actors, retained noisy scenarios, example-table overuse, blurred phases, and vague scenarios that only restate the rule.
[^keogh-criteria-scenarios]: Keogh, [Acceptance Criteria vs. Scenarios](https://lizkeogh.com/2011/06/20/acceptance-criteria-vs-scenarios/), distinguishes abstract criteria from concrete examples and recommends leaving criteria unwritten as scenarios until automation requires them.
[^farley-four-layer]: [Building Acceptance Tests Using a Four-Layer Model](https://www.adamsanderson.co.uk/blog/2025-02-22-acceptance-tests-and-playwright/) demonstrates test cases calling a domain DSL, drivers implementing that DSL per interface, and the same specifications running against different interfaces.
[^bdd-quality-study]: [Characterising the Quality of Behaviour Driven Development Specifications](https://pmc.ncbi.nlm.nih.gov/articles/PMC7251619/), reports practitioner support for conservation of steps, conservation of domain vocabulary, elimination of technical vocabulary, and conservation of proper abstraction.
[^martraire-living-docs]: [Principles of Living Documentation](https://hilton.org.uk/blog/living-documentation-principles) summarizes Martraire's collaborative, insightful, reliable, and low-effort documentation, made reliable by automated checks.
[^pact-intro]: [Pact](https://docs.pact.io/) defines consumer-driven contract testing as contract by example, with the consumer asserting only what it actually uses.
[^characterization-tests]: [Regression, Characterization, and Approval Tests](https://understandlegacycode.com/blog/characterization-tests-or-approval-tests/) distinguishes tests that capture actual behavior from tests that assert intended behavior.
