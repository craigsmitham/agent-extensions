---
type: Guide
title: Designing cross-boundary and end-to-end tests
description: Use when a material risk spans components, processes, services, storage, artifacts, or deployment configuration; design the smallest representative test world that can provide attributable evidence across the necessary boundaries.
tags:
  [
    testing,
    end-to-end-testing,
    e2e,
    system-testing,
    integration-testing,
    broad-stack-testing,
    test-architecture,
    test-fidelity,
    test-isolation,
    test-data,
    test-ownership,
    test-projects,
    monorepo,
    ci,
  ]
status: draft
sources:
  - id: istqb-risk
    resource: https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf
    title: ISTQB Certified Tester Foundation Level Syllabus v4.0.1
  - id: google-larger-testing
    resource: https://abseil.io/resources/swe-book/html/ch14.html
    title: Software Engineering at Google — Larger Testing
  - id: google-test-doubles
    resource: https://abseil.io/resources/swe-book/html/ch13.html
    title: Software Engineering at Google — Test Doubles
  - id: broad-stack-test
    resource: https://martinfowler.com/bliki/BroadStackTest.html
    title: Broad Stack Test
  - id: practical-test-pyramid
    resource: https://martinfowler.com/articles/practical-test-pyramid.html
    title: The Practical Test Pyramid
  - id: test-desiderata
    resource: https://testdesiderata.com/
    title: Test Desiderata
  - id: aspnet-integration
    resource: https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0
    title: Integration tests in ASP.NET Core
  - id: spring-mockmvc
    resource: https://docs.spring.io/spring-framework/reference/testing/mockmvc/vs-end-to-end-integration-tests.html
    title: Spring Framework — MockMvc vs End-to-End Tests
  - id: rails-testing
    resource: https://guides.rubyonrails.org/testing.html
    title: Testing Rails Applications
  - id: nx-playwright
    resource: https://nx.dev/docs/technologies/test-tools/playwright/introduction
    title: Nx with Playwright
  - id: nx-react-template
    resource: https://nx.dev/docs/templates/react
    title: Nx React template
  - id: playwright-projects
    resource: https://playwright.dev/docs/test-projects
    title: Playwright — Projects
  - id: flaky-tests-google
    resource: https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html
    title: Flaky Tests at Google and How We Mitigate Them
generated: { by: codex/gpt-5.6, at: 2026-09-02T14:30:02Z }
---

# Designing cross-boundary and end-to-end tests

Use this guide when the evidence you need depends on behavior crossing a real
boundary: components wired together, a protocol, process lifecycle, persistent
storage, a queue, an installed artifact, deployment configuration, or more than
one service. Use [Choosing browser-dependent interface
tests](choosing-browser-dependent-interface-tests.md) when the unresolved risk
is specifically browser rendering or interaction.

The goal is not to maximize realism. It is to create the **smallest test world
that preserves every distinction material to the claim**, produces a useful
contrary signal, and remains economical enough to trust and maintain. Larger
tests exist to close fidelity gaps, but fidelity, isolation, speed, specificity,
and predictiveness pull against one another.[^google-larger-testing][^test-desiderata]

## Desired outcomes

A good cross-boundary test architecture produces:

- **Claim-bearing evidence** — every test names the behavior and risk its
  result bears on.
- **Deliberate fidelity** — real and substituted boundaries are choices, with
  their accepted differences visible.
- **Useful failure** — a failure says which path or boundary contradicted the
  claim and preserves enough evidence to investigate it.
- **Independent execution** — tests can be selected, repeated, reordered, and
  parallelized unless an ordered sequence is itself the declared scenario.
- **Stable ownership** — the deployable, feature, integration, or system that
  owns the evidence also owns its lifecycle and diagnosis.
- **Proportionate feedback** — expensive worlds are reserved for risks that
  cheaper worlds cannot faithfully observe.
- **Replaceable machinery** — project layout, runners, containers, and
  frameworks implement the evidence contract without defining its meaning.

Risk-based testing focuses effort according to likelihood and impact rather
than treating every behavior and configuration as equally deserving of the
most expensive test.[^istqb-risk]

## Separate the dimensions

Testing labels are overloaded. Do not infer scope from the runner or directory
name. Describe a test on at least these dimensions:

