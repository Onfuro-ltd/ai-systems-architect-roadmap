# 05 — Preference Optimisation

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **05 — Preference Optimisation** within Fine-Tuning and Specialist Models;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose
Preference optimisation uses comparative feedback to shift model behaviour toward outputs judged better under defined criteria.

> Preference learning is only as meaningful as the rubric, comparisons, and population that produced the signal.

## Preference record

```text
Prompt/context
Candidate A
Candidate B
Preferred candidate
Rubric + metadata
```

Define what better means: factuality, completeness, concision, tone, safety, task success, tool behaviour, or another criterion.

## Label quality
Preserve rubric version, labeler population, disagreement, adjudication, and confidence where useful. Preference data can encode systematic bias or superficial style.

## SFT vs preference learning
SFT teaches desired examples directly. Preference methods teach relative desirability. They can complement each other, but add complexity only when comparative data has value.

## Proxy optimization
If labels reward verbosity, confidence, or polish, the model may optimize those rather than correctness. Independently measure the real task outcome.

## AI judges
Model judges can scale comparison but inherit model biases. Calibrate against trusted humans or deterministic evaluation. Avoid circular pipelines where a model generates, judges, and validates its own training data without independent checks.

## Multi-objective behaviour
Different workloads may need conflicting preferences. Routing or separate specialists can be cleaner than one universal preference signal.

## Evaluation
Use held-out comparisons plus objective task metrics, critical failures, factuality, safety/system regression, latency, and downstream outcomes.

## Exercise
Design preference data for a domain assistant: rubric, comparison generation, labeler guidance, disagreement handling, model-judge role, contamination controls, and independent evaluation.

## Takeaway
> Preference optimisation shapes what the model tends to choose. Make the preference signal explicit, governed, and independently evaluated.

Next: **06 — Synthetic Data**.
