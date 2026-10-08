# Weekly knowledge checks

The Knowledge safety check workflow contains the weekly review-queue logic, but the scheduled trigger is intentionally **disabled** on the default branch until the owner confirms an effective no-overage / no-charge condition for private GitHub Actions.

The intended cadence, once explicitly enabled, is Monday 00:17 UTC (09:17 JST). GitHub may delay scheduled delivery. Enabling that cron is a billing/operations decision, not a knowledge-review decision.

## What is integrated now

On `push`, `pull_request`, and `workflow_dispatch`, the existing workflow:

1. runs the repository unit tests;
2. runs the existing Schema and automated safety scan;
3. produces a read-only Review Queue summary for `docs/proposals/**/*.md`;
4. never calls an AI model, adopts candidates, commits files, writes artifacts/caches, or changes repository data.

The workflow uses a standard Linux runner, read-only contents permission and a five-minute job timeout. Runner startup still consumes Actions usage.

Formal Knowledge is stored only as `knowledge/**/*.json` and is checked by the existing entry schema. Proposal Markdown is scanned for repository safety but is not a formal Knowledge Entry.

## Current integrated queue

The default branch contains 12 formal Knowledge Entries. The historical A〜I proposal document has full disposition: eight candidates were formalized as EXP-000005〜EXP-000012 and one was excluded as substantially overlapping EXP-000003. That proposal is marked `Review status: FORMALIZED`.

The engineering-lessons batch contains 20 generalized candidates and remains `PENDING_REVIEW`. Its files stay outside `knowledge/`; machine PASS must not be treated as independent AI review or adoption.

## Review status convention

An explicit standalone line before the first `##` section controls document-level queue disposition:

- `Review status: REVIEWED`
- `Review status: REJECTED`
- `Review status: FORMALIZED`
- anything else, no line, or conflicting lines => pending.

For mixed batches, do not mark the document resolved until every candidate has a disposition. Prose, referenced EXP IDs, CI PASS or safety-scan PASS never sets review status automatically.

## Duplicate hints

The queue summary may show possible overlap using existing EXP-ID references or heading/title string similarity. This is only a review hint. No detected overlap does not prove uniqueness. Prefer improving or qualifying an existing Entry over creating a near-duplicate.

## Independent review

Machine PASS is not privacy/safety approval. Pending candidates require an independent reviewer for safety, rights, generalization, evidence level, limitations and duplicate/consolidation decisions before formalization.

Preferred normal reviewer: GPT-6.1 Sol. GPT-6 Astra is not the default reviewer. Candidate collection must not block product work.

## Enabling the weekly schedule later

Before adding the cron trigger to the default branch, confirm the private Actions allowance and an effective stop-spending / no-overage condition in GitHub billing. This repository remains PRIVATE; this workflow does not change billing, budgets, visibility, license, merge policy or publication state.

Target schedule when approved:

```yaml
schedule:
  - cron: '17 0 * * 1' # Monday 00:17 UTC / 09:17 JST
```

References: GitHub scheduled events and job summaries documentation.
