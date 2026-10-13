# Faraday

**Turn intuition into falsifiable, instrumented knowledge.**

Faraday is the research and experimental control plane for the UseKarma ecosystem. It preserves the lineage of ideas, turns concepts into testable hypotheses, routes experiments to the right implementation repositories, gathers evidence, invites adversarial review, and updates the program without silently rewriting history.

Faraday does **not** own production infrastructure or deployment authority. It coordinates questions and evidence while Adage, `aws-config`, `aws-iac`, adage-fabric, Karma, and experiment-specific repositories retain their own implementation and authorization boundaries.

## Core loop

```text
intuition / surprise
        ↓
observation or concept
        ↓
formalized hypothesis
        ↓
skeptical challenge
        ↓
falsifiable experiment
        ↓
scoped work packages
        ↓
external apparatus / repositories
        ↓
evidence
        ↓
interpretation
        ↓
strengthen / weaken / split / falsify
        ↺
```

A result is not promoted because an agent finds it persuasive. Evidence, explicit assumptions, counterexamples, and human judgment determine status.

## What belongs here

Faraday owns:

- ideas worth preserving;
- observations and surprises;
- concepts and formal definitions;
- falsifiable hypotheses;
- experiment specifications and acceptance criteria;
- cross-repository research programs and work packages;
- evidence references and provenance;
- counterexamples and competing explanations;
- decisions about what to investigate next;
- claim maturity and revision history.

Faraday does not automatically own the implementation. An experiment may route work to `iot-digital-twin`, `adage-fabric`, `aws-config`, `aws-iac`, Karma, or another repository.

## Ecosystem roles

```text
Faraday      What should we learn or prove next?
Adage        How does intent become a controlled system?
aws-config   What should exist?
aws-iac      How is it implemented safely?
adage-fabric What happened, and how is it observed?
Karma        What does the evidence justify, and what may proceed?
Faraday      What did we learn, and what should change next?
```

The machine-readable version lives in `registry/ecosystem.json`. Faraday owns direction, not final authority.

## Explicit knowledge state

Faraday separates durable research history from volatile operating context:

```text
registry/records.json          durable research lineage
registry/ecosystem.json        system roles and repository boundaries
registry/epistemic.json        observation → interpretation → claim vocabulary
registry/authority.json        execution and authorization boundaries
current-state/repositories.json captured repository revisions
current-state/programs.json    active programs and decision gates
current-state/blockers.json    unresolved questions and decisions they block
current-state/evidence-freshness.json revision/freshness applicability
```

`current-state/` is deliberately **not** authoritative truth. It is a reviewable snapshot. Evidence tied to revision A does not silently become evidence for revision B. A refresh proposes changes through `workflows/ecosystem-sync.md`; it does not rewrite historical evidence or grant execution authority.

Faraday distinguishes:

```text
observation
measurement
derived fact
interpretation
hypothesis
counterexample
decision
authorization
```

In particular:

```text
evidence says safe
!=
authorization to execute
```

## Record types

| Type | Meaning |
| --- | --- |
| `I` | Idea / intuition worth preserving |
| `O` | Observation: something actually happened |
| `C` | Concept: proposed interpretation or definition |
| `H` | Hypothesis: falsifiable claim |
| `EXP` | Experiment: attempt to distinguish outcomes |
| `E` | Evidence: recorded result or external artifact |
| `CE` | Counterexample / competing explanation |
| `D` | Decision: human-reviewed program decision |
| `Q` | Open question |
| `WP` | Work package routed to another repository |

## Claim maturity

Claims may move forward or backward:

```text
SPECULATIVE → FORMALIZED → TESTABLE → UNDER_TEST → SUPPORTED → REPLICATED
                     ↘        ↓             ↓
                      WEAKENED / REFORMULATED / FALSIFIED
```

`SUPPORTED` never means proven in all contexts. `REPLICATED` requires independent or meaningfully distinct evidence.

## Start here

The current [first live research program](programs/karma-adage-ecosystem/README.md) assesses the Karma/Adage IoT engineering history in [E-003](evidence/E-003-live-program-history.md). Its next recommended experiment is [EXP-004](experiments/EXP-004-blinded-discrepancy-challenge.md). **STOP_FOR_HUMAN before creating new cross-repository work packages.** Earlier WP-001/WP-002 remain historical proposals and do not authorize this work.

For the latest research-director assessment, read [RDC-001](programs/karma-adage-ecosystem/cycles/RDC-001.md) and [Q-004](questions/Q-004-independent-discrepancy-oracle.md). Its next-investigation and current-state changes are proposals, not execution authority. The original [WP-001](work-packages/WP-001-trace-evidence-boundaries.md) read-only inventory was completed in E-002; its preserved proposal status does not imply unfinished inventory or authorize further work.

1. Read `AGENTS.md` and `PROGRAM_BRIEF.md`.
2. Read the ecosystem, epistemic, authority, and current-state registries before directing active work.
3. Capture a new intuition with `templates/concept.md` or a real event with `templates/observation.md`.
4. Add durable research records to `registry/records.json`.
5. Ask **Researcher** to locate related records and prior art.
6. Ask **Formalizer** to produce the strongest falsifiable version.
7. Ask **Skeptic** to attack the claim and propose competing explanations.
8. Ask **Experiment Designer** for the smallest experiment with high information value.
9. Route implementation through work packages; do not give Faraday blanket execution authority.
10. Ask **Verifier** to connect returned evidence to claims without overstating conclusions.
11. Ask **Program Director** what should be strengthened, weakened, split, falsified, or investigated next.

Run deterministic checks with:

```bash
python3 scripts/validate.py
python3 scripts/validate_context.py
python3 -m unittest discover -s tests -v
```

or simply:

```bash
make check
```

## GitHub tasks (small, explicit assignments)

Use [GitHub Issues](https://github.com/usekarma/faraday/issues) for a bounded task or Post-it-style idea. The [task issue template](.github/ISSUE_TEMPLATE/task.md) records a goal, scope, acceptance criteria, verification evidence, and approval boundaries. When you explicitly give Faraday and an implementation agent an issue, they can follow the [issue-to-PR workflow](workflows/issue-to-pr.md) to prepare a branch, run the target repository's checks, and submit a **draft** PR with evidence. This is a documented handoff, **not** a background queue, automatic agent launch, or proven autonomous execution. Keep the IoT POC first; validate one small task end-to-end before adding coordination.

## Initial research directions

Try the first executable demonstration:

```bash
python3 scripts/evidence_traps.py
```

[Evidence traps](experiments/EXP-002-evidence-traps/spec.md) asks whether “the action succeeded” justifies continuing. Twelve synthetic cases exercise identity, permission, freshness, intent, and contradiction. [The first result](evidence/E-001-evidence-traps.md) preserves both the failure of a success-only rule and the limits of an explicit checklist. No ecosystem implementation is tested.

The starter records intentionally label ambitious ideas as speculative:

- engineering backpropagation;
- meaningful difference vs representational difference;
- care vs control;
- preservation of agency under corrective feedback;
- alignment as a property of coupled human–AI–environment systems;
- information gain as a way to prioritize experiments.

The purpose of Faraday is not to prove these ideas. It is to make them increasingly precise and easy to kill if they are wrong.
