# 03 — Evaluation Pipelines and Quality Gates

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **03 — Evaluation Pipelines and Quality Gates** within MLOps and LLMOps;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Evaluation pipelines turn quality requirements into repeatable release controls.

> CI tells you whether software still builds. AI evaluation must also tell you whether behaviour is still acceptable.

## Evaluation layers

Use deterministic tests, task metrics, model-graded rubrics where calibrated, human review where warranted, safety/policy tests, adversarial cases, operational benchmarks and outcome evaluation.

## Golden and held-out suites

Maintain representative datasets with difficult, negative and consequential cases. Protect clean holdouts from tuning and prompt overfitting.

## Quality gates

Define thresholds before viewing results. A candidate can require minimum task quality, maximum critical-error rate, schema/tool correctness, safety regression limits, latency SLO and cost ceiling.

## Slices

Evaluate meaningful cohorts separately. Aggregate gains must not hide severe regressions by language, document type, task class or other relevant segment.

## Continuous evaluation

Run fast checks on changes and broader suites before promotion. Periodically evaluate production samples using governed sampling and privacy controls.

## Judge calibration

Model judges are scalable but not independent truth. Compare them with deterministic references or trusted human judgments and monitor judge-version changes.

## Exercise

Design a release gate where a cheaper model may deploy only if quality, critical failures, latency and cost all remain within agreed bounds.

## Takeaway

> Evaluation becomes operationally valuable when it can block a bad release.

Next: **04 — Deployment Strategies and Release Engineering**.
