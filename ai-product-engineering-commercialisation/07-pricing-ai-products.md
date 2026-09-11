# 07 — Pricing AI Products

## Purpose

Pricing an AI product requires balancing customer value, usage variability, infrastructure cost, predictability, and growth. AI pricing should be designed together with the product's unit economics rather than added after launch.

## Core principle

> Price the value of the product, while protecting the economics of delivering that value.

## 1. Start with customer value

Ask:

- What valuable outcome does the product create?
- How frequently is that outcome delivered?
- What does the customer currently spend on the problem?
- What is the cost of doing nothing?
- How does the customer's willingness to pay change as usage or value increases?

Do not anchor pricing only to model/API cost.

## 2. Main pricing models

### Seat-based

Charge per user or role.

Strengths:

- predictable revenue;
- simple to understand;
- familiar for SaaS buyers.

Weakness:

Usage-heavy customers can become unprofitable if AI consumption varies substantially between users.

### Usage-based

Charge for measurable consumption such as tasks, documents, credits, or processed records.

Strengths:

- aligns revenue with usage;
- scales naturally with consumption.

Weaknesses:

- less predictable bills;
- customers may restrict usage because of cost anxiety.

### Tiered pricing

Offer defined capability and usage levels.

```text
Starter → Growth → Business → Enterprise
```

This is often a strong default for AI SaaS because it combines packaging with economic guardrails.

### Outcome/value-based

Price around business value rather than activity volume.

This can produce strong economics where outcomes are measurable, but requires credible measurement and customer trust.

### Hybrid

Combine a platform subscription with included usage and overage/expansion pricing.

```text
Base subscription
+
Included AI allowance
+
Additional usage / premium capabilities
```

## 3. Credits and units

Credits can simplify complicated underlying costs.

However, credits should correspond to something customers can understand. Avoid arbitrary units whose only purpose is hiding pricing complexity.

Good examples:

- AI analyses;
- workflow runs;
- processed products;
- documents reviewed.

## 4. Protect the economics

Every plan should have a cost envelope.

```text
Expected revenue
− expected variable delivery cost
= contribution
```

Model worst-case and high-usage behaviour, not only average usage.

Consider:

- unusually large prompts;
- repeated agent loops;
- expensive model routing;
- heavy retrieval;
- tool/API charges;
- human review.

## 5. Avoid punitive pricing

Do not make customers afraid to use the product because every useful interaction creates an unexpected charge.

Prefer:

- clear allowances;
- transparent overages;
- sensible limits;
- usage visibility;
- predictable enterprise contracts.

## 6. Packaging AI capabilities

Do not package only by model access.

Better packaging can be based on customer outcomes:

```text
Starter
- Core insights
- Limited automation

Growth
- More workflows
- Advanced intelligence
- Higher usage

Business
- Automation
- Integrations
- Controls
- Analytics

Enterprise
- Custom limits
- Security
- Governance
- Support
- Contractual requirements
```

## 7. Free trials and free tiers

A trial should demonstrate the value moment without creating an uncontrolled compute liability.

Controls can include:

- time-limited trials;
- bounded workflow counts;
- rate limits;
- lower-cost models for exploration;
- restricted high-cost features.

The objective is to prove value, not maximise free inference.

## 8. Enterprise pricing

Enterprise customers may require:

- annual contracts;
- committed usage;
- volume discounts;
- security/compliance packages;
- support tiers;
- custom deployment arrangements.

Discounts should be based on predictable economics, not arbitrary negotiation.

## 9. Pricing experiments

Test:

- packaging;
- price points;
- included usage;
- feature boundaries;
- annual vs monthly commitment;
- expansion triggers.

Measure:

- conversion;
- activation;
- usage;
- retention;
- expansion;
- gross margin;
- customer objections.

## 10. SEMLIS application

SEMLIS should not necessarily charge simply because an AI model was invoked.

A stronger eventual model could combine a platform subscription with usage or capability tiers tied to merchant scale and value.

For example, packaging could evolve around:

- number of products managed;
- marketplace connections;
- intelligence workflows;
- automation capabilities;
- advanced analytics;
- enterprise controls.

The exact price should be validated with customers and backed by measured unit economics rather than guessed in advance.

## 11. Pricing anti-patterns

### Cost-plus pricing

Charging model cost plus a fixed markup ignores the value created and can leave substantial willingness to pay unrealised.

### Unlimited AI too early

Unlimited plans can expose the company to pathological usage and negative margins.

### Feature dumping

Adding features to justify higher tiers can create confusing products instead of meaningful value differences.

### Artificial limits

Limits that feel unrelated to customer value damage trust.

### Ignoring expansion

AI usage often grows with customer success. Pricing should provide a natural path for customers to expand without forcing disruptive migrations.

## 12. Enterprise decision checklist

Before launching pricing, answer:

1. What outcome is the customer paying for?
2. What is the primary pricing metric?
3. Does the metric correlate with value?
4. Does it correlate sufficiently with cost?
5. What happens with extreme usage?
6. Is the bill predictable?
7. Can customers understand it quickly?
8. Can the product expand naturally as customers grow?
9. Can enterprise contracts accommodate security and governance requirements?
10. Can margins remain healthy as model providers and infrastructure change?

## Takeaway

> Great AI pricing makes value obvious to the customer and economics sustainable for the company.

The best pricing model is usually discovered through evidence, not chosen from a template.
