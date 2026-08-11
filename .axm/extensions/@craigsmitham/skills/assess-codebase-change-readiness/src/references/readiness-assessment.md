# Codebase Change Readiness Assessment shape

Use this shape selectively. Omit inapplicable sections and empty fields.

```markdown
# Readiness Assessment: <change>

Disposition: Ready | Not Ready | Blocked
Assessment snapshot: <identity and observation time>

## Scope and Authority
- Change boundary: ...
- Governing accepted sources: ...
- Current-state evidence: ...
- Material drift or provenance limits: ...

## Readiness Summary
<Why implementation can or cannot begin; calibrate to risk.>

## Coverage
| Obligation or source ID | Evidence | Planned work | Verification method | Status |
| --- | --- | --- | --- | --- |

Use `Covered`, `Gap`, `Accepted risk`, or `Not applicable` for status.

## Findings
### R1 — <finding>
- Classification: Blocker | Accepted risk | Advisory
- Routes: <one or more of: Needs acceptance | Needs research | Needs design | Needs specification | Needs planning>
- Affected scope: ...
- Evidence: ...
- Consequence: ...
- Smallest next action: ...
- Acceptance authority and rationale: <accepted risks only>

## Conditions Checked
<Relevant behavioral, technical, security, migration, operational, and delivery
conditions; explain material omissions rather than reproducing a checklist.>

## Handoff
<Unblocking evidence, preserved accepted scope, and the exact point at which a
new assessment can resume.>
```
