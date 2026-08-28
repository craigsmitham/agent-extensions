# Behavioral evaluation cases

The machine-readable authority is `evals.json`. Run each case in a fresh,
disposable context. The suite verifies that the deprecated compatibility skill
provides a bounded migration route to `$spec` followed by `$design`, never
activates either replacement, and is not selected from unprefixed language.
