# Behavioral evaluation cases

The machine-readable authority is `evals.json`. Run each case in a fresh,
disposable context with the Gen Stack knowledge support path. The suite covers
explicit selection, implicit abstention, stage-specific happy and boundary
execution, read-only focused reviewer delegation, action disposition, stale
claim re-review, unavailable-freshness fallback, and forbidden side effects.
Missing side-effect evidence is `unknown`, never an inferred pass.
