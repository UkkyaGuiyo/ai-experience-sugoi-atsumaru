# Legacy failure lessons migration — Batch 04

Review status: PENDING_REVIEW

Generalized lessons migrated from a retired legacy failure-lesson repository. Source `confirmed` status is provenance only; Atsumaru independent review is still pending. No raw logs, conversations, private repository identifiers, personal paths, credentials, or project-specific artifacts are intentionally carried over.

## LFA-046 — Validate the whole batch before changing caller state

- Source area: unity
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: generator-batch-atomicity

### Intent

Add generated parameters to a caller-owned Animator controller.

### Observed failure

A collision with a later reserved name rejected the build after earlier parameters had already been appended.

### Failed assumption / approach

Validation interleaved with per-item mutation was assumed to make rejection atomic.

### Root cause

Confirmed: the append loop changed state before discovering all conflicts.

### Correction

Preflight the complete reserved-name/type set before any addition. For transformations that can fail midway, prepare isolated results before committing them.

### Verification

Twelve later-name/type collision cases preserved parameters, layers and clips after rejection. A related migration fault control preserved full serialization and original object identities using clone-transform-commit.

### Reusable rule

Validate every batch constraint before the first mutation, and stage fallible transformations before commit. Test a last-item conflict and compare the whole pre-state.

### Applicability

Bounded in-memory Unity generators/migrations. This does not establish disk rollback or immunity to errors after the commit boundary.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-047 — Scope cache exclusions to the project root and verify copy completeness independently

- Source area: unity
- Source type: workflow
- Source certainty: confirmed
- Source status: active
- Scope: unity-project-migration

### Intent

Migrate selected Unity projects while excluding regenerable project caches and preserving required source files.

### Observed failure

The copy manifest recorded nine skipped directories across three projects. Among the skipped contents were 30 required third-party source files: 19 in a runtime Library directory, six in an editor Library directory, and five in a nested editor-module Cache directory. A later compile reported a missing namespace despite matching hashes for all selected source and destination files.

### Failed assumption / approach

Any directory whose basename was Library or Cache was treated as generated, cached, or system content, regardless of its position in the project. The verifier reused the copier's exclusion rules, so matching selected-file hashes were mistaken for proof of a complete migration.

### Root cause

Confirmed: basename-only exclusions also matched nested source directories with legitimate Library and Cache names. Those files were never selected for copying. Reusing the same selection logic in hash validation made the omission invisible: the validator proved integrity only for the selected set, not completeness of the required source inventory.

### Correction

Recover the 30 identified source files from the official package of the same version and verify each recovered file's hash. For future migrations, scope generated-cache exclusions to documented project-relative locations, such as the project-root Library directory; preserve nested names unless their generated status is independently established.

### Verification

The skipped-directory manifest established the exclusion mechanism. Recovery restored 30 identified source files from a same-version official package, with individual hashes verified. This confirms the identified omissions and recovery bytes, not full project recovery: the original drive was unavailable for a complete source rescan, so additional missing files outside the recorded manifest were not ruled out. A full Unity compile and runtime validation had not yet passed.

Before calling a future migration complete, compare the destination against an independently obtained expected source inventory, review every excluded path and its reason, then import and compile. Include fixtures where root Library is excluded but nested runtime/editor Library and Cache source directories are retained. These are required future checks, not tests reported as already run for this incident.

### Reusable rule

Exclude Unity caches by documented project-relative location, never by matching every directory basename Library or Cache. Verify destination completeness against an independent expected source inventory as well as hashes; a verifier sharing the copier's filter cannot prove that the filter selected all required files. Keep byte-integrity, inventory-completeness, and compile/runtime results separate.

### Applicability

Applies to project migration, backup, packaging, and source synchronization when cache-like names can also occur in maintained source trees. Do not infer that every nested Cache directory must be copied or that root-only exclusions alone prove completeness; classify each exclusion from its actual role and verify the intended migration scope.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-048 — Place Unity test sources inside their test assembly

