---
title: "Integrity, Fault Detection, and Safety-Quantifiable Localization"
slug: "integrity-localization"
description: "Navigation systems that estimate both state and trust — fault detection, non-Gaussian overbounding, protection-level computation, and integrity-constrained optimization for safety-critical autonomy."
keywords:
  - "navigation integrity"
  - "fault detection"
  - "protection level"
  - "overbounding"
  - "non-Gaussian errors"
  - "integrity-constrained FGO"
  - "safety-critical localization"
  - "spoofing detection"
weight: 5
lead: "penggao-yan"
---

Accuracy is not enough for safety-critical navigation: a confident answer in the wrong place is more dangerous than an honest *"I don't know."* This pillar builds systems that estimate not only **where** they are, but **whether that answer can be trusted** — outputting a state estimate and a quantified protection level together.

<img src="/images/research/blueprint-integrity-localization.svg" alt="Conventional estimators output only a position with no measure of trust, dangerous for safety-critical autonomy; IPNL estimates state and trust together — fault detection, non-Gaussian overbounding and protection levels — and outputs a safety decision." style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

We develop fault detection, non-Gaussian error bounding, protection-level computation, and integrity-constrained optimization. Representative threads: *Principal Gaussian Overbound for Heavy-tailed Error Bounding* (Yan, Zhong, Hsu, IEEE TAES 2024), *Integrity-Constrained Factor Graph Optimization* (Xia, Wen, Hsu, NAVIGATION 2024), and *Fault Detection for Gaussian Mixture Noises in Lidar/IMU Integrated Localization* (Yan et al., NAVIGATION 2025).

This pillar is the technical core of the **2023 ION Per Enge Early Achievement Award** and the **RGC Research Impact Fund R5009-21** (HK$4.5M, PI, 2021–2026).
