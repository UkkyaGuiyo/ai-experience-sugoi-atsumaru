# Legacy failure lessons migration — Batch 01

Review status: PENDING_REVIEW

Generalized lessons migrated from a retired legacy failure-lesson repository. Source `confirmed` status is provenance only; Atsumaru independent review is still pending. No raw logs, conversations, private repository identifiers, personal paths, credentials, or project-specific artifacts are intentionally carried over.

## LFA-001 — An archive extension does not prove a regular file

- Source area: python
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: archive-discovery

### Intent

Discover sibling archive providers without changing provider identity or resolution rules.

### Observed failure

An archive reader received a directory whose name ended in the expected archive extension. Normal import failed before semantic parsing.

### Failed assumption / approach

Candidate generation treated a matching suffix as sufficient evidence that the path was an archive file. A second inspection entry point had the same assumption.

### Root cause

Confirmed in the tested discovery paths: directories passed extension filtering and were supplied to the archive reader. This was a candidate-type defect, not proof of missing archive dependencies.

### Correction

Require a regular file at each candidate boundary before archive inspection. Preserve existing provider-resolution rules and inspect all entry points that can supply candidates.

### Verification

Public directory-named-like-archive controls reproduced failure at both boundaries. The corrected focused suite passed; an affected real input then passed normal import and unchanged save/reopen. Roundtrip acceptance remained separate.

### Reusable rule

Do not infer filesystem type from a suffix. Test directories with archive-like names at every discovery entry point before diagnosing package dependency resolution.

### Applicability

Local archive and provider discovery in Python or similar tools. A file-type check alone does not establish archive validity, permissions, content identity, or race-free access.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-002 — Separate callback execution from effective target fidelity

- Source area: unity
- Source type: diagnosis
- Source certainty: confirmed
- Source status: active
- Scope: model-importer-numeric-diagnostics

### Intent

Determine why imported Mesh data lost positive skin influences even though exported FBX and authored receipts preserved them.

### Observed failure

Exact receipt-keyed target comparison reported missing influences. A public importer getter returned a default-like minimum value, suggesting either a callback/timing problem or a simple small-weight cutoff.

### Failed assumption / approach

Callback absence, startup compilation timing, a getter value, or a four-influence cap looked plausible without observing the actual callback and target associations.

### Root cause

The importer loss mechanism remains unknown. Confirmed diagnostic limits: an exact-input disposable control recorded callback invocation and zero-minimum assignment, then forced reimport after helper compilation. Target associations remained identical. Some points lost influences despite having at most four, others retained more than four, and retained weights smaller than missing weights refuted a global monotonic cutoff in the examined raw and normalized domains.

### Correction

Improve diagnosis rather than guessing a production fix. Join authored, generated and imported influences by existing exact control-point/bone receipts; record assigned values separately from public getters. Preserve the strict RED and unresolved mechanism.

### Verification

The control locked model and policy revisions, observed callback phases, verified original inputs unchanged, and compared exact target association dictionaries before and after forced reimport. Variable-length weight APIs excluded an observer limited to four entries. Representation comparison remained not reached when its prerequisite association gate failed.

### Reusable rule

Prove exact callback invocation and assigned settings, then measure actual target data before blaming timing or a getter. Refute simple cutoff/cardinality explanations with retained-and-missing counterexamples; never widen tolerances or claim a downstream numeric stage ran after its prerequisite gate refused.

### Applicability

Unity public ModelImporter and other callback-driven data pipelines. The verified result is the diagnostic method and exclusion of those explanations in scope, not a universal Unity threshold bug or a solved import mechanism.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-003 — Explicit triangles still need destination importer controls

- Source area: unity
- Source type: diagnosis
- Source certainty: confirmed
- Source status: active
- Scope: synthetic-fbx-topology-transport

### Intent

Preserve Blender final explicit triangle connectivity through FBX into Unity.

### Observed failure

