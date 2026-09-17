# 10 — Fine-Tuning and Specialist Models Capstone

## Purpose
Design an enterprise specialist-model factory that converts verified workload gaps into governed, measurable, deployable capabilities.

> The factory must be equally capable of approving a fine-tune and proving that fine-tuning is the wrong intervention.

## Scenario
A multitenant AI platform has high-volume tasks currently handled by general models. It wants lower cost and latency without sacrificing quality, privacy, auditability, or model independence.

Some gaps are behavioural. Others are stale knowledge, retrieval, tools, deterministic rules, state, or workflow problems.

## Architecture

```text
Observed workload gap
      ↓
Root-cause classification
      ↓
Choose intervention
      ↓
If tuning justified:
Governed dataset
      ↓
SFT / PEFT / preference / distillation
      ↓
Independent evaluation
      ↓
Registry + governance
      ↓
Routed specialist deployment
      ↓
Deterministic validation / policy
      ↓
Verified outcome
      ↓
Curated feedback
      ↓
Controlled next version
```

## Required design

Select at least four workload gaps and classify each as knowledge, behaviour, capability, workflow, state, tool, or deterministic-policy failure. At least one must explicitly reject fine-tuning.

For each tuning candidate define baseline, target, unacceptable regressions, latency/cost objective, and break-even assumptions.

Define dataset schema, production distribution, hard/negative cases, rubric, source rights, privacy, tenant policy, deduplication, immutable splits, and provenance.

If synthetic data is used, define generator/version, trusted reference, validation, sampling, diversity checks, contamination controls, and synthetic labels.

Design comparable SFT, LoRA/QLoRA, preference, or distillation experiments with immutable model, tokenizer, dataset, configuration, code/environment, checkpoint, and artifact identities.

Define each specialist's supported boundary and escalation behaviour.

Compare base + best system design, alternative models, tuned candidates, and specialist + escalation. Measure task success, critical errors, schema/tool behaviour, regression slices, latency, throughput, resources, and cost per successful outcome.

Create registry states from experiment through evaluation, approval, canary, production, restriction, deprecation, and retirement.

Design serving as workflow → eligibility/policy → router → specialist or general model → validation/escalation → workflow. Keep deterministic business controls outside both model routes.

For adapter fleets define loading, switching, cache, concurrency, compatibility, tenant isolation, and base-upgrade strategy.

Cover training-data access, poisoning, secrets, checkpoints, experiment tracking, artifact integrity, activation permissions, tenant isolation, and retention/deletion.

Production feedback must follow outcome → candidate feedback → verification → curation → next dataset → offline evaluation → controlled promotion. No raw automatic self-training.

Monitor drift and diagnose source before retraining.

Calculate full economics including data, labeling, synthetic validation, training, experiments, serving, escalation, evaluation, monitoring, governance, and retraining.

## Failure matrix
Cover contaminated data, label error, privacy breach, poisoning, overfitting, regression, incompatible base upgrade, wrong adapter routing, serving failure, out-of-domain input, synthetic error amplification, drift, and failed rollback.

## Deliverables
Produce intervention matrix, tuning ADRs, dataset specification, lineage/governance design, synthetic policy, training plan, specialist contracts, held-out suite, regression matrix, model/adapter registry, serving/routing design, security/privacy model, feedback workflow, drift plan, economic model, failure matrix, rollout/rollback plan, and at least three ADRs.

## Acceptance criteria
The strongest non-tuned baseline must be known. Tuning must solve stable behavioural/capability gaps. Current truth and deterministic rules stay outside weights. Datasets are governed/versioned. Evaluation is independent. Synthetic data is traceable. Artifacts have immutable lineage. Specialists have explicit boundaries. Fallbacks are safe. Tenant isolation is deterministic. Feedback is verified before training. Regressions block promotion. Rollback is proven. Economics compare the complete system.

## Final principle
> Durable organizational intelligence should survive a model replacement. Keep knowledge, evaluations, datasets, policies, tools, skills, and outcome feedback as first-class assets; use model weights only for the learned behaviour they are best suited to encode.

**Domain 15 — Fine-Tuning and Specialist Models complete.**

Next domain: **16 — GPU and Inference Infrastructure**.
