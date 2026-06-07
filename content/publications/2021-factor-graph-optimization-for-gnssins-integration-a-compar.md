---
title: "Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter"
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
themes:
  - "urban-gnss-reliability"
  - "optimization-estimation"
tags: []
---

<img src="/images/pubs/fgo-vs-ekf.svg" alt="The EKF estimates only the current epoch; factor graph optimization jointly optimizes a window of past states with re-linearization, giving more accurate and robust GNSS/INS integration." style="max-width:620px;width:100%;height:auto;display:block;margin:1.25rem auto;" />

**Key idea.** Classical GNSS/INS integration uses an Extended Kalman Filter, which condenses all history into a single current state. This paper recasts the problem as **factor graph optimization (FGO)** — jointly optimizing a sliding window of states with re-linearization, so the estimator can revisit past epochs and handle outliers far more flexibly.

**Impact.** It became the reference comparison establishing *why* FGO outperforms filtering for navigation, and was named the **2024 Most-Cited Paper in *NAVIGATION***. The result reframed how the field approaches GNSS/INS fusion and underpins much of IPNL's later integrity and multi-sensor work.
