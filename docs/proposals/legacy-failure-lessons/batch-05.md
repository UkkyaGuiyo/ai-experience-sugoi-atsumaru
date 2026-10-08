# Legacy failure lessons migration — Batch 05

Review status: PENDING_REVIEW

Generalized lessons migrated from a retired legacy failure-lesson repository. Source `confirmed` status is provenance only; Atsumaru independent review is still pending. No raw logs, conversations, private repository identifiers, personal paths, credentials, or project-specific artifacts are intentionally carried over.

## LFA-061 — Regenerate run-owned fixtures instead of relying on cleaned predecessors

- Source area: unity
- Source type: workflow
- Source certainty: confirmed
- Source status: active
- Scope: isolated-test-fixture-lifecycle

### Intent

Construct a fresh Unity verification project using approved synthetic shader and assembly-definition fixtures.

### Observed failure

Preparation stopped because an old manifest listed twelve fixture paths whose assets and metadata were absent. An initial diagnostic described a malformed manifest when a missing folder metadata read threw.

### Failed assumption / approach

A retained historical manifest was assumed to imply that the previous run's disposable fixture tree still existed. Restoring those files into the old verification project was considered before checking cleanup provenance.

### Root cause

Confirmed from the recorded cleanup history: the prior run intentionally removed its owned fixtures and restored the historical manifest. The manifest described a historical inventory, not a live readiness guarantee.

### Correction

Check listed paths and metadata before hashing and distinguish missing inputs from malformed manifests. Generate canonical fixture payloads with fresh unique GUIDs inside the new run's isolated template, and bind a new manifest to the actual source revision and generated hashes. Leave the old project read-only.

### Verification

Recorded regressions verify canonical payload hashes, GUID uniqueness, fresh manifest consistency, tamper rejection, and preservation of the old project and its intentionally absent assets. The preparation checkpoint passed 317/317 in the non-Unity harness; that checkpoint did not establish Unity execution.

### Reusable rule

Treat a manifest as evidence about a specific inventory, not proof that its files still exist. Recreate run-owned fixtures from reviewed definitions in a fresh owned location instead of depending on artifacts that a previous run was entitled to delete.

### Applicability

Disposable integration fixtures and isolated verification projects. Do not regenerate missing user assets, purchased content, or irreplaceable source data, and do not silently replace an unexplained hash mismatch with freshly trusted inputs.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-062 — Separate Unity metadata line endings from GUID validation

- Source area: unity
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: unity-metadata-parsing

### Intent

Validate Unity asset metadata before constructing an isolated verification project.

### Observed failure

Valid metadata using CRLF line endings was rejected as an invalid GUID before Unity launched. The same parser accepted LF metadata.

### Failed assumption / approach

A multiline regular expression required the GUID capture to be followed immediately by the line-end anchor, without accounting for the carriage return preceding LF.

### Root cause

Confirmed by source inspection and the recorded input audit: CRLF left a carriage return outside the expected 32-character hexadecimal identifier, so a valid line failed the expression. This was a line-terminator incompatibility, not evidence of a corrupt identifier.

### Correction

Accept one optional carriage return outside the GUID capture. Retain the exact identifier syntax required by the tool, the exactly-one-GUID-line rule, duplicate-GUID checks, and the original asset/meta byte hashes. Do not normalize the entire metadata file merely to make an identity check pass.

### Verification

Committed regressions cover successful preparation with LF and CRLF metadata and rejection of a malformed 31-character GUID with CRLF. The checkpoint records a 314/314 non-Unity harness pass; Unity was not launched for that checkpoint.

### Reusable rule

Treat line terminators separately from identifier content. Test LF, CRLF, malformed identifiers, and duplicate identity declarations without weakening content or hash validation.

### Applicability

Line-oriented Unity metadata readers. The observed tool required lowercase hexadecimal GUIDs; this lesson does not establish that every Unity producer must use that casing or that arbitrary whitespace should be accepted.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-063 — Keep test, process, artifact and postflight results independent

- Source area: agents
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: automated-validation-orchestration

### Intent

Report automated validation accurately when tests, host execution and cleanup each have separate requirements.

### Observed failure

One recorded Unity run passed 271/271 tests and exited normally, but its outer wrapper returned failure because it expected an obsolete cleanup message. In a separate workflow, 31/31 tests and a zero Unity exit still failed overall acceptance because postflight detected an unexpected ProjectSettings change.

