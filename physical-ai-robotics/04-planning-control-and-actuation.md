# 04 — Planning, Control and Actuation

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **04 — Planning, Control and Actuation** within Physical AI and Robotics;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Translate goals into physically feasible trajectories and stable actuator commands.

## Planning hierarchy

```text
Task goal
 ↓
Task plan
 ↓
Motion/path plan
 ↓
Trajectory
 ↓
Controller
 ↓
Actuators
```

High-level reasoning should not directly emit raw motor commands for safety-critical systems.

## Path and motion planning

Plans must respect obstacles, kinematics, dynamics, joint limits, workspace constraints and task-specific rules.

## Control

Controllers execute trajectories while correcting deviations using feedback. Control loops often require deterministic timing far faster than language-model reasoning.

## Actuators

Motors, grippers, hydraulics and other actuators have force, speed, thermal and mechanical limits.

## Preconditions

Verify object pose, free space, tool state, human clearance and other physical preconditions before executing motion.

## Replanning

If the world changes or tracking error exceeds tolerance, stop or replan rather than blindly completing the old trajectory.

## Safe state

Define what happens on uncertainty, communication loss, sensor failure or controller fault.

## Exercise

Design the execution state machine for grasping and moving a fragile object with explicit preconditions and abort conditions.

## Takeaway

> Semantic intelligence decides what should happen; motion planning and control determine how it can happen within physical constraints.

Next: **05 — Vision-Language-Action and Embodied Models**.
