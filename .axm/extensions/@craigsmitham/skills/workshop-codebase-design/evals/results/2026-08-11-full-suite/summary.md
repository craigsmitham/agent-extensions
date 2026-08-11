# Full forward evaluation: 2026-08-11

Evaluated all 14 cases from `evals/evals.json` in separate fresh Codex
collaboration-subagent contexts. Each run received only the case prompt and an
isolated copy of `src/`; expected outputs and assertions were withheld. The
parent agent graded each raw response after completion.

- Tested `src/` SHA-256: `6fa0f6007b293809ddde43359963d17d27e98de3e5843dac880e9119e49bf05c`
- Hash construction: SHA-256 over the sorted relative path and SHA-256 digest of
  every file in `src/`
- Runtime: Codex collaboration subagents
- Model: Inherited session model; exact public identifier unavailable
- Resources: `SKILL.md` and `references/codebase-design-record.md` were available;
  case 14 read the record reference
- State changed by case runs: None

| Case | Assertions passed |
| --- | ---: |
| 1. Relevant research-to-design drift | 4/4 |
| 2. Irrelevant research-to-design drift | 4/4 |
| 3. Snapshot changes before acceptance | 4/4 |
| 4. Functional ambiguity blocks an otherwise complete design | 4/4 |
| 5. Direct evidence without Git or a research report | 4/4 |
| 6. One consequential decision at a time | 4/4 |
| 7. Design request that also asks for implementation planning | 5/5 |
| 8. No consequential design choice | 3/3 |
| 9. Discover technical decisions without a supplied agenda | 4/4 |
| 10. Technical incompleteness blocks design acceptance | 4/4 |
| 11. Do not manufacture technical alternatives | 4/4 |
| 12. Authorization boundary and stakeholder visibility | 5/5 |
| 13. Missing operational objective remains a decision | 5/5 |
| 14. Finalize a complete accepted design record | 5/5 |
| **Total** | **59/59** |

The preserved diagnostics document two material corrections found before the
final run:

1. An unresolved observer-visible behavior received only a `D<n>` decision ID,
   so the skill now requires a corresponding `B<n>` behavior ID.
2. A drift-blocked response preserved the new snapshot but left its validation
   time implicit, so the skill now requires both identity and time whenever
   later acceptance depends on revalidation.

The final run establishes directional behavioral coverage for this exact source
identity. It is not a statistical reliability claim, and the exact underlying
model build was not exposed by the runtime.