| Dimension | Question | Example values |
| --- | --- | --- |
| **Claim scope** | What behavior and causal path does the result cover? | One function, component, application, workflow, multi-service journey |
| **Boundary reality** | Which production boundaries remain real? | In-process dispatch, real serialization, live database, real subprocess, substituted third party |
| **Execution distance** | How is the system obtained? | Imported module, framework test host, local processes, installed artifact, isolated deployment, shared environment |
| **Observation and control** | How is it driven and observed? | Direct call, HTTP client, message client, CLI, browser, external probe, human evaluation |

This yields combinations that names alone often hide:

| | Narrow claim scope | Broad claim scope |
| --- | --- | --- |
| **Non-browser observer** | A module or adapter test | An API-, CLI-, worker-, or message-driven system test |
| **Browser observer** | A component, rendering, or interaction test | A browser-driven cross-boundary journey |

A browser test is therefore not necessarily end-to-end. Conversely, a test can
exercise most of a system through a service or command interface without using
a browser. Broad-stack testing is a continuum, and its UI is only one possible
entrypoint.[^broad-stack-test]

Use **end-to-end** only with a declared start and a declared end. “From the public
HTTP request through persistence,” “from the installed command through its
output artifact,” and “from browser navigation through the application-owned
backend” are meaningful scopes. “Tests everything” is not.

## Design the evidence contract

### 1. Start with the decision, risk, and claim

Write four statements before choosing a runner:

1. **Decision:** what will this result permit or prevent?
2. **Risk:** what material failure could cross the boundary?
3. **Claim:** what observable behavior should hold, under which conditions?
4. **Contrary condition:** what plausible departure must make the test fail?

Include success, boundary, failure, interruption, and recovery conditions when
they materially change the decision. Do not turn an example count, coverage
percentage, or existing regression into an automatic mandate for a broad test.

### 2. Trace the minimum causal path

List the path from stimulus to observable consequence. Mark each boundary and
the failure it could introduce:

| Boundary | Distinctions a cheaper world might erase |
| --- | --- |
| Framework dispatch | Routing, middleware order, binding, validation, filters, error mapping |
| Serialization or protocol | Wire names, encoding, headers, status, framing, compatibility |
| Process lifecycle | Startup, shutdown, signals, environment, working directory, readiness |
| Persistent store | Real schema, transactions, constraints, queries, locking, migrations |
| Asynchronous work | Scheduling, acknowledgment, retry, ordering, eventual visibility |
| Service integration | Authentication, protocol contract, timeout, partial failure, version skew |
| Built or installed artifact | Packaging, omitted files, executable permissions, resolution, runtime dependencies |
| Deployment | Configuration binding, routing, identity, platform limits, asset and network behavior |

Retain a boundary only when its real behavior is necessary to discriminate the
claim. Replace the rest deliberately. A double is useful when its behavior is
understood and checked against the real collaborator; an unvalidated double can
make a test confidently green against an invented contract.[^google-test-doubles]

### 3. Choose the smallest representative test world

Move down this ladder only until the claim becomes observable:

| Test world | Preserves | Commonly omits |
| --- | --- | --- |
| Direct or composed in-process execution | Application logic and selected real collaborators | Host lifecycle, transport, packaging, deployment |
| Framework-native test host | Framework wiring, dispatch, rendering or serialization | Real server/container and network behavior |
| Live local process set | Process startup, real transport, local services | Installed/deployed topology and shared-platform behavior |
| Built or installed artifact | Packaging and runtime resolution | Deployment control plane and production topology |
| Isolated deployment | Deployment configuration and realistic topology | Shared traffic and production-only integrations |
| Shared staging or production observation | Actual shared environment | Hermeticity, early feedback, safe destructive control |

Framework-native tests are not “less real” in the abstract. ASP.NET Core can
bootstrap the application with an in-memory test server, and Spring MockMvc can
exercise framework request handling without a live server; each preserves
substantial behavior while omitting specific host and network distinctions.
Those omissions determine whether the world fits the claim.[^aspnet-integration][^spring-mockmvc]

If two worlds answer different risks, keep both. Do not make the broadest world
repeat all detailed cases already proved more specifically; use a small number
of representative cross-boundary examples to establish the integration claim.

### 4. Declare every real and substituted boundary

For each dependency, record:

- whether it is real, fake, simulated, recorded, or unavailable;
- which behavior the substitute must preserve;
- how compatibility with the real dependency is checked;
- which failures the world can and cannot reveal; and
- who owns drift between the substitute and reality.

Prefer a controlled local or isolated instance for application-owned
dependencies when their implementation matters. Prefer a substitute plus
contract evidence for third-party systems unless the decision genuinely needs
a safe provider-owned test environment. Broad tests against uncontrolled third
parties commonly add latency and instability without creating accountable
evidence.[^practical-test-pyramid][^google-larger-testing]

