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
summary: 這篇論文針對 Gaussian-mixture measurement noise 推導 chi-squared fault detector，並在 lidar/IMU localization system 中驗證。
highlights:
- 方法把 GMM 假設下的 EKF residuals 轉換成可用 chi-squared statistic 檢測的形式。
- CARLA-based lidar/IMU 實驗比較 Gaussian 與 Gaussian-mixture detectors 在 step 與 slope failures 下的表現。
hero_image: "/images/pubs/2025-fault-gmm-simulation-platform-hero.png"
hero_alt: "用於 fault detection validation 的 CARLA simulation route、vehicle scene 與 extracted LiDAR/IMU map face。"
hero_caption: "圖 4 視覺細節：用於 fault detection validation 的 CARLA simulation route、vehicle scene 與 extracted LiDAR/IMU map face。"
figures:
- src: /images/pubs/2025-fault-gmm-fig2-system-architecture.png
  alt: lidar/IMU localization system 與 fault-detection process 的架構圖。
  context: 在推導 residual transformation 後，論文把方法套用到含 lidar range-bearing measurements 與 IMU propagation 的 EKF-based localization system。
  caption: 圖 2：lidar/IMU localization system 的 fault-detection architecture 與 sensor platform。
- src: /images/pubs/2025-fault-gmm-fig3-lidar-measurement-model.png
  alt: 2D lidar line-segment extraction 與 plane-based measurement model 圖。
  context: lidar measurement model 定義後續進入 EKF 與 fault-detection statistic 的 residuals。
  caption: 圖 3：line segments extraction 與 2D lidar measurement model construction。
- src: /images/pubs/2025-fault-gmm-fig4-simulation-platform.png
  alt: CARLA simulated route、vehicle view 與 extracted building face model。
  context: 可控制的 simulation platform 提供可重複的 vehicle motion、map geometry 與可配置的 GMM-distributed noise。
  caption: 圖 4：CARLA simulation platform、vehicle track 與 extracted environmental faces。
- src: /images/pubs/2025-fault-gmm-fig6-positioning-error.png
  alt: fault-free simulated environment 中的 absolute translation error plot。
  context: 在加入 faults 前，論文先顯示 simulated route 中定位誤差增加的位置，特別是 feature 較少的大轉彎附近。
  caption: 圖 6：fault-free simulated environment 的 positioning absolute translation error。
- src: /images/pubs/2025-fault-gmm-fig7-step-failure-detection.png
  alt: 比較 total Gaussian-GMM 與 Gaussian methods 的 step-failure detection plots。
  context: step-failure experiment 比較 GMM-based statistic 是否比 Gaussian baseline 更穩定偵測 shaded failure period。
  caption: 圖 7：total Gaussian-GMM 與 Gaussian methods 的 step-failure detection results。
- src: /images/pubs/2025-fault-gmm-fig8-slope-failure-detection.png
  alt: 比較 total Gaussian-GMM 與 Gaussian methods 的 slope-failure detection plots。
  context: slope-failure case 測試 fault magnitude 隨時間增加時，同一 detector 的偵測行為。
  caption: 圖 8：total Gaussian-GMM 與 Gaussian methods 的 slope-failure detection results。
themes:
- optimization-estimation
- integrity-localization
tags: []
---

<aside class="translation-stub">本論文以英文發表。完整書目詳情、DOI / PDF 連結請見 <a href="/en/publications/2025-fault-detection-algorithm-for-gaussian-mixture-noises-an-ap/">英文頁面</a>。</aside>
