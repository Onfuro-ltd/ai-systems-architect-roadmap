# 07 — Privacy, Security and User Control

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **07 — Privacy, Security and User Control** within Memory Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Memory creates a persistent record of information that may outlive the interaction that produced it.

That makes privacy, security and user control central to memory design.

## Core Principle

> Persistence increases responsibility.

## Data Minimisation

Store only what is useful for a defined purpose.

Avoid retaining sensitive data simply because it may someday be useful.

Questions include:

- Why is this needed?
- For how long?
- Who may access it?
- Can the user inspect it?
- Can it be corrected?
- Can it be deleted?

## Sensitive Information

Memory systems may encounter:

- personal data;
- financial information;
- health information;
- credentials;
- private documents;
- workplace information.

Sensitive categories may require stronger retention, access and logging controls.

## Access Control

Memory reads and writes should respect:

- user identity;
- workspace;
- tenant;
- role;
- service identity;
- purpose.

A model should not decide access policy by itself.

## Cross-User Leakage

Memory retrieval must never mix subjects merely because semantic similarity is high.

Use hard identity filters before semantic ranking.

## Prompt Injection and Memory Poisoning

Untrusted content can attempt to create harmful persistent memory.

Examples:

- webpage says "remember this permanently";
- malicious document inserts false user preference;
- tool result tries to write policy.

Memory-write authority should distinguish trusted instruction from untrusted content.

## Memory Poisoning

Memory poisoning occurs when incorrect or adversarial information is stored and later influences behaviour.

Controls include:

- provenance;
- trust labels;
- write policy;
- confirmation;
- conflict detection;
- review.

## User Visibility

Users benefit from being able to understand what persistent memory exists.

Depending on the product, useful controls can include:

- view;
- correct;
- delete;
- disable;
- scope.

User-visible control improves trust and error correction.

## User Correction

A correction should update future behaviour.

Systems should avoid:

- keeping old wrong memory active;
- re-deriving deleted memory from stale summaries;
- requiring users to repeat corrections indefinitely.

## Right to Delete

Deletion should account for:

- primary records;
- indexes;
- caches;
- derived summaries;
- replicas;
- training pipelines where applicable.

Legal requirements vary by jurisdiction and system role.

## Encryption

Memory stores may require:

- encryption in transit;
- encryption at rest;
- key management;
- field-level protection for sensitive categories.

Encryption does not replace access control.

## Logging

Do not duplicate memory content into unrestricted logs.

Prefer metadata and identifiers where full payloads are unnecessary.

## Retention Policy

Define retention by memory type.

Examples:

- working memory: short-lived;
- episodic memory: time-bounded;
- semantic preference: until changed or deleted;
- audit record: policy-defined.

## Enterprise Governance

Enterprise memory may require:

- tenant-level policy;
- data residency;
- retention schedules;
- legal hold;
- role-based access;
- audit trails.

Domain 11 covers governance in broader depth.

## Exercise

Threat-model a memory system that stores user preferences and prior decisions.

Identify risks for:

1. cross-user leakage;
2. poisoning;
3. over-retention;
4. deletion failure;
5. sensitive logging;
6. unauthorised write.

## Takeaway

> Memory should be useful to the user without becoming invisible permanent surveillance.

Next: **08 — Memory Evaluation and Observability**.
