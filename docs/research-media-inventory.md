# Research Media Inventory

This is the backend inventory for paper, project, video, figure, code, and dataset links.
It is intentionally not a public website page.

## Current Policy

- Public paper pages may show videos, repositories, datasets, and related project/resource links when the source is known.
- Public paper figures should come from the paper PDF or an official paper/supplement source.
- Do not use newly generated diagrams or redrawn schematics as paper figures unless explicitly approved.
- When a flagship paper lacks a paper-sourced figure, keep it out of any public visual flagship grid until the figure is extracted and checked.

## Rich Paper Media Status

| Paper slug | Current public media links | Paper-sourced figure status | Next step |
|---|---|---|---|
| `2025-grid-based-3dma-gnss-with-clustering-and-doppler-velocity-us` | Cambridge PDF link, paper-sourced hero and five figure crops | Extracted from official Cambridge PDF rendered at high resolution; rich page only, not in flagship grid | Verify rendered publication page with desktop and mobile screenshots. |
| `2025-fault-detection-algorithm-for-gaussian-mixture-noises-an-ap` | PolyU repository PDF link, paper-sourced hero and six figure crops | Extracted from PolyU repository PDF rendered at high resolution; rich page only, not in flagship grid | Verify rendered publication page with desktop and mobile screenshots. |
| `2024-integrity-constrained-factor-graph-optimization-for-gnss-pos` | PolyU repository PDF link, paper-sourced hero and six figure crops | Extracted from PolyU repository PDF rendered at high resolution; rich page only, not in flagship grid | Verify rendered publication page with desktop and mobile screenshots. |
| `2024-enhancing-smartphone-based-pedestrian-positioning-using-fac` | Bon View PDF link, GitHub code link, paper-sourced hero and six figure crops | Extracted from official Bon View PDF rendered at high resolution; rich page only, not in flagship grid | Verify rendered publication page with desktop and mobile screenshots. |
| `2021-factor-graph-optimization-for-gnssins-integration-a-compar` | YouTube webinar, GraphGNSSLib repo, GraphGNSSLib resource/project, paper-sourced hero and seven figure crops | Extracted from local paper PDF | Verify rendered publication page with desktop and mobile screenshots. |
| `2023-hong-kong-urbannav-an-open-source-multisensory-dataset-for` | UrbanNav videos, UrbanNavDataset repo, UrbanNav resource/project, paper-sourced hero and seven figure crops | Extracted from local paper PDF | Verify rendered publication page with desktop and mobile screenshots. |
| `2021-3d-mapping-database-aided-gnss-rtk-and-its-assessments-in-ur` | 3DMA project link, paper-sourced hero and seven figure crops | Extracted from local paper PDF | Verify rendered publication page with desktop and mobile screenshots. |
| `2021-robust-gnss-shadow-matching-for-smartphones-in-urban-canyons` | 3DMA project link, paper-sourced hero and six figure crops | Extracted from local paper PDF | Verify rendered publication page with desktop and mobile screenshots. |
| `2023-glio-tightly-coupled-gnsslidarimu-integration-for-continu` | Paper-sourced hero and five figure crops | Extracted from local paper PDF | Verify rendered publication page with desktop and mobile screenshots. |
| `2023-positionnet-cnn-based-gnss-positioning-in-urban-areas-with` | Paper-sourced hero and six figure crops | Extracted from local paper PDF | Verify rendered publication page with desktop and mobile screenshots. |

## Supported Publication Fields

See `docs/publication-frontmatter-schema.md` for the frontmatter contract used by the website templates.

## Paper Figure Extraction Log

### 2021 FGO vs EKF

- Source PDF: local archive copy named `Factor graph optimization for GNSSINS integration A comparison with the extended Kalman filter.pdf` under the IPNL website publication full-paper archive. The PDF itself was not copied into the website repo.
- PDF metadata checked with Poppler: title `Factor graph optimization for GNSS/INS integration: A comparison with the extended Kalman filter`; 17 pages; page rotation 0; unencrypted.
- Rendered candidate pages at 300 DPI before cropping.
- Published crops:
  - page 4 / Figure 1 -> `static/images/pubs/2021-fgo-fig1-flowchart.png`
  - page 7 / Figure 2 -> `static/images/pubs/2021-fgo-fig2-factor-graph.png`
  - page 8 / Figure 3 -> `static/images/pubs/2021-fgo-fig3-experiment-setup.png`
  - page 10 / Figure 5 -> `static/images/pubs/2021-fgo-fig5-tc-results.png`
  - page 11 / Figure 8 -> `static/images/pubs/2021-fgo-fig8-window-size.png`
  - page 12 / Figure 9 -> `static/images/pubs/2021-fgo-fig9-skyview.png`
  - page 13 / Figure 10 -> `static/images/pubs/2021-fgo-fig10-pseudorange-gmm.png`
  - page 14 / Figure 13 -> `static/images/pubs/2021-fgo-fig13-computation-time.png`

