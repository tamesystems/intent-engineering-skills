# Change Locality

A well-designed codebase makes the intended change **obvious, local, and contained**.

## Three properties

- **Obvious** — an unfamiliar contributor can form a good placement hypothesis without repository folklore.
- **Local** — the behavior and its proof mostly change behind one coherent ownership boundary.
- **Contained** — unrelated consumers depend on a controlled surface rather than implementation details.

Locality is not file count. Ten files changed inside one coherent module may be healthier than three files changed across three unrelated owners. Track **architectural boundaries crossed** and knowledge leaked, not merely diff size.

## Design around change

Decomposition should follow the system's dominant units of independent change. For a business application those may be capabilities such as billing or recruiting; for a compiler they may be parser/lowering/optimizer/codegen; for a developer platform they may be core/plugins/adapters. Do not impose vertical slices when the observed change structure says otherwise.

Useful evidence includes domain language, existing public surfaces, dependency rules, tests, ownership, and git history showing files/modules that repeatedly change together.

## Expected blast radius

Before a consequential realization, record:

- owner of the behavior;
- supported public operation;
- expected modules/paths touched;
- legitimate collaborators;
- important areas expected to remain unchanged.

After realization, compare this prediction with the actual diff. Unexpected cross-boundary movement is a discrepancy to investigate, not proof by itself that the implementation is wrong.

Repeated discrepancy is architectural evidence. It may mean implementation is leaking, a capability is missing, two concepts actually change together, or a declared boundary is artificial. Do not respond automatically by adding another lint rule.

## Common locality failures

- horizontal scattering of one behavior across global technical folders;
- `shared/`, `common/`, `utils/`, or `helpers/` becoming ownership sinks;
- callers reaching into module internals;
- public APIs exposing persistence/provider representation;
- premature micro-packages that add navigation without hiding complexity;
- a local product change requiring edits to unrelated registration/configuration machinery.
