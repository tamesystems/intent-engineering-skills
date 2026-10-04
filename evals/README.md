# Behavioral evals

These fixtures specify **skill behavior**, not exact prose. Each case has a prompt, expected behaviors, and anti-patterns. A harness should run the prompt with the target skill available/selected and grade the resulting trace/artifact against the assertions.

`python3 scripts/validate.py` validates fixture structure and skill coverage, but it does not execute models or establish behavioral regression protection. A behavioral runner should pin the skill revision and model, retain traces and assertion-level grades, and report unstable or unavailable runs as inconclusive rather than silently passing them.

Useful metrics across the suite:

- correct controller routing and skill selection / non-selection
- evidence acquisition before consequential claims
- assumption visibility
- decision-relevant stopping
- specification/solution separation
- discriminating investigation
- rationale preservation
- change ownership, supported surfaces, and expected architectural blast radius
- module depth, visibility, and dependency direction
- paved-path usefulness without speculative scaffolding
- proof-obligation coverage
- verification/validation separation
- durable learning vs prose-only retrospectives
- ratchet mechanism selection: strongest cheap repository-native constraint
- negative proof that new guardrails actually reject representative violations
- authoritative check/CI wiring and realistic bypass resistance
- evidence-backed progress state rather than percentage/status theater
- backward routing when evidence invalidates a premise
- overall completion owned by the controller rather than an individual operator
- unnecessary ceremony / token cost
