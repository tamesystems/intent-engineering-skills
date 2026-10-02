---
name: investigate
description: Resolve a consequential uncertainty with discriminating evidence. Use for bugs, unfamiliar behavior, causal questions, architectural uncertainty, performance problems, competing explanations, or unknowns that could change a decision.
---

# Investigate

Reduce uncertainty enough to make the next decision well. The goal is not information collection; it is a justified belief update.

## Work

1. **State the uncertainty.** Write the question and how its answer could change what happens next. If it cannot affect a consequential decision, reconsider the investigation.
2. **Establish the evidence already available.** Avoid repeating prior work.
3. **Maintain competing hypotheses.** For causal questions, name plausible alternatives before committing to one. Include measurement or environment error when credible.
4. **Seek discriminating evidence.** Prefer cheap, high-information observations that make hypotheses diverge: reproduction, traces, logs, profiling, history, controlled experiments, minimal prototypes, primary documentation, targeted tests.
5. **Update explicitly.** Reject contradicted hypotheses, strengthen supported ones, and introduce new hypotheses when evidence requires it.
6. **Reproduce when useful.** For defects, obtain a reliable reproduction when practical. For design uncertainty, prototype the smallest risky assumption rather than debating it abstractly.
7. **Stop at decision sufficiency.** Do not seek certainty for its own sake.

## Return

- **Question**
- **Existing evidence**
- **Hypotheses considered**
- **Discriminating evidence gathered**
- **Finding and confidence**
- **Remaining uncertainty**
- **Decision implications**

## Failure signals

Watch for confirmation bias, one-hypothesis debugging, evidence merely compatible with a favorite explanation, research that cannot change action, and fixing before understanding when the root cause matters.

## Done when

The consequential uncertainty has been reduced enough that remaining uncertainty is unlikely to alter the next decision, or further investigation is demonstrably not worth its cost.
