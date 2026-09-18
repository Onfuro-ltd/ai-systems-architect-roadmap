# 06 — User Control, Correction and Recovery

## Purpose

Make AI behaviour steerable without forcing users to restart whenever the system is wrong.

## Control

Support edit, regenerate, constrain, pause, cancel, undo, retry, take over and escalate where the workflow permits.

## Correction

When a user corrects one field, preserve valid work elsewhere. Avoid regenerating an entire artifact unless necessary.

## State visibility

For agentic tasks show queued, running, awaiting approval, completed, failed, cancelled and unknown states.

## Undo

Undo must correspond to real system reversibility. Do not display an undo affordance if an external action cannot actually be reversed.

## Recovery

After failure, preserve context and completed steps and explain the next safe option.

## Preferences

Distinguish durable user preferences from one-task instructions. Let users inspect or change important persistent settings where appropriate.

## Exercise

Design correction and recovery UX for a multi-step AI workflow that fails after completing three of five operations.

## Takeaway

> A controllable AI product lets the user correct the trajectory, not merely complain about the final answer.

Next: **07 — Failure UX and Graceful Degradation**.