A synthetic mesh exported three explicit triangles, including a zero-area triangle with distinct control-point identities and coincident positions. Unity 2022.3.22f1 retained two. FBX still contained all three.

### Failed assumption / approach

Freezing final triangles before FBX export was treated as sufficient to preserve destination topology. An existing exact-revision Skin importer policy changed weight settings but left vertex welding enabled.

### Root cause

Confirmed causal setting effect in this bounded control: identical FBX and initial meta with only ModelImporter.weldVertices changed from true to false retained three instead of two triangles. Other observed settings were unchanged and original meta/settings were restored. Unity's internal removal mechanism remains unknown.

### Correction

A disposable copy of the exact-revision opt-in importer assigns weldVertices=false after revision validation. This is a scoped candidate, not a reason to change every imported asset globally.

### Verification

The unchanged helper's no-policy, exact-policy and repeated imports all produced 3-to-2 topology mismatch. The one-line candidate retained 3-to-3 topology exactly after policy application and repeat import; its no-policy control still failed. Existing control-point comparisons also reported UV and measured Skin numeric sets exact. Console error/warning counts were zero and original source/helper hashes were unchanged.

### Reusable rule

When explicit exported triangles disappear downstream, compare authored, serialized and imported topology before blaming export staging. Test destination weld settings with identical bytes and one changed variable, preserve and restore settings, and measure actual Mesh topology. Scope any policy change to proven inputs; do not filter triangles or relax acceptance to manufacture a pass.

### Applicability

Confirmed for this synthetic zero-area/coincident-position FBX control in Unity 2022.3.22f1. It does not prove all topology problems, Shape Keys, full Skin identity or deformation fidelity are fixed. A separate missing-influence control was unaffected by disabling welding and must remain a separate unresolved failure.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-004 — Use a same-input short-path control before blaming content

- Source area: python
- Source type: environment
- Source certainty: confirmed
- Source status: active
- Scope: windows-archive-and-oracle-staging

### Intent

Extract identical archive bytes and copy a disposable Editor Oracle on Windows.

### Observed failure

Extraction and a later Oracle copy failed on deeply nested destination paths. Source files and their parent directories existed; this initially obscured later product measurements.

### Failed assumption / approach

A missing-file exception was treated as if it necessarily indicated absent archive content or broken product input. Reusing a long campaign directory reproduced the environment failure in a different staging operation.

### Root cause

Confirmed bounded finding: the destination-path environment changed the outcome. Identical archive bytes extracted without errors under a short root; the identical Oracle copy also succeeded after shortening its target. The exact OS/library long-path policy was not isolated and remains unknown.

### Correction

Keep the failed attempt and create a fresh short disposable target. Lock input hashes, preserve the original source, and rerun the same operation. Label subsequent product verdicts separately from the environment retry.

### Verification

Long and short controls used identical input hashes. The short extraction completed with no errors; a separate short Oracle copy preserved every source lock. No global Windows policy or archive reader behavior was changed.

### Reusable rule

When Windows staging fails with missing-path errors, first compare identical input under a fresh short destination. Record actual source existence and target length; do not patch content or change global OS settings before isolating the path effect.

### Applicability

Windows extraction, generated project staging, and nested output trees. This does not imply every missing-file error is a length limit or that one numeric path threshold applies to every API.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-005 — Unity GPU render tests require a graphics device

- Source area: unity
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: unity-shader-render-validation

### Intent

Run shader image comparisons from Unity batch mode.

### Observed failure

A GPU render validator produced many failing image checks when Unity was launched with `-nographics`. The editor log identified the active backend as Null Gfx, so the validator was not exercising the intended graphics path.

### Failed assumption / approach

Batch mode was treated as sufficient for headless GPU rendering, and `-nographics` was added to make the run non-interactive.

### Root cause

Confirmed: `-nographics` selected Unity's Null Gfx backend. That backend cannot provide the GPU rendering surface the image validator requires, so its failures were invalid evidence about shader output.