- Source area: unity
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: unity-editor-test-fixtures

### Intent

Run a focused Unity EditMode test suite from an isolated project snapshot.

### Observed failure

A test source outside the Editor test assembly directory was compiled as part of `Assembly-CSharp`; Unity reported unresolved NUnit references and the test run produced no results XML.

### Failed assumption / approach

The test was assumed to be included in the suite because it was under a general `Tests` folder.

### Root cause

Confirmed: Unity assembly definition boundaries, not the folder name alone, determine which references compile a source file. The source was outside the test assembly's scope and therefore lacked its NUnit references.

### Correction

Move the source under the intended Editor test assembly directory and ensure the test asmdef references the runtime assembly being exercised.

### Verification

The isolated Unity project compiled and ran the focused EditMode suite after the move, producing matching XML with all six tests passing.

### Reusable rule

Before running Unity tests, verify that each test source is inside the intended test asmdef boundary and that the asmdef references its target runtime assembly. Treat compiler failure or missing result XML as an invalid test run, not a test pass.

### Applicability

Unity projects using assembly definitions and NUnit EditMode tests. Do not generalize the exact folder convention to projects with a different asmdef layout; inspect their assembly boundaries.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-049 — Keep fixture oracles separate from product policy

- Source area: agents
- Source type: architecture
- Source certainty: confirmed
- Source status: active
- Scope: final-state-geometry-validation

### Intent

Design a bounded integration test for a product that treats an edited final mesh as authoritative.

### Observed failure

A fixture-specific test expected a topology edit to preserve source face and vertex semantics. A design review incorrectly elevated that expectation into a general product requirement for explicit source-vertex lineage.

### Failed assumption / approach

The test's geometry-equality oracle was treated as evidence that every accepted final mesh must prove source-to-final vertex correspondence, even though the approved product contract allowed complete source mesh replacement.

### Root cause

Confirmed: test oracle and product policy answered different questions. The test asked whether one synthetic seam split preserved selected source semantics. The product contract asked whether a valid Blender-authored final mesh could replace the source mesh while Unity semantic references were restored.

### Correction

Read the approved product model before defining acceptance policy. Keep source-relative geometry checks inside the fixture oracle; validate the final mesh on its own streams, indices, weights, bone/rest bindings and material identities. Require lineage only when transferring or asserting continuity of source-indexed state. Otherwise reject unsupported index-dependent components or explicitly exclude them from scope.

### Verification

The approved architecture states that final Blender geometry/topology/UV/weights/shape/material assignment is authoritative and that source geometry lineage is normally unnecessary. The Unity finalizer assigns the imported final mesh to the Variant renderer. An independent review confirmed that mesh assignment itself does not require source-vertex correspondence; Cloth/custom vertex-index state and source-relative parity claims are separate responsibilities.

### Reusable rule

Before adding transport fields or rejecting edited geometry, separate what the fixture must prove from what the product promises to accept. Add source-to-final lineage only when a named preservation or migration responsibility consumes it; otherwise validate the final mesh and explicitly refuse unsupported dependent state.

### Applicability

Applies to final-state-authoritative geometry pipelines where the edited mesh may replace its source. It does not apply when the product promises source-vertex continuity, transfers vertex-indexed component data, or validates source-relative face/material/weight equivalence.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-050 — Bind generated FBX hashes to the fixture run

- Source area: blender
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: synthetic-fbx-integration-tests

### Intent

Verify generated FBX fixtures through a Unity import and integration test.

### Observed failure

A test case expected one fixed FBX SHA-256 across fixture rebuilds, coupling the test to bytes from an earlier run.

### Failed assumption / approach

The fixture's geometry and material identities were treated as sufficient to make the exported FBX bytes stable.

### Root cause

Confirmed for Blender 5.2.1's binary FBX exporter: output metadata includes the current creation timestamp and the source blend-file path. Rebuilding the same synthetic geometry can therefore change the whole-file hash without changing the behavior under test.

