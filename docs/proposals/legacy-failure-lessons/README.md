# Legacy failure lessons migration

Review status: PENDING_REVIEW

A retired, lower-level failure-lesson knowledge base contained **72 generalized Lessons**. All 72 reusable lesson bodies have been migrated into this Atsumaru proposal batch as `LFA-001` through `LFA-072`.

This migration preserves each source Lesson's core intent, failure, assumptions, root-cause evidence, correction, verification and reusable rule. Applicable scope and essential diagnostic notes have been reconciled where omissions were found; incidental historical notes are not copied verbatim. The original confirmed label remains historical evidence, not approval by Atsumaru. The old repository's operational manuals, agent handoff instructions, templates, index machinery and validator are **not** migrated as Knowledge because Atsumaru supersedes those mechanisms.

The source repository had already generalized/anonymized these Lessons and marked them confirmed. That status is retained only as source provenance. It does **not** satisfy Atsumaru's independent-review requirement. Every migrated candidate remains `PENDING_REVIEW` until an independent reviewer checks technical generalization, safety/rights, evidence level, limitations, and overlap with the 12 formal Knowledge Entries plus other pending proposal batches.

## Review and remediation (2026-10-09)

A per-candidate comparison against the original generalized Lessons found 14 missing Applicability sections, two truncated GZip explanations and one missing bounded Material diagnostic note. These passages have been restored or generalized from the source Lessons in the existing five batches. Three mixed-evidence candidates now explicitly separate verified and unresolved routes. **All 72 IDs remain in the pending proposal archive, not in formal Knowledge.**

[Scoped remediation audit](../../reviews/2026-10-09-candidate-remediation.md) / [10 candidate overlaps consolidated into seven reviewed rule proposals](../../reviews/2026-10-09-consolidated-candidates.md).

## Migration completeness gate

- Source generalized Lessons counted: **72**
- Migrated candidate IDs found: **72**
- Missing IDs: **0**
- Duplicate migration IDs: **0**
- Raw conversations/logs/screenshots/project repositories: not intentionally migrated
- Source repository operational/template files: intentionally excluded
- Formal Knowledge Entries created by this migration: **0**

The retired source repository may be deleted only after this batch is saved on GitHub, repository safety checks pass, and the remote tree is read back with all 72 IDs present. Deletion is a repository-retirement action, not evidence that all 72 candidates were independently reviewed or formalized.

## Batches

- [Batch 01](batch-01.md): LFA-001–LFA-015
- [Batch 02](batch-02.md): LFA-016–LFA-030
- [Batch 03](batch-03.md): LFA-031–LFA-045
- [Batch 04](batch-04.md): LFA-046–LFA-060
- [Batch 05](batch-05.md): LFA-061–LFA-072

## Candidate map

