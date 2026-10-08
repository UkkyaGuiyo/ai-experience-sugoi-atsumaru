# Weekly knowledge checks

The existing Knowledge safety check workflow also has a weekly schedule:
Monday 00:17 UTC (09:17 JST). This is approximate; GitHub can delay scheduled runs.
It uses a standard Linux runner, read-only contents permission and a five-minute
job timeout. The existing schema, validator, safety scan and unit tests are reused.

The Actions run summary reports check outcomes and lists existing Markdown
documents under `docs/proposals/` recursively that are still `PENDING_REVIEW`. A document can
contain multiple candidates; this is a document queue, not a count of lessons.
Proposal Markdown receives the existing repository safety scan, not the JSON
entry schema check. Only `knowledge/**/*.json` are checked as formal entries.
No new candidate schema or stored state is introduced.

An explicit standalone `Review status: REVIEWED`, `Review status: REJECTED`, or
`Review status: FORMALIZED` line before the first `##` section removes that whole
document from the pending queue. A reviewer/maintainer sets this line only after
the corresponding independent review or disposition, referring to the existing
review record where available. For mixed batches, leave the document pending
until every candidate has a disposition. No line, an unknown status, conflicting
lines, or `Review status: PENDING_REVIEW` stays pending. Prose, entry references
and machine PASS never set review status automatically. This is a small explicit
Markdown convention, not a new entry schema or review framework.

Existing historical review records are in `docs/reviews/` on other work branches;
for example `generalized-workflow-eight-entries.md` records eight adopted
candidates and one excluded duplicate. Those records are not on this workflow's
base/default branch and are not automatically imported or interpreted. That
branch currently has zero formal Knowledge entries; twelve entries on the
curation branch are a separate integration decision.

Possible overlap with checked-out Knowledge is extracted from existing entry ID
references and proposal heading / entry title similarity (threshold 0.8). These
are review hints, not semantic duplicate decisions. No detected overlap does not
prove uniqueness. Other branches are not read or imported by the workflow.

If the scan fails, proposal details are withheld and the job still fails. No
candidates means a successful no-op for review collection; runner startup and
checks still consume Actions usage. Nothing is committed or adopted. There are
no AI calls, extra credentials, paid services, artifacts or caches.

Machine PASS is not safety approval. Without an independent reviewer, proposals
remain `PENDING_REVIEW`, not a failure. Prefer batch review with GPT-6.1 Sol;
GPT-6 Astra is not the normal reviewer. Before adopting a candidate, independently
check safety, rights, generalization and evidence, prefer improving or qualifying
an existing entry over a near-duplicate, then follow the existing entry schema
and approved contribution process. Storage still requires the existing pre-save
safety check; pending status never permits private or raw material.

## Activation is on hold

Keep this change on its work branch until the owner confirms no-charge
conditions. GitHub schedules execute only from the default branch; pushing this
work branch runs existing push CI but does not enable the weekly schedule.
The repository must stay private. Private Actions usage is free only within the
owner's remaining included allowance. Payment settings and stop-spending budgets
have not been verified, so zero charges cannot be guaranteed, even for no-op runs.

Before applying to the default branch, the owner should confirm the remaining
allowance and an effective no-overage / stop-spending condition for Actions in
GitHub billing settings, then explicitly approve default-branch integration.
This implementation does not change billing, budgets, visibility or the default
branch. No merge or schedule activation is authorized by a validator PASS.

References: [scheduled events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule),
[job summaries](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#adding-a-job-summary).
