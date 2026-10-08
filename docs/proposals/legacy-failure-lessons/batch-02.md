# Legacy failure lessons migration — Batch 02

Review status: PENDING_REVIEW

Generalized lessons migrated from a retired legacy failure-lesson repository. Source `confirmed` status is provenance only; Atsumaru independent review is still pending. No raw logs, conversations, private repository identifiers, personal paths, credentials, or project-specific artifacts are intentionally carried over.

## LFA-016 — A created version is not the live deployment target

- Source area: other
- Source type: diagnosis
- Source certainty: confirmed
- Source status: active
- Scope: versioned-service-deployment

### Intent

Observe new build/authentication diagnostics through an existing integration endpoint.

### Observed failure

Expected diagnostics were absent even though the new immutable service version existed.

### Failed assumption / approach

Version creation or propagation delay was treated as equivalent to updating the endpoint's deployment target.

### Root cause

Confirmed: deployment metadata still pointed to the previous version. Separately, workflow parser/final-output definitions dropped the new diagnostic fields. The exact failed operator step was unknown.

### Correction

Require the exact existing deployment to reference the intended version, then preserve required diagnostics end to end. This was the recorded recovery plan, not a completed live repair at that checkpoint.

### Verification

Read-only version/deployment and endpoint-identity comparisons established the mismatch. Seventeen local tests passed but did not assert the full new response; no corrected live result was established there.

### Reusable rule

Verify control-plane target and observed runtime marker separately. Waiting cannot fix metadata that still selects the old version.

### Applicability

Apps Script deployment plus Dify integration. Do not confuse draft execution with a published API surface or infer authentication failure before the intended version is reachable.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-017 — Distinguish explicit null from malformed references

- Source area: unity
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: serialized-material-reference

### Intent

Project a serialized material-slot override and realize its intended value.

### Observed failure

A Unity-authored explicit fileID: 0 override was discarded and reported unresolved.

### Failed assumption / approach

A reference without a GUID was assumed to be uniformly unknown.

### Root cause

Confirmed: the parser conflated an explicit null value with incomplete non-null references.

### Correction

Retain valid null as a known slot-clear operation. Keep nonzero references without GUIDs and zero references with invalid GUIDs unresolved. Require exact occurrence/native receipts before clearing live slots.

### Verification

Unity 2022.3.22f1 authored RED became parser/projection GREEN. A separate exact-witness direct native realization and save/reopen control passed; the historical normal nested import path was still native-missing at that checkpoint.

### Reusable rule

Model absent, explicit null, and malformed references separately. Verify live clearing independently from parsed-state correctness.

### Applicability

One-slot synthetic Variant controls. Array-size changes, multi-level precedence and export were not established by this evidence.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-018 — Verify identifiers after serialization and import

- Source area: blender
- Source type: diagnosis
- Source certainty: confirmed
- Source status: active
- Scope: fbx-identifier-transport

### Intent

Transport a stable object identifier through FBX to a destination finalizer.

### Observed failure

Package generation succeeded, but a temporary-scene export lacked the identifier in FBX and the destination could not identify its mesh.

### Failed assumption / approach

Setting the custom property and enabling custom-property export was assumed sufficient.

### Root cause

Confirmed bounded observation: staging context changed identifier transport for the same synthetic mesh. The deeper exporter mechanism was not isolated.

### Correction

Use the observed working temporary-object context and inspect serialized identifiers plus destination callback receipts; reject absent or duplicate identifiers.

### Verification

The alternative current-scene control contained the identifier in FBX and Unity's public property callback. Missing/duplicate controls rejected; display-name changes were accepted.

An additional bounded Blender 5.2.1 observation imported an exported FBX in a fresh process with the add-on disabled. Three Material names survived as ordered transport labels and their per-slot triangle counts matched an independent source-FBX oracle. A custom Material property lookup was empty after native import; the serialized/imported Material names, not that custom property, carried these particular labels.

### Reusable rule

