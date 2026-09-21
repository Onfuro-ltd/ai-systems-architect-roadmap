# 03 — Localization, Mapping and World Models

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **03 — Localization, Mapping and World Models** within Physical AI and Robotics;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Maintain a spatial and semantic representation of where the robot is and what surrounds it.

## Coordinate frames

Robotics relies on explicit frames: world/map, robot/base, sensor, joint and tool/end-effector frames.

Transform errors can become dangerous physical errors.

## Localization

Estimate robot pose using appropriate combinations of odometry, inertial sensing, visual features, lidar, landmarks or satellite positioning.

## Mapping

Maps may represent occupancy, geometry, traversability, semantics, objects, zones and dynamic obstacles.

## SLAM

Simultaneous localization and mapping estimates pose while constructing/updating a map when a trusted map is unavailable.

## World models

An embodied AI system may maintain semantic state beyond geometry: object identities, locations, affordances, task state, people, restricted zones and uncertainty.

## Dynamic worlds

Do not assume a map is current. People and objects move; doors close; shelves change. Reconcile stored world state with fresh perception.

## Provenance

Track which observations or authoritative systems produced important world-state facts.

## Exercise

Design a world-state representation for a robot moving inventory between rooms while people and movable obstacles change the environment.

## Takeaway

> A world model is useful only while the system remembers which parts are measured, inferred, stale or uncertain.

Next: **04 — Planning, Control and Actuation**.
