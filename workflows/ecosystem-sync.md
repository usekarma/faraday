# Ecosystem knowledge refresh

Faraday learns by revising an explicit, reviewable knowledge state from evidence. It does not learn by silently accumulating conversational context.

## Purpose

Keep `current-state/` useful without turning it into an authority source or rewriting durable research history.

## Read-only refresh loop

1. Read `registry/ecosystem.json`, `registry/epistemic.json`, `registry/authority.json`, and `registry/records.json`.
2. Inspect only the repositories and evidence sources required by active programs.
3. Record exact repository/revision/path provenance for every observation used.
4. Compare observed state with `current-state/`.
5. Produce proposed updates for repository revisions, active programs, blockers, evidence freshness, contradictions, and negative results.
6. Run a Skeptic pass: identify a simpler explanation, missing provenance, and what could make the proposed update wrong.
7. Run a Verifier pass: classify each item using `registry/epistemic.json` and identify exactly which claims it bears on.
8. **STOP_FOR_HUMAN** before changing claim maturity, routing a new work package, or requesting consequential downstream execution.

## Non-negotiable distinctions

`current-state/` is a convenience snapshot, not durable truth.

A refresh may say:

> Repository X moved from revision A to B, therefore evidence tied to A is historical for current-code claims.

It may not say:

> The claim is false because the repository changed.

without new evidence.

Likewise:

```text
evidence says safe
!=
authorization to execute
```

## Decision relevance

Every unresolved question should state the decision that changes depending on the answer. A question that changes no decision should normally be lower priority unless it is intentionally exploratory.

Rank candidate experiments qualitatively:

```text
decision importance × expected discrimination × evidence quality
---------------------------------------------------------------
                         cost / risk
```

Use `HIGH`, `MEDIUM`, or `LOW` unless a defensible quantitative model exists. Never invent numerical information gain.

## Completion report

Report:

- sources inspected and exact revisions;
- proposed current-state changes;
- stale or superseded evidence;
- claim transitions proposed, if any;
- blockers added or cleared;
- strongest counterexample or simpler explanation;
- highest-value next experiment;
- exact human decision required.

A refresh itself grants no downstream authority.
