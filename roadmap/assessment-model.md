# Assessment Model

This project does not treat reading a page or ticking a checkbox as mastery.

Assessment is evidence-based and should answer: **Can the learner make good decisions and build reliable systems?**

## Assessment dimensions

Each roadmap topic can be assessed across the following dimensions.

### 1. Explanation
Can the learner explain what the concept is, why it exists and how it works?

### 2. Selection
Can the learner determine when to use it and when not to use it?

### 3. Implementation
Can the learner build a representative implementation without hiding behind a no-code demo?

### 4. Failure analysis
Can the learner identify, reproduce and diagnose important failure modes?

### 5. Security and governance
Can the learner identify data, permission, autonomy and abuse risks and place appropriate controls?

### 6. Economics
Can the learner reason about latency, token/GPU cost, engineering cost, utilisation and cost per successful outcome?

### 7. Evaluation
Can the learner define a baseline, success criteria and regression tests?

### 8. Architecture
Can the learner integrate the capability into a larger system while preserving clear boundaries and replaceability?

### 9. Operations
Can the learner define observability, rollback, incident handling, versioning and maintenance requirements?

### 10. Outcome
Can the learner connect the capability to a measurable user, operational or business result?

## Suggested scoring

Use a 0–3 score for each applicable dimension:

- **0 — Not demonstrated**
- **1 — Conceptual**: can discuss the dimension but lacks practical evidence
- **2 — Demonstrated**: practical evidence exists in a controlled environment
- **3 — Production-grade judgement**: evidence includes realistic constraints, failures and operational controls

Do not calculate a single universal percentage and pretend it represents expertise. Different roles and projects require different profiles.

## Mastery gate

Before marking a topic complete, provide evidence for these questions:

- Can I explain it?
- Can I identify when to use it?
- Can I identify when not to use it?
- Have I built or operated it?
- Do I understand the important failure modes?
- Do I understand the security implications?
- Do I understand the economic implications?
- Can I compare credible alternatives?
- Can I evaluate whether it is actually working?
- Can I place it correctly inside a larger architecture?

## Evidence examples

Strong evidence includes:
- reproducible experiments;
- evaluation datasets and results;
- architecture decision records;
- incident/postmortem analysis;
- threat models;
- benchmark methodology and raw results;
- working implementations with tests;
- production metrics and traces;
- documented trade-off decisions.

Weak evidence includes:
- screenshots without methodology;
- vendor benchmark claims repeated without validation;
- GitHub star counts;
- influencer endorsements;
- a successful happy-path demo;
- model-generated self-evaluation with no independent checks.

## The core rule

**A system is not reliable because it worked once. A technology is not valuable because it is impressive. Mastery requires evidence, judgement and repeatability.**
