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

1. Read `AGENTS.md` and `PROGRAM_BRIEF.md`.
2. Capture a new intuition with `templates/concept.md` or a real event with `templates/observation.md`.
3. Add the record to `registry/records.json`.
4. Ask **Researcher** to locate related records and prior art.
5. Ask **Formalizer** to produce the strongest falsifiable version.
6. Ask **Skeptic** to attack the claim and propose competing explanations.
7. Ask **Experiment Designer** for the smallest experiment with high information value.
8. Route implementation through work packages; do not give Faraday blanket execution authority.
9. Ask **Verifier** to connect returned evidence to claims without overstating conclusions.
10. Ask **Program Director** what should be strengthened, weakened, split, falsified, or investigated next.

Run deterministic checks with:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

## Initial research directions

The starter records intentionally label ambitious ideas as speculative:

- engineering backpropagation;
- meaningful difference vs representational difference;
- care vs control;
- preservation of agency under corrective feedback;
- alignment as a property of coupled human–AI–environment systems;
- information gain as a way to prioritize experiments.

The purpose of Faraday is not to prove these ideas. It is to make them increasingly precise and easy to kill if they are wrong.
