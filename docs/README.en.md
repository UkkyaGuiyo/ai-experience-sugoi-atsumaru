# AI Experience Sugoi Atsumaru
*AIの経験がスゴーイアツマール — a reusable knowledge base of practical AI experience*

**Language:** English (this page) | [日本語 README](../README.md) | [Contribution guide in English](CONTRIBUTING.en.md)

> **Collect experiences, not people.**
>
> **Never store personal or re-identifiable information, confidential information, or material that creates rights, contractual, or legal risks. No exceptions.**

## What is this?

AI Experience Sugoi Atsumaru collects **reusable lessons about working with AI**, including successes, failures, experiments, corrections, prompts, tool use, agent operations, human–AI collaboration, workflows, and anti-patterns. It is **not limited to programming**: research, writing, creative work, office tasks, data analysis, verification, and other domains are welcome when the insight can be safely generalized.

The intended transformation is:

**Experience → Analysis → Generalization → Reusable Knowledge**

This is **not** a repository of people, private projects, chat histories, raw prompts, logs, or screenshots. A project-derived lesson may be eligible, but only if it stands on its own without exposing or allowing reconstruction of the original person, organization, project, or private source.

## Find and reuse knowledge

1. **Browse [`knowledge/`](../knowledge/).** Approved knowledge is stored as JSON under category directories: `agents/`, `anti-patterns/`, `case-studies/`, `experiments/`, `failures/`, `patterns/`, `prompts/`, `successes/`, `tools/`, and `workflows/`. Some categories may be empty. You can also use GitHub's repository file finder or code search for a task, technique, or `EXP-000001`-style ID.
2. **Check the scope before applying a lesson.** Read `goal`, `approach`, `improved_method`, `when_to_use`, `when_not_to_use`, and `known_limitations`. Look at `task_type` and `environment` to determine whether your situation is comparable.
3. **Check the evidence, not just the title.** `evidence_type` distinguishes direct or repeated experiments, documentation, research, generalized community reports, and inference. `reproduction_status`, `confidence`, `observation_date`, and known `model` / `tool_version` qualify the claim. `knowledge_status: historical` means the information must not be presented as a current capability without revalidation. Neither a high-confidence label nor an approved entry establishes universal truth.
4. **Adapt responsibly.** Verify applicability in your own environment, respect the content license, and do not infer that untested conditions were tested.

The authoritative format is [`schema/experience-entry.schema.json`](../schema/experience-entry.schema.json); see the [knowledge model](KNOWLEDGE_MODEL.md) and [entry-writing guide](../templates/EXPERIENCE_ENTRY.md).

## Approved knowledge vs. review candidates

| Location | Status | How to treat it |
| --- | --- | --- |
| [`knowledge/**/*.json`](../knowledge/) | **Formal Knowledge Entry** | JSON entries admitted through the required review and validation process; inspect each entry's evidence and limits. |
| [`docs/proposals/`](proposals/) | **Review candidates, not adopted knowledge** | Generalized ideas awaiting candidate-level technical, safety, rights, evidence, and duplicate review. Publication in GitHub does **not** mean approval. |
| [`docs/reviews/`](reviews/) | Review records and consolidation proposals | Records the scope of reviews, explicit adoption decisions, and remaining gates. Read each record's limits; a remediation or consolidation proposal alone is **not** formal adoption. |

