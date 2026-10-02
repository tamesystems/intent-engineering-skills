# Intent Engineering Progress Protocol

Progress is evidence-backed state transition, not percentage complete.

The controller uses this protocol to make long or multi-step work inspectable without turning every action into process overhead.

## State model

A task has:

- **Intent** — the governing outcome.
- **Operator runs** — attempts to satisfy one operator's postcondition.
- **Evidence** — concrete observations or artifacts supporting a run's result.
- **Open predicates** — conditions not yet satisfied that can change what happens next.
- **Current operator** — optional; the move presently in flight.
- **Terminal result** — set only when the controller can stop.

An operator run is not complete merely because the agent produced prose. Its postcondition must be satisfied or its failure/blocker must be explicit.

## Status vocabulary

Use these statuses for operator runs:

- `SATISFIED` — the operator's postcondition is met with credible evidence.
- `PARTIAL` — useful progress exists, but a material part of the postcondition remains unmet.
- `BLOCKED` — progress requires a dependency, authorization, capability, or human decision that cannot currently be resolved.
- `FAILED` — the attempted move did not satisfy its postcondition and did not merely reveal a route to another operator.
- `SUPERSEDED` — later evidence invalidated this run's premise or conclusion. Preserve the history; do not rewrite it as if it never happened.

Use these terminal task results:

- `SATISFIED`
- `PARTIAL`
- `BLOCKED`
- `FAILED`
- `INSUFFICIENT EVIDENCE`

## Minimal in-chat form

For ordinary multi-step work, a compact state block is enough:

```text
Intent: Users can reliably recover an interrupted import.

Progress
✓ ground      Current restart behavior reproduced. Evidence: trace-17.json
✓ investigate Cursor state is lost before durable persistence. Evidence: src/import/state.ts:42, repro-3
✓ decide      Persist cursor transactionally. Evidence: ADR-0012
→ realize     Candidate implementation in progress.
○ verify      Waiting on realized artifact.

Open
- Crash-recovery path has not yet been exercised.

Next predicate
- A coherent candidate exists that preserves the import invariants and can be independently verified.
```

Symbols are presentation only. The evidence and predicates are authoritative.

## Durable artifact form

For long-running, autonomous, resumable, or handoff-heavy work, keep `.intent/<task-slug>.md`.

Recommended shape:

```markdown
# <task>

## Intent
<governing outcome>

## Current
- Operator: verify
- Next predicate: crash recovery succeeds without duplicate side effects

## Transitions

### ground — SATISFIED
- Result: restart behavior reproduced
- Evidence: `artifacts/restart-trace.json`, `src/import/state.ts:42`

### investigate — SATISFIED
- Result: cursor state is lost before durable persistence
- Evidence: `artifacts/repro.md`

### decide — SATISFIED
- Result: persist cursor in the same transaction as the imported batch
- Evidence: `docs/adr/0012-import-cursor.md`
- Reconsider when: write latency exceeds the agreed operational budget

### realize — SATISFIED
- Result: candidate implementation exists
- Evidence: commit `abc1234`

### verify — PARTIAL
- Evidence: unit and integration suites pass
- Open: crash recovery has not been exercised against the real persistence boundary

## Open
- [ ] Crash-recovery verification.
- [ ] Representative validation, if this behavior reaches production users.
```

Keep evidence as pointers whenever possible: command output, file/line, commit, test result, trace, screenshot, metric, issue, or authoritative record. Do not paste long narratives into the progress artifact.

## Transition rules

1. The controller chooses the next operator from the smallest unresolved predicate.
2. A successful operator run satisfies its own postcondition only; it does not automatically satisfy downstream operators.
3. New evidence may supersede an earlier transition and route backward.
4. Preserve superseded decisions and findings when they materially shaped the work. Append the correction instead of rewriting history.
5. A blocker is a state, not a dead end. Continue independent branches when they remain valid.
6. Do not report numeric percent complete unless the work itself has a meaningful measurable denominator.

## Completion rule

A task is complete when the controller can justify a terminal result from the governing intent and accumulated evidence.

For outcome-bearing work, technical verification alone is not enough when representative validation is both material and obtainable. When validation cannot yet be obtained, use `INSUFFICIENT EVIDENCE` or `PARTIAL` rather than silently converting verification into validation.