Prove identity at each transport boundary, not just in pre-export metadata. Inspect the destination field that actually carries the identifier; do not substitute a custom property for a serialized Material-name label. Keep the exact output revision bound to destination receipts.

### Applicability

The historical callback evidence covers Blender 5.2.1 and Unity 2022.3.22f1 with one static UV mesh. The added Material-label evidence covers one synthetic three-slot skinned mesh and Blender 5.2.1 native FBX import. No universal exporter defect or general Skin/multi-object guarantee is inferred.

### Separate transport claims before formalization

- **Verified in the bounded identifier route:** the exact identity was observed in exported FBX and in the destination's callback receipts, with missing or duplicated identifiers rejected.
- **Separately observed in the native Material-label route:** serialized Material names carried three ordered transport labels into Blender; the attempted custom Material-property lookup did not carry those labels. This does not establish a general material-slot or Skin reconstruction contract.
- The two routes require separate acceptance boundaries and evidence classifications when converted to formal Knowledge. A successful serialization of one field does not prove the other field, importer context, or downstream use.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-019 — Declare external references and inspect every provider kind

- Source area: unity
- Source type: diagnosis
- Source certainty: confirmed
- Source status: active
- Scope: script-provider-preflight

### Intent

Finalize exported content whose framework components remain external.

### Observed failure

Output compiled, yet finalization refused 55 missing scripts; the dependency manifest was empty and an initial source-script search missed compiled providers.

### Failed assumption / approach

The exported dependency contract omitted script prerequisites, and the initial provider search covered C# metadata only.

### Root cause

Confirmed: required exact script references were undeclared; provider identity could reside in compiled script assets, not only source files.

### Correction

Declare selected-chain GUID/signed-localID references with revision-bound requiring contexts. Preflight public MonoScript resolution before mutation; explicitly refuse absent or malformed providers.

### Verification

Retrying the same output with exact providers changed missing scripts from 55 to zero and passed first/repeated Apply. Ten public controls covered declarations, absent-provider refusal and same-output recovery.

### Reusable rule

Separate preserved reference identity from provider availability. Search all relevant provider kinds and verify exact references before blaming unrelated geometry or bundling a framework.

### Applicability

One bounded Unity 2022.3.22f1 route. This does not prove arbitrary component fidelity, all avatars, or permission to redistribute external SDKs.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-020 — Validate helper handles and bound response waits

- Source area: other
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: tcl-helper-process-protocol

### Intent

Recover recording/playback UI after helper launch or response failure.

### Observed failure

Launch error text remained in a channel-handle variable, causing modal write errors; a wait ignoring EOF/deadline hung stop and left the UI busy.

### Failed assumption / approach

Any nonempty handle string was treated as a channel, and a helper was assumed eventually to answer.

### Root cause

Confirmed: diagnostic text and resource identity shared storage, while protocol waits lacked terminal failure handling.

### Correction

Check live-channel membership, convert EOF/read/write/timeout into normal errors, use finite event-driven waits, and clear handles/busy state while releasing helpers on every exit.

### Verification

A stale error string injected before a second stop triggered safe controller recovery; a third recording succeeded. Consecutive cycles passed and termination completed within eight seconds with no residual processes.

### Reusable rule

Keep handles distinct from diagnostics. Test helper death between request and response, and make cleanup plus return-to-idle unconditional.

### Applicability

Observed Windows/Tcl helper protocol. This addresses control flow, not all underlying native audio or device failures.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-021 — Hierarchy enumeration must include nonvisual occurrences

- Source area: unity
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: nested-prefab-hierarchy

### Intent

Reconstruct a complete semantic hierarchy from nested prefabs.

### Observed failure

An independent Unity oracle had 12 nodes and 11 edges, while normal import produced 10 and 9; two renderer-free occurrences were absent.

### Failed assumption / approach

Renderer-driven model expansion was assumed to cover the semantic hierarchy.

### Root cause

