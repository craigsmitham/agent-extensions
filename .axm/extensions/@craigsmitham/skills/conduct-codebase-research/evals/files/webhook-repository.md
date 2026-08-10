# Synthetic webhook repository

The checked-out repository is `w200`. `webhooks/accept.ts` persists a delivery
and enqueues it; `webhooks/worker.ts` calls the partner and records latency and
terminal status. Tests establish the current control flow and timeout behavior.
A fixture trace at `w200` shows queue latency below one second and partner
response latency of 45 seconds. No incident commit, deployment, dependency
version, trace, or observation time was supplied, and history cannot identify
which environment produced the report.
