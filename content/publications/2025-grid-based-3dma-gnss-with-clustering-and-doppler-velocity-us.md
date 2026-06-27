---
title: Grid-based 3DMA GNSS with clustering and Doppler velocity using factor graph optimisation
slug: 2025-grid-based-3dma-gnss-with-clustering-and-doppler-velocity-us
authors:
- Ng, H. F.
- Zhong, Q.
- Groves, P.
- Hsu, L. T.
year: 2025
venue: The Journal of Navigation
type: journal
cv_number: 6
featured: false
quartile: Q1
doi: 10.1017/s0373463325000220
pdf: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4CA0FA5382164ABE5B9B6D4A7B4BB4E9/S0373463325000220a.pdf/grid-based-3dma-gnss-with-clustering-and-doppler-velocity-using-factor-graph-optimisation.pdf
code: ''
data: ''
summary: Grid-based 3DMA GNSS combines candidate clustering, Doppler-derived velocity, and factor graph optimization to improve urban GNSS positioning in deep urban scenes.
highlights:
- Region-growing clustering separates multimodal 3DMA GNSS candidate locations before factor graph optimization.
- The paper evaluates static London data and a vehicular Canary Wharf experiment, comparing loosely coupled and hybrid-coupled FGO variants.
hero_image: /images/pubs/2025-grid-3dma-fgo-fig1-flowchart.png
hero_alt: Flowchart of the proposed grid-based 3DMA GNSS algorithm with clustering, Doppler velocity estimation, and factor graph optimization.
hero_caption: 'Figure 1: the proposed workflow routes pseudorange and Doppler information through candidate distribution, region-growing clustering, and factor graph optimization.'
figures:
- src: /images/pubs/2025-grid-3dma-fgo-fig2-region-growing.png
  alt: Simplified region-growing example with sampled candidates, score ordering, thresholds, and clustering results.
  context: After candidate scores are computed, the paper uses region growing to split likely receiver locations into separate clusters instead of forcing a single candidate cloud.
  caption: 'Figure 2: simplified example of the region-growing algorithm used for clustering sampled 3DMA GNSS candidates.'
- src: /images/pubs/2025-grid-3dma-fgo-fig4-hybrid-factor-graph.png
  alt: Hybrid-coupled factor graph structure with state nodes, pseudorange factors, Doppler factors, and selected 3DMA GNSS cluster factors.
  context: The selected cluster then becomes one of the measurement factors in a hybrid-coupled graph that also uses pseudorange and Doppler information.
  caption: 'Figure 4: factor graph structure for the proposed hybrid-coupled 3DMA GNSS approach.'
- src: /images/pubs/2025-grid-3dma-fgo-fig5-skymask-experiment.png
  alt: Experiment statistics and sky masks showing building-boundary elevation angle, SNR, LOS satellites, and NLOS satellites.
  context: Before reporting accuracy, the paper documents the urban obstruction level and satellite visibility conditions used in the experiments.
  caption: 'Figure 5: average building-boundary elevation, received SNR, and sky masks for representative test locations.'
- src: /images/pubs/2025-grid-3dma-fgo-fig7-clustering-result.png
  alt: Static positioning result plots comparing clustered and non-clustered 3DMA GNSS FGO methods at a difficult street location.
  context: The static result shows how clustering reduces lateral street-direction error and separates competing candidate clusters near the true position.
  caption: 'Figure 7: horizontal errors, map plots, and multiple-cluster example for a static urban test location.'
- src: /images/pubs/2025-grid-3dma-fgo-fig9-vehicular-summary.png
  alt: Bar chart of vehicular experiment RMSE and 50th, 90th, and 95th percentile positioning errors across algorithms.
  context: The vehicular summary extends the static findings to a dynamic route, comparing error percentiles across conventional, grid-filter, and FGO-based methods.
  caption: 'Figure 9: RMSE and percentile horizontal radial positioning errors for the vehicular experiment.'
themes:
- urban-gnss-reliability
- environment-aware-pnt
- optimization-estimation
tags: []
---