Confirmed: prefab-local object/nested-occurrence expansion omitted nodes with no renderer.

### Correction

Expand source objects using root context and ordered instance edges, retaining source object/transform identities independently of renderers.

### Verification

Normal import changed from zero to two nested occurrences. All 48 oracle dimensions matched; rename/save/reopen retained semantic identity. Malformed-source and comparator controls passed.

### Reusable rule

Compare complete independent node populations, including repeated nonvisual nodes. Never make semantic hierarchy existence depend on renderable content.

### Applicability

Public synthetic semantic hierarchy in Unity 2022.3.22f1/Blender 5.2.1. This checkpoint alone did not prove native Skin, renderer or bone attachment parity.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-022 — A local flag does not release a host modal handler

- Source area: blender
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: editor-operator-lifecycle

### Intent

Finish foreground import and return safely to normal editor interaction.

### Observed failure

Import completed, then ordinary view interactions caused a native access violation with a modal-callback stack.

### Failed assumption / approach

The same operator opened a dialog while its preparation modal remained registered; clearing a Python flag was treated as handler removal.

### Root cause

Confirmed lifecycle defect: host-owned modal registration survived the local flag change and execution reentered the same object.

### Correction

Return FINISHED to end preparation in the host, then start separate dialog/prepared operators on later event-loop turns. Bound session lifetime and clean success, cancel and exception paths.

### Verification

Corrected foreground import finished without the preparation handler; 100 interaction cycles and two distinct serial sessions completed with process exit zero and no new crash dump. An invalid timer-context Undo probe was excluded.

### Reusable rule

End the host-owned lifecycle before reentrant phase changes. Verify post-completion interaction and host state rather than a local Boolean.

### Applicability

Blender 5.2.1 tested import path. Arbitrary dialog clicking and normal UI Undo remained unverified; no universal native-crash fix is claimed.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-023 — Inspect workflow body and file outputs separately

- Source area: other
- Source type: tooling
- Source certainty: confirmed
- Source status: active
- Scope: workflow-response-classification

### Intent

Consume a provider's JSON response in a workflow normalizer.

### Observed failure

The provider returned HTTP 200, but the node body was empty and a GeoJSON file appeared in files; the normalizer rejected the response.

### Failed assumption / approach

HTTP success and JSON-related content type were assumed to guarantee body delivery.

### Root cause

Confirmed observed Dify Cloud behavior: the response with an inline filename Content-Disposition was classified as file output.

### Correction

Use a bounded authenticated fixed-endpoint transport that envelopes the provider object as ordinary application/json; validate transport marker, provider status and call count.

### Verification

Later recorded live geocode/place checks succeeded. Initial execution used two provider calls and cache replay zero; provider/backend regression checks passed.

### Reusable rule

Inspect status, headers, body and files before blaming upstream data. Exercise a minimal actual node-output smoke test before extending the workflow.

### Applicability

This is a scoped compatibility workaround, not a change to the provider or a universal MIME rule. Do not turn the transport into an unrestricted proxy.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-024 — Isolate template expansion before changing encodings

- Source area: other
- Source type: diagnosis
- Source certainty: confirmed
- Source status: active
- Scope: workflow-raw-text-interpolation

### Intent

Transport encoded input through a workflow template to a receiver.

### Observed failure

The receiver rejected the encoded value even though a direct request to the same deployment decoded correctly; changing Base64 to hexadecimal did not fix the workflow path.

### Failed assumption / approach

Transport-symbol interpretation was initially blamed.

### Root cause

Confirmed: a reference containing a hyphenated node ID arrived literally rather than expanding. Privacy-safe character-class/length diagnostics distinguished a placeholder from corrupted data.

### Correction

Use the observed working numeric IDs for HTTP-referenced nodes and verify actual interpolation. Diagnose subsequent authorization failure separately.

### Verification

The next request decoded and reached provider execution; later full smoke succeeded after the independent external-request authorization issue was resolved.

### Reusable rule

