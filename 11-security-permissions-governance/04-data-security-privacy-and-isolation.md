# 04 — Data Security, Privacy and Isolation

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **04 — Data Security, Privacy and Isolation** within Security, Permissions and Governance;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

AI systems often combine sensitive data from users, organisations, memory, tools and external services.

Data security must survive model context, logging, retrieval and multi-tenant operation.

## Core Principle

> Give the model the minimum data required for the current task.

## Data Classification

Classify data according to sensitivity.

Example categories:

- public;
- internal;
- confidential;
- restricted.

The exact scheme should match the organisation.

## Data Minimisation

Ask:

- Does the model need this field?
- Does the tool need this record?
- Does the log need this payload?
- Does memory need to retain this information?

Remove unnecessary exposure.

## Tenant Isolation

Tenant isolation should exist at:

- authentication;
- authorization;
- query;
- storage;
- cache;
- vector index;
- memory;
- logging.

A model should not enforce tenant boundaries through prompt instructions.

## Retrieval Isolation

Apply hard tenant and access filters before similarity ranking.

Semantic similarity must never cross an authorization boundary.

## Context Isolation

Only place necessary data into model context.

Avoid loading:

- unrelated user history;
- entire databases;
- credentials;
- unnecessary secrets.

## Data Residency

Some systems may have geographic processing or storage requirements.

Track where:

- model processing;
- storage;
- logging;
- backups;
- third-party tools

occur.

## Retention

Define retention for:

- chats;
- tool payloads;
- traces;
- memory;
- eval datasets;
- logs.

"Keep everything" is not a governance strategy.

## Privacy by Design

Useful product controls can include:

- user visibility;
- correction;
- delete;
- consent;
- memory controls.

Applicable legal requirements depend on jurisdiction and role.

## Redaction

Redaction can remove:

- credentials;
- identifiers;
- sensitive fields

before data reaches:

- model;
- logs;
- external tools.

Redaction should preserve enough semantics for the task.

## Encryption

Use:

- encryption in transit;
- encryption at rest;
- key management.

Encryption does not prevent an authorised but over-privileged agent from reading data.

## Logging

Logs can become shadow data stores.

Prefer:

- identifiers;
- metadata;
- hashes;
- redacted payloads.

Limit full content logging.

## Backup

Backups need:

- access controls;
- retention;
- encryption;
- deletion strategy.

A deleted production record may remain in backup according to policy.

## Exercise

Map the data flow for a generic document-analysis agent.

For each boundary identify:

1. data category;
2. purpose;
3. access;
4. retention;
5. logging;
6. encryption;
7. deletion.

## Takeaway

> AI data security is the discipline of limiting where sensitive information can flow and persist.

Next: **05 — Agent and Tool Security**.
