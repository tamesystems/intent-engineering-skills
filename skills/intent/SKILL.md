---
name: intent
description: Run the smallest sufficient intent-engineering loop for a non-trivial task. Use as the default entry point when the user wants an outcome carried through, when the next operator is not obvious, or when work may need to move backward as evidence changes. Route among ground, specify, investigate, decide, realize, verify, validate, and learn; use codebase-design skills when placement or architecture is unresolved; track evidence-backed progress; and own the overall completion claim.
---

# Intent

Run the intent-engineering loop. This skill is the **controller**, not a ninth cognitive operator. It owns routing, progress, loop control, and the overall completion claim; the eight operator skills own the work itself.

## Start

1. **Recover the governing intent.** State the real-world outcome the user is trying to achieve. Preserve proposed interventions as context, but do not silently promote them into the objective.
2. **Assess existing state.** Reuse evidence, specifications, decisions, artifacts, verification, and validation already present in the conversation or workspace. Do not rerun completed operators without a reason.
3. **Choose the smallest sufficient next operator.** Route by the unresolved postcondition, not by a fixed sequence:
   - reality is materially unclear → `ground`
   - success or preservation conditions are materially unclear → `specify`
   - a consequential uncertainty could change the next move → `investigate`
   - multiple materially different interventions remain viable → `decide`
   - software ownership/placement or expected blast radius is materially unclear → `design-change`, then return to the controlling operator
   - an owning module is known but its supported surface or hidden responsibilities are materially unclear → `design-module`, then return
   - a validated recurring architectural operation is needlessly hard or inconsistent → `pave-path`
   - a justified change must be made real → `realize`
   - technical conformance or preserved behavior is unproven → `verify`
   - technical correctness is established but intended outcome is unproven → `validate`
   - surprise, failure, correction, or repeated friction warrants a durable ratchet → `learn`
4. **Skip unnecessary operators.** A typo may route `realize → verify`. A read-only question may end after `ground` or `investigate`. Do not perform ceremony merely because an operator exists.

## Run the loop

For each selected operator:

1. **Declare the transition.** Record why this operator is the smallest sufficient next move and what postcondition would let the loop advance.
2. **Invoke the operator skill.** Let that skill own its method and return shape. Do not duplicate its instructions here.
3. **Inspect evidence, not narration.** Treat the operator as complete only when its `Done when` postcondition is supported by evidence or the operator explicitly reports a blocker/remaining uncertainty.
4. **Update progress.** Record the operator result, evidence pointers, open blocker/uncertainty, and next completion predicate using the progress protocol.
5. **Re-route from the new state.** If evidence invalidates an earlier premise, move backward to the operator that owns that premise. Never force forward motion to preserve a plan.

Keep the loop bounded by the governing outcome:

- Separate required acceptance evidence from optional hardening. When the human changes scope or defers validation, update the controlling predicates immediately; preserve required safety and integrity invariants and disclose remaining limits.
- Before expanding implementation or verification infrastructure, identify the unresolved predicate it serves and why existing evidence/tools cannot settle it. A possible improvement is not automatically a completion requirement.
- If repeated attempts consume time without changing the evidence or next decision, reassess the hypothesis, measurement method, and approach. Continue necessary work with a discriminating next step; do not repeat the same probe or accumulate gates to demonstrate activity.
- Reuse passing evidence until a relevant change, failure, or environment difference invalidates it. Stop adding proof once required predicates have sufficient evidence.

## Progress

Maintain one compact task state for non-trivial multi-step work. It may live in the conversation for short tasks or in `.intent/<task-slug>.md` when the work is long-running, handed off, or needs an auditable artifact.

Track:

- **Intent** — the governing outcome.
- **Current operator** — the move presently being executed, if any.
- **Transitions** — operator, result, evidence pointers, and postcondition outcome.
- **Open** — material blockers, uncertainties, failed predicates, or human decisions.
- **Next predicate** — the concrete condition that determines the next state transition.

Progress is **not a percentage** and not a prose status story. It is the set of evidenced predicates already satisfied and the smallest unresolved predicate that controls what happens next.

Update the current state in place. Retain consequential decisions and superseded evidence as concise pointers; do not append a full narrative for every command or continuation. The next operator should be able to resume without rereading the entire execution history.

Follow [`references/progress.md`](references/progress.md) for the canonical shape and status vocabulary.

## Human decisions

Find facts yourself when tools or evidence can settle them. Ask the user only for a genuine preference, product judgment, authorization, or value choice that cannot be established empirically.

If such a decision blocks only one branch, continue any independent work that remains valid. Record the human decision as an open predicate rather than pretending the loop is globally blocked.

## Overall completion

Only this controller owns the overall task completion claim.

An operator succeeding does not imply the intent is satisfied. In particular:

- `realize` means a candidate change exists, not that it is correct.
- `verify: PASS` means the artifact conforms to the specification, not that the governing intent was achieved.
- `validate: SATISFIED` is the strongest evidence that the intended outcome was achieved, when validation is applicable and obtainable.
- some tasks legitimately complete without `validate` or `learn`; record why they were unnecessary rather than manufacturing them.

## Return

For non-trivial loops, finish with:

- **Intent**
- **Result:** SATISFIED / PARTIAL / BLOCKED / FAILED / INSUFFICIENT EVIDENCE
- **Progress** — completed operator transitions with evidence, kept compact.
- **Open** — remaining blockers, uncertainty, or validation gap.
- **Next move** — only when the intent is not yet satisfied.

For trivial loops, return the result naturally; do not expose internal ceremony that adds no value.

## Failure signals

Correct course if you are running all eight operators by default, repeating work already evidenced, letting an operator self-declare completion without checking its postcondition, treating todo completion as proof, preserving a stale plan after evidence changes, asking the user for facts you can determine, or declaring the overall intent satisfied because implementation or verification passed.

## Done when

The governing intent is satisfied with sufficient evidence for the task, or the loop has reached an explicit terminal state (`PARTIAL`, `BLOCKED`, `FAILED`, or `INSUFFICIENT EVIDENCE`) with the controlling unresolved predicate and next move made clear.
