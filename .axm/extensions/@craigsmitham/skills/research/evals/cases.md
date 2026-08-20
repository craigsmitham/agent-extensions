# Behavioral evaluation cases

Run each prompt in a fresh agent context with only the `research` skill and the
read-only research tools available to that host. Do not provide expected output
or assertions to the test agent. `evals.json` is the machine-readable authority.

The cases cover a multi-question brief, a paraphrased empirical policy question,
an incomplete blind brief, a hard research cap, and the adjacent question-
framing boundary.

The suite passes when reports preserve question identity, use the stable report
contract, support material claims with traceable evidence, expose conflict and
uncertainty, respect decision authority and research limits, and refuse to
invent a missing frame.
