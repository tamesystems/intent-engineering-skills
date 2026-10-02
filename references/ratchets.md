# Ratchet Contract

Ratchets change the environment future engineering work executes inside. They are not additional cognitive operators in the intent loop.

A ratchet converts an observed engineering lesson into repository-owned machinery so a known-invalid path becomes harder or impossible to repeat while the intended path remains easy to discover.

## Universal contract

Every ratchet should:

1. **Observe** — cite the concrete failure, correction, friction, or invariant that motivates the change.
2. **Generalize** — state the recurring failure class independently of the single instance.
3. **Select** — choose the strongest cheap mechanism using [`mechanism-ladder.md`](mechanism-ladder.md); inspect existing repository machinery before adding tooling.
4. **Install** — change repository-owned code, configuration, tests, scripts, structure, or APIs. Prose alone is not a mechanical ratchet.
5. **Prove** — demonstrate the guardrail catches a representative recurrence. Prefer clean PASS → forbidden mutation FAIL → clean PASS.
6. **Wire** — ensure the guardrail participates in the authoritative contributor/CI path when it is important enough to gate changes.
7. **Explain** — make failures point toward the intended architecture or corrective path where practical.
8. **Preserve** — do not weaken unrelated standards, erase tests, or rewrite local policy merely to make the new check pass.

## Outcomes

- **RATCHETED** — durable mechanism installed, proven, and appropriately wired.
- **DOCUMENTED_JUDGMENT** — the lesson matters but is not usefully mechanically expressible; rationale/guidance was recorded in the narrowest durable place.
- **NOT_WORTH_RATCHETING** — recurrence/consequence does not justify permanent machinery.
- **BLOCKED** — a justified ratchet cannot be completed safely; state the missing prerequisite or decision.

## Ownership

Prefer repository-owned policy over policy that exists only in an agent's installed skill. A setup skill may install or vendor a mechanism, but future contributors and CI should encounter the constraint even if the skill is absent.

## Positive path

For every prohibition ask: **is the intended path at least as easy to discover and use?** If not, add or improve the canonical abstraction, helper, generator, type, diagnostic, or nearby documentation. A repository made only of prohibitions causes thrashing rather than leverage.
