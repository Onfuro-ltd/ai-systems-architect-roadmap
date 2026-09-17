# Domain 15 — Fine-Tuning and Specialist Models

## Purpose

Fine-tuning changes model behaviour by changing model parameters or learned adapters. It can create durable specialist capability, but it is not the default solution for missing knowledge, weak system design, or unreliable workflows.

> Put knowledge in weights only when learned behaviour is the right abstraction. Keep changing facts, permissions, business state, and auditable rules outside the model.

This domain covers dataset design, supervised fine-tuning, LoRA/QLoRA, preference optimisation, distillation, synthetic data, specialist models, evaluation, adapter lifecycle, and the decision to fine-tune or not.

## Learning objectives

By the end of this domain, you should be able to decide whether a problem belongs in prompting, RAG, tools, skills, deterministic code, memory, or fine-tuning; define a measurable specialist-model objective; design and govern training datasets; understand SFT and parameter-efficient tuning; reason about LoRA/QLoRA; understand preference optimisation, synthetic data, and distillation; evaluate tuned models; and manage adapters through production lifecycle.

## Domain structure

01 When to Fine-Tune and When Not To  
02 Dataset Design and Data Quality  
03 Supervised Fine-Tuning  
04 LoRA and QLoRA  
05 Preference Optimisation  
06 Synthetic Data  
07 Distillation and Specialist Models  
08 Evaluation and Regression Testing  
09 Adapter and Model Lifecycle and Governance  
10 Fine-Tuning and Specialist Models Capstone

## 1. Diagnose before tuning

Ask what is actually failing.

```text
Missing current facts?       → RAG / tools / authoritative data
Missing deterministic rule?  → code / policy engine
Missing reusable procedure?  → skill / workflow
Missing session/user context? → memory / state
Weak instructions?           → prompt/context engineering
Stable behavioural gap?      → consider fine-tuning
Capability gap?              → stronger/specialist model or training
```

Fine-tuning is appropriate only after the failure mode is understood.

## 2. Good uses

Fine-tuning can improve stable behaviours such as domain output conventions, classification/extraction patterns, structured transformations, style, task-specific patterns, and specialist performance. It can sometimes let a smaller model handle a bounded task with lower latency or cost.

## 3. Keep authoritative facts outside weights

Do not use fine-tuning as the authoritative store for current prices, inventory, permissions, customer state, frequently changing policy, secrets, transaction state, or rules requiring explicit traceability.

These belong in deterministic systems, governed knowledge, retrieval, or tools.

## 4. Dataset before algorithm

```text
Task definition
      ↓
Data specification
      ↓
Collection
      ↓
Cleaning / deduplication
      ↓
Label / response quality
      ↓
Train / validation / test separation
      ↓
Training
```

Training cannot rescue a confused task definition.

## 5. Data governance

Track provenance, rights, privacy classification, tenant boundaries, licensing, retention, transformations, synthetic origin, label source, dataset version, and approval state.

Training data is a governed production dependency.

## 6. Supervised fine-tuning

SFT trains the model toward desired outputs for representative inputs. Falling training loss is not enough; held-out task success must improve without unacceptable regressions.

## 7. LoRA and QLoRA

LoRA-style approaches train small low-rank adapters while leaving most base weights unchanged. QLoRA-style training combines a quantized base with trainable adapters to reduce training-memory requirements.

These approaches can make experimentation and specialist variants cheaper, but they do not remove dataset, evaluation, serving, or governance requirements.

## 8. Preference optimisation

Preference data encodes that one output is preferred to another under defined criteria.

```text
Input
 ↓
Candidate A vs Candidate B
 ↓
Preference signal
 ↓
Optimisation
```

Preference quality depends on a precise rubric and trustworthy labeling.

## 9. Synthetic data

Synthetic examples can expand coverage, but model errors can become training data and then be amplified.

Use provenance, deterministic validation, trusted reference data, diversity controls, human review where warranted, and held-out real-world evaluation.