### Failed assumption / approach

A single wrapper exit, test-pass count or native process exit was liable to be treated as the complete validation result.

### Root cause

Confirmed by the separate execution records: test assertions, compiler results, process lifecycle, protected-input changes, cleanup evidence and reporting predicates are different contracts. Success or failure in one does not establish the others.

### Correction

Record each required gate with source/run identity and fresh evidence. Diagnose wrapper/reporting failures separately from product assertions. Preserve original failed runs and attribute any independently verified recovery explicitly; do not rerun an expensive application merely to repair a stale reporting predicate, or erase a real postflight failure because tests passed.

### Verification

The first record separately checked the completed test XML, native exit, removed owned paths, restored manifest and unchanged inputs after the wrapper mismatch. The second retained overall failure despite passing tests. A later package smoke recorded all of its own required gates as passing, without retroactively changing either earlier result. These are recorded observations from distinct runs, not one combined pass.

### Reusable rule

Report test results, compiler status, native exit, owned-process completion, artifact checks and postflight separately. Claim overall success only when every required gate for the same run is satisfied; label unexecuted or blocked stages rather than treating them as passes.

### Applicability

Multi-stage build/test/export automation. Required gates depend on the operation; a diagnostic-only run and a release run need not have identical acceptance criteria, but those criteria must be explicit before interpreting results.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-064 — A changed cwd does not revoke an approved work root

- Source area: agents
- Source type: workflow
- Source certainty: confirmed
- Source status: active
- Scope: delegated-work-root-recovery

### Intent

Continue an approved isolated diagnostic from a delegated handoff while preserving the original checkout.

### Observed failure

The resumed assistant found an older checkout at cwd, did not find the diagnostic files there, and stopped with an environment-unavailable claim. The handoff already named an approved independent publication root in the writable workspace.

### Failed assumption / approach

The assistant treated cwd as the only permitted checkout and invented a prohibition on using the existing independent root.

### Root cause

Confirmed: cwd and the authorized working root were conflated. Missing files in one checkout did not establish that the approved root or remote artifact was inaccessible.

### Correction

Read the explicit root's instructions, verify its actual repository remote, and use the regular approved execution path. Preserve the older checkout and materialize an exact remote revision into an isolated diagnostic directory with source and byte hashes.

### Verification

The named publication root existed with the expected remote. A normally approved fetch succeeded and supplied the committed diagnostic. The older checkout remained unchanged. A later launch prerequisite stopped on measured memory availability before starting an Editor; this was recorded separately from permission or source availability.

### Reusable rule

Treat cwd as execution context, not as a revocation of explicit prior authorization. Check named approved roots and artifact revisions before reporting an environment blocker. Use formal approval for restricted operations, report actual denial details, and never bypass access controls.

### Applicability

Applies when the user or handoff explicitly authorizes a separate work root. It does not authorize arbitrary new roots, overwrites, deletion, or retrying a rejected operation through a bypass.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-065 — Diagnostic outputs must not clobber inputs

- Source area: python
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: file-based-diagnostic-tools

### Intent

Write a machine-readable result from a diagnostic script that reads user-supplied source files.

### Observed failure

A review found that a probe used `Path.write_text()` for its result without checking whether the destination resolved to an input file. The operation could overwrite the package or currently opened scene. It also replaced an existing output from an earlier run.

### Failed assumption / approach

The output option was treated as a distinct path because it had a separate command-line argument. No filesystem check enforced that assumption.

### Root cause

Confirmed by direct code inspection: ordinary text write mode truncates an existing destination, and lexical argument separation does not prevent path aliases.

### Correction

Resolve and normalize the output and protected input paths before work; reject aliases; create the result with exclusive-create mode (`x`) so an existing file fails closed. Bind a fixed-evidence reproduction to the expected source fixture hashes when it claims to reproduce one exact result.

### Verification

Seven focused path tests passed. They reject an output alias of a protected input, aliases between outputs including a derived export path, and existing output files while confirming existing bytes remain unchanged. Distinct new paths are accepted. Python syntax compilation and `git diff --check` passed.

### Reusable rule

