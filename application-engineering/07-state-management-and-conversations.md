# State Management and Conversations

## Why state matters

A useful AI application rarely handles a single isolated request.

It needs to understand what has happened before, what is currently happening and what information is required to complete a task.

State turns individual model calls into reliable workflows.

## Types of state

### Conversation state

The immediate interaction history:

- previous messages;
- current topic;
- unresolved questions.

### User state

Information about the user:

- preferences;
- permissions;
- account information;
- historical interactions.

### Workflow state

The progress of a process:

- current step;
- completed actions;
- pending approvals;
- failures and retries.

### Business state

The authoritative system data:

- orders;
- inventory;
- financial records;
- customer records.

## Important principle

Do not confuse AI memory with system of record.

A model should not become the database.

```text
Business Database
       |
       v
Application State
       |
       v
AI Context
```

## Conversation design

Good conversation systems manage:

- history length;
- summaries;
- important facts;
- user intent;
- uncertainty.

Poor systems simply append every previous message forever.

## Workflow state machines

Complex tasks benefit from explicit states:

```text
Received
   |
Validated
   |
Analysing
   |
Waiting Approval
   |
Completed
```

This is more reliable than asking an agent to remember the entire process.

## Failure modes

### Lost state

The system forgets important information.

### Incorrect state

The AI believes something happened when it did not.

### State leakage

One user or tenant receives another user's information.

### Uncontrolled growth

History becomes expensive and irrelevant.

## Architecture guidance

Use deterministic storage for:

- permissions;
- financial data;
- orders;
- workflow status;
- compliance records.

Use AI memory/context for:

- interpretation;
- summarisation;
- assistance;
- retrieval of relevant knowledge.

## Practical exercise

Design an AI support workflow:

Track:

- customer identity;
- conversation summary;
- order lookup result;
- escalation state;
- approval state.

Separate authoritative data from AI-generated information.

## Mastery gate

You understand state management when you can:

- design different state types;
- prevent AI from becoming an unreliable database;
- create recoverable workflows;
- manage context growth and privacy.
