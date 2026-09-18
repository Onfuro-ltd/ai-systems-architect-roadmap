# 06 — Drift, Feedback and Continuous Improvement

## Purpose

AI systems degrade or change as inputs, knowledge, providers, workflows and user behaviour evolve.

## Drift types

Monitor input/data drift, label/outcome drift, retrieval-corpus drift, model/provider behaviour changes, tool/API drift, prompt/configuration drift and business-process drift.

Not every metric change is model drift.

## Diagnose first

```text
Quality change
   ↓
Data? Retrieval? Tool? Prompt? Model? Policy? Infrastructure? Process?
   ↓
Root cause
   ↓
Correct intervention
```

Do not automatically retrain when the cause is elsewhere.

## Feedback

Separate raw signals from verified evidence. Clicks, thumbs-up, acceptance and lack of complaint may be noisy proxies.

Use outcome verification, human correction or authoritative comparison where appropriate.

## Continuous improvement

```text
Observe → detect → diagnose → curate → experiment → evaluate → controlled release
```

This is a governed loop, not autonomous self-modification.

## Provider drift

Hosted models can change behaviour. Use pinned versions where available, contract tests, recurring evaluation and routing fallback.

## Exercise

Create a drift dashboard and diagnostic playbook for an AI workflow whose accuracy falls while endpoint health remains normal.

## Takeaway

> Drift detection should start an investigation, not automatically change the model.

Next: **07 — Rollback, Incident Response and Recovery**.
