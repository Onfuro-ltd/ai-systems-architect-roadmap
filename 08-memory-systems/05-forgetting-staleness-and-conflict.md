# 05 — Forgetting, Staleness and Conflict

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **05 — Forgetting, Staleness and Conflict** within Memory Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

A system that remembers but cannot forget eventually accumulates stale, conflicting and privacy-sensitive information.

Forgetting is a core memory operation.

## Core Principle

> Memory systems need deletion, expiry and supersession as first-class capabilities.

## Why Forgetting Matters

Information can become invalid because:

- the user changed their mind;
- the world changed;
- a workflow completed;
- a preference expired;
- a policy changed;
- retention is no longer justified;
- a deletion request was made.

## Expiry

Some memories should have explicit expiry.

Examples:

- temporary travel preference;
- short-lived project role;
- promotional preference;
- session-derived intent.

Expiry can be absolute or based on last confirmation.

## Time-to-Live

TTL is useful when a memory type has predictable validity.

Examples:

- cached status;
- temporary operating constraint;
- transient recommendation preference.

TTL should not be used blindly for records that require deliberate retention.

## Supersession

A newer memory can supersede an older memory.

Keep enough history to explain change where needed, but prevent the old value from being retrieved as current truth.

```text
Old Preference
    |
superseded by
    |
New Preference
```

## Contradiction

Two memories can disagree.

The system should not always choose the newest automatically.

Consider:

- source authority;
- timestamp;
- explicitness;
- confidence;
- scope;
- user confirmation.

## Tombstones

A deleted or superseded memory may leave a tombstone or audit marker.

This can prevent re-creation from stale upstream data.

Tombstones must themselves follow retention and privacy policy.

## Forgetting Policies

Possible policies include:

- explicit delete;
- expiry;
- inactivity decay;
- relevance decay;
- supersession;
- legal retention limit;
- user-controlled removal.

## Confidence Decay

Some inferred memories can lose confidence over time.

Confidence decay is useful when old behaviour should not remain permanently predictive.

## Reconfirmation

A memory can require reconfirmation before use.

Example:

> "This preference was last confirmed two years ago."

The system may ask before applying it to a consequential task.

## Conflict Graph

For important domains, represent relationships such as:

- supports;
- contradicts;
- supersedes;
- derived from.

This can improve explainability.

## Deletion Propagation

Deleting memory can require removal from:

- primary store;
- search index;
- vector index;
- cache;
- derived summaries;
- downstream replicas.

A deletion architecture should know where copies exist.

## Backups

Backup retention can complicate deletion.

Systems should define how deletion requests interact with backup restoration and retention policies.

## Anti-Pattern: Never Delete

Permanent retention increases:

- privacy risk;
- retrieval noise;
- stale behaviour;
- storage cost;
- governance complexity.

## Exercise

Design lifecycle rules for:

1. explicit user preference;
2. inferred preference;
3. past decision;
4. temporary workflow constraint;
5. sensitive personal detail.

For each, define expiry, supersession, deletion and reconfirmation behaviour.

## Takeaway

> Forgetting is not memory failure. It is memory hygiene.

Next: **06 — Memory Architecture and Storage Patterns**.
