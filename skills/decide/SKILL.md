---
name: decide
description: Choose a sufficient intervention from credible alternatives using evidence, constraints, tradeoffs, and reversibility, and preserve why. Use before consequential implementation or whenever multiple materially different approaches remain viable.
---

# Decide

Choose what to do and preserve why. Do not confuse generating options with making a decision.

## Work

1. **Frame the decision.** Reference the governing intent, specification, grounded state, and relevant findings.
2. **Identify real decision drivers.** Use only factors that materially distinguish acceptable approaches: correctness, simplicity, reliability, compatibility, performance, security, reversibility, operational burden, cost, time, etc. Avoid decorative scorecards.
3. **Generate credible alternatives.** Consider more than one serious approach when consequences justify it. Include defer/do-nothing when legitimate; do not manufacture strawmen.
4. **Collapse risky assumptions.** If the choice hinges on an uncertain claim, investigate or prototype it instead of reasoning indefinitely from assumption.
5. **Compare consequences.** Examine coupling, failure modes, migration, blast radius, reversibility, maintenance, and what each option makes easier or harder.
6. **Prefer the smallest sufficient commitment.** When outcomes are comparable, avoid irreversible or speculative complexity.
7. **Record the rationale.** Capture rejected serious alternatives and the evidence or tradeoff that decided the choice.

## Return

- **Decision**
- **Rationale**
- **Alternatives considered**
- **Tradeoffs accepted**
- **Assumptions**
- **Reconsider when** — evidence or conditions that would invalidate the decision.

## Failure signals

Watch for choosing the first workable idea, architecture by fashion, fake alternatives, unexplored assumptions that dominate the choice, and reopening settled decisions without new evidence.

## Done when

There is enough justified commitment to realize the change without silently re-litigating the same decision, and the conditions that should reopen it are explicit.
