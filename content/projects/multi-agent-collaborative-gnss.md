---
title: "Multi-Agent Collaborative GNSS for Intelligent Transportation Systems"
description: "Vehicles share GNSS measurements through inter-vehicle ranging to improve urban positioning accuracy and integrity for ITS — the anchor RGC RIF program of the lab."
category: "research-program"
status: "completed"
flagship: true
start_date: 2022
end_date: 2025
funding: "RGC Research Impact Fund R5009-21 (HK$4.43M total project cost incl. matching, Project Coordinator, 2022–2025)"
themes: ["urban-gnss-reliability", "environment-aware-pnt", "optimization-estimation", "integrity-localization", "seamless-pnt-embodied"]
people: ["weisong-wen", "guohao-zhang", "hoi-fung-ng", "penggao-yan", "xiao-xia", "penghui-xu", "yihan-zhong", "qian-meng", "zhengdao-li"]
tags: ["RIF", "RGC", "multi-agent", "collaborative positioning", "ITS", "integrity", "factor graph"]
weight: 1
aliases:
  - /projects/integrity-fgo/
  - /projects/integrity-first-navigation/
  - /projects/integrity-constrained-factor-graph-optimization/
---

This program develops **reliable multi-agent collaborative GNSS positioning** for intelligent transportation systems — vehicles in an urban convoy share their raw GNSS measurements through inter-vehicle ranging, so that collectively they recover position fixes that individual vehicles couldn't trust on their own. The work spans the full stack: measurement-quality assessment in urban canyons, environment-aware NLOS handling, factor-graph optimization to fuse heterogeneous measurements, and integrity monitoring to bound the trust of the shared solution.

**Why it matters.** Single-vehicle GNSS in dense cities is unreliable. Multi-agent collaboration is a route to both accuracy and integrity at once — if peer vehicles can detect each other's faults, the swarm becomes more trustworthy than any single sensor.

**Funding & recognition.**
- **RGC Research Impact Fund R5009-21** — HK$4.43M total project cost (RGC contribution HK$3.1M + 30% institutional matching), Project Coordinator (the only RIF held as PC in Li-Ta's career to date), 2022–2025
- **2023 ION Per Enge Early Achievement Award** — second-ever Asian-university recipient, citing the foundational urban-GNSS-reliability + integrity work
- **2024 Most-Cited Paper in NAVIGATION** — *Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter* (Wen, Pfeifer, Bai, Hsu) — the FGO foundation that the multi-agent collaboration builds on
- **PolyU Presidential Award in Knowledge Transfer 2022–24** — recognizing the broader KT impact of the multi-agent collaborative GNSS research line and its industry translations
- **US12123961B2** patent (granted 2024) — *3D LiDAR Aided GNSS NLOS Detection and Correction*

**Outputs (representative).**
- [UrbanNav](/projects/urbannav/) — open multisensory benchmark dataset for multi-agent positioning research
- *Integrity-Constrained Factor Graph Optimization for GNSS* (Xia, Wen, Hsu, NAVIGATION 2024)
- *Principal Gaussian Overbound for Heavy-tailed Pseudorange Error Bounding* (Yan, Zhong, Hsu, IEEE TAES 2024)
- *3D Mapping Database Aided GNSS-based Collaborative Positioning via FGO* (Zhang, Ng, Hsu, IEEE TITS 2020)
- *GNSS RUMS — Realistic Urban Multi-Agent Simulator for Collaborative Positioning Research* (Zhang et al., Remote Sensing 2021)
- *Multiple Faults Isolation for Multi-Constellation GNSS Positioning* (Yan et al., IEEE Sensors J 2025)
