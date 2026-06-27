---
title: "Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter"
slug: "2021-factor-graph-optimization-for-gnssins-integration-a-compar"
authors:
  - "Wen W."
  - "Pfeifer T."
  - "Bai X."
  - "Hsu L. T."
year: 2021
venue: "NAVIGATION: Journal of the Institute of Navigation"
type: "journal"
cv_number: 80
featured: true
quartile: "Q1"
doi: "10.1002/navi.421"
pdf: ""
code: ""
data: ""
summary: "Factor graph optimization recasts GNSS/INS integration as a sliding-window estimation problem rather than a one-epoch filtering problem."
project: "graphgnsslib"
resources:
  - "graphgnsslib-software"
repo: "https://github.com/weisongwen/GraphGNSSLib"
video: "https://www.youtube.com/watch?v=f5bIh96SRsk"
themes:
  - "urban-gnss-reliability"
  - "optimization-estimation"
tags: []
---

**Key idea.** Classical GNSS/INS integration uses an Extended Kalman Filter, which condenses all history into a single current state. This paper recasts the problem as **factor graph optimization (FGO)** — jointly optimizing a sliding window of states with re-linearization, so the estimator can revisit past epochs and handle outliers far more flexibly.

**Impact.** It became the reference comparison establishing *why* FGO outperforms filtering for navigation, and was named the **2024 Most-Cited Paper in *NAVIGATION***. The result reframed how the field approaches GNSS/INS fusion and underpins much of IPNL's later integrity and multi-sensor work.
