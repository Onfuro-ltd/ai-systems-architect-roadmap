# 01 — Physical AI and Robotics Foundations

## Purpose

Understand the architecture that turns goals into controlled physical behaviour.

## Closed-loop system

```text
Goal → perceive → estimate state → plan → safety check → control → act → sense again
```

Unlike many digital agents, physical systems continuously interact with dynamics, uncertainty and time.

## Layers

Separate mission/task planning, semantic reasoning, perception/state estimation, motion planning, control, safety supervision and hardware interfaces.

Different layers operate at different frequencies and assurance levels.

## Dynamics

Robots have mass, inertia, friction, actuator limits, latency and mechanical tolerances. A valid semantic plan may still be physically infeasible.

## Degrees of freedom

Understand joints, coordinate frames, kinematics, workspace, end effectors and constraints at an architectural level.

## Autonomy levels

Autonomy is task-specific. A robot may autonomously navigate but require approval for grasping, entering a zone or interacting with people.

## APIs vs models

Use deterministic robotics libraries/controllers for geometry, control and safety constraints where appropriate. Models add perception, generalization and high-level reasoning.

## Exercise

Decompose a warehouse pick-and-place task into semantic planning, perception, motion, control and safety layers.

## Takeaway

> A robot is a layered feedback system, not an LLM attached to motors.

Next: **02 — Sensors, Perception and State Estimation**.
