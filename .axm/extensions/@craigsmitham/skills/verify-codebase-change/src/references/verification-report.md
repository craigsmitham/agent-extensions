# Codebase Change Verification Report shape

Use this shape selectively. Omit inapplicable sections and empty fields.

```markdown
# Verification Report: <change>

Disposition: Verified | Not Verified | Blocked
Accepted contract: <source, authority, identity, and time>
Implementation snapshot: <identity, comparison boundary, and observation time>

## Scope and Limitations
<Included surfaces, material drift, environment, access, provenance, and
independence limits.>

## Verification Summary
<What is established, contradicted, or still unverified.>

## Obligation Matrix
| Source ID or obligation | Implementation evidence | Verification evidence | Status |
| --- | --- | --- | --- |

Label material evidence `Observed`, `Declared`, or `Inferred`. Include its
locator and snapshot or observation time when attribution affects the claim.

## Findings
### V1 — <finding>
- Status: Unsatisfied | Unverified
- Expected: <accepted source>
- Actual or missing: <implementation/evidence>
- Consequence and affected scope: ...
- Reproduction or observation path: ...

## Checks Performed
| Check or command | Target and environment | Observed at | Result | Evidence, side effects, or limitation |
| --- | --- | --- | --- | --- |

## Unplanned Scope and Plan Deviations
<Separate accepted-contract effects from harmless implementation differences.>

## Conformance and Outcome Validation
- Contract conformance: ...
- Outcome evidence: ...

## Closeout Boundary
<Exact blockers or remaining evidence; do not turn this into a repair plan.>
```