**Snapshot — 2026-10-09:** There are **75 formal Knowledge Entries** (12 existing entries plus 63 newly admitted entries following the owner's explicit adoption instruction). Of the 20 engineering candidates, 15 were admitted; of the 72 migrated legacy candidates, 48 were admitted. **29 candidates remain unadopted**: 10 overlapping candidates awaiting duplicate/consolidation decisions and 19 repaired candidates still requiring individual admission approval. They remain in `docs/proposals/` and must not be treated as formal knowledge. Counts are a dated snapshot; inspect the JSON entries and candidate-level dispositions for later changes.

See the [63-entry formalization and independent content-review record](reviews/2026-10-09-63-knowledge-formalization.md) for the adopted IDs (`EXP-000013`–`EXP-000075`), provenance, evidence, and limitations. The 15 new generalized entries are `inference / not reproduced / low`; the 48 legacy-derived entries are `historical`, and all 63 are `not reproduced / low` for this registration. No original experiment was rerun during admission. Their `observation_date` of 2026-10-09 is the knowledge-conversion/review date, not a new measurement or the date of the original event.

The review record states that the content reviewer was separate from the original candidate author, but also performed JSON conversion and writing. **A further review of the converted 63 JSON entries by another model was not performed.** Do not present the record as that additional approval, or as independent approval of this English-documentation PR.

The original proposal narratives and historical triage/remediation records are retained. The two mixed batches still contain 20 and 72 narratives respectively, including adopted items, and remain `PENDING_REVIEW` at document level while unresolved candidates remain. **92 retained narratives does not mean 92 pending candidates.** Use candidate-level dispositions and the formal JSON IDs, rather than document counts, to determine adoption.

A proposal document's `Review status: PENDING_REVIEW` is not interchangeable with a formal entry's `safety_review` approval. The [weekly review rules](WEEKLY_REVIEW.md) distinguish proposal disposition from adoption. Automated queue summaries never promote candidates.

## Safety is a release requirement

Before creating **any repository file or public GitHub artifact**, remove information that must not be published. This includes:

- Direct or indirect personal identifiers and combinations that allow re-identification; identifying handles, addresses, personal links, locations, and unique project details.
- Credentials, tokens, secrets, private repositories or source material, confidential or NDA-covered data.
- Raw conversations, prompt histories, emails, logs, screenshots, user-provided data, or source artifacts.
- Content you cannot lawfully store, redistribute, or license: unpermitted code or quotations, copyright- or contract-restricted material, or material with unresolved rights.

**Removing a name is not sufficient anonymization.** Generalize and minimize *before* creating a branch, commit, Issue, PR, review comment, or workflow output. Public GitHub history, forks, and caches may retain data even after deletion. Do not use Draft PRs or non-default branches as a confidentiality mechanism.

When safety or rights cannot be established, **do not submit or store the material**. Read the binding [root AI/work rules](../AGENTS.md), [privacy rules](PRIVACY_RULES.md), [collection policy](COLLECTION_POLICY.md), [source policy](SOURCE_POLICY.md), and [security reporting instructions](../SECURITY.md). This English introduction adds no exceptions or weaker conditions.

**Automated validation != privacy guarantee.** Passing CI is never a substitute for the mandatory independent Safety Review or the required technical/rights review.

## Contribute safely

Start with the [English contribution guide](CONTRIBUTING.en.md). In brief: generalize an experience without uploading raw material, complete a pre-file Safety Review, use the existing proposal and JSON formats appropriately, run validation and tests, and obtain independent review before formal adoption. Do not mark `independent_review` or other approval fields as complete before they truly are.

To run the repository's checks locally, without creating Python bytecode/cache files:

```sh
python -B scripts/validate_knowledge.py
python -B -m unittest discover -s tests -v
```

GitHub Actions also performs schema checks, automated safety scanning, unit tests, and read-only proposal-queue summaries. The scheduled review-queue run does **not** automatically invoke an AI agent, accept candidates, or change repository files. See [weekly review behavior](WEEKLY_REVIEW.md).

Bulk retrospective collection or migration from older projects, archives, or conversations requires **explicit authorization of the specific scope**, and follows the [migration policy](MIGRATION_POLICY.md); it is not implied by ordinary permission to submit newly generalized experience.

## Reuse and licensing

This repository distinguishes written content from executable tooling:

- **Knowledge, documentation, and other written content:** [CC BY 4.0](../LICENSE-CONTENT). Sharing, adaptation, and commercial reuse are permitted subject to the license. Provide attribution, a license link, and an indication of changes as required.
- **Software, validators, schemas, tests, and workflow code:** [MIT License](../LICENSE-CODE). Preserve the required copyright and license notice.

See the authoritative [repository license scope](../LICENSE). Third-party material retains its own rights; inclusion or a link does **not** relicense it or guarantee permission to reuse it.

## Where to read next

[Contributing in English](CONTRIBUTING.en.md) · [Knowledge model](KNOWLEDGE_MODEL.md) · [Privacy rules](PRIVACY_RULES.md) · [Source policy](SOURCE_POLICY.md) · [Security reporting](../SECURITY.md) · [日本語 README](../README.md)