### Correction

Record each newly generated FBX hash in that run's fixture evidence. In the consumer test, bind the evidence entry to the expected case, Export ID, filename, and owned path, then compare the copied FBX bytes with that same-run hash. Keep semantic checks for imported geometry and material assignment separate from byte identity.

### Verification

The installed Blender exporter source writes `CreationTimeStamp` from the current time and serializes the blend-file path as `ApplicationNativeFile`. The fixture builder records per-run SHA-256 values and the Unity integration test consumes those values.

### Reusable rule

Do not use a previous run's whole-file FBX hash as the expected value for a regenerated fixture when exporter metadata can vary. Produce evidence alongside the fixture and validate its case identity and path before using the hash.

### Applicability

Applies to generated FBX fixtures when the exporter serializes timestamps or source paths. It does not imply that every FBX exporter or every format is nondeterministic.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-051 — Preserve raw identity before normalizing serialized values

- Source area: unity
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: serialized-provider-identity

### Intent

Resolve one narrowly allowlisted serialized provider by its exact identity.

### Observed failure

A YAML reference with a fractional numeric file ID was converted with `int()` to the allowlisted integer ID. In one direct-reference path the original scalar was retained, but the Prefab variant override parser independently extracted the integer prefix and discarded the fractional suffix before projection. The normalized value then passed an exact provider check, even though the source scalar was malformed.

### Failed assumption / approach

The parsed integer was treated as sufficient proof of the original serialized identity.

### Root cause

Confirmed: integer conversion is lossy for fractional floats, and a second parser boundary can discard the raw scalar before a later projection has an opportunity to preserve it.

### Correction

Retain the original scalar at the earliest parser boundary, then carry it through variant/direct projection and dependency capture. Require the raw value to have the expected exact type and value before applying the narrow allowlist; keep normalized fields for existing consumers. Exclude parser-only evidence from semantic comparison views that do not consume it.

### Verification

A synthetic control confirmed that the fractional source value normalizes to the same integer as the allowlisted ID, while the raw-value guard rejects it. A separate variant override regression reproduced the integer-prefix loss and then verified that the raw string survives parser, projection, and dependency planning. Integer identity, wrong GUID, wrong reference kind, ordinary missing provider, and explicit null remained outside the allowlist.

### Reusable rule

When a decision depends on exact serialized identity, preserve the original scalar at every parser boundary, alongside normalized fields, until validation is complete. Validate type and exact value before allowing a provider-specific route; test malformed values through direct and inherited/variant paths that collapse to a valid identity under normalization.

### Applicability

Applies to narrow provider allowlists fed by parsed serialized data. It does not require every general-purpose parser to reject all numeric formats or establish semantics for other Unity reference kinds.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-052 — Use a run-owned temporary directory for restricted Python processes

- Source area: python
- Source type: environment
- Source certainty: confirmed
- Source status: active
- Scope: python-tempdir-restricted-windows

### Intent

Run an integration test that uses Python temporary files inside a restricted Windows execution environment.

### Observed failure

A Blender import operator failed before opening its input package with `No usable temporary directory found`. Python listed its default temporary-directory candidates, but none were writable in the restricted process context.

### Failed assumption / approach

The default Windows temporary-directory candidates were assumed to be usable by every child process started from the workspace.

### Root cause

Confirmed in the observed execution environment: the child process could not create a temporary directory under its default `TEMP`/`TMP` candidates. Python's `tempfile` initialization therefore failed before the tested import work began.

### Correction

Create a temporary directory inside the current task's owned writable run directory. Set `TEMP` and `TMP` for the child process only, then restore the caller's environment. When a failed run already created an output directory that must be absent on entry, preserve that directory and use a fresh run-owned output path for the retry.

### Verification

Python 3.13.13 created a `TemporaryDirectory` with the process-local `TEMP`/`TMP` set to the owned run directory. The Blender package importer then completed its Material ON/OFF Skin/Shape parity run, including save/reopen checks. The default-path run had failed before package import.

