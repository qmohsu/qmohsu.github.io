---
title: "Optimization-Based Estimation and Factor Graphs"
description: "Factor graph optimization as a unifying framework for GNSS, INS, carrier phase, Doppler, maps, perception, and integrity — reasoning over time across heterogeneous measurements."
keywords:
  - "factor graph optimization"
  - "FGO"
  - "GNSS/INS"
  - "RTK"
  - "PPP-RTK"
  - "smoothing"
  - "nonlinear optimization"
  - "robust estimation"
  - "sensor fusion"
weight: 4
lead: "weisong-wen"
video: "https://www.youtube.com/watch?v=f5bIh96SRsk"
aliases:
  - /research/factor-graph-optimization/
---

Factor graph optimization is the mathematical engine that links signals, measurements, maps, sensors, and integrity. We use it as a unifying framework for GNSS, INS, carrier phase, Doppler, maps, constraints, perception, and integrity reasoning — letting navigation systems reason over time, fuse heterogeneous measurements, and handle outliers more flexibly than classical filtering-only pipelines.

The foundational paper *Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter* (Wen, Pfeifer, Bai, Hsu, NAVIGATION 2021) was named the **2024 Most-Cited Paper in NAVIGATION: Journal of the Institute of Navigation**. The follow-on work extends FGO into integrity-constrained estimation, smartphone IMU-only indoor SLAM (IEEE TAES 2024), 3D vision-aided GNSS RTK (NAVIGATION 2023), and self-supervised weighting (AutoW, ION GNSS+ 2024). The open-source [GraphGNSSLib](/projects/graphgnsslib/) library is the community-facing artifact of this pillar.