| ID | Generalized lesson | Batch |
| --- | --- | --- |
| LFA-001 | An archive extension does not prove a regular file | batch-01.md |
| LFA-002 | Separate callback execution from effective target fidelity | batch-01.md |
| LFA-003 | Explicit triangles still need destination importer controls | batch-01.md |
| LFA-004 | Use a same-input short-path control before blaming content | batch-01.md |
| LFA-005 | Unity GPU render tests require a graphics device | batch-01.md |
| LFA-006 | Do not defer hierarchy identity repair beyond an EditMode test frame | batch-01.md |
| LFA-007 | Wait for a Unity Editor process to release its project before relaunch | batch-01.md |
| LFA-008 | Avoid mirroring stale generated assets into Unity verification projects | batch-01.md |
| LFA-009 | Separate movement intent from attack facing | batch-01.md |
| LFA-010 | Animation addresses must be unique in the target scheme | batch-01.md |
| LFA-011 | Asset rollback must restore metadata identity | batch-01.md |
| LFA-012 | Coordinate basis conversion must include scale | batch-01.md |
| LFA-013 | Dependency identity must include the binding role | batch-01.md |
| LFA-014 | Verify the committed artifact in a clean checkout | batch-01.md |
| LFA-015 | Compiled component types still need resolvable script assets | batch-01.md |
| LFA-016 | A created version is not the live deployment target | batch-02.md |
| LFA-017 | Distinguish explicit null from malformed references | batch-02.md |
| LFA-018 | Verify identifiers after serialization and import | batch-02.md |
| LFA-019 | Declare external references and inspect every provider kind | batch-02.md |
| LFA-020 | Validate helper handles and bound response waits | batch-02.md |
| LFA-021 | Hierarchy enumeration must include nonvisual occurrences | batch-02.md |
| LFA-022 | A local flag does not release a host modal handler | batch-02.md |
| LFA-023 | Inspect workflow body and file outputs separately | batch-02.md |
| LFA-024 | Isolate template expansion before changing encodings | batch-02.md |
| LFA-025 | Use invariant node types and verify the active render path | batch-02.md |
| LFA-026 | Reapplication must prove that managed state is still owned | batch-02.md |
| LFA-027 | Mandatory evidence retrieval must be enforced by control flow | batch-02.md |
| LFA-028 | Material slot numbers do not prove face assignment | batch-02.md |
| LFA-029 | Matching transforms do not prove evaluated geometry | batch-02.md |
| LFA-030 | Parse numbers together with their units | batch-02.md |
| LFA-031 | Monotonic timestamps may lack sufficient resolution | batch-03.md |
| LFA-032 | A neutral mean does not prove stable return | batch-03.md |
| LFA-033 | Supervise the whole native lifecycle outside the child | batch-03.md |
| LFA-034 | Do not parse language representations as JSON | batch-03.md |
| LFA-035 | Preserve scheduler phase after delayed wakes | batch-03.md |
| LFA-036 | A reset instruction is not conversation isolation | batch-03.md |
| LFA-037 | Rollback must reverse executed mutations only | batch-03.md |
| LFA-038 | Verify fields across the actual serialized payload | batch-03.md |
| LFA-039 | A zero SDK version can mean its query failed | batch-03.md |
| LFA-040 | A search label does not prove result category | batch-03.md |
| LFA-041 | Serialize generated content instead of interpolating JSON | batch-03.md |
| LFA-042 | Shortcut tests must traverse real event bindings | batch-03.md |
| LFA-043 | Speech does not remove model and tool latency | batch-03.md |
| LFA-044 | Residual takeoff contact must not reset jump state | batch-03.md |
| LFA-045 | Bound uncertainty without silently discarding aliases | batch-03.md |
| LFA-046 | Validate the whole batch before changing caller state | batch-04.md |
| LFA-047 | Scope cache exclusions to the project root and verify copy completeness independently | batch-04.md |
| LFA-048 | Place Unity test sources inside their test assembly | batch-04.md |
| LFA-049 | Keep fixture oracles separate from product policy | batch-04.md |
| LFA-050 | Bind generated FBX hashes to the fixture run | batch-04.md |
| LFA-051 | Preserve raw identity before normalizing serialized values | batch-04.md |
| LFA-052 | Use a run-owned temporary directory for restricted Python processes | batch-04.md |
| LFA-053 | Calibrate BakeMesh coordinate frames with pointwise skin equations | batch-04.md |
| LFA-054 | Materialize float tolerance edges before inclusive comparisons | batch-04.md |
| LFA-055 | Disabling Unity Package Manager can remove package assembly references | batch-04.md |
| LFA-056 | Read Unity compiler diagnostics from the completed build pass | batch-04.md |
| LFA-057 | Validate archive compatibility against real producer output | batch-04.md |
| LFA-058 | Count verified batch-import outcomes rather than attempted inputs | batch-04.md |
| LFA-059 | Include Editor window lifecycle side effects in test isolation | batch-04.md |
| LFA-060 | Successful decompression does not prove complete GZip framing | batch-04.md |
| LFA-061 | Regenerate run-owned fixtures instead of relying on cleaned predecessors | batch-05.md |
| LFA-062 | Separate Unity metadata line endings from GUID validation | batch-05.md |
| LFA-063 | Keep test, process, artifact and postflight results independent | batch-05.md |
| LFA-064 | A changed cwd does not revoke an approved work root | batch-05.md |
| LFA-065 | Diagnostic outputs must not clobber inputs | batch-05.md |
| LFA-066 | Dynamic imports must not reuse unverified modules | batch-05.md |
| LFA-067 | Redact binary FBX strings by their declared length | batch-05.md |
| LFA-068 | Bind completion evidence and verify identity readers | batch-05.md |
| LFA-069 | A passing in-process Unity test does not prove a command-line gate ran | batch-05.md |
| LFA-070 | Unity package import does not run explicit finalizers | batch-05.md |
| LFA-071 | Unity LicensingClient IPC needs the matching user session | batch-05.md |
| LFA-072 | Keep the shared Unity MCP server opt-in out of batch clients | batch-05.md |

## Review rule

Prefer updating or qualifying an existing Knowledge Entry over creating a near-duplicate. A source `confirmed` label must not be converted mechanically into a formal Atsumaru approval. Batch review is preferred; the normal independent reviewer remains GPT-6.1 Sol. Machine validation is not privacy or technical approval.