### Reusable rule

When a restricted Windows child process reports `No usable temporary directory found`, direct only that process's `TEMP`/`TMP` to a newly created task-owned writable directory and restore the parent environment afterward. Preserve failed outputs and use a new output directory if the command requires a nonexistent destination.

### Applicability

Applies to restricted Windows runners where the default temporary candidates are inaccessible to Python child processes. Do not generalize it to environments whose normal temporary paths are writable.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-053 — Calibrate BakeMesh coordinate frames with pointwise skin equations

- Source area: unity
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: unity-skinned-mesh-baking

### Intent

Choose a world/root coordinate conversion for `SkinnedMeshRenderer.BakeMesh` output in an Editor verification fixture.

### Observed failure

In Unity 2022.3.22f1, a synthetic renderer with positive uniform scale 100, nontrivial rotation, and no shear was checked against a per-vertex skin equation. `BakeMesh(useScale:true)` followed by position/rotation only had maximum root-local error 0.014 and root-bounds delta 0.0099, beyond the 0.001 tolerance. Assuming that the `useScale` argument alone identified the baked coordinate frame was wrong for this fixture.

### Failed assumption / approach

The boolean named `useScale` was treated as sufficient proof that renderer scale must or must not be applied again by the subsequent transform.

### Root cause

Confirmed for this Unity version and fixture: the coordinate frame must be measured, not inferred from the argument name. The four combinations produced different results: `true + localToWorld` max root error 1.86e-9; `true + position/rotation only` 0.0140; `false + localToWorld` 1.4001; `false + position/rotation only` 9.32e-10.

### Correction

Evaluate the actual `BakeMesh` point cloud against the independent weighted bindpose/bone skin equation, per vertex and in root-local coordinates. Record point error and world/root AABBs for each candidate transform. Assert and report the fixture's scale, rotation, handedness, and no-shear properties. Do not introduce a guessed fixed scale multiplier.

### Verification

The selected `true + localToWorld` path passed a real Finalizer Apply/repeat run on the fixture: maximum root-local point error 1.86e-9, bounds delta 1.86e-9, repeat Apply idempotent, and all protected source assets unchanged. This is a fixture-specific observation.

### Reusable rule

For each Unity version and transform class, compare all plausible BakeMesh/useScale and renderer-frame combinations against an independent per-vertex skin equation. Require pointwise error, bounds parity, and an explicit transform control before choosing a conversion. Do not generalize a result to negative, nonuniform, or sheared transforms without separate controls.

### Applicability

Unity Editor diagnostics for skinned meshes. The measured combination is not a universal rule for other Unity versions, rigs, transform hierarchies, or scale/shear cases.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-054 — Materialize float tolerance edges before inclusive comparisons

- Source area: unity
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: unity-float-bounds-validation

### Intent

Make a tolerance-expanded bounds comparison inclusive at exactly computed single-precision edges.

### Observed failure

In a Unity EditMode test, the negative-X edge was constructed as `bounds.min.x - 0.001f`. A direct inline comparison rejected it even though the stored point and threshold had identical float bits (`BF8020C5`). Round-tripping the threshold through a stored `float` made the comparison pass. The other five exact edges and points just inside/outside the tolerance were checked separately.

### Failed assumption / approach

An inline comparison such as `point.x >= bounds.min.x - tolerance` was assumed to compare two already-rounded single-precision values.

### Root cause

Confirmed in the tested Unity Editor runtime: the comparison evaluated an intermediate with precision different from the stored `Vector3` component, so equal serialized single-precision bit patterns did not guarantee the inline expression accepted the edge.

### Correction

Compute the six expanded min/max edges once per bounds set, force each through a single-precision round trip, then compare stored vertex components against those stored limits. Keep the configured tolerance unchanged. Reuse the limits inside vertex loops.

### Verification

