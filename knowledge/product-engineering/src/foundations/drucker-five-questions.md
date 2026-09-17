---
type: Explanation
title: Drucker's five most important questions
description: How Peter Drucker's self-assessment questions of mission, customer, customer value, results, and plan connect why an organization exists to whom it serves, how it recognizes results, and what it commits to, and how they can organize the intent behind a software product.
tags: [drucker, five-questions, mission, customer, customer-value, results, planning, self-assessment, pe-foundations]
status: draft
sources:
  - id: five-questions
    resource: https://www.shared-impact.com/wp-content/uploads/2020/09/5.-Most-Important-Questions-You-will-ever-ask-about-your-organization.pdf
    title: Audio-Tech Business Book Summaries — The Five Most Important Questions You Will Ever Ask About Your Organization, by Peter F. Drucker with Jim Collins, Philip Kotler, James Kouzes, Judith Rodin, V. Kasturi Rangan, and Frances Hesselbein (Jossey-Bass, 2008)
  - id: managing-for-results
    resource: https://archive.org/details/managingforresul00pete
    title: Peter F. Drucker — Managing for Results, 1964
  - id: results
    resource: https://drucker.institute/wp-content/uploads/2018/08/Reading-Drucker-on-Results.pdf
    title: Drucker Institute — Reading Drucker on Results, adapted from The Five Most Important Questions You Will Ever Ask About Your Organization and Management, revised edition
  - id: customer-centric
    resource: https://drucker.institute/wp-content/uploads/2018/08/Reading_Drucker-on-Being-Customer-Centric.pdf
    title: Drucker Institute — Reading Drucker on Being Customer-Centric
generated: { by: claude-code/claude-opus-5, at: 2026-09-17T03:01:33Z }
---

# Drucker's five most important questions

A team can specify a product precisely and still be unable to say whom it is
for, what they value, or how anyone will know it worked. Which questions should
an account of a product's intent answer before its behavior is specified?

Peter Drucker's self-assessment asks five questions of an organization: What
is our mission? Who is our customer? What does the customer value? What are
our results? What is our plan? The 2008 edition presents them as a way to
assess what the organization does, why, and what it must do to improve.[^five-questions]
Drucker first posed them for the social sector, and the 2008 edition
addresses businesses as well. Their application to software products below is
this bundle's interpretation, illustrated with
[Northbank Equipment](../northbank-equipment.md).

## The five questions

| Question | What Drucker asks for | Northbank illustration |
| --- | --- | --- |
| What is our mission? | Why the organization does what it does, not how, matched to its opportunities, competencies, and commitment | Keep contractors' crews working through dependable equipment access |
| Who is our customer? | One primary customer whose life the work changes, and the supporting customers who must also be satisfied | Small contractors coordinating equipment with a job start; depot staff, repair suppliers, and partner depots as supporting customers |
| What does the customer value? | What satisfies customers' needs, wants, and aspirations, as customers themselves say | A trustworthy promise that the equipment will be there when the crew starts |
| What are our results? | The changes the work brings about outside the organization, recognized by qualitative and quantitative measures together | Fewer lost crew days, and what contractors report about relying on a confirmation |
| What is our plan? | Mission, vision, goals, objectives, action steps, budget, and appraisal, beginning with what to abandon | Which service commitments to make, which to stop, and how progress will be appraised |

### Mission starts outside

Drucker says an effective mission is short, states why rather than how, and
starts from the outside environment. An organization that starts from its
resources and looks for places to use them will, he warns, focus on
yesterday.[^five-questions] In *Managing for Results* he makes a related point about
effort: "Results are obtained by exploiting opportunities, not by solving
problems."[^managing-for-results] Solving a problem restores normal operation; results come
from opportunities.

For a product team, this separates the mission from the software. Northbank's
contribution is dependable access for contractors; a reservation system is one
way to make it.

### Primary and supporting customers

The primary customer is the person whose life is changed by the work, and
Drucker asks for one primary customer rather than several. The primary
customer is never the only customer: supporting customers, such as
volunteers, members, partners, funders, referral sources, and employees, must
also be satisfied.[^customer-centric] They can say no, and satisfying one
customer without the others is no performance.[^five-questions] The
distinction is whose life changes and who must be satisfied, not who uses
what the organization offers.

In a product this separates people the product serves from people it must
satisfy, whether or not either group uses the product. A contractor's supervisor is served by a dependable confirmation. A
repair supplier who never uses the portal is still a supporting customer,
because Northbank cannot keep its promise if the supplier rejects the
arrangement.

