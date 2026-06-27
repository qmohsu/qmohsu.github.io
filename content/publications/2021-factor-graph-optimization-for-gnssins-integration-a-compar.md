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
hero_image: "/images/pubs/2021-fgo-fig2-factor-graph.png"
hero_alt: "Factor graph structure for loosely coupled and tightly coupled GNSS/INS integration."
hero_caption: "Figure 2 from the paper: the implemented factor graph structure for loosely coupled and tightly coupled GNSS/INS integration."
highlights:
  - "Compares EKF and FGO for both loosely coupled and tightly coupled GNSS/INS integration."
  - "Uses an urban-canyon experiment in Hong Kong with low-cost GNSS, INS, fisheye imagery, and ground-truth reference equipment."
  - "Shows that sliding-window FGO can revisit historical states and reduce the impact of outliers and non-Gaussian GNSS errors."
figures:
  - src: "/images/pubs/2021-fgo-fig1-flowchart.png"
    alt: "Flowchart of loosely coupled and tightly coupled GNSS/INS integrations implemented using EKF."
    context: "Before the factor graph model, the paper first establishes the EKF loosely coupled and tightly coupled baselines that the new formulation is compared against."
    caption: "Figure 1 from the paper: loosely coupled and tightly coupled GNSS/INS integration flowcharts implemented using EKF."
  - src: "/images/pubs/2021-fgo-fig3-experiment-setup.png"
    alt: "Experimental vehicle sensor setup and Hong Kong urban canyon test scene."
    context: "After defining the estimation structure, the paper moves to the Hong Kong vehicle setup and urban canyon route used for the EKF-versus-FGO comparison."
    caption: "Figure 3 from the paper: experimental vehicle sensor setup and Hong Kong urban-canyon test scene."
  - src: "/images/pubs/2021-fgo-fig5-tc-results.png"
    alt: "Tightly coupled GNSS/INS trajectory and two-dimensional error results comparing EKF and FGO."
    context: "The first main result turns the method into trajectory evidence by comparing tightly coupled EKF and FGO against the reference path."
    caption: "Figure 5 from the paper: tightly coupled GNSS/INS trajectory and 2D positioning error comparison between EKF and FGO."
  - src: "/images/pubs/2021-fgo-fig8-window-size.png"
    alt: "Two-dimensional positioning error under different FGO window sizes."
    context: "The window-size study explains why FGO performance depends on how much historical information is optimized together."
    caption: "Figure 8 from the paper: 2D positioning error under different sliding-window sizes for tightly coupled FGO."
  - src: "/images/pubs/2021-fgo-fig9-skyview.png"
    alt: "Sky-view images showing line-of-sight and non-line-of-sight satellite visibility at selected epochs."
    context: "These sky-view epochs interpret the window-size result by showing the LOS/NLOS satellite conditions during difficult periods."
    caption: "Figure 9 from the paper: fisheye sky-view images and LOS/NLOS satellite visibility at selected epochs."
  - src: "/images/pubs/2021-fgo-fig10-pseudorange-gmm.png"
    alt: "GPS and BeiDou pseudorange error histograms with fitted Gaussian mixture models."
    context: "The pseudorange histograms connect the positioning behavior to non-Gaussian urban measurement noise."
    caption: "Figure 10 from the paper: GPS and BeiDou pseudorange error histograms with fitted Gaussian mixture models."
  - src: "/images/pubs/2021-fgo-fig13-computation-time.png"
    alt: "Computational time comparison between tightly coupled FGO and tightly coupled iSAM."
    context: "The final comparison checks the practical computation cost of solving the tightly coupled graph with FGO versus iSAM."
    caption: "Figure 13 from the paper: computational-time comparison between tightly coupled FGO and tightly coupled iSAM."
themes:
  - "urban-gnss-reliability"
  - "optimization-estimation"
tags: []
---

**Key idea.** Classical GNSS/INS integration uses an Extended Kalman Filter, which condenses all history into a single current state. This paper recasts the problem as **factor graph optimization (FGO)** — jointly optimizing a sliding window of states with re-linearization, so the estimator can revisit past epochs and handle outliers far more flexibly.

**Impact.** It became the reference comparison establishing *why* FGO outperforms filtering for navigation, and was named the **2024 Most-Cited Paper in *NAVIGATION***. The result reframed how the field approaches GNSS/INS fusion and underpins much of IPNL's later integrity and multi-sensor work.
