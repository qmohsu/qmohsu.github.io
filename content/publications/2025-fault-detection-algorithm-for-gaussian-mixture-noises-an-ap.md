---
title: 'Fault Detection Algorithm for Gaussian Mixture Noises: An Application in Lidar/IMU Integrated Localization Systems'
slug: 2025-fault-detection-algorithm-for-gaussian-mixture-noises-an-ap
authors:
- Yan, P.
- Li, Z.
- Huang, F.
- Wen, W.
- Hsu, L. T.
year: 2025
venue: 'NAVIGATION: Journal of the Institute of Navigation'
type: journal
cv_number: 7
featured: true
quartile: Q1
doi: 10.33012/navi.684
pdf: https://ira.lib.polyu.edu.hk/bitstream/10397/112926/1/navi.684.full.pdf
code: ''
data: ''
summary: This paper derives a chi-squared fault detector for Gaussian-mixture measurement noise and validates it in a lidar/IMU localization system.
highlights:
- The method transforms EKF residuals under GMM assumptions so they can be tested with a chi-squared statistic.
- CARLA-based lidar/IMU experiments compare Gaussian and Gaussian-mixture detectors under step and slope failures.
hero_image: "/images/pubs/2025-fault-gmm-simulation-platform-hero.png"
hero_alt: "CARLA simulation route, vehicle scene, and extracted LiDAR/IMU map face used for fault detection validation."
hero_caption: "Figure 4 visual detail: CARLA simulation route, vehicle scene, and extracted LiDAR/IMU map face used for fault detection validation."
figures:
- src: /images/pubs/2025-fault-gmm-fig2-system-architecture.png
  alt: Architecture of the lidar/IMU localization system and fault-detection process.
  context: After deriving the residual transformation, the paper applies it to an EKF-based localization system with lidar range-bearing measurements and IMU propagation.
  caption: 'Figure 2: fault-detection architecture and sensor platform for the lidar/IMU localization system.'
- src: /images/pubs/2025-fault-gmm-fig3-lidar-measurement-model.png
  alt: 2D lidar line-segment extraction and plane-based measurement model diagrams.
  context: The lidar measurement model defines the residuals that later enter the EKF and the fault-detection statistic.
  caption: 'Figure 3: extracting line segments and constructing the 2D lidar measurement model.'
- src: /images/pubs/2025-fault-gmm-fig4-simulation-platform.png
  alt: CARLA simulated route, vehicle view, and extracted building face model.
  context: The controlled simulation platform supplies repeatable vehicle motion, map geometry, and configurable GMM-distributed noise for testing.
  caption: 'Figure 4: CARLA simulation platform, designed vehicle track, and extracted environmental faces.'
- src: /images/pubs/2025-fault-gmm-fig6-positioning-error.png
  alt: Absolute translation error plot for the fault-free simulated environment.
  context: Before introducing faults, the paper shows where localization error grows in the simulated route, especially near large turns with fewer features.
  caption: 'Figure 6: absolute translation error of positioning results in the fault-free simulated environment.'
- src: /images/pubs/2025-fault-gmm-fig7-step-failure-detection.png
  alt: Step-failure detection plots comparing total Gaussian-GMM and Gaussian methods.
  context: The step-failure experiment then compares whether the GMM-based statistic detects the shaded failure period more reliably than the Gaussian baseline.
  caption: 'Figure 7: step-failure detection results for total Gaussian-GMM and Gaussian methods.'
- src: /images/pubs/2025-fault-gmm-fig8-slope-failure-detection.png
  alt: Slope-failure detection plots comparing total Gaussian-GMM and Gaussian methods.
  context: The slope-failure case tests the same detector when the fault magnitude grows over time rather than appearing as a fixed step.
  caption: 'Figure 8: slope-failure detection results for total Gaussian-GMM and Gaussian methods.'
themes:
- optimization-estimation
- integrity-localization
tags: []
---
