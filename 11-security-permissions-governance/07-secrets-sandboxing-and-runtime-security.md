# 07 — Secrets, Sandboxing and Runtime Security

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **07 — Secrets, Sandboxing and Runtime Security** within Security, Permissions and Governance;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Models and agents often run code, access tools and interact with credentials.

Runtime controls contain the damage if reasoning or external input becomes malicious or incorrect.

## Core Principle

> Keep secrets out of model-visible context and contain execution inside the smallest practical sandbox.

## Secret Management

Store secrets in dedicated secret systems or protected runtime configuration.

Avoid:

- prompts;
- source code;
- logs;
- memory;
- model-visible files.

## Credential Injection

Inject credentials only at the component that needs them.

Example:

```text
Model
  |
Tool request
  |
Tool service
  |
Credential broker
  |
External API
```

The model never needs to see the raw credential.

## Short-Lived Credentials

Prefer temporary credentials where possible.

Benefits:

- reduced replay window;
- easier revocation;
- narrower audit scope.

## Environment Variables

Environment variables are convenient but can leak through:

- process dumps;
- debug logs;
- subprocess inheritance;
- tool output.

Treat them as secrets, not harmless configuration.

## Sandboxing

A sandbox limits:

- filesystem;
- network;
- processes;
- CPU;
- memory;
- time;
- devices.

The stronger the code-execution capability, the stronger the sandbox should be.

## Filesystem Isolation

Use:

- dedicated working directory;
- read-only mounts;
- explicit writable paths;
- no host filesystem access by default.

## Network Isolation

Control outbound destinations.

A code interpreter should not automatically have unrestricted internet access.

Network policy reduces exfiltration risk.

## Process Isolation

Prevent:

- privilege escalation;
- host process access;
- arbitrary daemon creation.

Containers can help but are not automatically secure sandboxes.

## Code Execution

Treat generated code as untrusted.

Apply:

- sandbox;
- resource limits;
- dependency controls;
- output validation.

## Package Installation

Dynamic package installation introduces supply-chain risk.

Prefer:

- approved dependencies;
- pinned versions;
- isolated environments.

## Browser and Computer Use

Computer-use agents can interact with arbitrary untrusted interfaces.

Controls may include:

- domain allowlists;
- transaction limits;
- approval;
- isolated browser profile;
- no saved credentials.

## Runtime Limits

Enforce:

- CPU;
- memory;
- execution time;
- file size;
- network volume;
- subprocess count.

## Egress Monitoring

Monitor unusual outbound traffic from agents or tool runtimes.

Exfiltration can happen through legitimate network capability.

## Exercise

Design a sandbox for an agent that can execute Python on uploaded files.

Define:

1. filesystem;
2. network;
3. secrets;
4. packages;
5. CPU/memory;
6. output handling.

## Takeaway

> Runtime isolation assumes the model may eventually make a dangerous choice and limits what that choice can affect.

Next: **08 — Audit, Incident Response and Governance**.
