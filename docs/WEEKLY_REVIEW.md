# Weekly knowledge checks

The Knowledge safety check workflow runs a read-only review-queue maintenance job every Monday at 00:17 UTC (09:17 JST). GitHub may delay scheduled delivery.

## What the workflow does

On `schedule`, `push`, `pull_request`, and `workflow_dispatch`, the workflow:

1. runs the repository unit tests;
2. runs the existing Schema and automated safety scan;
3. produces a read-only Review Queue summary for `docs/proposals/**/*.md`;
4. never calls an AI model, adopts candidates, commits files, writes repository data, or changes review status.

The workflow uses the standard GitHub-hosted `ubuntu-latest` runner, read-only contents permission and a five-minute job timeout.

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

The weekly machine check does not replace independent AI review and does not automatically promote any candidate.