### Correction

Run GPU image validation with graphics enabled. Keep batch mode if useful, but omit `-nographics`; inspect the Unity log for the selected graphics device/backend before interpreting image failures.

### Verification

The same GPU render suite was rerun with graphics enabled on the workstation's graphics adapter. Effect-specific image probes then passed; the remaining failure was independently traced to a missing nested mesh in a separate fixture.

### Reusable rule

For any Unity test that reads rendered pixels, do not pass `-nographics`. Confirm the log shows a real graphics backend before treating image comparisons as shader evidence.

### Applicability

Applies to Unity GPU/image render tests. It does not apply to compile-only or other tests that do not render pixels; those may use `-nographics` if their requirements permit it.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-006 — Do not defer hierarchy identity repair beyond an EditMode test frame

- Source area: unity
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: unity-editor-object-change-handling

### Intent

Assign independent serialized identity when Unity publishes a new Scene hierarchy containing an authoring component.

### Observed failure

A repair scheduled through `EditorApplication.delayCall` did not run within the yielded frames of a batch EditMode UnityTest. The test observed the creation event, but the duplicated object still shared its source identity and Settings.

### Failed assumption / approach

Deferring work to `delayCall` was assumed to guarantee execution before the next EditMode test-frame assertions.

### Root cause

Confirmed for the tested Unity 2022.3.22f1 batch EditMode path: the delayCall callback was not observed during the yielded test frames, while synchronous processing of the published event stream completed and passed the same assertions. This does not establish that delayCall never runs in other Editor contexts.

### Correction

Process only the newly created hierarchy directly after iterating the published `ObjectChangeEvents` stream. Record changes with Undo, and suppress identity generation when the same frame reports Undo/Redo so redo restores the recorded value.

### Verification

An isolated Avatar SDK 3.10.5 EditMode run passed tests for hierarchy duplication, independent deep Settings, Undo/Redo restoration and prefab placement. The created-object event was observed; synchronous event handling passed the identity assertions.

### Reusable rule

When an EditMode test requires an object-change repair in the next yielded frames, verify that deferred callbacks actually execute within that test loop. If not, process the published event synchronously and explicitly cover Undo/Redo to avoid reassigning restored identities.

### Applicability

Applies to Unity Editor `ObjectChangeEvents` handling tested in batch EditMode at Unity 2022.3.22f1. Do not generalize it into a ban on `EditorApplication.delayCall` for ordinary interactive Editor work.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-007 — Wait for a Unity Editor process to release its project before relaunch

- Source area: unity
- Source type: workflow
- Source certainty: confirmed
- Source status: active
- Scope: unity-project-process-lifecycle

### Intent

Run a Unity batch validation again against a project that had just been used by another Editor process.

### Observed failure

The second Editor printed: "It looks like another Unity instance is running with this project open. Multiple Unity instances cannot open the same project." It then exited before running the requested validation.

### Failed assumption / approach

The previous run's log had printed its batch-mode completion message, so a new Editor was started without first confirming that the process holding the same project path had exited.

### Root cause

The first Unity process still held the exact project open when the second process attempted to initialize it. The second process log identified the duplicate project lock directly.

### Correction

Wait for the owning Unity process to exit. Before relaunching, inspect running Unity command lines and confirm that none targets the same project directory.

### Verification

The duplicate launch reproduced the explicit project-lock message. After the earlier process exited, a single batch Editor ran the validation and completed successfully.

### Reusable rule

Before starting Unity on a project, check all running Unity process command lines for that exact project path. Do not treat a completion line in the log as proof that the process has released the project; wait for process exit first.

### Applicability

Applies when reopening the same Unity project from batch mode or the interactive Editor. It does not prohibit separate Unity processes that target different projects, such as asset-import workers.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-008 — Avoid mirroring stale generated assets into Unity verification projects

- Source area: unity
- Source type: workflow
- Source certainty: confirmed
- Source status: active
- Scope: unity-project-source-sync

