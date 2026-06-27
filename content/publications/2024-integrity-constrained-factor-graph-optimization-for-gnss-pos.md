---
title: Integrity-Constrained Factor Graph Optimization for GNSS Positioning in Urban Canyons
slug: 2024-integrity-constrained-factor-graph-optimization-for-gnss-pos
authors:
- Xia, X.
- Wen, W.
- Hsu, L. T.
year: 2024
venue: 'NAVIGATION: Journal of the Institute of Navigation'
type: journal
cv_number: 15
featured: false
quartile: Q1
doi: 10.33012/navi.660
pdf: https://ira.lib.polyu.edu.hk/bitstream/10397/111854/1/navi.660.full.pdf
code: ''
data: ''
summary: Integrity-constrained FGO reweights faulty GNSS measurements with switchable pseudorange and chi-square-test factors while preserving geometry for protection-level calculation.
highlights:
- The factor graph combines switchable pseudorange, switch prior, switch reliable, and chi-square test factors.
- UrbanNav experiments connect the method to real medium and harsh urban scenarios, including HPE, HPL, skyplot, and trajectory results.
hero_image: /images/pubs/2024-integrity-fgo-fig1-method-flowchart.png
hero_alt: Flowchart of integrity-constrained factor graph optimization with switchable pseudorange modeling, chi-square testing, measurement reweighting, and protection-level calculation.
hero_caption: 'Figure 1: the proposed method links switchable factors, chi-square testing, measurement reweighting, and HPL calculation.'
figures:
- src: /images/pubs/2024-integrity-fgo-fig2-factor-graph.png
  alt: Integrity-constrained factor graph with satellite nodes, switch variables, pseudorange factors, switch priors, switch reliable factors, and chi-square test factor.
  context: The flowchart becomes a factor graph in which switch variables are estimated across epochs instead of removing satellites outright.
  caption: 'Figure 2: graph structure of the proposed integrity-constrained factor graph.'
- src: /images/pubs/2024-integrity-fgo-fig6-hpe-hpl.png
  alt: HPE and HPL curves for FGO, RAIM-FGO, SW-FGO, and SWFDE-FGO during a bias-injection period.
  context: The controlled bias test shows how the chi-square-test factor affects horizontal position error and protection level during the fault period.
  caption: 'Figure 6: HPE and HPL for the four methods during injected satellite biases.'
- src: /images/pubs/2024-integrity-fgo-fig7-skyplot-switch-values.png
  alt: Skyplots comparing FGO, RAIM-FGO, SW-FGO, and SWFDE-FGO switch values at epoch A.
  context: 'The skyplot explains the key design choice: faulty satellites are downweighted by switch values, helping preserve useful geometry.'
  caption: 'Figure 7: skyplot of switch values for four methods at epoch A.'
- src: /images/pubs/2024-integrity-fgo-fig8-urbannav-trajectories.png
  alt: Bird's-eye-view trajectories for UrbanNav-Medium and UrbanNav-Harsh datasets.
  context: The real UrbanNav trajectories move the evaluation from controlled bias injection to medium and harsh urban routes.
  caption: 'Figure 8: bird''s-eye-view trajectories for the UrbanNav-Medium and UrbanNav-Harsh datasets.'
- src: /images/pubs/2024-integrity-fgo-fig9-urban-medium-results.png
  alt: UrbanNav result curves for snapshot test statistic, HPE, and HPL across algorithms.
  context: The UrbanNav result curves connect trajectory behavior to the integrity metrics used to compare the methods.
  caption: 'Figure 9: snapshot test statistic, HPE, and HPL during the UrbanNav experiment.'
- src: /images/pubs/2024-integrity-fgo-fig13-pseudorange-error-distribution.png
  alt: Distribution of switchable pseudorange errors for FGO, SW-FGO, and SWFDE-FGO.
  context: The pseudorange-error distribution explains how switch values narrow or reshape residuals while retaining geometric information.
  caption: 'Figure 13: switchable pseudorange error distribution for FGO, SW-FGO, and SWFDE-FGO.'
themes:
- urban-gnss-reliability
- optimization-estimation
- integrity-localization
tags: []
---
