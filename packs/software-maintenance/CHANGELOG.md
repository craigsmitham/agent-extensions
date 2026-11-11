# Changelog

## 0.2.0

Reorganizes the pack around continuing maintenance: prioritization, dependable
behavior and feedback, support lifecycles, removal, simplification, independent
change, and selected quality improvements.

- Adds `assess`, `stabilize`, `refresh`, and `simplify` at 0.1.0.
- Retains `prune`, `modularize`, and `improve`, requiring their strengthened
  0.2.0 contracts.
- Removes `align`, `reconcile`, `reuse`, and `generalize` from pack membership.
  Those packages remain available independently; their 0.1.1 releases update
  companion documentation, recommendations, and opportunity-question handling
  without changing their purpose.
- Adds conditional sequencing, recurring-maintenance guidance, and examples
  distinguishing opportunity questions from implementation requests.
- Preserves standalone installation and explicit-only invocation for every member.

### Retaining former members

Declare any former member you still need directly before updating the pack:

```bash
axm install @craigsmitham/skills/align
axm install @craigsmitham/skills/reconcile
axm install @craigsmitham/skills/reuse
axm install @craigsmitham/skills/generalize
axm update @craigsmitham/packs/software-maintenance
```

Install only the companions you intend to retain. Direct selections are
independent of membership; inspect the update preview for the actual removal
and retention plan in your workspace. Pack-only consumers should expect the
new seven-member set after updating. Version 0.1.0 remains a historical release.

## 0.1.0

Initial seven-member pack: `align`, `reconcile`, `modularize`, `generalize`,
`reuse`, `prune`, and `improve`.
