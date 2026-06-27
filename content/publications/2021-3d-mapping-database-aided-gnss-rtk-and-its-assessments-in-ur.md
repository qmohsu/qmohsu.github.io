---
title: "3D Mapping Database Aided GNSS RTK and Its Assessments in Urban Canyons"
slug: "2021-3d-mapping-database-aided-gnss-rtk-and-its-assessments-in-ur"
authors:
  - "Ng H.F."
  - "Hsu L.T."
year: 2021
venue: "IEEE Transactions on Aerospace and Electronic Systems"
type: "journal"
cv_number: 72
featured: true
quartile: "Q1"
doi: "10.1109/taes.2021.3069271"
pdf: ""
code: ""
data: ""
summary: "3D building models are used inside RTK processing to predict and exclude NLOS satellites before they corrupt ambiguity resolution."
hero_image: "/images/pubs/2021-3dma-rtk-fig1-flowchart.png"
hero_alt: "Flowchart of the proposed 3D mapping database-aided GNSS RTK method."
hero_caption: "Figure 1 from the paper: 3D mapping database-aided GNSS RTK flow from skymask generation to ambiguity resolution."
figures:
  - src: "/images/pubs/2021-3dma-rtk-fig2-candidate-heatmap.png"
    alt: "Heatmaps of position hypothesis mean square error and candidate score."
    context: "After the pipeline defines 3D-map-aided RTK, this heatmap shows how candidate positions are scored before ambiguity resolution."
    caption: "Figure 2: scoring position hypotheses with carrier-phase consistency."
  - src: "/images/pubs/2021-3dma-rtk-fig3-experiment-skymask.png"
    alt: "Hong Kong experiment locations and skymasks at five urban test locations."
    context: "The paper then tests the method across Hong Kong sites with different skyline obstruction patterns, making skymasks central to the evaluation."
    caption: "Figure 3: experiment locations and skymasks used for urban canyon assessment."
  - src: "/images/pubs/2021-3dma-rtk-fig4-equipment.png"
    alt: "Experiment equipment with antenna, splitter, geodetic receiver, commercial receiver, and PC."
    context: "The shared antenna and receiver setup lets the study compare geodetic and commercial receivers under the same satellite environment."
    caption: "Figure 4: experiment equipment for ground truth and RTK evaluation."
  - src: "/images/pubs/2021-3dma-rtk-fig5-positioning-adop-pdop.png"
    alt: "Positioning error, ADOP, PDOP, and satellite number time series for 3DMA GNSS RTK."
    context: "With the experiment fixed, the paper links positioning error to ambiguity dilution, geometry dilution, and satellite availability over time."
    caption: "Figure 5: time-series comparison of positioning error, ambiguity dilution, geometry dilution, and satellite count."
  - src: "/images/pubs/2021-3dma-rtk-fig6-7-cdf-boxplot.png"
    alt: "CDF of 2D positioning error and box plots for 3DMA BIE RTK experiments."
    context: "The time-series behavior is summarized statistically to show how often the 3DMA-aided RTK solution improves the 2D error distribution."
    caption: "Figures 6 and 7: distribution and box-plot summaries of 2D positioning error."
  - src: "/images/pubs/2021-3dma-rtk-fig8-position-heatmap-skymask.png"
    alt: "Position heatmap and skymasks showing satellite selection at ground truth and 3DMA hypothesis."
    context: "This diagnostic case explains the scoring behavior by comparing the position heatmap and visibility decisions at candidate locations."
    caption: "Figure 8: position heatmap and skymask comparison explaining a noisy-measurement case."
  - src: "/images/pubs/2021-3dma-rtk-fig10-positioning-visibility.png"
    alt: "2D positioning error and visibility classification correctness over a three-hour experiment."
    context: "The long-duration test checks whether the same visibility-based logic remains stable over several hours of urban data."
    caption: "Figure 10: three-hour positioning error and visibility-classification correctness."
project: "3dma-gnss"
themes:
  - "urban-gnss-reliability"
  - "environment-aware-pnt"
  - "optimization-estimation"
tags: []
---

**Key idea.** Carrier-phase RTK collapses in urban canyons because reflected (NLOS) signals corrupt ambiguity resolution. This work brings a **3D building model** into the RTK engine to predict and exclude NLOS satellites before they poison the solution.

**Impact.** It demonstrated that map-aware RTK can hold centimetre-class fixes in environments where conventional RTK fails — a building block of the lab's 3D-mapping-aided GNSS line and its smartphone/automotive applications.
