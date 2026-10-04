---
name: learn
description: Convert meaningful outcomes, failures, surprises, human corrections, and repeated friction into durable improvements to future agent and engineering work. Use after incidents, failed verification/validation, repeated mistakes, discoveries worth ratcheting into the system, or requests to audit recurring correction patterns in repository history.
---

# Learn

Make future work better because this work happened. A retrospective that changes nothing is not learning.

## Work

1. **Name the surprise.** Identify where reality differed from the prior model: failure, rework, human correction, repeated confusion, missing context/tooling, architectural violation, or unexpectedly effective behavior. For a scoped recurring-correction audit, inspect relevant commits, reverts, review findings, incident records, agent instructions, and workaround comments; group cited examples into failure classes instead of treating each file as a separate lesson. Prioritize by recurrence, consequence, and confidence. A single severe failure may justify action; two minor examples do not automatically justify machinery.
2. **Find the earliest preventable cause.** Look beyond the immediate mistake to why the system permitted or encouraged it: missing knowledge, ambiguous intent, weak specification, missing invariant, architecture, test, observability, capability, skill guidance, eval, or decision heuristic. Account for the agent's local view: nearby examples, import visibility, competing APIs, split ownership, and manually synchronized sources can make the shortest compiling path the wrong path.
3. **Treat repeated locality discrepancies as architectural evidence.** If changes repeatedly cross boundaries that `design-change` expected to hold, investigate whether implementation leaks, a capability/public surface is missing, concepts actually change together, or the declared boundary is artificial. Do not fossilize a questionable architecture by reflexively adding another rule.
4. **Choose the strongest durable correction.** Prefer roughly: mechanical prevention → automated detection → executable verification → better tooling/observability → improved skill/reference → durable documentation → remembered advice.
5. **Route recurring mechanical lessons to `ratchet`.** A learning is not complete merely because it was recorded. If the failure class is recurrent or consequential and mechanically preventable/detectable, invoke `ratchet` (or apply its contract directly for a trivial change). Prefer prevention over detection and detection over instruction.
6. **Install the durable correction when authorized.** Add or improve the type/API constraint, lint/architecture rule, test/check, instrumentation, abstraction, capability, skill, eval, or documentation. Simplify or remove a footgun when that is stronger than adding guidance. Documentation is the fallback for irreducibly judgment-based lessons, not the default.
7. **Verify the ratchet.** For mechanical guardrails, prove a representative recurrence is rejected; prefer clean PASS → forbidden mutation FAIL → clean PASS. For skill changes, add/update an eval case where practical.
8. **Avoid overfitting.** Not every mistake deserves a rule. Generalize when recurrence, cost, or consequence justifies it; periodically remove obsolete or redundant guidance.

## Return

- **Learned**
- **Earliest preventable cause**
- **Durable change**
- **Evidence the ratchet helps**
- **Remaining exposure**
- **Follow-up**, if any

## Failure signals

Watch for blame, retrospective prose with no changed system, another instruction where a mechanical constraint is possible, rules derived from one harmless anomaly, ratcheting a boundary whose repeated blast-radius discrepancies have not been investigated, and ever-growing guidance that makes the harness less legible.

## Done when

The learning has become a durable improvement with evidence it helps, or there is an explicit, justified decision that no system change is warranted.