### Value is what customers say

Drucker calls *What does the customer value?* the most important question and
the one least often asked. Organizations assume they know what they deliver;
he recommends starting from what the organization believes customers value
and comparing it with what customers actually say.[^five-questions] This is
the same discipline that [Jobs to Be Done](jobs-to-be-done.md) applies to customer progress: value is
established by evidence, not by the offering's description of itself.

### Results are qualitative and quantitative

Drucker locates results outside the organization: "results exist only on the
outside," and inside there are only costs. The result of a business is a
satisfied customer, and "it is the customer who creates a 'profit'"; for the
social sector, results are changed lives and conditions, in people's
behavior, circumstances, health, hopes, and competence and
capacity.[^results] He adds that a business cannot last without profit,
though whether profit alone is an adequate measure can be debated. The
published summary's list of sales, profit, and market share as business
results comes from a co-author's essay, not from Drucker's
chapter.[^five-questions] Qualitative measures show how deep and broad a change
is, and quantitative measures give definite standards; both are
needed.[^results]

A software objective therefore needs more than a count of its outputs. "At
least 60% of reservations are made online" is quantitative; "contractors
report that they plan crews around a confirmation without calling the depot"
is qualitative evidence of the same result. The
[Key performance indicators](key-performance-indicators.md) explanation
develops how measures connect to objectives and decisions.

### A plan begins with abandonment

The plan converts intentions into action. Goals are few and long-range;
objectives are specific and measurable levels of achievement that move the
organization toward its goals; action steps and budgets follow. Drucker lists
abandonment first among the elements of an effective plan: "If we were not
committed to this today, would we go into it?"[^five-questions]

For a product, the equivalent of abandonment is deciding what it will not do.
An explicit exclusion is a commitment, as much as an inclusion is.
[Drucker's four disciplines of organizational renewal](drucker-organizational-renewal.md)
develop abandonment alongside improvement, exploiting success, and innovation.

## Using the questions to organize product intent

The questions can arrange the intent behind a product so that a reader sees
what the business cares about, and which of those concerns nobody has
answered. In this bundle's interpretation:

| Question | Product intent it organizes |
| --- | --- |
| What is our mission? | Mission, vision, and principles; the opportunity that makes the product worth building now |
| Who is our customer? | The jobs of the people served, the product's users, and the stakeholders who must be satisfied or can say no |
| What does the customer value? | Evidence for those jobs and needs, and what each stakeholder values |
| What are our results? | Objectives, each a change outside the product with quantitative and qualitative indicators |
| What is our plan? | Strategy, the few things concentrated on now and what is set aside; and Scope, what the product takes on and what it deliberately leaves out |

The mapping of the plan is an interpretation: Drucker's plan holds no scope,
but its concentration, its abandonment, and his question of what the business
should not be come closest. Goals, action steps, budgets, and release plans
remain planning records rather than
product intent; the questions show where they connect without making them part
of a specification.

A gap under one question is informative. A product with detailed requirements
but no stated results cannot tell whether it succeeded; one with objectives but
no evidence of customer value may be measuring the wrong change.

## Connections across product engineering

- [Drucker's theory of the business](drucker-theory-of-the-business.md)
  examines the assumptions about environment, mission, and competencies that
  the first two questions make explicit.
- [Outcomes and evidence](../problem/outcomes-and-evidence.md) distinguishes
  observed results from the interpretation attached to them.
- [Strategy perspectives and their relationships](strategy-perspectives.md)
  compares Drucker's perspective with other accounts of strategic choice.

[^five-questions]: [Audio-Tech Business Book Summaries, The Five Most Important Questions You Will Ever Ask About Your Organization](https://www.shared-impact.com/wp-content/uploads/2020/09/5.-Most-Important-Questions-You-will-ever-ask-about-your-organization.pdf), summarized by arrangement with Jossey-Bass from Peter F. Drucker et al., 2008.
[^managing-for-results]: [Peter F. Drucker, Managing for Results](https://archive.org/details/managingforresul00pete), 1964.
[^results]: [Drucker Institute, Reading Drucker on Results](https://drucker.institute/wp-content/uploads/2018/08/Reading-Drucker-on-Results.pdf), adapted from *The Five Most Important Questions* and *Management*, revised edition.
[^customer-centric]: [Drucker Institute, Reading Drucker on Being Customer-Centric](https://drucker.institute/wp-content/uploads/2018/08/Reading_Drucker-on-Being-Customer-Centric.pdf).
