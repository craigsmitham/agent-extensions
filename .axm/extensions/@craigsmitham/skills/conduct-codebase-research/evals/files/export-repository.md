# Synthetic export repository

At `c333`, `api/export.ts::startExport` validates the request, creates an
`ExportJob`, and enqueues its ID. `worker/export.ts::runExport` moves the job
through `queued -> running -> completed|failed`; it writes the object before the
terminal transition. Tests cover success, object-store failure, and duplicate
worker delivery. Worker image 3.4 is current.

Between `b222` and `c333`, commit `c010` made `running` durable before the object
write and added recovery for jobs left in `running`. At `a111`, the transition
was in memory until the write completed. The supplied synthetic reproduction at
`c333` with an object-store timeout recovers and completes; no runtime evidence
from the partner environment at `a111` is available.