Synthetic data must never silently masquerade as verified ground truth.

## 10. Distillation

Distillation can transfer useful behaviour from a stronger teacher/system into a smaller specialist.

The objective is not to copy every capability. Preserve the capability that matters for a defined workload and measure whether latency/cost improve without unacceptable quality loss.

## 11. Specialist models

Specialists are attractive for narrow, frequent, measurable, stable tasks such as classification, extraction, routing, normalization, scoring, and domain transformations.

Consequential authorization and business effects remain outside the model.

## 12. Evaluation

Compare the base model, prompt/RAG/tool improvements, fine-tuned candidate, and alternative specialist models.

Use held-out data and measure task success, critical failures, schema validity, tool behaviour, latency, throughput, cost, and relevant subgroup performance.

## 13. Contamination and regression

Keep training, validation, and test sets separate. Prevent near-duplicate leakage and synthetic generation from test cases.

Improving one behaviour can damage another, so maintain regression suites for important base capabilities and safety/system requirements.

## 14. Adapter lifecycle

Treat an adapter as a versioned artifact:

```text
Base model revision
+ Dataset version
+ Training configuration
+ Adapter hash
+ Evaluation
+ Approval
= Deployable specialist
```

A base-model upgrade can invalidate adapter assumptions.

## 15. Serving specialists

Specialists may use separate models, hot-swapped adapters, dedicated serving pools, or routing. Choose according to model size, adapter support, latency, concurrency, isolation, and workload frequency.

Avoid creating an unmanageable fleet of specialists.

## 16. Multi-tenancy

Per-tenant tuning creates privacy, ownership, evaluation, and operational complexity. Often a shared specialist plus tenant-specific retrieval, configuration, or skills is safer and easier to maintain.

## 17. Security and privacy

Training data may contain sensitive information, poisoned labels, malicious examples, or secrets. Apply provenance, minimization, access controls, sanitization, poisoning defenses, artifact security, and deployment permissions.

Never treat model weights as a secret store.

## 18. Economics

Fine-tuning cost includes data collection, labeling/review, training compute, experiments, evaluation, serving, monitoring, retraining, and governance.

Compare lifecycle cost with better prompting, retrieval, deterministic automation, or routing to a stronger model.

## 19. Feedback loops

```text
Model decision
      ↓
Human/system outcome
      ↓
Verified feedback
      ↓
Curated dataset
      ↓
Evaluation
      ↓
Controlled retraining
```

Do not automatically train on every production interaction.

## 20. Model independence

Store durable organizational knowledge in datasets, evaluation suites, schemas, skills, tools, and policies, not only inside one model's weights.

## Architecture principles

1. Diagnose before tuning.
2. Dataset quality dominates training cleverness.
3. Changing facts belong outside weights.
4. Fine-tuned output remains probabilistic.
5. Held-out evaluation decides promotion.
6. Synthetic data requires provenance and verification.
7. Treat adapters as production artifacts.
8. Keep authoritative rules and permissions deterministic.
9. Optimize cost per successful outcome.
10. Preserve organizational knowledge outside any one model.

## Capstone direction

The capstone will design a specialist-model factory:

```text
Observed workload gap
      ↓
Root-cause / fine-tune decision
      ↓
Dataset specification
      ↓
Governed data pipeline
      ↓
SFT / PEFT / distillation experiment
      ↓
Held-out evaluation
      ↓
Registry + approval
      ↓
Canary / routed deployment
      ↓
Outcome monitoring
      ↓
Curated feedback
      ↓
Controlled next version
```

The learner must also demonstrate a case where fine-tuning is rejected in favor of RAG, tools, skills, memory, deterministic logic, or model routing.

## Takeaway

> Fine-tuning is a way to encode stable learned behaviour, not a replacement for architecture. Keep truth, policy, permissions, and changing business knowledge outside the model, and promote specialists only when measured outcomes justify their lifecycle cost.

Next: **01 — When to Fine-Tune and When Not To**.