### 5. Select the control and observation surface

Choose the surface that exposes the user- or consumer-visible claim while
preserving the necessary path:

- public API or protocol for service behavior;
- command invocation and resulting output, state, and exit status for a CLI;
- message publication and observable downstream effect for an asynchronous
  workflow;
- browser interaction for browser-dependent consequences; or
- an external probe for a deployed availability or routing claim.

Use internal probes only when the claim itself is internal or when they provide
diagnostic evidence without replacing the public outcome. A test that drives a
public surface but proves success only through private state can miss a broken
consumer-visible response.

### 6. Give the harness an honest owner

Project layout should reflect evidence ownership and lifecycle:

| Placement | Use when |
| --- | --- |
| **Collocated with the subject** | The framework-native harness is part of that subject's normal build and dependency context, with no independent orchestration or release concern. |
| **Complementary project for one deployable** | The harness has distinct dependencies, configuration, tasks, artifacts, or runtime lifecycle and primarily verifies one application. |
| **Feature-owned project or suite** | A large deployable has stable feature ownership and independent selection needs that are proven by scale, not anticipated. |
| **Cross-system project** | The claim spans deployables or teams and has an explicit owner responsible for the whole journey and its failures. |

Start with one complementary project per deployable when a distinct harness is
warranted. Split only when ownership, dependency boundaries, selection, or
execution scaling has become independently meaningful. Keep browser, device,
environment, or authentication variations in the runner's configuration unless
they truly have different semantic owners.

Nx's frontend templates illustrate the complementary-project pattern with an
application and a sibling E2E project, while its Playwright integration can
also configure an existing project. Playwright projects represent repeated
configurations and subsets within a harness. These are useful examples of the
distinction between **repository project ownership** and **test-runner matrix**,
not universal folder requirements.[^nx-react-template][^nx-playwright][^playwright-projects]

Give every spanning test one diagnosis owner even when several teams must help
repair the product. Cross-boundary tests without clear ownership tend to rot
because no single component owner can interpret the whole failure path.[^google-larger-testing]

### 7. Design state and lifecycle as part of the test

A complete test contract includes:

1. obtain the exact system under test;
2. establish a known environment and identity;
3. create the minimum representative seed state;
4. wait for observable readiness;
5. perform the stimulus;
6. observe the public consequence and relevant contrary conditions;
7. capture diagnostic evidence; and
8. release resources or leave uniquely attributable data safe for later
   cleanup.

Prefer setup through stable domain or support APIs when their behavior belongs
to the scenario. Direct seeding is appropriate when it shortens setup without
erasing a boundary the claim depends on. Make generated identities unique and
record the seed or case identity needed to reproduce a failure.

Tests should not depend on the outcome of earlier tests. An intentionally
ordered workflow can live in one scenario or declare its sequence explicitly;
splitting it into order-dependent test cases creates misleading selection and
parallelism semantics. Rails, Google, and browser-framework guidance all expose
the same tradeoff: broader user workflows are valuable, but they cost more to
run, isolate, and maintain.[^rails-testing][^google-larger-testing]

Do not rely exclusively on teardown after success. Namespace test data,
constrain mutations, make cleanup idempotent, and plan for interruption so a
crashed worker does not poison later executions.

### 8. Define execution and evidence semantics

Place each suite at the earliest decision point its world can faithfully
support:

| Decision point | Suitable evidence |
| --- | --- |
| Local change | Fast, isolated worlds with focused selection and useful local diagnosis |
| Change review | Representative cross-boundary claims affected by the change |
| Post-merge | Wider or slower worlds whose delay does not invalidate submission feedback |
| Pre-deployment | Built-artifact, configuration, and isolated-deployment claims |
| Post-deployment | Non-destructive probes and observations that only the live environment can answer |

Bind the suite to a repository task whose inputs, dependencies, environment,
freshness, artifacts, and meaning of success are explicit. Use [Designing a
coherent repository task interface](repository-task-interface.md) for those
execution-surface semantics.

A retry is another observation, not proof that the first failure was harmless.
Preserve attempt-level results and distinguish product failure, test defect,
environment failure, and unknown. At large scale, flaky signals consume
diagnostic attention and train teams to ignore legitimate failures.[^flaky-tests-google]

### 9. Make failure attributable

On failure, retain the smallest safe evidence set that reconstructs the path:

