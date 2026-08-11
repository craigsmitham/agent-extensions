# Verify Codebase Change

Verify an implemented codebase change against its accepted contract, applicable
repository obligations, and a named implementation snapshot using reproducible
evidence.

The skill traces obligations to code and checks, separates contract conformance
from outcome validation, treats implementation plans as supporting rather than
normative, and reports `Verified`, `Not Verified`, or `Blocked` without modifying
the implementation.

Use it after implementation when an accepted change contract and identifiable
implementation snapshot are available. It is not a substitute for ordinary code
review, pre-implementation readiness assessment, deployment validation without a
contract, or implementation and remediation work.

Install it with:

```sh
axm install @craigsmitham/skills/verify-codebase-change
```

For example:

> Verify the completed retry-policy change against the accepted specification at
> commit `abc123`, including repository checks and the supplied rollout evidence.
