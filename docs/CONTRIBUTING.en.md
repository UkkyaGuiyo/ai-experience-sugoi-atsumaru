# Contributing to AI Experience Sugoi Atsumaru

**Language:** English (this page) | [日本語 Contribution手順](../CONTRIBUTING.md) | [English README](README.en.md)

Thank you for helping turn AI experiences into reusable knowledge. Contributions may concern coding, research, writing, creative tasks, agents, prompting, tools, verification, or other fields.

**Safety is mandatory; collecting more knowledge is optional.** The [root `AGENTS.md`](../AGENTS.md), [privacy rules](PRIVACY_RULES.md), [collection policy](COLLECTION_POLICY.md), [source policy](SOURCE_POLICY.md), and [migration policy](MIGRATION_POLICY.md) govern all work. This English guide is an explanation, **not permission to relax those rules**. If any requirement is unclear, do not publish the material until it is resolved. Do not choose a less protective interpretation.

## 1. Non-negotiable restrictions

**Do not submit, store, or reproduce any of the following**, including in proposals, Issues, Pull Requests, comments, branch names, commit messages, CI output, or review notes:

- Personal identifiers or combinations that can identify or re-identify a person; personal handles, contact details, identifying locations, organizations, project names, personal URLs, or unique circumstances.
- Passwords, API keys, tokens, cookies, credentials, private keys, secrets, private repositories, confidential/private information, NDA-covered material, or unpublished business information.
- Raw transcripts, full prompts or prompt histories, emails, logs, screenshots, user-provided personal data, private source code, or raw project artifacts.
- Text, code, images, or other information that cannot be lawfully stored, published, or redistributed because of copyright, license, contractual, confidentiality, or other legal restrictions.

Deleting names alone does **not** make an item anonymous. Consider combinations of seemingly harmless metadata, including dates, software versions, unusual environments, and descriptions of events. Remove the original identifying context and keep only the **minimum generalized conditions and lesson** necessary for reuse.

**Perform a Safety Review before creating a file or public GitHub artifact**, not only before merging. If you cannot establish privacy, confidentiality, redistribution rights, or legal safety, **do not store or submit the material**. A Draft PR, private branch name, later deletion, or reverted commit does not protect it from Git history or external copies.

## 2. Decide what kind of contribution you have

| Material | Appropriate route | What it does **not** mean |
| --- | --- | --- |
| Newly observed, safely generalized AI experience | Use the ordinary contribution flow below; draft a candidate for independent review | New experience alone is not approval |
| A review candidate not yet independently approved | Keep it in the maintainer-approved proposal area under [`docs/proposals/`](proposals/), as generalized Markdown | It is **not** a formal Knowledge Entry |
| A candidate independently cleared for formal admission | Prepare validated JSON under [`knowledge/<category>/`](../knowledge/) in the established format, with genuinely completed approvals | A generated `approved` flag cannot substitute for a review |
| Retrospective bulk extraction or transfer of older repositories, lessons, projects, or chats | Obtain **explicit authorization for the specific migration scope** first, then follow [Migration Policy](MIGRATION_POLICY.md) | Ordinary contribution permission is not blanket backfill approval |

The current [English README](README.en.md) explains the difference between formal entries and pending candidates. A candidate's presence in `docs/proposals/`, a repaired draft, a duplicate-consolidation plan, or a passing CI run is **not** formal adoption.

You may submit generalized English-language explanations for review; keep machine-readable schema property names and required formats unchanged.

## 3. Turn an experience into a safe lesson

Before writing anything to GitHub:

1. **Extract the lesson locally:** identify the general goal, relevant conditions, method, observation, failure or success, explanation, improvement, applicability, and limitations.
2. **Generalize:** replace identifying entities, project-specific behavior, unique timestamps or paths, and any confidential technical details with conditions that stand alone. Do not import or attach raw source material.
3. **Minimize:** remove details not needed to understand or apply the lesson. Check whether combinations of retained details permit re-identification or reconstruction.
4. **Check sources and rights:** confirm that every retained claim and optional reference is safe to publish and that submitted content is yours or properly authorized. Public availability is not redistribution permission. Never copy large blocks of external text or code.
5. **Conduct the pre-file Safety Review:** check identifiers, indirect identification, secrets, private sources, rights, licenses, contracts, law, and necessity. If any check is uncertain, do not create the file; generalize further or abandon the submission.

Use entirely **synthetic** data for illustrative tests. Do not use a real secret to test the scanner. If evidence cannot be retained safely, do not invent a replacement or misrepresent inference as a verified result.

## 4. Proposals, evidence, and formal JSON entries

### Pending proposals

Follow the existing proposal organization and coordinate its placement with maintainers. The repository's review queue reads Markdown under `docs/proposals/`. An unresolved standalone proposal document uses the status line below, placed **before its first level-2 heading**:

