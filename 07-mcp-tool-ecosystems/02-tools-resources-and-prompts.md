# 02 — Tools, Resources and Prompts

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **02 — Tools, Resources and Prompts** within MCP and Tool Ecosystems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

MCP servers expose three central primitives: tools, resources and prompts.

They are intentionally different because executable actions, contextual data and reusable interaction templates have different control models.

## Core Principle

> Choose the primitive that matches the capability instead of forcing every integration into a tool call.

## Tools

Tools expose executable functions.

Examples include:

- querying a service;
- creating a record;
- modifying a file;
- running a calculation;
- triggering an external operation.

Tools are model-oriented capabilities: the model may decide that a tool is useful, subject to the host's policies and user controls.

## Tool Discovery

A client can discover tools through the protocol's tool-list operation.

Tool definitions include metadata and schemas that describe expected inputs.

Tool lists can change over time and should not be assumed to be permanently static.

Availability can also depend on the authorization attached to a request.

## Tool Invocation

Tool invocation is a capability request.

The host should distinguish:

```text
Model proposes tool use
        |
        v
Harness validates request
        |
        v
Policy / approval check
        |
        v
MCP client invokes server
        |
        v
Result validation
        |
        v
Model or workflow continues
```

The protocol call itself should not bypass the harness.

## Tool Inputs

Tool input schemas should be explicit.

Good schemas improve:

- interoperability;
- validation;
- model tool selection;
- error reporting;
- testing.

Descriptions should explain semantics, not merely repeat field names.

## Tool Outputs

Tool results can contain structured and unstructured content.

Where downstream automation depends on the result, structured outputs are preferable to ambiguous prose.

Results may include different content types and may link or embed resources.

## Resources

Resources expose contextual data.

Examples include:

- files;
- documents;
- schemas;
- records;
- reference material;
- generated data representations.

Resources are application-controlled rather than autonomous actions.

The client decides when and how resource content enters model context.

## Resource Identity

Resources use URIs.

A resource URI identifies the resource from the protocol perspective.

A URI should not be treated as automatic proof of authority, freshness or safety.

The host can still apply:

- access policy;
- provenance rules;
- freshness requirements;
- context filtering.

## Prompts

Prompts expose reusable interaction templates.

They can provide structured starting points for recurring user-directed workflows.

Prompts are not equivalent to skills.

A prompt can be one component inside a larger skill, while a skill may also contain contracts, tool dependencies, context rules, validation and evaluation.

## Control Model

A useful mental model is:

| Primitive | Primary role | Typical control |
| --- | --- | --- |
| Tool | Execute capability | Model requests, host governs |
| Resource | Provide context | Application selects |
| Prompt | Reusable interaction template | User selects |

This is a conceptual control model, not a substitute for application policy.

## Annotations and Metadata

Protocol metadata can help clients understand content characteristics such as intended audience, priority or modification time.

Metadata is useful input to application decisions but should not automatically override policy or provenance checks.

## Dynamic Capability Sets

Servers may expose capability sets that change.

Clients should therefore avoid assumptions such as:

- every tool is always present;
- every authorized user sees the same capabilities;
- list ordering is arbitrary;
- discovery only needs to happen once forever.

Caching and list-change behaviour should follow the protocol version being implemented.

## Tool Design Rule

A tool should represent a coherent operation with a clear contract.

Avoid tools that:

- expose unrestricted shell access without a justified boundary;
- combine unrelated actions;
- accept opaque free-form instructions where structured parameters would work;
- hide consequential side effects;
- return ambiguous success states.

## Resource Design Rule

A resource should expose useful context without forcing the server to decide how the model must reason about it.

The host remains responsible for context engineering.

## Prompt Design Rule

Prompts should improve user-directed reuse without becoming hidden policy.

Consequential controls should be enforced by the host or application, not only described in prompt text.

## Exercise

For a generic project-management integration, classify the following as tool, resource or prompt:

- read project status;
- create task;
- retrieve project guidelines;
- run weekly review template;
- close milestone;
- inspect task history.

Explain each choice.

## Takeaway

> Tools act, resources inform, and prompts guide interaction.

Next: **03 — Clients, Servers and Transports**.