Compare direct receiver and templated-path controls before re-encoding data. Inspect non-sensitive structure to prove expansion without logging payloads or secrets.

### Applicability

Observed Dify raw-text behavior at that revision. This is not a universal ban on hyphenated IDs or a claim that encoding changes repair interpolation.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-025 — Use invariant node types and verify the active render path

- Source area: blender
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: localized-material-graphs

### Intent

Construct textured material graphs in more than one UI locale.

### Observed failure

English-name lookups failed under Japanese UI, creating duplicate shader/output nodes; none of 48 texture chains reached the active output.

### Failed assumption / approach

Built-in display names and the mere presence of images/nodes were treated as stable rendering evidence.

### Root cause

Confirmed: localized names defeated lookup, and new links reached an inactive sink.

### Correction

Select nodes by invariant type, prefer the active output and its connected shader, and explicitly establish the active Surface link.

### Verification

English/Japanese controls each reached 48/48 active surfaces with no duplicate outputs. Separate-process reopen preserved graph signatures and 147 slot bindings. Manual viewport preview was not verified in this recorded checkpoint.

### Reusable rule

Address built-in nodes by invariant identifiers. Test graph reachability to the active sink, including nondefault locales and save/reopen.

### Applicability

Blender 5.2.1 observed material graph. Transparent paths and multiple engine-specific outputs were not covered.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-026 — Reapplication must prove that managed state is still owned

- Source area: blender
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: managed-texture-state

### Intent

Re-resolve previously bound material textures without losing user edits.

### Observed failure

Resolve replaced a user-selected image; a changed node link was rewired after save/reopen.

### Failed assumption / approach

A saved BOUND status was treated as permission to reapply a provider.

### Root cause

Confirmed: no applied-state comparison distinguished automation-owned state from subsequent user edits.

### Correction

Record the scoped image/link signature when applying a binding. Preserve mismatches with an explicit user-edit status; leave legacy receipt-free bindings unverified.

### Verification

Pre-fix image/link sequences failed. Corrected edit, provider-loss/readdition, and save/reopen controls passed; forcing signature acceptance made the focused regression fail. An unedited owned binding still cleared on provider loss.

### Reusable rule

Before replaying managed state, compare it with the exact state automation installed. Preserve unproven ownership rather than upgrading it by assumption.

### Applicability

Bounded Blender texture bindings. Unrelated nodes remain untouched; these results do not establish exact export fidelity.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-027 — Mandatory evidence retrieval must be enforced by control flow

- Source area: agents
- Source type: architecture
- Source certainty: confirmed
- Source status: active
- Scope: grounded-workflow-orchestration

### Intent

Require evidence retrieval and a valid handoff before producing grounded answers.

### Observed failure

An autonomous agent omitted the required tool in one of ten searches; valid handoffs were four of ten for search and zero of five for detail/comparison, while four existing tests passed.

### Failed assumption / approach

Prompts and generic helper tests were assumed to enforce mandatory operations and output contracts.

### Root cause

Confirmed: operation choice and contract generation remained discretionary, with conflicting legacy instructions and missing graph guards.

### Correction

Route required operations through fixed intent-specific tool nodes, validate untrusted results, gate remote work on parser success, and model non-evidence/failure outcomes explicitly.

### Verification

Targeted search/detail/comparison checks improved to 10/10 and 5/5; 55 malformed inputs rejected and invalid-input remote calls stayed zero. Later soak still failed final validation, so overall architecture acceptance remained incomplete.

### Reusable rule

Make mandatory operations structural invariants. Test omitted-tool, malformed-result and failure paths in the actual graph; targeted success is not full-system acceptance.

### Applicability

Observed Dify grounded workflow. The lesson does not require removing every model or claim that later external validation failures were solved.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-028 — Material slot numbers do not prove face assignment

- Source area: unity
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: material-partition-transport

### Intent

Preserve effective material assignment while round-tripping a skinned mesh.

### Observed failure