```md
# Proposed generalized lesson

Review status: PENDING_REVIEW

## Generalized problem
...
```

A proposal must already satisfy all publication-safety requirements. The marker is **not** permission to expose unreviewed sensitive content; it means the candidate has **not** completed independent review for adoption.

Review status markers (`REVIEWED`, `REJECTED`, `FORMALIZED`) describe document-level disposition under [weekly review rules](WEEKLY_REVIEW.md). Do not set a mixed batch to resolved until **every** candidate has a disposition; none of these markers automatically generates or approves a formal JSON entry.

### Formal Knowledge Entries

Only after genuine independent technical, rights, and Safety Review should an entry be admitted to `knowledge/`. Follow the [writing guide](../templates/EXPERIENCE_ENTRY.md), the [knowledge model](KNOWLEDGE_MODEL.md), and the authoritative [JSON schema](../schema/experience-entry.schema.json):

- Use `EXP-` followed by six digits for the entry ID; use an appropriate existing category directory.
- State `goal`, `approach`, results, `why`, `improved_method`, `when_to_use`, `when_not_to_use`, and `known_limitations` without overstating what was observed.
- Distinguish `evidence_type` (for example, `direct experiment` versus `inference`), `reproduction_status` (`reproduced` or `not reproduced`), and `confidence` (`low`, `medium`, or `high`).
- Record `observation_date` as a truthful, safe ISO date. Do **not** invent dates, model names, tool versions, reproductions, test results, or source evidence. If a mandatory field cannot truthfully and safely be provided, defer formal admission.
- Mark `knowledge_status` as `current` or `historical` according to the evidence and time scope. A historical result is not proof of current capability.
- In `safety_review`, the required `status: approved` and boolean fields (`independent_review`, `data_minimization`, `no_identifiers`, `no_private_data`, `rights_checked`) must reflect **reviews actually performed**. Never fill them with approval values just to pass schema validation.
- Only permitted optional source references are independently safety-reviewed official documentation or public research, with safe HTTPS URLs free of credentials, query strings, fragments, IP addresses, or identifying details. Do not cite individual social profiles or community posts by personal URL or handle.
- For `failures`, include the schema's required `failure_details` fields. Do not add personal or original-project traceability fields.

## 5. Validate and request independent review

Run the standard checks from the repository root:

```sh
python -B scripts/validate_knowledge.py
python -B -m unittest discover -s tests -v
```

Use `-B` (or `PYTHONDONTWRITEBYTECODE`) to avoid generating Python bytecode/cache files that the repository-wide safety scan will inspect. GitHub Actions runs schema validation, automated safety checks, tests, and read-only proposal-queue reporting.

Then submit a **sanitized** Pull Request using the existing [PR checklist](../.github/pull_request_template.md). Briefly describe the generalized change, its evidence and limits, where it belongs, and which checks were *actually* run. Do not copy prohibited source text into PR descriptions or reviewer discussions.

An **independent reviewer**, separate from the author/implementer, must assess at least privacy and re-identification, source/rights and legal constraints, minimization, technical accuracy, evidence and reproducibility claims, applicability, schema compliance, and duplication or consolidation against existing entries and candidates. The required Safety Review cannot be self-certified by toggling JSON fields.

If revisions are required, revise the safe generalized material and rerun the checks. Follow the repository's approved review and merge process. **CI PASS is necessary but is never independent privacy approval, rights clearance, or permission to adopt.** Neither scheduled checks nor an ordinary PR automatically formalize a candidate.

Do **not** bypass warnings by disabling validation, adding broad allowlists, or excluding directories from scanning. Any justified narrow detector fix needs synthetic regression tests and separate review.

## 6. Security problems and uncertain material

If you encounter a possible credential, identifying information, or sensitive source, **stop normal publication and review**. Do not quote the value, paste it into a public Issue/PR/comment, or try to "fix" exposure by only deleting a tracked file. Refer to [`SECURITY.md`](../SECURITY.md) for private vulnerability reporting through GitHub's **Report a vulnerability** when available. If no safe private channel is available, do not transmit the sensitive details.

## 7. Contribution licensing

Only contribute material you have the right to submit. Repository [`LICENSE`](../LICENSE) determines scope:

- Knowledge, proposals, documentation, templates, and other written content in the covered paths: **CC BY 4.0**, [full notice](../LICENSE-CONTENT).
- Software, tests, validators, schemas, and workflow code in the covered paths: **MIT License**, [full notice](../LICENSE-CODE).

Accepted contributions are distributed under the license applicable to their destination. Third-party material is **not** relicensed just because it is mentioned or linked. License compatibility does not waive privacy, safety, source, independent-review, or legal requirements.

**Final check before submitting:** Is the lesson reusable without its original person, organization, or project? Can every field be published and redistributed safely? Are claims and approvals truthful? If any answer is uncertain, do not publish.
