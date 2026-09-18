# 02 — Sensors, Perception and State Estimation

## Purpose

Convert noisy physical measurements into an estimate of the world a robot can safely use.

## Sensors

Robotic systems may use cameras, depth cameras, lidar, radar, IMUs, encoders, force/torque, tactile, proximity, microphones, GPS/GNSS and other domain sensors.

Each has range, resolution, latency, failure and environmental limitations.

## Perception

Tasks include detection, segmentation, pose estimation, tracking, depth, free-space detection, object state and human presence.

## State estimation

Fuse measurements over time rather than treating one sensor reading as truth.

```text
Sensor observations + prior state + motion model → estimated state + uncertainty
```

## Calibration

Camera intrinsics/extrinsics, sensor-to-robot transforms, timing and actuator calibration materially affect downstream accuracy.

## Time synchronization

Misaligned timestamps can create a physically incorrect fused state even when each sensor is individually accurate.

## Redundancy

For safety-relevant perception, consider diverse sensors and independent safety mechanisms rather than trusting one learned detector.

## Degradation

Rain, dust, glare, darkness, occlusion, vibration and sensor contamination can change perception quality. Detect degraded operating conditions.

## Exercise

Design perception for a mobile robot operating around people in variable lighting and explain which failures cannot be solved by a vision model alone.

## Takeaway

> Physical perception is an uncertain measurement process; state estimation must preserve that uncertainty rather than converting every detection into a fact.

Next: **03 — Localization, Mapping and World Models**.