For file-based probes, canonicalize every declared and derived output against protected inputs and against other outputs before reading or writing, then create reports exclusively instead of replacing them. If a script claims to reproduce a fixed fixture, assert the fixture hash; otherwise label it as a general inspector and avoid fixed-result claims.

### Applicability

Applies to diagnostic, conversion, and evidence scripts that write user-selected output paths. It does not replace input validation or atomic publication when partially written output must also be prevented.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-066 — Dynamic imports must not reuse unverified modules

- Source area: python
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: source-bound-reproduction

### Intent

Run an evidence probe against a selected source checkout from an embedded Python process that may already have imported the same package name.

### Observed failure

A probe replaced only the package root in `sys.modules`. Python could retain child modules such as `package.submodule` from an earlier import, so the probe could execute code from a different checkout than the path it reported.

### Failed assumption / approach

Replacing the root package object was assumed to make subsequent imports use the selected source tree.

### Root cause

Confirmed by import semantics: `sys.modules` caches each fully qualified module independently; assigning a new root does not invalidate cached child entries.

### Correction

For source-bound evidence runs, fail closed when the target package name or any child module is already present. Run in a clean interpreter namespace; do not unload or replace the host application's loaded package. Test both the cached-child rejection and the clean-load path.

### Verification

Focused tests inserted a fake cached child module, verified the loader rejected it without replacing it, and verified loading with an empty namespace. Eight total output/import-safety tests passed in the embedded Python interpreter.

### Reusable rule

When dynamically importing a chosen checkout, inspect the full root-and-child module namespace first. Reject unverified cached modules rather than replacing only the root; avoid unloading application modules to make a probe pass.

### Applicability

Applies to plugin, addon, and evidence tooling that imports source trees into a long-lived Python process. It is not a claim that every module cache is unsafe; cached modules are acceptable when their exact provenance and source revision are independently validated.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-067 — Redact binary FBX strings by their declared length

- Source area: blender
- Source type: tooling
- Source certainty: confirmed
- Source status: active
- Scope: fbx-binary-path-anonymization

### Intent

Remove absolute workspace paths from a binary FBX copy while preserving its structure and geometry for a downstream verification.

### Observed failure

A byte-regex replacement that ran from a drive-letter path through the next null byte produced an FBX that Blender could not parse and reported a nested-block sentinel error.

### Failed assumption / approach

The path was treated as a null-terminated byte string. Binary FBX stores string properties with an `S` type marker and a length prefix, and arbitrary binary fields can follow the string before a null byte.

### Root cause

The regex replaced bytes beyond the string payload, corrupting later binary structure. This was reproduced by the failed import; preserving the declared string length fixed that failure.

### Correction

For each candidate path, require the preceding `S` marker, read the little-endian 32-bit payload length, validate the full payload and expected suffix, and replace only that payload with an equal-length neutral value. Fail closed if any check is unexpected.

### Verification

The redacted copy retained the original byte length; byte comparison showed that only the matched string payload ranges changed. Blender imported the copy, and a geometry/winding comparison completed on that copy.

### Reusable rule

Do not redact binary FBX paths with null-terminated regex spans. Parse and validate the string-property marker and declared length, replace only the payload with equal-length bytes, then verify both structural import and the downstream semantic check.

### Applicability

Applies to path redaction in binary FBX files with the described string-property encoding. Do not generalize this replacement code to other FBX versions, binary formats, or arbitrary properties without format-specific validation.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-068 — Bind completion evidence and verify identity readers

- Source area: unity
- Source type: workflow
- Source certainty: confirmed
- Source status: active
- Scope: headless-read-only-mcp-runner

### Intent

Allow normal exit only for the headless Editor launched by the current bounded read-only MCP run.

### Observed failure

Independent source review found that a reusable runner accepted successful same-root MCP JSON without binding it to the current run, PID or process start. Its duplicate check also filtered by the selected Unity executable and missed other Editor versions.

### Failed assumption / approach

Same-root successful reads and a session-present flag were treated as current-run evidence. Matching the requested executable was treated as a sufficient inventory of open Editors.

### Root cause

A stable Project path survives across runs, and different Unity installations can target the same Project. Neither identifies a particular live process. A boolean session-present field does not establish session continuity across requests.

### Correction