The exact six min/max +/- tolerance edges passed after the correction; the immediately adjacent single-precision values outside were rejected. The existing 1.0009-inside and 1.0011-outside controls remained. The focused Unity suite passed 7/7 with no C# compiler errors.

### Reusable rule

When an inclusive float edge unexpectedly fails, log component values and bit patterns before changing the tolerance. Materialize computed float thresholds once, and test both the exact edge and the adjacent representable value outside it. Avoid per-vertex allocation when the limits can be computed once per bounds set.

### Applicability

The observed behavior and fix apply to the tested Unity Editor runtime and single-precision bounds checks. Revalidate on other runtimes or comparison types.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-055 — Disabling Unity Package Manager can remove package assembly references

- Source area: unity
- Source type: environment
- Source certainty: confirmed
- Source status: active
- Scope: unity-editor-package-resolution

### Intent

Compile an isolated Unity project without permitting dependency downloads.

### Observed failure

Unity 2022.3.22f1 was launched with `-noUpm`. Existing Editor test sources then failed compilation with `CS0246` for NUnit `Test` and `TestCase` attributes. The exact Test Framework and NUnit package directories were already present in the project package cache and the manifest/lockfile pinned them.

### Failed assumption / approach

The cached packages were assumed to remain available to script compilation when the Package Manager was disabled.

### Root cause

Confirmed: disabling UPM prevented the project package assemblies from being resolved into Unity's compilation inputs, even though their cached package files were present. The resulting error was missing NUnit symbols in the existing test assembly.

### Correction

Keep the existing package manifest and lockfile unchanged. When the exact required package versions are already cached, allow Unity's Package Manager to resolve the existing lock/cache; do not add or update dependencies. If the required package is unavailable and obtaining it is not authorized, stop at compile-only scope or report the blocker.

### Verification

The `-noUpm` run emitted the NUnit `CS0246` errors and exited with code 1. Package directories for `com.unity.test-framework` 1.1.33 and `com.unity.ext.nunit` 1.0.6 were already present. With UPM enabled, Unity reported restoring the resolved package state from cache and registered the four locked packages. The manifest and lockfile stayed byte-identical, and the 693-file PackageCache inventory SHA256 stayed `bab1234131e4e081fe8e62e0c6ae3a65c89ea54a8174a6d31cf0e9c850cac135`. A subsequent standalone Editor compile exited 0 with zero `error CS` diagnostics.

### Reusable rule

Do not use `-noUpm` to avoid downloads in a Unity project whose compile depends on UPM packages. First verify exact versions in the lockfile and package cache, then let UPM restore those existing packages without changing the manifest. Verify a clean compile after package resolution; if that cannot happen without a new package download, stop and report instead of compiling with missing references.

### Applicability

Unity projects whose scripts or test assemblies depend on packages installed through UPM, especially NUnit-backed EditMode tests. Do not generalize this to projects that use only built-in Unity assemblies or have no UPM dependencies.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-056 — Read Unity compiler diagnostics from the completed build pass

- Source area: unity
- Source type: diagnosis
- Source certainty: confirmed
- Source status: active
- Scope: unity-editor-compilation

### Intent

Diagnose compiler errors during an incremental Unity Editor build after adding authored C# files and an Editor test assembly.

### Observed failure

An early Bee compiler response did not include a newly synchronized source file and reported missing-type errors. A later response in the same build included that file and reduced the remaining diagnostics to an unrelated missing namespace import. After correcting the import, compilation and the focused EditMode suite passed.

### Failed assumption / approach

The first response-file errors were initially liable to be treated as the final compiler state, which would have sent diagnosis toward a missing assembly reference or a product-code defect.

### Root cause

Confirmed: the build emitted multiple compiler passes with different source inputs. The early pass's missing-type diagnostics did not describe the final pass. Separately, the final pass exposed a real namespace import error. The source file and its metadata had also been omitted from the initial targeted sync; that omission was confirmed by the first failed compile and corrected before the later build.

### Correction

