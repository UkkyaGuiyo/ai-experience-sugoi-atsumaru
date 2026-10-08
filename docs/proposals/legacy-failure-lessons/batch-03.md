# Legacy failure lessons migration — Batch 03

Review status: PENDING_REVIEW

Generalized lessons migrated from a retired legacy failure-lesson repository. Source `confirmed` status is provenance only; Atsumaru independent review is still pending. No raw logs, conversations, private repository identifiers, personal paths, credentials, or project-specific artifacts are intentionally carried over.

## LFA-031 — Monotonic timestamps may lack sufficient resolution

- Source area: python
- Source type: environment
- Source certainty: confirmed
- Source status: active
- Scope: high-rate-receive-ordering

### Intent

Enforce a strictly increasing receive watermark for a high-rate stream.

### Observed failure

Separate callbacks received equal coarse timestamps and were rejected as out of order.

### Failed assumption / approach

Monotonicity was assumed to imply enough resolution to distinguish each arrival.

### Root cause

Confirmed: clock quantization was too coarse for callback cadence; this was independent of the unresolved native hang.

### Correction

Use one high-resolution monotonic clock consistently for receive times, age, deadlines and latency; preserve source-order checks.

### Verification

A regression quantized time to 1/64 second at 120 callbacks/second: the old path aborted, the precise path accepted 120. Threaded rate/burst/stall tests and a later 1,200-callback live run passed.

### Reusable rule

Test clock resolution against burst arrival rates. Distinguish source time, receive time and consumer cadence; do not fabricate epsilon timestamps to conceal collisions.

### Applicability

Observed runtime and injected-clock controls. This is not a universal defect in every monotonic-clock implementation or Python version.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-032 — A neutral mean does not prove stable return

- Source area: python
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: windowed-motion-acceptance

### Intent

Decide whether a sampled motion window has returned to neutral.

### Observed failure

Opposite displacements or rotations canceled to a neutral average while oscillation continued, yet the result was accepted.

### Failed assumption / approach

Mean proximity, plus stability in a different window, was treated as sufficient.

### Root cause

Confirmed: return-window dispersion was computed but omitted from the acceptance decision.

### Correction

Require both mean-return proximity and return dispersion within the existing allowance, including selected and opposite-side joints; retain independent invariant failures.

### Verification

Symmetric plus/minus translation and rotation fixtures now remained unverified rather than passing. Neutral and small-noise controls still passed. The recorded current run covered 128 related tests, not a new full-suite result.

### Reusable rule

Validate central tendency and stability in every required acceptance window. Include adversarial cancellation fixtures instead of relying only on average error.

### Applicability

Offline motion-analysis controls. No live body-motion acceptance or universal threshold choice was established.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-033 — Supervise the whole native lifecycle outside the child

- Source area: python
- Source type: architecture
- Source certainty: confirmed
- Source status: active
- Scope: native-sdk-probe-containment

### Intent

Finish a short native-SDK observation and report its outcome within a bound.

### Observed failure

A nominal twenty-second probe was still alive after 43.1 seconds with no final aggregate; forced stop left stage/activity uncertain.

### Failed assumption / approach

The observation-loop deadline was assumed to cover native initialization and teardown, and final-only output was assumed sufficient.

### Root cause

Confirmed containment gap: synchronous lifecycle calls lay outside the loop deadline. The historical stalled stage and underlying native cause remained unknown.

### Correction

Use parent-owned child-process supervision with a total deadline and cleanup reserve, bounded intermediate aggregates and pre-close evidence. Record both result and actual child exit.

### Verification

Spawned import/constructor/open/close/exit-hang controls and partial-IPC tests passed. A later live recovery exited normally in about 20.25 seconds with 1,200 valid callbacks; this did not retrospectively identify the original hang.

### Reusable rule

Bound the complete lifecycle externally and retain partial evidence. Missing summary means unknown activity; a pre-close result does not prove cleanup completed.

### Applicability

Tested Python/Windows supervision. No hard-real-time OS guarantee or general native-SDK defect is asserted; terminate only the owned child.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-034 — Do not parse language representations as JSON

- Source area: python
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: generated-object-boundary

### Intent

Accept a generated structured object without discarding valid content.

### Observed failure

Every audited record used whole-output safety fallback despite a valid generated object.

### Failed assumption / approach

The guard stringified a dictionary and passed that representation to json.loads.

### Root cause