Bind evidence to a fresh run GUID, PID, UTC process start and canonical Project root; match a run-bound controller connection log, timestamp acquisition, and verify a stable HTTP session after each sequential request. Use a fixed run-owned evidence path, exclusive creation and a one-shot consume receipt. Reject stale, future, mismatched or replayed evidence. Query all Unity Editor versions using explicit permitted metadata projections. When external command-line access is prohibited and a root is unknown, refuse launch without closing user work.

Group mixed boolean operators explicitly in PowerShell permission predicates. A PID type check accepting both Int32 and Int64 must be parenthesized inside a rejection chain; otherwise left-to-right `-and`/`-or` evaluation can cancel an earlier schema/run rejection for Int32. Serialization can change numeric runtime types, so set and assert the intended type after any JSON roundtrip in regression tests.

Unknown-root refusal is a conservative fallback, not proof that a parallel-Project environment is complete. MCP names/hashes and project-info roots without PID/start binding do not justify an allowlist. Native Unity same-Project rejection can underpin a separately accepted bounded attempted-launch policy, but does not promise zero Unity startup writes. Do not silently weaken a prelaunch-denial policy or install identity infrastructure across all Editors merely to hide this missing proof.

A smaller design may use an existing fixed read-only self-identity call and fresh OS/directory corroboration instead of installing Project source. Inspect the actual execution backend: in the reviewed Unity MCP revision, Roslyn emits in memory, but CodeDom writes temporary files and starts a compiler despite the generic tool's in-memory wording. Require existing Roslyn with safety checks enabled, fresh challenges, a successful strictly typed result, and reported compiler exactly Roslyn; unavailable capabilities, string serialization fallback or denial stop the route. Accept only disclosed in-memory cache/history/log effects, retain all-version coverage and a cooperative no-Project-switch interval, and never infer current roots from labels or historical PID-only records.

### Verification

Pure negative tests reject different run IDs, PIDs, starts, roots, stale/future acquisition times, missing or changed sessions, dirty/empty Scenes, another Editor version and replayed evidence claims. The corrected reusable runner has not been rerun against Unity; these checks are distinct from the earlier bounded runtime pilot.

Additional Int32 positive and wrong-schema/wrong-run tests pass. Reverting only the predicate grouping in memory makes the targeted regression fail, confirming that the tests exercise the prior defect. The reviewed native-lock alternative remains unimplemented and unproven.

Independent source review confirmed the backend and serialization behavior for a zero-Project-source-change self-identity design. A pure request builder and supplied-observation validator were subsequently implemented and independently tested. Review of the actual vendor API exposed gaps that mirrored fixtures missed: the method body needs a return statement, the action argument is required, and the success envelope contains a message. Fresh acquisition end alone also allowed arbitrarily old observations; bound the entire acquisition interval and corroborating observations. Bind target directory metadata to a separately configured target path, not to the observation's own path.

The initial bounded runtime attempt stopped before identity execution because an OS-snapshot script was denied by the active execution policy. No unauthorized policy bypass or identity retry occurred. After explicit approval for one exact-hash script in one child-process policy scope, that snapshot succeeded. A dedicated MCP session confirmed its exact Project root but the cached Editor state was stale and not ready; the identity operation was never executed. A cached false compilation flag is not proof of current readiness. No forced refresh, polling, transport change or retry followed. Scene-file hashes and process generations were preserved; loaded-Scene state was not read. Runtime self-identity, receipt integration, capability/Roslyn execution and coexistence remain unproven; the launch guard remains unchanged.

Another task reported a different server PID. Fresh local PID/parent-PID metadata subsequently established a wrapper, intermediate Python process and actual listener chain with the same owner/session and separate closely spaced start timestamps. The different reports named different processes in that chain, not demonstrated restarts. Verify the actual endpoint owner and ancestry before interpreting a launcher PID as a listener PID; query explicit metadata rather than external command lines.

### Reusable rule

Before publishing a completion runner, test evidence from a prior same-root run and an Editor using a different executable. Require both to fail closed. Check request/envelope fixtures against the actual vendor implementation, bind configured targets independently, and bound acquisition start as well as end. Recheck live identity and freshness immediately before marker publication and retain the distinction between source/pure-test verification and runtime proof. A denied prerequisite must not be reported as an attempted or successful identity execution.

### Applicability

Applies to trusted local evidence files used to authorize process completion. This binding is not cryptographic authentication of hostile evidence. Inventory checks cannot make process launch atomic with unrelated user activity; host Project locking and live checks remain necessary.