Check the complete compiler sequence and final response-file inputs before changing assembly references or implementation. Sync and verify every intended authored source file and its Unity metadata, then fix only the error that remains in the completed compile.

### Verification

Unity 2022.3.22f1 logs showed two compiler responses: the first lacked the newly added source; the later response included it and reported only the namespace error. After adding the required import, an independent source compile succeeded and the isolated EditMode run produced NUnit XML with 17 of 17 tests passing and no compiler errors.

### Reusable rule

For incremental Unity builds, inspect the final compiler response and completed build diagnostics before acting on a transient early-pass missing-type error. Verify the exact source and metadata sync separately; do not infer an assembly-reference defect until the final pass still lacks the type.

### Applicability

Applies to incremental Unity Editor/Bee builds that invoke more than one C# compiler pass while source inputs are changing. Do not generalize to a clean build with a single stable compiler response; diagnose that response directly.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-057 — Validate archive compatibility against real producer output

- Source area: unity
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: unitypackage-format-compatibility

### Intent

Check that a bounded package reader accepts actual Unity ExportPackage output while rejecting unapproved contents.

### Observed failure

Synthetic package tests passed, but a small self-authored archive exported by the actual Unity producer was rejected. The real producer used a GZip header containing an original filename (FNAME) and an old-GNU TAR marker; neither variant matched the synthetic-only reader profile.

### Failed assumption / approach

The synthetic writer and reader shared the same assumed GZip/USTAR header profile. Agreement between those two implementations was incorrectly treated as compatibility evidence for the independent real producer.

### Root cause

The observed producer bytes had a filename-bearing GZip header and an old-GNU TAR marker, but the validator's supported profile was narrower. The observation did not justify weakening header checksums, archive-path safety, asset identity or content-hash requirements.

### Correction

Retain a hash-pinned, self-authored real export as a regression fixture. Add only the measured header variants, with bounded filename handling and explicit rejection of unsupported extension fields. Keep checksum, exact inventory, GUID, path, raw asset/meta hash, and complete framing checks.

### Verification

The recorded follow-up accepted the pinned real archive and rejected malformed FNAME/extension variants. A later actual Unity 2022.3.22f1 run passed 303/303 EditMode cases, including real export, zero-finding audit, and import into an absent run-owned target with GUID/hash/name assertions. This was not a broad arbitrary-content release test.

### Reusable rule

Obtain a minimal real-producer fixture early, before treating synthetic reader/writer agreement as compatibility. Add bounded support from observed bytes and pair every new acceptance case with rejection controls.

### Applicability

Import/export tools and version-sensitive serialization formats. One Unity export fixture does not establish every archive variant, optional member, asset type, SDK dependency, or Unity version.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-058 — Count verified batch-import outcomes rather than attempted inputs

- Source area: blender
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: batch-fbx-import-reporting

### Intent

Import several FBX files and report whether the resulting Blender scene is complete.

### Observed failure

Source inspection showed that the completion message used the input-file count even though the loop caught individual import exceptions and continued. A file that returned no objects could also leave the final message overstating success.

### Failed assumption / approach

Reaching the end of the batch, or obtaining some objects, was treated as equivalent to importing every input successfully.

### Root cause

Confirmed directly in the before/after implementation: len(input_paths) measured attempts, not successful per-file results. Caught failures were printed but were not included in the user-facing aggregate outcome.

### Correction

Record a terminal result for each attempted input, distinguishing imported objects, an exception, and no produced objects. Derive the summary from those results, preserve per-file details, and propagate partial failures into the persisted scene outcome and user-facing warning.

### Verification

The reviewed committed regression supplies one successful import, one RuntimeError, and one empty result. It asserts three distinct statuses, only the successful object in the returned collection, and totals of one imported out of three. UI/outcome assertions also require the partial-failure indicator. This curation verified the code and test definitions; it did not execute that Blender pipeline or establish a new runtime pass.

### Reusable rule

