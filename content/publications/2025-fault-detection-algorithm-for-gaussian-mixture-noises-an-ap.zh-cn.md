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
featured: false
quartile: Q1
doi: 10.33012/navi.684
pdf: https://ira.lib.polyu.edu.hk/bitstream/10397/112926/1/navi.684.full.pdf
code: ''
data: ''
summary: 这篇论文针对 Gaussian-mixture measurement noise 推导 chi-squared fault detector，并在 lidar/IMU localization system 中验证。
highlights:
- 方法把 GMM 假设下的 EKF residuals 转换成可用 chi-squared statistic 检测的形式。
- CARLA-based lidar/IMU 实验比较 Gaussian 与 Gaussian-mixture detectors 在 step 与 slope failures 下的表现。
hero_image: /images/pubs/2025-fault-gmm-fig1-gmm-transformation.png
hero_alt: 比较 GMM 与 Gaussian 假设下 measurement residual transformation 的流程图。
hero_caption: 图 1：GMM 与 Gaussian noise assumptions 下 residuals 的 transformation methods。
figures:
- src: /images/pubs/2025-fault-gmm-fig2-system-architecture.png
  alt: lidar/IMU localization system 与 fault-detection process 的架构图。
  context: 在推导 residual transformation 后，论文把方法套用到含 lidar range-bearing measurements 与 IMU propagation 的 EKF-based localization system。
  caption: 图 2：lidar/IMU localization system 的 fault-detection architecture 与 sensor platform。
- src: /images/pubs/2025-fault-gmm-fig3-lidar-measurement-model.png
  alt: 2D lidar line-segment extraction 与 plane-based measurement model 图。
  context: lidar measurement model 定义后续进入 EKF 与 fault-detection statistic 的 residuals。
  caption: 图 3：line segments extraction 与 2D lidar measurement model construction。
- src: /images/pubs/2025-fault-gmm-fig4-simulation-platform.png
  alt: CARLA simulated route、vehicle view 与 extracted building face model。
  context: 可控制的 simulation platform 提供可重复的 vehicle motion、map geometry 与可配置的 GMM-distributed noise。
  caption: 图 4：CARLA simulation platform、vehicle track 与 extracted environmental faces。
- src: /images/pubs/2025-fault-gmm-fig6-positioning-error.png
  alt: fault-free simulated environment 中的 absolute translation error plot。
  context: 在加入 faults 前，论文先显示 simulated route 中定位误差增加的位置，特别是 feature 较少的大转弯附近。
  caption: 图 6：fault-free simulated environment 的 positioning absolute translation error。
- src: /images/pubs/2025-fault-gmm-fig7-step-failure-detection.png
  alt: 比较 total Gaussian-GMM 与 Gaussian methods 的 step-failure detection plots。
  context: step-failure experiment 比较 GMM-based statistic 是否比 Gaussian baseline 更稳定检测 shaded failure period。
  caption: 图 7：total Gaussian-GMM 与 Gaussian methods 的 step-failure detection results。
- src: /images/pubs/2025-fault-gmm-fig8-slope-failure-detection.png
  alt: 比较 total Gaussian-GMM 与 Gaussian methods 的 slope-failure detection plots。
  context: slope-failure case 测试 fault magnitude 随时间增加时，同一 detector 的检测行为。
  caption: 图 8：total Gaussian-GMM 与 Gaussian methods 的 slope-failure detection results。
themes:
- optimization-estimation
- integrity-localization
tags: []
---

<aside class="translation-stub">本论文以英文发表。完整书目详情、DOI / PDF 链接请见 <a href="/en/publications/2025-fault-detection-algorithm-for-gaussian-mixture-noises-an-ap/">英文页面</a>。</aside>
