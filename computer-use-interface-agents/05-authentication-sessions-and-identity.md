# 05 — Authentication, Sessions and Identity

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **05 — Authentication, Sessions and Identity** within Computer Use and Interface Agents;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Operate interfaces without weakening account security or confusing user identity.

## Session model

Bind automation sessions to an explicit user, organization/tenant, target system, authorization scope, environment and expiry.

## Credentials

Prefer secure credential stores, delegated authorization, short-lived tokens and provider-supported login mechanisms. Keep passwords, tokens and recovery secrets out of model-visible context where possible.

## MFA

Design for legitimate user participation in MFA when required. Do not build flows that bypass security controls.

## Session isolation

Separate users, tenants, environments and sensitive workflows. Cookies, local storage, downloads, clipboard and browser profiles can leak state across sessions if reused carelessly.

## Reauthentication

Consequential actions may require fresh authentication or step-up approval even if the browser session is already logged in.

## Account confirmation

Before consequential actions, verify the current account/tenant/workspace from trusted interface state.

## Session expiry

Agents must detect expired sessions and re-enter an authorized authentication path rather than improvising around it.

## Audit

Record which authorized identity/session executed each action without logging secrets.

## Exercise

Design session management for a multitenant browser-agent platform where users connect several third-party business accounts.

## Takeaway

> Authentication proves who may act; the agent must never turn a valid session into broader authority than the user granted.

Next: **06 — Permissions, Sandboxing and Consequential Actions**.