### Separate evidence and scope before formal Knowledge conversion

- **Observed code defects and verified pure controls:** stale/mismatched completion receipts, insufficient Editor-version coverage, and a mixed PowerShell predicate had distinguishable negative/positive tests. Reverting the predicate grouping caused its focused regression to fail.
- **Reviewed implementation proposal only:** in-memory Roslyn self-identity and its input-envelope contract were examined through source review and synthetic request validation; this is not native Unity execution proof.
- **Native runtime not demonstrated for the corrected reusable identity runner:** an OS prerequisite was denied in one attempt, and a later permitted read found stale Editor readiness. Do not propagate the earlier bounded pilot result to the new identity route.
- **Separate process-anatomy observation:** a wrapper PID and actual listener PID may refer to different members of the same ancestry rather than a restarted server. Review this as a distinct sub-lesson if reused.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-069 — A passing in-process Unity test does not prove a command-line gate ran

- Source area: unity
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: command-line-owned-test-gates

### Intent

Verify both a rendered shader path and a guarded asset transaction from an EditMode test.

### Observed failure

A selected Unity test passed its GPU render assertions, but the run did not produce transaction-specific preflight and restore evidence. The test source invoked the transaction only when an ownership predicate found a valid run context.

### Failed assumption / approach

A passing test case was treated as possible evidence that every later operation in the test body had run. The in-process test interface accepted test filters but did not accept the command-line results path or the external journal required by the ownership predicate.

### Root cause

Confirmed from the test control flow and runner interface: the guarded operation was conditional on process arguments identifying a run directory under the project verification folder and a prepared asset journal bound to that project and run ID. An ordinary in-process test result alone cannot establish that those conditions were met or that the guarded branch executed.

### Correction

Inspect guards and early returns around the operation being validated. Separate the always-run assertions from conditional transaction work, and use the existing external runner that creates the run context and passes the required arguments. Preserve the guard and record the transaction as unverified until branch-specific evidence exists.

### Verification

Source review confirmed the conditional branch, the required command-line arguments and journal checks, and an external runner that provides them. The external runner was not launched during this diagnosis, so transaction acceptance remains unverified.

### Reusable rule

Before interpreting a test pass, inspect the control flow and confirm that the required branch ran using branch-specific output or evidence. If a gate depends on command-line run identity and a prepared journal, use a runner that supplies both; do not hand-create artifacts or infer execution from unrelated assertions.

### Applicability

Applies to Unity EditMode tests and other in-process test interfaces when a guarded operation depends on external run identity or prepared artifacts. It does not imply that every GUI test skips guarded work; inspect the actual process arguments and the specific branch before making that claim.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-070 — Unity package import does not run explicit finalizers

- Source area: unity
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: unity-package-import-workflow

### Intent

Validate a Unity package that contains an export manifest and a task that creates a Prefab Variant.

### Observed failure

The package import completed successfully, but a follow-up probe failed because the manifest's Variant path did not resolve in the AssetDatabase.

### Failed assumption / approach

The probe treated a successful package import as if it had also performed the manifest's explicit finalization task.

### Root cause

The Variant was created by an explicit Editor finalizer call. Importing the package only materialized its assets and scripts; it did not execute that call.

### Correction

Follow the consumer workflow in order: import the package, explicitly invoke the finalizer with the imported manifest, then inspect the generated Variant in a fresh or otherwise well-defined observation step. Preserve evidence for each stage separately.

### Verification

In Unity 2022.3, package import exited successfully and the generated model hash matched the pinned fixture. The Variant inspection failed before the finalizer stage ran. Source review of the public roundtrip probe confirmed it calls `VapbModelSkinFinalizer.Apply` before loading the Variant. A dedicated apply probe was prepared to record the call result, source FBX/meta hashes before and after, destination vacancy, and Variant creation; its Unity execution remains pending.

### Reusable rule

Do not infer that an imported manifest's actions have run. Read the consumer workflow and execute each explicit Editor stage before asserting its outputs.

### Applicability

Applies to Unity packages whose manifests drive explicit Editor finalizers, such as creating Prefab Variants. It does not apply to checks that only need to confirm package files were imported.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-071 — Unity LicensingClient IPC needs the matching user session