Confirmed: language dictionary notation is not JSON text; valid object input was misclassified.

### Correction

Accept mappings directly and parse only JSON strings. Add parity tests for host and embedded workflow guards.

### Verification

Local contract and embedded-guard tests passed, and the fix was present in a draft. The latest recorded live attempt stopped upstream at HTTP 401; existing records were not regenerated and end-to-end recovery was unverified.

### Reusable rule

Branch on the actual input type at serialization boundaries. Test object and string forms, and measure fallback frequency so safe degradation does not conceal systematic rejection.

### Applicability

Historical Python/Dify guard. Local/draft correctness does not prove the deployed graph, published version or persisted outputs were repaired.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-035 — Preserve scheduler phase after delayed wakes

- Source area: python
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: latest-only-periodic-consumer

### Intent

Consume the latest sample near a configured periodic rate.

### Observed failure

Sleeping a full period after work delivered about 21.6 Hz at a 30 Hz target and 32.3 Hz at 60 Hz. Resetting deadlines from each late start also failed.

### Failed assumption / approach

Processing duration and repeated wake delay were assumed not to accumulate into schedule drift.

### Root cause

Confirmed: work-plus-sleep and late-start phase resets continually moved the deadline grid.

### Correction

Preserve the original deadline phase, include work within each period, skip missed ticks without catch-up replay, and consume newest state only.

### Verification

Deterministic work/early-wake/late-wake/burst/stall controls passed. Repeated synthetic IPC measurements improved approximately 21.635 to 30.143 Hz and 32.316 to 58.876 Hz.

### Reusable rule

Test processing time and delayed wakes explicitly. Preserve phase for periodic latest-state work and report measured cadence rather than claiming the configured rate.

### Applicability

Recorded synthetic consumer path. The numbers do not prove later wrapper or live cadence, and skipping ticks is inappropriate for workloads requiring every event.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-036 — A reset instruction is not conversation isolation

- Source area: agents
- Source type: architecture
- Source certainty: confirmed
- Source status: active
- Scope: multi-session-conversation-boundaries

### Intent

Start a new independent service session without reusing prior-session context.

### Observed failure

A reset phrase and marker controls passed narrow checks, but a later acceptance run reused the previous session's candidates.

### Failed assumption / approach

Prompt-level reset was treated as if it removed the platform's retained conversation history.

### Root cause

Confirmed: the old history remained in the same conversation container. A new-container canary also exposed a separate tendency to invent an absent referent from the current catalog.

### Correction

Start a new platform conversation at the session boundary and reuse its identifier only within that session. Require clarification when no candidate was presented in the current session.

### Verification

The initial migration verified zero old inputs/candidates/answers and reran the complete two-session sequence after the canary correction. A later bounded-state design recorded five separation cases across eleven turns with zero observed leaks.

### Reusable rule

Use actual history-container isolation at independent session boundaries. Test a previous-session reference after switching and distinguish isolation from unsupported referent guessing.

### Applicability

Observed Dify designs at historical checkpoints; later bounded-state acceptance is not proof that the earlier full-history design passed. No universal confidentiality guarantee is inferred.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-037 — Rollback must reverse executed mutations only

- Source area: blender
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: transactional-editor-renames

### Intent

Recover safely from a failed bone/group merge.

### Observed failure

Rollback renamed an existing target-only group even when the forward phase had never renamed it.

### Failed assumption / approach

The full planned rename mapping was inverted on failure.

### Root cause

Confirmed: the undo plan contained operations that had not executed.

### Correction

Journal actual completed renames and replay that list in reverse; retain original values.

### Verification

Injected failures before the first write and after writes preserved target-only group name and weight. Blender 5.2.1 pose/chain/parenting/identity/rollback/Undo controls and the recorded Python suite passed.

### Reusable rule

Build rollback from executed-operation receipts, not intended operations. Test failure before the first mutation as well as midway through the transaction.

### Applicability

Tested bone/group merge operations. This is not a guarantee for untested animation state or arbitrary multi-resource transactions.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-038 — Verify fields across the actual serialized payload

- Source area: other
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: workflow-api-storage-contract

### Intent

Persist derived fields alongside canonical inputs.

### Observed failure

Registration succeeded but generated and nearby-information columns were blank.

### Failed assumption / approach

Backend header mappings were treated as proof that corresponding values arrived.

### Root cause

