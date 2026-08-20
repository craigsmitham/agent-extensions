# Behavioral evaluation cases

Run each prompt in a fresh agent context with only the `question` skill. Do not
provide the expected output or assertions to the test agent. `evals.json` is
the machine-readable authority.

The cases cover opportunity framing, isolation of originating hypotheses,
balanced evaluation of a policy claim, caller-supplied question limits, and the
boundary between framing and conducting research.

The suite passes when the skill selects concerns from the nature and intended
use of the subject, returns a compact Research Brief with stable question IDs,
identifies required evidence without answering, and never labels a same-context
result as blind.