Unity permuted native submeshes while the finalizer retained the source material array; a public three-slot fixture reproduced the mismatch.

### Failed assumption / approach

Equal source and destination slot indices were used as material correspondence.

### Root cause

Confirmed: slot ordering was not stable across this transport path.

### Correction

Attach exact-reference transport labels to disposable cloned materials, then resolve actual imported submesh order to preserved material assets.

### Verification

Initial/repeated Apply passed; invalid-identity controls rejected without creating a Variant. A bounded real occurrence preserved exact material face partitions despite slot-number permutation. Source material bytes and editing state remained unchanged.

### Reusable rule

Compare effective material partitions using authoritative material identity and triangle-corner multisets in an independently declared common frame, preserving duplicate-triangle multiplicity. Report winding separately: one uniform reversal preserves face membership but does not prove oriented or culling fidelity. Do not infer correspondence from counts, names or slot ordinals.

### Applicability

Bounded direct Skin route. Unassigned/unused carrier slots are refused; UV, normals, deformation and broader component fidelity remain separate gates.

### Supplemental diagnostic and provenance boundary (from original Lesson)

A later bounded diagnostic compared native FBX import, fresh package import before and after explicit renderer confirmation, and a saved confirmed scene. At a declared coordinate quantization, triangle membership corresponded after one uniform reversal. Renderer confirmation did not change geometry or polygon indices but did yield a mismatch between exact Material identities on the corresponding face partitions. This strengthens the **material-membership** problem description; it does not prove winding/culling fidelity or explain the cause of the reversal.

A diagnostic and an import fixture may use **different package contexts**. Before treating their material scopes as the same, compare the exact source FBX and metadata, source Prefab renderer-to-mesh identity, and material references. An output-package identity must never be substituted for the original input fixture's material scope.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-029 — Matching transforms do not prove evaluated geometry

- Source area: blender
- Source type: diagnosis
- Source certainty: confirmed
- Source status: active
- Scope: direct-mesh-coordinate-frame

### Intent

Place directly referenced mesh resources in nested occurrences.

### Observed failure

Transform checks passed while evaluated world-point errors exceeded 3.6 units in a public fixture.

### Failed assumption / approach

The native FBX object transform was assumed to belong to the directly referenced mesh subasset.

### Root cause

Confirmed for the fixture: importer file scale applied to mesh coordinates, but the FBX Model-node translation did not belong to that direct mesh frame.

### Correction

Apply the independently verified mesh frame, excluding Model translation, only when exact receipts/revisions and supported importer settings validate.

### Verification

An asymmetric four-point probe isolated basis/unit conversion. Corrected normal import and rename/resolve/reopen stayed within 1e-5; omitted scale, doubled Model transform and omitted instance transform controls failed.

### Reusable rule

Verify evaluated world geometry independently of transform matrices. Distinguish resource-local coordinates from scene-node placement before applying either.

### Applicability

Unity 2022.3.22f1/Blender 5.2.1, depth-one MeshRenderer and supported FBX settings. Point-set parity is not topology, Skin or general FBX-frame equivalence.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-030 — Parse numbers together with their units

- Source area: other
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: compound-measurement-parsing

### Intent

Normalize an area string containing metric and alternate-unit values.

### Observed failure

A string containing both values used the first number as the alternate unit and converted it incorrectly.

### Failed assumption / approach

The first numeric token plus a unit appearing anywhere in the string was assumed to identify a measurement.

### Root cause

Confirmed: numeric extraction happened before unit-specific association.

### Correction

Read the numeric token immediately associated with each unit. Convert only when exactly one of the expected units is absent.

### Verification

A recorded diagnostic stored both supplied values correctly; five focused parsing cases passed.

### Reusable rule

Parse number-unit pairs rather than separate number and unit lists. Test both orders, each single unit, separators and malformed input.

### Applicability

Compound area strings in the observed parser. Other unit systems, locale separators and ambiguous input need their own explicit contracts.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