Never calculate batch success from the number of inputs or from completion of the loop. Test a mixed success/exception/empty-result batch and ensure per-item outcomes reach both persisted reports and the visible overall status.

### Applicability

Best-effort batch importers and converters. An empty result is a failure only when the input contract requires produced objects; legitimate no-output operations need their own explicit success state.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-059 — Include Editor window lifecycle side effects in test isolation

- Source area: unity
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: unity-editor-preview-fixtures

### Intent

Test preview behavior without leaving shared product settings or generated assets changed.

### Observed failure

An EditMode suite left a persisted settings asset changed after a preview-window test. The diff contained migrated Effect selections, even though the test was intended to inspect playback rather than edit shared settings.

### Failed assumption / approach

Creating an Editor window was treated as harmless setup. Isolation focused on objects directly edited by the test and did not cover lifecycle callbacks executed during window creation.

### Root cause

Confirmed in the recorded source/log diagnosis: EditorWindow.OnEnable loaded shared settings and ran an authoring migration, marking them dirty. A later global asset save could persist that change. This was separate from a stale generated-shader failure in the same suite.

### Correction

The reviewed test-only change snapshots settings, generated shader and shared Material before the first window lifecycle callback, prepares current generated inputs, then restores and verifies raw bytes, metadata and loaded state after synchronous refresh. Prefer fixture-owned settings when the supported entrypoint permits them; do not disable legitimate authoring migration just to satisfy a test.

### Verification

The recorded full run had 122/123 test cases pass but independently failed the unexpected-asset-change gate. The log stack and asset diff identified the migration path. A test-only isolation change was reviewed, but the inspected checkpoint explicitly had no subsequent Unity compile/run proving restoration; the correction must not be described as runtime-verified.

### Reusable rule

Audit OnEnable, initialization, migration and later global-save effects before creating Editor windows in tests. Isolate shared assets before those callbacks, restore both bytes and loaded state, and require post-run asset checks independently of assertion results.

### Applicability

Unity Editor tests that open windows, custom Inspectors or other callback-driven tooling. This lesson does not imply every authoring migration is erroneous, nor that restoring one settings file proves all side effects are isolated.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-060 — Successful decompression does not prove complete GZip framing

- Source area: other
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: dotnet-archive-validation

### Intent

Audit an archive without extraction while enforcing the application's bounded single-member GZip framing contract.

### Observed failure

A truncated trailer could still produce a complete decompressed payload. Additional controls appended garbage with a copied valid footer, or an empty additional GZip member; those malformed or unsupported streams were accepted by the earlier audit.

### Failed assumption / approach

Successful GZipStream decompression and reading a footer at the end of the overall input were treated as evidence that the input contained exactly one complete, valid GZip member.

### Root cause

Confirmed by recorded failing regressions: decoder output was insufficient to establish the exact consumed compressed-stream boundary. Checking the final bytes did not prove they immediately followed the decoded member, and transparent concatenation did not enforce the application's one-member policy.

### Correction

Validate the supported header, establish the actual DEFLATE endpoint, compute CRC32 and expanded size over the decoded bytes, verify the immediately following trailer, and enforce the intended EOF/member policy. Preserve archive size and entry limits. The recorded implementation used a one-byte bounded feed to avoid read-ahead; this mechanism is not a general performance recommendation.

### Verification

The recorded baseline failed two focused framing controls. The corrected focused suite passed 11/11 and the full non-Unity harness passed 328/328, including empty-member prefix/suffix cases. Large-package performance and Unity/Mono behavior were not established by that checkpoint.

### Reusable rule

Do not equate decompression success with container integrity. Include truncated trailers, wrong CRC/size, copied-footer garbage, and extra-member controls, and verify the actual member endpoint rather than only the file's last bytes.

### Applicability

This guidance applies to auditors with an explicit single-member policy. Concatenated GZip members can be valid for other consumers; reject them when the application contract requires a single member, not because concatenation is inherently malformed.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

