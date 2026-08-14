# Consecutive cases

1. Invoke `author-agent-skill`: create a skill from the repeated library workflow
   in the fixture. Do not install or publish it.
2. Invoke `evaluate-agent-skill`: evaluate the resulting exact revision on the
   available host, including implicit routing and explicit execution.
3. Invoke `audit-agent-skill`: audit the same package for internal use. Begin
   statically and do not execute package code.
4. Invoke `admit-agent-skill`: decide whether the exact candidate should enter
   the engineering cohort using the accumulated evidence and governance
   supplement. Do not modify or publish it.
5. Invoke `govern-agent-skill-library`: assess the bounded catalog snapshot in
   the governance supplement and route its findings without mutating the library.
6. Without explicit invocation: design the overall agent harness configuration,
   context budget, tool policy, and observability for this library workflow.