- Source area: unity
- Source type: environment
- Source certainty: confirmed
- Source status: active
- Scope: unity-editor-license-ipc

### Intent

Run a headless Unity Editor probe against an isolated project without changing license configuration.

### Observed failure

A Unity Editor process launched by a restricted execution context could not connect to the running LicensingClient IPC channel. It waited for the client channel and exited with code 199 before invoking the probe.

### Failed assumption / approach

The failure was initially treated as a general Editor/license failure, although the Unity Hub and LicensingClient were running in a different logged-in user session.

### Root cause

Confirmed for the tested Windows setup: the default restricted process context did not share the LicensingClient IPC identity/session used by Unity Hub. Running the same Editor version, project and probe in the explicitly authorized logged-in user session connected to LicensingClient and completed successfully. No license or credential setting changed.

### Correction

Check the Unity process owner and session using non-secret process metadata. If the process is in the restricted context and licensing IPC fails, stop that attempt and request the normal authorized user-session execution route. Preserve the failed log and run the probe once after the process context is confirmed.

### Verification

The restricted launch exited 199 before the probe. The authorized logged-in session established the LicensingClient channel, completed the same headless probe with exit 0, and emitted the probe's success marker. The successful log still contained a nonfatal validation warning, so this does not establish that every licensing status or warning is resolved.

### Reusable rule

When Unity exits with LicenseIPC 199 before invoking an Editor method, compare the Editor's owner/session with the Hub and LicensingClient before diagnosing license configuration. Use the normal authorized matching user session when appropriate; do not change license settings or credentials to work around an IPC context mismatch.

### Applicability

Applies to Windows Unity batch runs where the Hub and LicensingClient are already active in a logged-in session and the Editor is launched from a separate restricted process context. It does not establish the cause of licensing failures in other setups, nor does a successful IPC connection prove that all license entitlements or warning states are healthy.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-072 — Keep the shared Unity MCP server opt-in out of batch clients

- Source area: unity
- Source type: workflow
- Source certainty: confirmed
- Source status: active
- Scope: unity-mcp-shared-server-lifecycle

### Intent

Connect a one-shot headless Unity Editor to an already running local Unity MCP HTTP server and exit the Editor without stopping that shared server.

### Observed failure

In the tested CoplayDev Unity MCP v10.2.0 environment, `McpEditorShutdownCleanup.ShouldRunCleanup` returns true for a batch Editor when `UNITY_MCP_ALLOW_BATCH` is nonempty. The subscribed quit callback then stops both local transports and calls `StopManagedLocalHttpServer`, which can follow the global PID/port handshake and stop a server created by another Editor.

### Failed assumption / approach

The batch environment variable appeared to be only a switch for allowing a headless client to connect. Applying it to a one-shot client would have also armed the shared server shutdown callback.

### Root cause

The same batch opt-in guards more than headless connection startup: it also enables shared shutdown cleanup. Treating the variable as a local bridge opt-in can therefore break server continuity at normal Editor exit.

### Correction

Review the installed package revision's startup and quit handlers before setting any vendor batch environment variable. If the bounded client can connect to the existing HTTP server without it, leave `UNITY_MCP_ALLOW_BATCH` empty in the child process and use a separate, narrow, process-local opt-in for the client controller. Never change user or machine environment state to run this pilot. Recheck the listener identity and MCP response after exit.

### Verification

The bounded Project-specific client connected to the existing loopback HTTP server without `UNITY_MCP_ALLOW_BATCH`, completed read-only MCP requests, consumed a run-bound marker, and exited through `EditorApplication.Exit(0)`. The pinned quit callback ran and the existing listener PID/start/owner/executable remained unchanged. The tested conclusion applies to the recorded package revision only.

### Reusable rule

Before a headless Unity MCP pilot, inspect both batch-start gates and `EditorApplication.quitting` handlers in the exact installed revision. Do not enable `UNITY_MCP_ALLOW_BATCH` when the callback can stop a shared server. Keep vendor process-global settings untouched, use the narrow process-local client opt-in, and verify listener continuity independently after shutdown.

### Applicability

Applies to a batch-mode Unity MCP client connecting to an existing shared local HTTP server. It does not apply to a separately managed server process that is intentionally owned by and bounded to the batch Editor; review its lifecycle independently.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