- test identity, claim, case data, and seed;
- source, built artifact, deployment, and configuration identities;
- dependency and substitute versions;
- structured request, response, message, exit-status, or domain-event facts;
- lifecycle and readiness failures;
- logs and correlation identifiers from every owned boundary; and
- browser traces, screenshots, or console/network evidence when a browser is
  the observer.

Do not collect secrets, unbounded production data, or opaque bodies merely
because they might help. Prefer structured, redacted, attributable diagnostics
designed with the system.

### 10. Review and retire deliberately

Review a test when its claim, boundary, dependency, deployment, or ownership
changes, or when runtime and flakiness alter its decision value. Ask:

- Does this risk still require these real boundaries?
- Has a narrower test or contract check made the broad test redundant?
- Has the world drifted from the supported deployment?
- Does the failure remain attributable to an owner?
- Is the suite still early and reliable enough for its decision point?
- Would one representative scenario now provide the same evidence as several?

Retire tests whose claim is gone, duplicated, or no longer discriminated. Do
not retain them as ceremonial “coverage.”

## Completion check

Before admitting a new or materially widened cross-boundary suite, confirm:

- [ ] The decision, risk, claim, and contrary condition are explicit.
- [ ] Both ends and every necessary boundary of the claimed path are named.
- [ ] The selected world is the smallest one that preserves those distinctions.
- [ ] Real and substituted dependencies, drift checks, and blind spots are declared.
- [ ] The control and observation surface matches the consumer-visible claim.
- [ ] Project placement reflects one accountable semantic owner.
- [ ] State, readiness, interruption, cleanup, and parallel execution are designed.
- [ ] The repository task exposes inputs, environment, freshness, artifacts, and result meaning.
- [ ] Failures retain safe, attributable diagnostics; retries remain visible.
- [ ] Review and retirement triggers are identified.

If the unresolved reason for the test is browser behavior, continue with
[Choosing browser-dependent interface
tests](choosing-browser-dependent-interface-tests.md). If no material risk
requires a real boundary, use the narrower test architecture instead.

[^istqb-risk]: ISTQB, [Certified Tester Foundation Level Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), section 5.2, defines product-risk analysis as a way to focus testing according to likelihood and impact.
[^google-larger-testing]: Graves, [Larger Testing](https://abseil.io/resources/swe-book/html/ch14.html), explains fidelity, system-under-test forms, ownership, hermeticity, data, and the costs of larger tests.
[^test-desiderata]: Beck and Sutton, [Test Desiderata](https://testdesiderata.com/), presents valuable test properties as interacting aims rather than one universal test shape.
[^broad-stack-test]: Fowler, [Broad Stack Test](https://martinfowler.com/bliki/BroadStackTest.html), describes broad-stack scope as a continuum and notes that a UI is not required to exercise most of a system.
[^google-test-doubles]: Winters et al., [Test Doubles](https://abseil.io/resources/swe-book/html/ch13.html), distinguishes doubles and cautions against tests that validate only the behavior a mock author assumed.
[^aspnet-integration]: Microsoft, [Integration tests in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0), documents application bootstrapping through `WebApplicationFactory` and an in-memory test server.
[^spring-mockmvc]: Spring, [MockMvc vs End-to-End Tests](https://docs.spring.io/spring-framework/reference/testing/mockmvc/vs-end-to-end-integration-tests.html), states which request-handling behavior MockMvc preserves and which live-container behavior it omits.
[^practical-test-pyramid]: Ham Vocke, [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html), distinguishes narrow integration checks from broad-stack tests and recommends controlled substitutes for remote systems.
[^nx-react-template]: Nx, [React template](https://nx.dev/docs/templates/react), presents an application with a complementary Playwright E2E project as part of its workspace structure.
[^nx-playwright]: Nx, [Nx with Playwright](https://nx.dev/docs/technologies/test-tools/playwright/introduction), documents selecting Playwright during application generation and configuring it for an existing project.
[^playwright-projects]: Playwright, [Projects](https://playwright.dev/docs/test-projects), defines runner projects as logical test groups sharing configuration, such as browsers, environments, states, or subsets.
[^rails-testing]: Rails, [Testing Rails Applications](https://guides.rubyonrails.org/testing.html), distinguishes framework integration tests from browser-driven system tests and their cost and fidelity tradeoffs.
[^flaky-tests-google]: Micco, [Flaky Tests at Google and How We Mitigate Them](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html), reports the operational and decision costs of nondeterministic test results.