### 2023 UrbanNav Dataset

- Source PDF: local archive copy named `Hong Kong UrbanNav_An Open-Source Multisensory Dataset for Benchmarking Urban Navigation Algorithms.pdf` under the IPNL website publication full-paper archive. The PDF itself was not copied into the website repo.
- PDF metadata checked with Poppler: title `Hong Kong UrbanNav: An Open-Source Multisensory Dataset for Benchmarking Urban Navigation Algorithms`; 29 pages; page rotation 0; unencrypted.
- Rendered candidate pages at 300 DPI before cropping.
- Published crops:
  - page 3 / Figure 1 -> `static/images/pubs/2023-urbannav-fig1-overview.png`
  - page 7 / Figure 2 -> `static/images/pubs/2023-urbannav-fig2-platform.png`
  - page 8 / Figure 3 -> `static/images/pubs/2023-urbannav-fig3-hardware-flow.png`
  - page 11 / Figure 4 -> `static/images/pubs/2023-urbannav-fig4-sensor-installation.png`
  - page 13 / Figure 5 -> `static/images/pubs/2023-urbannav-fig5-scenarios-reconstruction.png`
  - page 15 / Figure 6 -> `static/images/pubs/2023-urbannav-fig6-skymasks.png`
  - page 24 / Figure 16 -> `static/images/pubs/2023-urbannav-fig16-benchmark-trajectories.png`
  - page 25 / Figure 18 -> `static/images/pubs/2023-urbannav-fig18-lessons-github.png`

### 2021 3DMA GNSS RTK

- Source PDF: local archive copy named `3D Mapping Database-Aided GNSS RTK and Its Assessments in Urban Canyons.pdf` under the IPNL website publication full-paper archive. The PDF itself was not copied into the website repo.
- PDF metadata checked with Poppler: title `3D Mapping Database-Aided GNSS RTK and Its Assessments in Urban Canyons`; 17 pages; page rotation 0; unencrypted.
- Rendered candidate pages at 300 DPI before cropping.
- Published crops:
  - page 3 / Figure 1 -> `static/images/pubs/2021-3dma-rtk-fig1-flowchart.png`
  - page 6 / Figure 2 -> `static/images/pubs/2021-3dma-rtk-fig2-candidate-heatmap.png`
  - page 7 / Figure 3 -> `static/images/pubs/2021-3dma-rtk-fig3-experiment-skymask.png`
  - page 8 / Figure 4 -> `static/images/pubs/2021-3dma-rtk-fig4-equipment.png`
  - page 9 / Figure 5 -> `static/images/pubs/2021-3dma-rtk-fig5-positioning-adop-pdop.png`
  - page 11 / Figures 6 and 7 -> `static/images/pubs/2021-3dma-rtk-fig6-7-cdf-boxplot.png`
  - page 12 / Figure 8 -> `static/images/pubs/2021-3dma-rtk-fig8-position-heatmap-skymask.png`
  - page 14 / Figure 10 -> `static/images/pubs/2021-3dma-rtk-fig10-positioning-visibility.png`

### 2021 Robust GNSS Shadow Matching

- Source PDF: local archive copy named `Robust GNSS Shadow Matching for Smartphones in Urban Canyons.pdf` under the IPNL website publication full-paper archive. The PDF itself was not copied into the website repo.
- PDF metadata checked with Poppler: metadata title is malformed; 12 pages; page rotation 0; unencrypted. The filename and rendered page title identify the paper.
- Rendered candidate pages at 300 DPI before cropping.
- Published crops:
  - page 3 / Figure 3 -> `static/images/pubs/2021-shadow-matching-fig3-flowchart.png`
  - page 2 / Figure 1 -> `static/images/pubs/2021-shadow-matching-fig1-skymask-format.png`
  - page 3 / Figure 2 -> `static/images/pubs/2021-shadow-matching-fig2-nlos-example.png`
  - page 4 / Figure 4 -> `static/images/pubs/2021-shadow-matching-fig4-key-satellite.png`
  - page 6 / Figure 6 -> `static/images/pubs/2021-shadow-matching-fig6-environment-skymask.png`
  - page 8 / Figure 11 -> `static/images/pubs/2021-shadow-matching-fig11-candidate-skymask.png`
  - page 10 / Figure 14 -> `static/images/pubs/2021-shadow-matching-fig14-reliability-cdf.png`

