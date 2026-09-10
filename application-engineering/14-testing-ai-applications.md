# Testing AI Applications

## Introduction

Traditional software testing asks whether the code produces the expected result.

AI application testing must answer a broader question:

> Does the system produce useful, reliable, safe and measurable outcomes under realistic conditions?

AI systems are probabilistic. A change that improves one example may damage many others. A model upgrade that sounds more capable may introduce new failure modes.

Therefore, testing is not an optional quality step. It is part of the architecture.

---

# 1. Why AI testing is different

Traditional software:

```
Input
  |
Code
  |
Expected output
```

AI application:

```
Input
  |
Context assembly
  |
Model selection
  |
Model inference
  |
Tool calls
  |
Validation
  |
Output/action
  |
Real-world outcome
```

The system can fail at every layer.

Examples:

- correct model, wrong context;
- correct context, wrong interpretation;
- correct answer, unsafe action;
- correct action, poor business outcome;
- successful demo, unreliable production behaviour.

---

# 2. Testing pyramid for AI systems

A mature AI application should have multiple testing layers.

## Unit tests

Test deterministic components:

- schemas;
- validators;
- permission checks;
- routing rules;
- business logic;
- tool interfaces.

AI should not be used where normal deterministic testing is possible.

## Component tests

Test individual AI capabilities:

- extraction;
- classification;
- retrieval;
- summarisation;
- tool selection.

## Integration tests

Test complete flows:

```
User request
    |
Context
    |
Model
    |
Tools
    |
Validation
    |
Outcome
```

## System tests

Test the complete product with realistic users, data and constraints.

## Production evaluation

Monitor real behaviour after deployment.

---

# 3. Golden datasets

A golden dataset is a controlled collection of representative tasks used to measure system behaviour.

A strong dataset includes:

- normal cases;
- edge cases;
- ambiguous cases;
- adversarial cases;
- known failures;
- safety-sensitive scenarios.

A weak dataset contains only examples where the AI already succeeds.

---

# 4. Regression testing

Every meaningful change should answer:

> Did we improve the system overall, or only improve one example?

Regression tests should run when changing:

- models;
- prompts/instructions;
- retrieval methods;
- tools;
- memory systems;
- routing logic;
- business rules.

---

# 5. Evaluation dimensions

AI quality should not be reduced to one score.

Evaluate:

## Accuracy

Is the result correct?

## Reliability

Does it behave consistently?

## Grounding

Is the response supported by available information?

## Safety

Does it respect permissions and policies?

## Cost

Does quality justify resource usage?

## Latency

Is the experience practical?

## User outcome

Did it actually improve the intended task?

---

# 6. Testing tool use

When AI can call tools, test:

- correct tool selection;
- incorrect tool selection;
- invalid arguments;
- permission failures;
- unavailable tools;
- duplicate execution;
- malicious tool instructions.

A tool-enabled AI system is effectively a software operator and must be tested accordingly.

---

# 7. Adversarial testing

Important attack categories:

- prompt injection;
- malicious documents;
- data extraction attempts;
- instruction conflicts;
- privilege escalation attempts;
- unexpected tool requests.

Security testing must assume users, data sources and external content may be untrusted.

---

# 8. Human evaluation

Human review remains important for:

- complex reasoning;
- usefulness;
- trust;
- preference;
- business suitability.

However, human evaluation must be structured.

Avoid:

> "It feels better."

Prefer:

- defined criteria;
- comparison against baseline;
- documented disagreements;
- repeatable scoring.

---

# 9. Model upgrade testing

Changing models is not automatically an improvement.

Before upgrading:

```
Current system
      |
Golden dataset
      |
New model
      |
Compare results
      |
Review regressions
      |
Deploy gradually
```

A newer model can improve reasoning while harming latency, cost or reliability.

---

# 10. Feedback loops

The strongest AI systems learn from operation.

Feedback sources:

- user corrections;
- successful outcomes;
- failed actions;
- support tickets;
- human approvals;
- business metrics.

Feedback should improve:

- evaluation sets;
- prompts;
- retrieval;
- routing;
- workflows;
- models.

---

# 11. The AI engineering rule

Never ask only:

> "Can the AI do this?"

Ask:

- Can we measure it?
- Can we detect failure?
- Can we recover safely?
- Can we prove improvement?
- Can we operate it at scale?

---

# Mastery gate

A learner completes this module when they can:

- design an AI evaluation strategy;
- create a meaningful golden dataset;
- test AI behaviour across normal and adversarial scenarios;
- evaluate model changes safely;
- connect technical metrics to real outcomes;
- build feedback loops for continuous improvement.

---

# Principle

**An AI system without evaluation is a changing opinion. An AI system with evaluation becomes an engineered capability.**
