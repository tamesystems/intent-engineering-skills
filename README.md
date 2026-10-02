# Intent Engineering Skills

[![Validate skills](https://github.com/tamesystems/intent-engineering-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/tamesystems/intent-engineering-skills/actions/workflows/validate.yml)

A portable collection of agent skills for intent-driven, reliable engineering—with codebase-design skills that make intended changes obvious and local, and executable ratchets that make known-invalid architectural change hard to repeat.

For most non-trivial work, start with **`intent`**. It recovers the governing intent, chooses the smallest sufficient path through the operators, tracks evidence-backed progress, routes backward when evidence invalidates a premise, and owns the completion claim.

## Install

Install the collection with the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills@latest add tamesystems/intent-engineering-skills
```

The installer detects supported agents and lets you choose skills interactively. To install the complete workflow for a specific agent:

```bash
# Codex
npx skills@latest add tamesystems/intent-engineering-skills --skill '*' --agent codex

# Claude Code
npx skills@latest add tamesystems/intent-engineering-skills --skill '*' --agent claude-code

# Cursor
npx skills@latest add tamesystems/intent-engineering-skills --skill '*' --agent cursor

# Pi
npx skills@latest add tamesystems/intent-engineering-skills --skill '*' --agent pi
```

Add `--global` for a user-level installation, `--yes` for a non-interactive installation, or `--copy` to copy files instead of linking them. Preview the discovered skills without installing:

```bash
npx skills@latest add tamesystems/intent-engineering-skills --list
```

The Skills CLI also supports GitHub Copilot, Gemini CLI, OpenCode, Windsurf, Cline, Amp, and other agents. See its [current agent list](https://github.com/vercel-labs/skills#supported-agents) for identifiers and install locations.

### Install from a local checkout

```bash
git clone https://github.com/tamesystems/intent-engineering-skills.git
cd intent-engineering-skills
npx skills@latest add . --skill '*' --agent codex
```

## Use

Ask your agent to use `intent`, or invoke it through the host's skill syntax—for example, `$intent` in Codex. Invoke an operator directly when you already know the exact cognitive move required.

The complete collection is recommended. Skills remain independently installable, but the workflow has deliberate relationships that installers do not resolve automatically:

- `intent` routes among all eight operators and into codebase design when placement or architecture is unresolved.
- `design-change` can route to `design-module`; `design-module` can route to `pave-path` and boundary ratchets.
- `pave-path` can route validated invariants to boundary and check ratchets.
- `learn` can route recurring or consequential mechanical lessons to `ratchet`.
- `ratchet` can route to `create-check`, `wire-check`, `harden-boundary`, and `harden-check`.

## Entry point

| Skill | Role |
|---|---|
| `intent` | Run the smallest sufficient loop, route among operators, track progress, and own completion. |

## Operators

`ground → specify → investigate → decide → realize → verify → validate → learn`

These are operators, not a mandatory waterfall. Use only the moves the task requires.

| Skill | Question |
|---|---|
| `ground` | What is actually true? |
| `specify` | What must become true? |
| `investigate` | What consequential uncertainty must we resolve? |
| `decide` | What should we do, and why? |
| `realize` | Make the chosen change real. |
| `verify` | Did we build it right? |
| `validate` | Did we achieve the intent? |
| `learn` | What should permanently improve? |

## Codebase design

Design skills are not mandatory stages in the intent loop. Use them when a software change needs an explicit home, module boundary, or paved contribution path. They turn architecture into a falsifiable change hypothesis before ratchets enforce it.

| Skill | Question |
|---|---|
| `design-change` | Where should this change live, what owns it, and what blast radius should surprise us? |
| `design-module` | What independently changing decision or capability belongs behind this module's supported surface? |
| `pave-path` | How do we make the validated architectural path easier than inventing a new one? |

The design doctrine is **organize around observed units of change; expose only intended capabilities; make the supported path easy; make validated boundaries executable**. See [`references/change-locality.md`](references/change-locality.md), [`references/module-design.md`](references/module-design.md), [`references/public-surfaces.md`](references/public-surfaces.md), and [`references/dependency-graphs.md`](references/dependency-graphs.md).

## Ratchets

Ratchets are not extra stages in the loop. They change the repository in which future operators work. `learn` routes recurring or consequential mechanical lessons into them.

| Skill | Question |
|---|---|
| `ratchet` | What is the strongest cheap durable mechanism for this lesson? |
| `create-check` | Can this invariant be deterministically rejected? |
| `wire-check` | Does the important check run in the normal contributor and CI path? |
| `harden-boundary` | Can this invalid dependency arrow be made mechanically impossible? |
| `harden-check` | What cheap bypasses can make the verifier green without satisfying the invariant? |

The shared contract is **observe → generalize → select → install → prove → wire → explain → preserve**. Mechanical guardrails should normally prove **clean PASS → representative violation FAIL → clean PASS**. See [`references/ratchets.md`](references/ratchets.md) and [`references/mechanism-ladder.md`](references/mechanism-ladder.md).

## Design rules

1. **Evidence over assertion.** Claims that control consequential work should be traceable to observations.
2. **Intent before intervention.** Do not silently turn a proposed solution into the objective.
3. **Decision sufficiency over exhaustive research.** Stop when more information is unlikely to change the next move.
4. **Verification is not validation.** Conformance to specification and achievement of intent are different claims.
5. **Ratchet, don't accrete.** Prefer tests, constraints, tooling, observability, and simplification over more instructions.
6. **Design for change locality.** Make placement and ownership obvious, preserve small supported surfaces, and investigate unexpected cross-boundary movement.
7. **Pave before prohibiting.** Make the intended path easier to discover and use before or alongside making known-invalid paths impossible.
8. **No mandatory ceremony.** A typo may need only `realize → verify`; a production incident may exercise the whole loop.

See [`references/kernel.md`](references/kernel.md) for shared semantics and transition rules and [`references/progress.md`](references/progress.md) for the evidence-backed progress protocol.

## Package formats

The repository follows the portable Agent Skills layout: every installable unit lives at `skills/<name>/SKILL.md`, with skill-specific resources packaged inside the same directory. No npm package or registry publication is required.

`.codex-plugin/plugin.json` also exposes the collection as a skill-only Codex plugin package. The portable Skills CLI installation above remains the recommended cross-agent path.

## Validation and evals

Run the repository checks locally:

```bash
python3 scripts/validate.py
npx skills@latest add . --list
```

`evals/cases/` contains harness-neutral behavioral fixtures. Each case states a scenario, expected skill behavior, and anti-patterns; they cover the intent operators, codebase-design skills, and ratchet layer.

## License

[MIT](LICENSE)