### 2023 GLIO

- Source PDF: local archive copy named `GLIO_Tightly-Coupled_GNSS_LiDAR_IMU_Integration_for_Continuous_and_Drift-Free_State_Estimation_of_Intelligent_Vehicles_in_Urban_Areas.pdf` under the organized published papers archive. The PDF itself was not copied into the website repo.
- PDF metadata checked with Poppler: title `GLIO: Tightly-Coupled GNSS/LiDAR/IMU Integration for Continuous and Drift-Free State Estimation of Intelligent Vehicles in Urban Areas`; 11 pages; page rotation 0; unencrypted.
- Rendered candidate pages at 300 DPI before cropping.
- Published crops:
  - page 4 / Figure 1 -> `static/images/pubs/2023-glio-fig1-system-pipeline.png`
  - page 5 / Figure 2 -> `static/images/pubs/2023-glio-fig2-lidar-association.png`
  - page 6 / Figure 3 -> `static/images/pubs/2023-glio-fig3-factor-graph.png`
  - page 7 / Figure 4 -> `static/images/pubs/2023-glio-fig4-tst-trajectory.png`
  - page 8 / Figures 5 and 6 -> `static/images/pubs/2023-glio-fig5-6-tst-errors.png`
  - page 9 / Figures 7 and 8 -> `static/images/pubs/2023-glio-fig7-8-whampoa-results.png`

### 2023 PositionNet

- Source PDF: local final ASC copy named `CNN-based GNSS Positioning in Urban Areas with Residual Maps_ASC.pdf` under the Applied Soft Computing PositionNet publication folder. The PDF itself was not copied into the website repo.
- PDF metadata checked with Poppler: 14 pages; page rotation 0; unencrypted. This final ASC copy was used instead of an earlier preprint-rendered copy.
- Rendered candidate pages at 300 DPI before cropping.
- Published crops:
  - page 4 / Figure 3 -> `static/images/pubs/2023-positionnet-fig3-network.png`
  - page 2 / Figure 1 -> `static/images/pubs/2023-positionnet-fig1-res-map-geometry.png`
  - page 3 / Figure 2 -> `static/images/pubs/2023-positionnet-fig2-sdres-map.png`
  - page 7 / Figure 4 -> `static/images/pubs/2023-positionnet-fig4-validation-map.png`
  - page 9 / Figure 5 -> `static/images/pubs/2023-positionnet-fig5-case1-solution.png`
  - page 9 / Figure 6 -> `static/images/pubs/2023-positionnet-fig6-case1-saliency.png`
  - page 12 / Figure 11 -> `static/images/pubs/2023-positionnet-fig11-saliency-weighting.png`

### 2025 Grid-based 3DMA GNSS with Clustering and Doppler Velocity

- Source PDF: official Cambridge Core PDF at `https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4CA0FA5382164ABE5B9B6D4A7B4BB4E9/S0373463325000220a.pdf/grid-based-3dma-gnss-with-clustering-and-doppler-velocity-using-factor-graph-optimisation.pdf`. The PDF itself was not copied into the website repo.
- PDF metadata checked with PyMuPDF: title `Grid-based 3DMA GNSS with clustering and Doppler velocity using factor graph optimisation`; 19 pages; page rotation 0; unencrypted.
- Rendered selected candidate pages at high resolution before cropping and inspected a crop contact sheet.
- Published crops:
  - page 4 / Figure 1 -> `static/images/pubs/2025-grid-3dma-fgo-fig1-flowchart.png`
  - page 6 / Figure 2 -> `static/images/pubs/2025-grid-3dma-fgo-fig2-region-growing.png`
  - page 10 / Figure 4 -> `static/images/pubs/2025-grid-3dma-fgo-fig4-hybrid-factor-graph.png`
  - page 11 / Figure 5 -> `static/images/pubs/2025-grid-3dma-fgo-fig5-skymask-experiment.png`
  - page 14 / Figure 7 -> `static/images/pubs/2025-grid-3dma-fgo-fig7-clustering-result.png`
  - page 16 / Figure 9 -> `static/images/pubs/2025-grid-3dma-fgo-fig9-vehicular-summary.png`

