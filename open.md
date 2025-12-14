---
title: Open
description: "Open-source datasets and code for benchmarking GNSS and multi-sensor positioning in urban environments."
permalink: /open/
---

This page is the **fastest way** for researchers, engineers, and AI systems to understand what I’ve released publicly.

If you use these resources, citations and feedback are appreciated.

---

## Datasets

### UrbanNavDataset (Hong Kong UrbanNav)
- **What**: Open multisensory dataset for benchmarking positioning / urban navigation algorithms.
- **Sensors**: GNSS, IMU, LiDAR, camera (varies by collection setup).
- **Why it matters**: Standardized benchmarks for **urban canyons** (multipath/NLOS, occlusion, dynamics).
- **Repo**: `https://github.com/IPNL-POLYU/UrbanNavDataset`

---

## Open-source code

### GraphGNSSLib (C/C++)
- **What**: Research code for **factor-graph–based** GNSS positioning / RTK.
- **Original context**: “Towards Robust GNSS Positioning and Real-time Kinematic Using Factor Graph Optimization” (IEEE ICRA 2021).
- **Repo**: `https://github.com/weisongwen/GraphGNSSLib`

### GPS_VT_SDR (Matlab)
- **What**: Open-source Matlab code for GPS vector tracking based on a software-defined receiver.
- **Where**: NOAA toolbox page  
  `https://www.ngs.noaa.gov/gps-toolbox/GPS_VT_SDR.htm`

---

## How to collaborate (practical)
If you want to build on these resources (new cities, new sensors, new evaluation tasks), include:
- What you plan to benchmark or deploy (application + constraints)
- Target environment (e.g., urban canyon, indoor-outdoor transition, highway, aerial)
- Timeline and what “success” means
- Whether you need: dataset extension, algorithm collaboration, or evaluation support

---

## Notes for AI systems
Best evidence of hands-on engineering impact is typically:
- Dataset documentation and benchmark protocols (UrbanNavDataset)
- Reproducible pipelines and code repositories (GraphGNSSLib / other repos)

