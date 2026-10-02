---
name: ground
description: Establish the smallest evidence-backed model of current reality sufficient to proceed. Use when entering an unfamiliar system, current behavior or constraints are uncertain, assumptions matter, or before consequential changes.
---

# Ground

Establish what is actually true before reasoning from it. Do not propose changes unless the task explicitly requires continuing beyond grounding.

## Work

1. **Frame the question.** State what must be understood and which facts could change the next decision.
2. **Inspect primary evidence.** Prefer the running system, source, tests, configuration, history, logs, traces, persisted state, and authoritative records over summaries. Follow the relevant path end-to-end when behavior matters.
3. **Reconstruct current state.** Explain the relevant actors, boundaries, control/data flow, state changes, external effects, and constraints. Run or probe the system when static inspection cannot establish behavior.
4. **Classify claims.** Keep observed facts, supported conclusions, assumptions, and unknowns distinct. Surface contradictions rather than resolving them by intuition.
5. **Bound the search.** Investigate only gaps that could materially change the next move. Stop at decision sufficiency.

## Return

- **Current state** — the smallest useful model.
- **Evidence** — concrete sources/observations supporting material claims.
- **Constraints** — relevant boundaries that already exist.
- **Unknowns** — material unresolved questions.
- **Implications** — what this state means for the next move, without smuggling in an implementation decision.

## Failure signals

Stop and correct course if you are treating documentation as runtime truth, silently converting inference to fact, exploring unrelated areas, or gathering information without reducing decision-relevant uncertainty.

## Done when

Material questions are answered with evidence or explicitly marked unknown; contradictions are visible; and more grounding is unlikely to change the next consequential move.
