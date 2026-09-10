# Function Calling and Tool Use

## Why tools change AI applications

A language model alone can reason and generate text, but it does not have direct access to current systems or the ability to safely perform business actions.

Tools connect intelligence to capability.

## Basic architecture

```text
User Intent
     |
     v
   Model
     |
 decides whether a tool is needed
     |
     v
 Tool Call
     |
     v
 External System
     |
     v
 Tool Result
     |
     v
 Model continues
```

## What a tool provides

A well-designed tool has:

- clear purpose;
- defined inputs;
- defined outputs;
- predictable errors;
- permission boundaries;
- auditability.

## Tool design principles

### Narrow capabilities

A tool should do one clear job.

Bad:

`manage_business()`

Better:

`get_inventory_level()`

`calculate_profit_margin()`

`create_customer_ticket()`

### Validate inputs

Never trust generated parameters without validation.

### Return useful information

Tool responses should be designed for the model and application, not only humans.

## Tool use vs agents

Tool calling is a capability.

An agent is a larger system that may:

- choose goals;
- plan steps;
- use multiple tools;
- evaluate results;
- recover from failure.

A tool-enabled application does not automatically require agents.

## Failure modes

### Wrong tool selection

The model chooses an inappropriate action.

### Incorrect parameters

The model calls a valid tool with bad inputs.

### Excessive permissions

The tool can perform more than the task requires.

### Hidden side effects

The model cannot understand consequences of an action.

## Safety pattern

```text
Model recommendation
        |
        v
Permission check
        |
        v
Validation
        |
        v
Action
        |
        v
Audit record
```

## Practical exercise

Build a read-only business assistant with tools:

- lookup product;
- retrieve inventory;
- calculate profitability.

Do not allow write actions initially.

Measure:

- correct tool selection;
- incorrect calls;
- missing information;
- latency.

## Mastery gate

You understand tool use when you can:

- design safe tools;
- distinguish tools from agents;
- define permission boundaries;
- explain when direct API integration is better than AI tool use.