Confirmed: the outgoing HTTP body omitted parser-derived keys despite receiver mappings being present.

### Correction

Add required derived fields and parser status to the payload, serialize structured fields, and test the producer/HTTP/receiver/storage contract together.

### Verification

A diagnostic stored nonempty derived columns. Recorded payload-contract and fixture tests checked the required field set; registration success alone had not detected the omission.

### Reusable rule

Assert that required producer values survive actual serialization and storage. Include diagnostic response fields too: parser or final-output projections can silently drop them independently.

### Applicability

Workflow/API/tabular boundaries. Presence and parse success do not prove value correctness, category accuracy or deployment freshness.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-039 — A zero SDK version can mean its query failed

- Source area: unity
- Source type: environment
- Source certainty: confirmed
- Source status: active
- Scope: android-sdk-jdk-compatibility

### Intent

Run an Android build with an external SDK and the editor's bundled Java.

### Observed failure

The editor reported SDK Platform Tools version 0.0 and failed to list API levels despite installed working platform-tools.

### Failed assumption / approach

The displayed zero and stale generated settings suggested missing or obsolete platform-tools.

### Root cause

Confirmed: command-line tools 20.0 required Java 17 while the tested Unity editor invoked OpenJDK 11; forced execution exposed class-file 61 versus supported 55.

### Correction

Choose a compatible tools/JDK pair. In the recorded environment, backed-up newer tools were replaced by the editor's Java-11-compatible tools 6.0; this is not a universal version recommendation.

### Verification

The same sdkmanager failed under editor Java and succeeded under another compatible Java. Corrected queries worked under actual editor Java, and Android Build And Run was recorded successful; a nonfatal XML warning remained.

### Reusable rule

Run the failing SDK query with the exact Java/executable/environment used by the build. Separate interrogation failure from actual installed package versions before changing project targets.

### Applicability

Historical Windows/Unity toolchain only. Current versions and device behavior were not reverified.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-040 — A search label does not prove result category

- Source area: other
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: typed-search-result-normalization

### Intent

Save search results belonging to requested facility categories.

### Observed failure

Locality names and unrelated businesses were stored as requested categories despite parse success.

### Failed assumption / approach

A titled search result or category query was treated as category evidence.

### Root cause

Confirmed: the normalizer retained titled entries without using available provider type fields as acceptance criteria.

### Correction

Combine provider type fields, require a category-specific allowlist match, reject missing/mismatched types, and deduplicate with diagnostic reasons.

### Verification

The subsequent recorded audit found 264 saved candidates with zero category mismatches, missing-type entries or JSON errors; fixture, contract and live checks were recorded.

### Reusable rule

Validate result semantics with provider evidence, not the request label or title. Preserve no-match and transport-failure as different outcomes.

### Applicability

Observed SerpApi Maps normalization. Type allowlists are provider/contract-specific; zero accepted candidates can be a valid result requiring human review.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-041 — Serialize generated content instead of interpolating JSON

- Source area: other
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: workflow-http-json

### Intent

Send canonical fields and generated text through an HTTP JSON request.

### Observed failure

The receiver rejected a POST with parse_invalid_json even though content type and body type looked correct.

### Failed assumption / approach

Quoted raw-text JSON templates were assumed safe for arbitrary generated text.

### Root cause

Confirmed in the recorded diagnosis: quotes and newlines from generated content broke the interpolated JSON.

### Correction

Build one complete payload object and serialize it once; give the HTTP node only the finished JSON string.

### Verification

The diagnostic request then returned creation success/HTTP 200, stored nonempty generated fields and reported parse success. Existing records were not changed during that diagnostic.

### Reusable rule

Serialize structured values at the final boundary rather than concatenating JSON. Include quotes, line breaks, Unicode, arrays and objects in sender-to-receiver tests.

### Applicability

Observed Dify raw-text HTTP to Apps Script flow. This is a serialization correction, not proof that every stored field is semantically correct.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-042 — Shortcut tests must traverse real event bindings

- Source area: other
- Source type: testing
- Source certainty: confirmed
- Source status: active
- Scope: tk-keyboard-dispatch

### Intent

Verify a press/release recording shortcut after interacting with UI controls.

### Observed failure

A direct recording-function self-test passed, but the shortcut failed when focused widgets consumed the key in class bindings.

### Failed assumption / approach

Testing the handler function was assumed to test keyboard dispatch.

### Root cause