### Intent

Synchronize product source into a separate Unity verification project before compiling or rendering.

### Observed failure

A broad `robocopy /MIR` sync removed verification-only files and folders from the target project. It also copied an older generated shader from the source checkout over the shader generated in the verification project.

A later recorded EditMode recurrence used a generated shader missing four palette/lookup declarations. The corresponding Effect test failed before another test eventually regenerated the shader.

### Failed assumption / approach

The target project was treated as a disposable exact mirror, and all files under the product subtree were assumed to be equally authoritative in both directions.

The recurrence also assumed that generation performed somewhere in the suite would prepare inputs for every test, regardless of execution order.

### Root cause

Confirmed: `/MIR` mirrors deletions as well as copies, so target-only verification artifacts were removed. The product checkout also contained a generated shader that was stale relative to the currently imported modules, and the sync overwrote the freshly generated target shader with that stale file.

In the recurrence, source inspection showed that explicit Effect selection and baker enablement were correct. The loaded shader lacked the required properties, and the recorded first generation occurred only after the failed assertion. This supports stale fixture input rather than changing the Effect-selection contract to make the test pass.

### Correction

Copy only the needed source files into the isolated verification project. Avoid `/MIR` when the target contains verification-only content. After syncing source, run the project's shader-generation step again before rendering or validating generated output.

Prepare and verify generated inputs before the first dependent test, including focused runs; do not depend on an unrelated later test to generate them. A reviewed recurrence fix added suite-level preparation and explicit property/binding assertions while preserving the product selection rules.

### Verification

The target-only files were observed missing after the mirror, and the generated shader was corrected by running the generator after source synchronization. Subsequent GPU checks used the regenerated target shader.

For the later recurrence, the inspected report records 122/123 passing EditMode cases, a missing lookup texture in the failed case, the stale shader declarations and the generation order. Its test-only preparation/restoration change had been reviewed but not compiled or rerun in Unity at that checkpoint. Do not carry the earlier GPU result forward as proof of this later correction.

### Reusable rule

Before synchronizing into a verification project, confirm the resolved target path and whether it contains target-only data. Prefer non-deleting copy behavior; if generated outputs are included in the source copy, regenerate and check them in the target before the first dependent test, including focused runs. Never rely on another test to prepare shared generated inputs.

### Applicability

Applies to Unity source copies that include generated assets or when verification projects contain test-only content. It does not mean `/MIR` is always wrong; use it only when exact target mirroring is intended and target-only files can be deleted safely.

### Rejected alternatives

Do not assume a successful source copy leaves generated output current or preserves verification-only target files.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-009 — Separate movement intent from attack facing

- Source area: unity
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: directional-combat-input

### Intent

Select front and backward aerial attacks relative to character facing.

### Observed failure

Opposite horizontal input immediately flipped facing in air, so backward aerial attack could not be selected.

### Failed assumption / approach

Movement direction was used to update orientation before interpreting attack intent.

### Root cause

Confirmed: the reference frame changed in response to the same input that was meant to select the backward attack.

### Correction

Under this game's rules, update facing from grounded movement only and retain the airborne attack reference frame.

### Verification

Five aerial attack variants were rechecked through actual Input Actions after correction.

### Reusable rule

Specify whether directional input changes orientation or selects an action relative to existing orientation. Test opposite input after takeoff before classifying the attack.

### Applicability

Directional combat with persistent airborne facing. Grounded-only facing is a design-specific correction, not a universal control rule; physical gamepad feel was not established.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-010 — Animation addresses must be unique in the target scheme

- Source area: unity
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: animation-binding-addresses

### Intent

Generate animation clips targeting a selected renderer.

### Observed failure

Distinct same-name sibling renderers produced identical animation binding addresses.

### Failed assumption / approach

Selecting distinct object identities was assumed to imply independent animation addressing.

### Root cause

