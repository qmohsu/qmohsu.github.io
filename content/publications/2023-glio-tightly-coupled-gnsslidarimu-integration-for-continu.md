---
title: "GLIO: Tightly-coupled gnss/lidar/imu integration for continuous and drift-free state estimation of intelligent vehicles in urban areas"
slug: "2023-glio-tightly-coupled-gnsslidarimu-integration-for-continu"
authors:
  - "Liu, X."
  - "Wen, W."
  - "Hsu, L. T."
year: 2023
venue: "IEEE Transactions on Intelligent Vehicles"
type: "journal"
cv_number: 42
featured: true
quartile: "Q1"
doi: "10.1109/tiv.2023.3323648"
pdf: ""
code: ""
data: ""
summary: "GLIO tightly couples GNSS, LiDAR, and IMU in a single factor graph for continuous drift-free state estimation in urban areas."
hero_image: "/images/pubs/2023-glio-urban-trajectory-hero.png"
hero_alt: "3D trajectory comparison for GLIO and other GNSS, LiDAR, and IMU integration methods."
hero_caption: "Figure 4 visual detail: 3D trajectory comparison across GNSS, LiDAR, and IMU integration methods."
figures:
  - src: "/images/pubs/2023-glio-fig2-lidar-association.png"
    alt: "Scan-to-map and scan-to-multiscan LiDAR association schemes."
    context: "After the system pipeline, this figure explains the LiDAR constraint design that supports smoother and more globally consistent optimization."
    caption: "Figure 2: LiDAR factor association through scan-to-map and scan-to-multiscan schemes."
  - src: "/images/pubs/2023-glio-fig3-factor-graph.png"
    alt: "Two-stage factor graph structure with GNSS, INS, Doppler, scan-to-map, and scan-to-multiscan factors."
    context: "The factor graph shows how GNSS, Doppler, IMU, and LiDAR constraints are organized across the first and second optimization stages."
    caption: "Figure 3: factor graph structure for first-stage fusion and second-stage optimization."
  - src: "/images/pubs/2023-glio-fig4-tst-trajectory.png"
    alt: "3D trajectory comparison in the Tsim Sha Tsui sequence."
    context: "The results begin with the Tsim Sha Tsui sequence, comparing trajectory consistency between GLIO variants and baseline methods."
    caption: "Figure 4: Tsim Sha Tsui trajectory comparison across RTKLIB, LIO, LIO-GNSS, GLIO-SS, and GLIO-DS."
  - src: "/images/pubs/2023-glio-fig5-6-tst-errors.png"
    alt: "Tsim Sha Tsui positioning error plots comparing GLIO variants and baselines."
    context: "These error plots quantify the same sequence and show where loosely coupled systems degrade while tighter fusion improves."
    caption: "Figures 5 and 6: Tsim Sha Tsui positioning errors and scan-to-multiscan frame comparison."
  - src: "/images/pubs/2023-glio-fig7-8-whampoa-results.png"
    alt: "Whampoa table, trajectory, and positioning error plots for GLIO and baseline methods."
    context: "The Whampoa case extends the evaluation to longer dense-urban driving with tunnels, traffic, and severe GNSS/LiDAR challenges."
    caption: "Figures 7 and 8: Whampoa trajectory and error results under dense urban driving."
themes:
  - "urban-gnss-reliability"
  - "optimization-estimation"
  - "seamless-pnt-embodied"
tags: []
---

**Key idea.** **GLIO** tightly couples GNSS, LiDAR, and IMU in a single factor graph, so absolute GNSS positioning and drift-free LiDAR-inertial odometry constrain each other — global accuracy without the long-run drift of LiDAR-only systems.

**Impact.** Delivers continuous, drift-free state estimation for intelligent vehicles across urban areas, and is a flagship example of the lab's multi-sensor fusion stack for real platforms.