Confirmed: root-window-only bindings ran too late for the affected focus paths.

### Correction

Install a first-priority recording bindtag on relevant widgets while exempting text entry; change self-tests to generated KeyPress/KeyRelease events.

### Verification

Three press-to-start/release-to-stop cycles traversed the binding path and ended with idle state, without dropped or padded frames.

### Reusable rule

Test the entry event with realistic focus, not just its callback. Preserve typing and modifier behavior when changing shortcut precedence.

### Applicability

Observed Windows/Tk application path. Synthetic event success does not establish every physical keyboard, widget or focus configuration.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-043 — Speech does not remove model and tool latency

- Source area: agents
- Source type: workflow
- Source certainty: confirmed
- Source status: active
- Scope: bounded-guided-capture

### Intent

Collect baseline, held-state and return windows inside a bounded observation period.

### Observed failure

A chat-paced attempt collected 60/0/0 samples; a spoken-countdown retry still ended at 60/20/0 without the return window.

### Failed assumption / approach

Changing communication modality or passing a manually driven terminal control was assumed to validate the real guidance path.

### Root cause

Confirmed: time-critical progression still depended on model/tool round trips. A later acknowledgment could not reconstruct uncaptured data.

### Correction

Move stage progression into a local state-aware wrapper under existing supervision/deadlines. Test the same wrapper with synthetic SDK and speech before requesting more user effort.

### Verification

Recorded local synthetic runs collected 60/20/20. Delayed, failed and hanging speech, lifecycle hangs, stop and cleanup cases passed; actual audibility and physical mapping remained unverified.

### Reusable rule

Keep model/tool round trips outside bounded real-time control. Test the exact execution path, distinguishing user confirmation from scheduled stage boundaries.

### Applicability

Guided capture orchestration. Offline timing success is not live human-motion acceptance, and no automatic retry of user effort is implied.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-044 — Residual takeoff contact must not reset jump state

- Source area: unity
- Source type: implementation
- Source certainty: confirmed
- Source status: active
- Scope: character-controller-transitions

### Intent

Enforce a two-jump budget through takeoff, ascent and landing.

### Observed failure

Brief ground contact during ascent reset the jump count.

### Failed assumption / approach

Any ground contact was interpreted as a landing event.

### Root cause

Confirmed in the tested controller: contact persisted briefly after takeoff and triggered the reset at the wrong lifecycle phase.

### Correction

Exclude immediate post-takeoff contact from landing reset in this controller.

### Verification

An editor driver injected keyboard state through actual Input Actions and observed jump, second jump and fall after correction. A dedicated timing unit test was not recorded for this exact defect.

### Reusable rule

Treat landing as a state transition supported by contact and motion/timing, not raw contact alone. Regress takeoff persistence through the actual input path.

### Applicability

Observed Unity controller and intended jump rules. Different physics/contact models need their own transition contract and timing tests.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

## LFA-045 — Bound uncertainty without silently discarding aliases

- Source area: unity
- Source type: diagnosis
- Source certainty: confirmed
- Source status: active
- Scope: prefab-material-projection

### Intent

Preserve usable material assignments while reporting unresolved overrides.

### Observed failure

Adding one unmatched override removed two otherwise valid dependencies; remove/reinsert controls toggled counts 2/0/2/0. A later alias fixture also showed that an unmatched override could affect a real target.

### Failed assumption / approach

An empty match initially invalidated all child records; a narrower response risked assuming every unmatched reference was unrelated.

### Root cause

Confirmed: the broad fallback poisoned unrelated rows. Independently, serialized nested aliases made the opposite blanket assumption unsound.

### Correction

Retain the unresolved issue, trace alias and instance edges, and invalidate only the class-compatible scope supported by evidence. Keep ambiguous siblings unknown rather than guessing.

### Verification

Historical causal replay isolated the global fallback. Unity-authored saved/reopened alias cases proved scoped effects; wrong-ID, missing-edge and revision controls retained fail-closed behavior.

### Reusable rule

Minimize uncertainty only after proving its scope. Test both unrelated unmatched inputs and real aliases so a precision improvement does not silently accept incomplete state.

### Applicability

Bounded material projection and nested-instance evidence. Package-only identity can remain unresolved; names, order and candidate counts do not complete a missing join.

**Migration status:** PENDING_REVIEW. Check overlap with existing formal Knowledge and pending candidates before formalization.

