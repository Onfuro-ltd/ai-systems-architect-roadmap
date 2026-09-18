# 01 — AI Threat Modelling

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **01 — AI Threat Modelling** within Security, Permissions and Governance;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Threat modelling identifies what can go wrong before a system is trusted with meaningful authority.

AI threat models need to include conventional software threats and model-mediated threats.

## Core Principle

> Threat-model the complete system, not only the model endpoint.

## Assets

Identify what must be protected.

Examples:

- user data;
- credentials;
- business records;
- files;
- money;
- privileged actions;
- memory;
- prompts and policies;
- proprietary data;
- infrastructure.

## Actors

Actors can include:

- legitimate user;
- malicious user;
- compromised account;
- external attacker;
- untrusted document;
- third-party tool;
- malicious MCP server;
- compromised dependency;
- insider;
- autonomous agent.

An untrusted document is not a human actor, but it can carry attacker-controlled instructions into a model.

## Entry Points

Examples:

- chat;
- uploaded files;
- email;
- webpage;
- API;
- webhook;
- tool output;
- retrieved document;
- memory;
- MCP server metadata;
- third-party plugin.

## Trust Boundaries

Draw boundaries around:

- model;
- application;
- tools;
- databases;
- external services;
- tenants;
- users;
- agents.

Ask what information and authority cross each boundary.

## Threat Categories

Useful categories include:

- prompt injection;
- data exfiltration;
- tool misuse;
- excessive privilege;
- identity abuse;
- malicious or compromised dependency;
- memory poisoning;
- unexpected code execution;
- insecure output handling;
- denial of service;
- cost abuse;
- unsafe autonomy.

## Goal Hijacking

An agent can be induced to pursue an attacker-controlled objective.

This can happen through:

- direct instruction;
- retrieved content;
- tool output;
- poisoned memory.

The control problem is broader than filtering a phrase.

## Tool Misuse

A legitimate tool can be used in an unintended way.

Examples:

- destructive arguments;
- excessive scope;
- chained actions;
- sensitive retrieval.

Tool design should account for misuse, not only ordinary use.

## Identity and Privilege Abuse

A model or agent may act with credentials broader than the user's actual need.

Avoid shared superuser credentials.

Bind operations to a real identity or delegated service identity where possible.

## Supply Chain

AI systems can depend on:

- models;
- SDKs;
- MCP servers;
- tools;
- plugins;
- datasets;
- prompts;
- containers;
- packages.

Each can introduce malicious or vulnerable behaviour.

## Abuse Cases

Write explicit abuse stories.

Example:

> An attacker places instructions in a document that cause the agent to send sensitive data through an allowed tool.

Then design controls against the full chain.

## Consequence

Risk depends on:

```text
Likelihood x Impact
```

Impact should include:

- confidentiality;
- integrity;
- availability;
- financial loss;
- legal exposure;
- safety;
- reputation.

## Control Mapping

For each threat, map:

- prevention;
- detection;
- containment;
- recovery.

Do not depend on prevention alone.

## Exercise

Threat-model a generic agent that reads files and sends email.

Identify:

1. assets;
2. entry points;
3. trust boundaries;
4. five attack paths;
5. preventive controls;
6. detection;
7. recovery.

## Takeaway

> AI security begins by understanding what authority an attacker could manipulate through the model.

Next: **02 — Identity, Least Privilege and Capabilities**.