Confirmed: the destination binding key used hierarchy path plus component type, which did not distinguish those siblings.

### Correction

Recompute the path, count matching path/type renderers and reject ambiguous bindings before output or descriptor writes.

### Verification

A duplicate-sibling fixture confirmed identical calculated paths, rejection and unchanged outputs/descriptor. Existing different-parent cases remained valid.

### Reusable rule

Validate uniqueness in the destination's actual addressing scheme. Stable source IDs cannot resolve ambiguity that the destination format cannot represent.

### Applicability

Unity path/type animation bindings. Repeated leaf names under distinct parents are not automatically ambiguous; this is separate from authoring-ID duplication.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-011 — Asset rollback must restore metadata identity

- Source area: unity
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: generated-asset-transactions

### Intent

Roll back generated menu assets after a later build step fails.

### Observed failure

Restoring serialized asset content alone lost metadata-backed reference identity after generated pages were deleted.

### Failed assumption / approach

An asset's payload bytes were treated as its complete transactional state.

### Root cause

Confirmed source gap: rollback snapshots omitted .meta identity.

### Correction

Snapshot and restore content and metadata before forced import; check transitive references after recovery.

### Verification

An injected fault after generation/page deletion restored asset bytes, metadata bytes, GUID/local fileID and root dependencies. The historical validator passed its bounded rollback controls.

### Reusable rule

Include identity metadata and reference graphs in asset snapshots. Inject failure after deletion and verify references, not just content equality.

### Applicability

Unity Editor generated assets. This is distinct from source-sync deletion risk and does not prove every filesystem or editor failure boundary.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-012 — Coordinate basis conversion must include scale

- Source area: blender
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: semantic-transform-conversion

### Intent

Convert semantic transform chains between coordinate systems.

### Observed failure

Nonuniform real-input matrices differed; a three-node synthetic chain failed an independent matrix oracle.

### Failed assumption / approach

Position and rotation were converted while scale remained in its original axis order.

### Root cause

Confirmed: under the tested basis mapping, diagonal scale required axis permutation while retaining signs.

### Correction

Change scale ordering consistently with the basis; leave native FBX handling separate.

### Verification

Nonuniform, negative and zero-scale controls failed before correction and passed six local/world conjugation checks afterward. Fresh import plus save/reopen matched 271 semantic identities/parents and local bases within 1e-5.

### Reusable rule

Test basis conversion using independent matrix conjugation and nonuniform, negative and zero scales. Uniform-scale examples cannot expose axis-order defects.

### Applicability

Tested semantic reconstruction in Blender 5.2.1. Previously saved scenes were not silently migrated; native geometry fidelity was not proved by these matrix checks.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-013 — Dependency identity must include the binding role

- Source area: blender
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: dependency-binding-resolution

### Intent

Resolve one image provider into multiple material uses, and preserve the exact consumer occurrence when a provider arrives later.

### Observed failure

A synthetic material using the same image for Base Color and Emission retained only one dependency.

A later FBX-material source audit found records with a provider GUID and source slot/path but no consumer object or mesh receipt. The generic resolver could not identify a safe native destination slot from those records. A separate grouped fixture selected a Prefab wrapper with no mesh data rather than the native Mesh object.

### Failed assumption / approach

The provider GUID was treated as the complete binding identity.

In the later diagnosis, discovering the provider or finding a wrapper with the expected Prefab ID was liable to be treated as proof of the actual material-slot consumer.

### Root cause

Confirmed: the original record key omitted role/property, and a GUID-to-role map collapsed distinct uses of one provider.

The later source-level finding is different evidence for the same identity principle: the FBX external-material route omitted consumer occurrence evidence required by the resolver. The separate Prefab fixture lacked a MeshFilter, so its renderer-to-native-mesh relationship was not established. A provider identity, wrapper identity and native consumer identity are not interchangeable.

### Correction

Key each binding by role and property as well as provider identity; classify canonical properties before fallback.