### 2025 Fault Detection Algorithm for Gaussian Mixture Noises

- Source PDF: PolyU repository PDF at `https://ira.lib.polyu.edu.hk/bitstream/10397/112926/1/navi.684.full.pdf`. The PDF itself was not copied into the website repo.
- PDF metadata checked with PyMuPDF: title `Fault Detection Algorithm for Gaussian Mixture Noises: An Application in Lidar/IMU Integrated Localization Systems`; 42 pages; page rotation 0; unencrypted.
- Rendered selected candidate pages at high resolution before cropping and inspected a crop contact sheet.
- Published crops:
  - page 9 / Figure 1 -> `static/images/pubs/2025-fault-gmm-fig1-gmm-transformation.png`
  - page 11 / Figure 2 -> `static/images/pubs/2025-fault-gmm-fig2-system-architecture.png`
  - page 14 / Figure 3 -> `static/images/pubs/2025-fault-gmm-fig3-lidar-measurement-model.png`
  - page 16 / Figure 4 -> `static/images/pubs/2025-fault-gmm-fig4-simulation-platform.png`
  - page 19 / Figure 6 -> `static/images/pubs/2025-fault-gmm-fig6-positioning-error.png`
  - page 21 / Figure 7 -> `static/images/pubs/2025-fault-gmm-fig7-step-failure-detection.png`
  - page 22 / Figure 8 -> `static/images/pubs/2025-fault-gmm-fig8-slope-failure-detection.png`

### 2024 Integrity-Constrained Factor Graph Optimization

- Source PDF: PolyU repository PDF at `https://ira.lib.polyu.edu.hk/bitstream/10397/111854/1/navi.660.full.pdf`. The PDF itself was not copied into the website repo.
- PDF metadata checked with PyMuPDF: title `Integrity-Constrained Factor Graph Optimization for GNSS Positioning in Urban Canyons`; 27 pages; page rotation 0; unencrypted.
- Rendered selected candidate pages at high resolution before cropping and inspected a crop contact sheet.
- Published crops:
  - page 5 / Figure 1 -> `static/images/pubs/2024-integrity-fgo-fig1-method-flowchart.png`
  - page 6 / Figure 2 -> `static/images/pubs/2024-integrity-fgo-fig2-factor-graph.png`
  - page 14 / Figure 6 -> `static/images/pubs/2024-integrity-fgo-fig6-hpe-hpl.png`
  - page 15 / Figure 7 -> `static/images/pubs/2024-integrity-fgo-fig7-skyplot-switch-values.png`
  - page 16 / Figure 8 -> `static/images/pubs/2024-integrity-fgo-fig8-urbannav-trajectories.png`
  - page 18 / Figure 9 -> `static/images/pubs/2024-integrity-fgo-fig9-urban-medium-results.png`
  - page 21 / Figure 13 -> `static/images/pubs/2024-integrity-fgo-fig13-pseudorange-error-distribution.png`

### 2024 Smartphone Pedestrian Positioning with Indoor/Outdoor Detection

- Source PDF: official Bon View Press PDF at `https://ojs.bonviewpress.com/index.php/jdsis/article/download/2961/1145/24389`. The PDF itself was not copied into the website repo.
- PDF metadata checked with PyMuPDF: title `Enhancing Smartphone-based Pedestrian Positioning: Using Factor Graph Optimization with Indoor/Outdoor Detection for 3DMA GNSS/Visual-inertial State Estimation`; 17 pages; page rotation 0; unencrypted.
- Rendered selected candidate pages at high resolution before cropping and inspected a crop contact sheet.
- Published crops:
  - page 4 / Figure 2 -> `static/images/pubs/2024-smartphone-fgo-fig2-system-flow.png`
  - page 5 / Figure 3 -> `static/images/pubs/2024-smartphone-fgo-fig3-io-svm-flow.png`
  - page 8 / Figure 4 -> `static/images/pubs/2024-smartphone-fgo-fig4-factor-graph.png`
  - page 9 / Figure 5 -> `static/images/pubs/2024-smartphone-fgo-fig5-experiment-trajectories.png`
  - page 9 / Figure 6 -> `static/images/pubs/2024-smartphone-fgo-fig6-lio-sam-ground-truth.png`
  - page 13 / Figure 13 -> `static/images/pubs/2024-smartphone-fgo-fig13-b2-error.png`
  - page 13 / Figure 14 -> `static/images/pubs/2024-smartphone-fgo-fig14-b2-trajectory.png`
