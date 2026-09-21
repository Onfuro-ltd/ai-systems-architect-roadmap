# 04 — Human Evaluation and Model Judges

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **04 — Human Evaluation and Model Judges** within Evaluation and Reliability;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Some AI behaviour cannot be evaluated reliably with deterministic rules.

Humans and model-based judges can provide behavioural evaluation, but both have limitations.

## Core Principle

> Treat every evaluator as a measurement instrument that must itself be validated.

## Human Evaluation

Humans are useful when:

- domain expertise matters;
- consequences are high;
- criteria are subjective;
- new failure modes are being discovered.

Human evaluation is not automatically perfect.

Humans can disagree, fatigue and interpret rubrics differently.

## Rater Instructions

Good human evaluation requires:

- clear rubric;
- examples;
- boundary cases;
- escalation path;
- blind comparison where useful.

## Inter-Rater Agreement

Measure whether raters agree.

Low agreement may indicate:

- unclear rubric;
- ambiguous task;
- insufficient training;
- genuinely subjective criteria.

Do not treat disagreement as merely a rater problem.

## Model Judges

A model judge can evaluate outputs at scale.

Useful applications include:

- rubric scoring;
- pairwise comparison;
- error classification;
- evidence checks;
- trace grading.

## Judge Risks

Model judges can exhibit:

- position bias;
- verbosity preference;
- style bias;
- self-preference;
- correlated error;
- prompt sensitivity.

Judge outputs need validation.

## Judge Calibration

Compare judge decisions with expert human labels.

Measure:

- agreement;
- false positives;
- false negatives;
- performance by slice.

## Reference-Guided Judge

Where possible, provide the judge with:

- rubric;
- reference evidence;
- expected answer properties.

This is stronger than asking:

> "Is this answer good?"

## Pairwise Judging

Pairwise comparison can reduce ambiguity.

Randomise output order.

Do not reveal system identity if it could bias the judge.

## Ensemble Judges

Multiple judges can reduce some errors.

However, using several similar models can preserve correlated bias.

Diversity of evaluators can matter more than count.

## Human-in-the-Loop Calibration

A practical pattern:

```text
Model Judge
   |
Low Confidence / High Risk
   |
Human Review
```

The boundary should be defined in advance.

## Cost

Human review is expensive.

Model judging consumes model cost.

Use deterministic evaluation first to reduce unnecessary subjective grading.

## Auditability

Store enough evaluation evidence to reproduce:

- input;
- output;
- rubric;
- judge version;
- score;
- rationale where appropriate.

## Exercise

Create a model-judge rubric for a generic summarisation task.

Then define:

1. calibration set;
2. human agreement target;
3. bias checks;
4. low-confidence escalation.

## Takeaway

> A model judge is useful automation, not ground truth.

Next: **05 — Agent, Tool and Workflow Evaluation**.
