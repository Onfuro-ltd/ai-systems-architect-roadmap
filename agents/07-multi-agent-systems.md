# 07 — Multi-Agent Systems

## Purpose

Multi-agent systems coordinate multiple specialised AI capabilities. This chapter focuses on engineering reality rather than the hype of simply creating many agents.

## Core Principle

More agents do not automatically create more intelligence. Multiple agents add value only when specialisation, coordination, and control improve the outcome.

## When Multi-Agent Systems Make Sense

Useful when:

- tasks require different expertise;
- independent analysis is valuable;
- responsibilities need separation;
- parallel work improves speed;
- different permissions are required.

Avoid multi-agent designs when a normal workflow or single agent is sufficient.

## Common Architectures

### Specialist Agents

```text
              Coordinator
                   |
    +--------------+--------------+
    |              |              |
Research      Analysis       Action
Agent         Agent          Agent
```

Each agent has a clear responsibility.

### Debate / Review Pattern

One agent creates a result and another evaluates it.

Useful for:

- quality checks;
- security reviews;
- verification.

### Hierarchical Systems

Strategic agents delegate to operational agents.

## Coordination Challenges

Multi-agent systems introduce:

- communication overhead;
- duplicated work;
- conflicting objectives;
- higher cost;
- harder debugging;
- unclear responsibility.

## Shared Memory

Agents should not blindly share all information.

A mature system requires:

- controlled access;
- ownership of information;
- audit trails;
- clear memory boundaries.

## Enterprise Pattern

```text
Business Goal
      |
Coordinator
      |
Specialised Agents
      |
Validation Layer
      |
Human Approval
      |
Business Action
```

## SEMLIS Connection

A future commerce intelligence platform could use specialised agents for:

- marketplace analysis;
- pricing intelligence;
- advertising analysis;
- customer insight;
- inventory planning.

However, recommendations should pass through business rules, validation, and approval before actions are taken.

## Key Lesson

The goal is not maximum autonomy. The goal is reliable business outcomes through controlled intelligence.
