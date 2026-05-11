---
title: "GraphGNSSLib"
description: "Open-source factor-graph platform for GNSS positioning, RTK, and GNSS/INS research."
category: "open-platform"
status: "active"
flagship: true
start_date: 2020
repo: "https://github.com/weisongwen/GraphGNSSLib"
themes: ["optimization-estimation", "urban-gnss-reliability", "integrity-localization", "seamless-pnt-embodied"]
tags: ["factor graph", "GNSS", "optimization", "C++", "ROS", "open-source"]
weight: 3
---

GraphGNSSLib is an open-source C/C++ platform for GNSS positioning, RTK, and GNSS/INS research using factor graph optimization. It connects raw GNSS data — pseudorange, Doppler, carrier phase, ambiguity resolution — to nonlinear optimization and to ROS-based robotic systems.

**Why it matters.** GraphGNSSLib gives navigation and robotics researchers a practical bridge from GNSS measurements to modern optimization-based estimation, replacing classical EKF pipelines with a unified framework that can fuse heterogeneous measurements, handle outliers more flexibly, and reason over time.

**Outputs:** [GitHub repository](https://github.com/weisongwen/GraphGNSSLib), code examples, ROS demos, integration with [UrbanNav](/projects/urbannav/), and the foundational *Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter* (Wen, Pfeifer, Bai, Hsu) paper that was named **2024 Most-Cited Paper in NAVIGATION**.
