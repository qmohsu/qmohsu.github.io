---
title: "Robust GNSS Shadow Matching for Smartphones in Urban Canyons"
slug: "2021-robust-gnss-shadow-matching-for-smartphones-in-urban-canyons"
authors:
  - "Ng H.F."
  - "Zhang G."
  - "Hsu L. T."
year: 2021
venue: "IEEE Sensors Journal"
type: "journal"
cv_number: 79
featured: true
quartile: "Q1"
doi: "10.1109/jsen.2021.3083801"
pdf: ""
code: ""
data: ""
summary: "Robust shadow matching compares smartphone satellite visibility against a 3D building model to improve urban canyon positioning."
hero_image: "/images/pubs/2021-shadow-matching-fig3-flowchart.png"
hero_alt: "Flowchart of the proposed robust GNSS shadow matching method."
hero_caption: "Figure 3 from the paper: robust GNSS shadow matching flow using measurements, candidate positions, skymasks, scoring, and reliability evaluation."
figures:
  - src: "/images/pubs/2021-shadow-matching-fig1-skymask-format.png"
    alt: "Skymask storage format beside a polar skymask visualization."
    context: "Before scoring candidate positions, the paper defines the skymask representation used to predict LOS and NLOS visibility from 3D buildings."
    caption: "Figure 1: skymask data format and skyplot visualization for visibility prediction."
  - src: "/images/pubs/2021-shadow-matching-fig2-nlos-example.png"
    alt: "NLOS reception example showing LOS, reflected, and NLOS paths around buildings."
    context: "This example motivates the robust method by showing how NLOS reception can make opposite-side street candidates look similarly plausible."
    caption: "Figure 2: example of NLOS reception affecting GNSS shadow matching."
  - src: "/images/pubs/2021-shadow-matching-fig4-key-satellite.png"
    alt: "Key satellite classification diagram with LOS, NLOS, skymask, and key satellite area."
    context: "After the basic shadow-matching flow, the reliability rules focus on key satellites near building edges to judge whether the geometry is distinctive enough."
    caption: "Figure 4: key satellite classification around the skymask building edge."
  - src: "/images/pubs/2021-shadow-matching-fig6-environment-skymask.png"
    alt: "Urban experiment environment panels paired with skymasks."
    context: "The evaluation then applies those rules across real streets with different building geometries and receiver types."
    caption: "Figure 6: experiment environments and corresponding skymasks."
  - src: "/images/pubs/2021-shadow-matching-fig11-candidate-skymask.png"
    alt: "Position candidate heatmap and skymasks showing satellite classification at selected candidates."
    context: "This diagnostic case shows why ambiguity remains when multiple candidate locations produce similar skymask evidence."
    caption: "Figure 11: candidate heatmap and skymask diagnostics for an ambiguous shadow-matching case."
  - src: "/images/pubs/2021-shadow-matching-fig14-reliability-cdf.png"
    alt: "CDF of across-street positioning error before and after reliability evaluation."
    context: "The final result shows how excluding unreliable shadow-matching epochs improves the across-street error distribution."
    caption: "Figure 14: reliability evaluation improves the across-street error distribution."
project: "3dma-gnss"
themes:
  - "urban-gnss-reliability"
  - "environment-aware-pnt"
  - "seamless-pnt-embodied"
tags: []
---

**Key idea.** Shadow matching positions a receiver by comparing *which satellites are visible* against a 3D building model — strong exactly where ranging is weak (cross-street). This paper makes the method **robust enough for smartphone-grade** signals and noisy visibility decisions.

**Impact.** A step toward consumer-device urban positioning, feeding directly into the lab's smartphone-positioning programme and the long-running Huawei collaboration.
