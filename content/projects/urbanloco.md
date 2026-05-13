---
title: "UrbanLoco"
description: "Full sensor-suite benchmark dataset for mapping and localization in highly urbanized scenes (San Francisco + Hong Kong)."
category: "open-platform"
status: "maintained"
flagship: false
start_date: 2020
repo: "https://github.com/weisongwen/UrbanLoco"
themes: ["urban-gnss-reliability", "environment-aware-pnt", "seamless-pnt-embodied"]
people: ["weisong-wen", "guohao-zhang", "xiwei-bai"]
tags: ["dataset", "benchmark", "LiDAR", "camera", "autonomous-vehicles"]
weight: 2
---

UrbanLoco is a multi-sensor dataset for benchmarking mapping and localization algorithms in highly urbanized environments. It contains 13 trajectories totaling over 40 km across San Francisco and Hong Kong — urban canyons, bridges, tunnels, and sharp turns — with synchronized LiDAR, cameras (360° in San Francisco; fish-eye sky-camera in Hong Kong), IMU, and GNSS measurements, with ground truth from a NovAtel SPAN CPT 7 + RTK system.

**Why it matters.** Existing public AV datasets either offered limited sensor coverage or avoided the most challenging urban scenarios. UrbanLoco captures real-world conditions where GNSS signals are severely degraded by multipath and where LiDAR/camera-based methods struggle with dynamic objects — providing a realistic stress test for autonomous-vehicle navigation algorithms.

**Outputs:** open dataset under CC BY-NC-SA 4.0; [GitHub repository](https://github.com/weisongwen/UrbanLoco); accompanying [ICRA 2020 paper](/news/urbanloco-dataset-released/) by Wen, Zhou, Zhang, Fahandezh-Saadi, Bai, Zhan, Tomizuka, and Hsu. Released in collaboration with the **Mechanical Systems Control Lab at UC Berkeley**.