The reviewed follow-up requires retaining the source package/FBX identity, exact object/mesh occurrence, target slot and ownership evidence for deferred material binding. Keep Prefab-renderer and FBX external-material routes separately testable. Do not select a destination by display name or by there being only one apparent candidate. This additional material route remained an identified implementation gap, not a completed fix.

### Verification

The old texture implementation failed the minimal fixture. Both bindings survived repeated resolve and fresh-process save/reopen after correction. Removing role/property again in an in-memory mutation made the focused test fail.

The material follow-up was checked through recorded source review and a failing grouped Blender fixture. Comparing two revisions reproduced the same wrapper failure, establishing only that the change between those revisions did not introduce it. No corrected late-material-binding runtime pass was recorded; the proposed missing/wrong/correct-provider, user-edit, repeated-resolve and save/reopen controls remained future work.

### Reusable rule

Separate provider identity from binding occurrence, including role/property and the exact consumer object/slot when relevant. Test same-provider different-role uses and deferred-provider binding, checking realized connections as well as dependency records. Refuse ambiguous consumers rather than resolving them by names or wrapper identity.

### Applicability

The original texture route was verified in Blender 5.2.1 synthetic resolution. The follow-up concerns source-level FBX/Prefab material binding and must not be generalized into a claim that arbitrary late binding or shader/export fidelity is implemented.

### Evidence boundaries for subsequent Knowledge entries

- **Reproduced within the recorded texture route:** a single provider used for distinct material roles no longer collapses those bindings; repeated resolution and save/reopen were checked.
- **Not yet demonstrated for the separate FBX external-material route:** receipt records still lacked a proven exact native consumer/slot mapping. The uncorrected grouped Prefab fixture must not inherit the texture-route PASS.
- Each implementation route requires its own evidence type, reproduction status, and applicability assessment before formalization; the source's confirmed status applies only to its individually described observations.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-014 — Verify the committed artifact in a clean checkout

- Source area: git
- Source type: workflow
- Source certainty: confirmed
- Source status: active
- Scope: source-handoff-completeness

### Intent

Recover and hand off a coherent tested source revision.

### Observed failure

The dirty workspace passed 238 tests while committed source had 172. A first recovery commit still imported parser APIs absent from the commit.

### Failed assumption / approach

Local passing tests were taken as evidence that the committed artifact was self-contained.

### Root cause

Confirmed: required semantic parser APIs remained only in a modified workspace file.

### Correction

Recover the specific missing dependency as an atomic change, then validate a fresh HEAD-only checkout with the correct package root.

### Verification

The clean checkout exposed the missing import. After dependency recovery, committed-source imports, the expected test population and compileall passed. Blender/Unity acceptance was not run in this recovery.

### Reusable rule

Test the exact committed artifact from a clean checkout and reconcile test-population differences. Do not sweep unrelated dirty files into a commit to make local results reproducible.

### Applicability

Source handoffs with mixed tracked/untracked changes; clean Python checks do not establish application-runtime acceptance.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-015 — Compiled component types still need resolvable script assets

- Source area: unity
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: generated-scene-components

### Intent

Generate playable scenes using newly compiled component types.

### Observed failure

Scene loading reported Unknown Behaviour after several public MonoBehaviour types were initially placed in one source file.

### Failed assumption / approach

Successful C# compilation was treated as sufficient for serialized component resolution.

### Root cause

Confirmed for the observed generated-scene path: component definitions did not align with Unity's script-asset resolution boundary.

### Correction

Split serializable component types into matching files and regenerate scenes through their source builder.

### Verification

Three regenerated scenes had zero missing scripts, broken prefabs or other validation issues; final console and Windows build checks were clean.

### Reusable rule

Verify serialized scene reload and component references after code generation. Keep component file/script-asset identity coherent with generated scene references.

### Applicability

This does not forbid multiple ordinary C# types per file or establish all Unity serialization cases. The evidence is the tested scene-generation path.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

