---
title: "Optimization and AI for Positioning"
description: "Factor graph optimization, machine learning, deep learning, and LLMs applied to GNSS and multi-sensor positioning — from supervised NLOS classifiers to self-supervised weighting and LLM-based data standardization."
category: "research-program"
status: "active"
flagship: true
start_date: 2017
themes: ["urban-gnss-reliability", "environment-aware-pnt", "optimization-estimation", "integrity-localization", "seamless-pnt-embodied"]
people: ["penghui-xu", "penggao-yan", "max-lee", "hongmin-zhang", "yihan-zhong", "zhengdao-li", "meiling-su"]
tags: ["factor graph optimization", "machine learning", "deep learning", "LLM", "AI for GNSS", "Android Location"]
weight: 5
aliases:
  - /projects/ai-for-positioning/
---

This program applies probabilistic graphical models, machine learning, and deep learning to GNSS and multi-sensor positioning. **Factor Graph Optimization (FGO)** is the mathematical backbone — a unifying framework for fusing heterogeneous measurements with rigorous uncertainty modelling — and the arc extends into ML methods that complement (rather than bypass) the optimization layer.

The thread began with supervised classifiers for GNSS multipath/NLOS detection (2017 ITSC; 2018 ANFIS in *Journal of Navigation*; 2020 Gradient Boosting Decision Tree in *Applied Soft Computing*) and evolved into deep-learning approaches (LSTM-based GNSS uncertainty prediction; CNN-based environment retrieval in IEEE TIV) and **probabilistic graphical models** — Factor Graph Optimization — which has become a foundational framework for the field. Most recently the thread reaches into **LLM-based data standardization** for positioning workflows (Lee, Lin, Hsu, IPIN 2024).

**Why it matters.** GNSS positioning is a noisy, partially observable, context-dependent inference problem — exactly the kind of problem where optimization-based estimators and modern ML methods extract leverage that hand-crafted models miss. But ML in safety-critical positioning must work *with* the integrity layer, not bypass it. This is the thread that cross-cuts every other pillar.

**Industry engagement — Google Android Location.** The program's optimization/ML methods sit close to industry-grade smartphone positioning. Prof. Hsu served as **Visiting Research Scientist at Google (Mountain View, USA)**, on the Android Location team for 20 months (2022–2023), working on FGO-based smartphone positioning. The collaboration continued with a **Pixel team talk in August 2024** and ongoing exchange between IPNL research and the Android Location group on factor-graph approaches to smartphone GNSS.

**Recognition.**
- **2024 Most-Cited Paper in NAVIGATION: Journal of the Institute of Navigation** — *Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter* (Wen, Pfeifer, Bai, Hsu)
- **TechConnect 2021 Innovation Award** — *3D LiDAR Aided GNSS for L4 AV*
- **US12123961B2** patent — *3D LiDAR Aided GNSS NLOS Detection and Correction* (Hsu, Wen, granted 2024)
- **IEEE Aerospace and Electronic Systems Magazine** review article *AI for GNSS* (Xu, Hsu et al., 2024)
- *Inside GNSS* feature article *What are the roles of artificial intelligence and machine learning in GNSS positioning?* (Hsu, 2020)

**Representative publications.** *AutoW: Self-Supervision Learning for Weighting Estimation in GNSS Positioning* (Xu, Hsu, ION GNSS+ 2024); *Principal Gaussian Overbound for Heavy-tailed Error Bounding* (Yan, Zhong, Hsu, IEEE TAES 2024); *ML-based LOS/NLOS Classifier for GNSS Shadow Matching* (Xu et al., *Satellite Navigation* 1(1), 2020).

**Open artifacts.** The FGO foundation for many of these ML methods is implemented in the open-source [GraphGNSSLib](/resources/) library, with companion code released alongside several of the cited papers — see the [Resources page](/resources/) for details.
