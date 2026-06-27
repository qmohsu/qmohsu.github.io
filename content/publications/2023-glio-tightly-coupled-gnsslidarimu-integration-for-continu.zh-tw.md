---
title: "GLIO: Tightly-coupled gnss/lidar/imu integration for continuous and drift-free state estimation of intelligent vehicles in urban areas"
slug: "2023-glio-tightly-coupled-gnsslidarimu-integration-for-continu"
authors:
  - "Liu, X."
  - "Wen, W."
  - "Hsu, L. T."
year: 2023
venue: "IEEE Transactions on Intelligent Vehicles"
type: "journal"
cv_number: 42
featured: true
quartile: "Q1"
doi: "10.1109/tiv.2023.3323648"
pdf: ""
code: ""
data: ""
hero_image: "/images/pubs/2023-glio-fig1-system-pipeline.png"
hero_alt: "Overview of the GLIO tightly coupled GNSS, LiDAR, and IMU integration pipeline."
hero_caption: "圖 1（GLIO 論文）：用於緊耦合 GNSS、LiDAR 和 IMU 因子圖最佳化的系統流程。"
figures:
  - src: "/images/pubs/2023-glio-fig2-lidar-association.png"
    alt: "Scan-to-map and scan-to-multiscan LiDAR association schemes."
    context: "在系統流程之後，這張圖解釋 LiDAR 約束設計如何支持更平滑且更具全域一致性的最佳化。"
    caption: "圖 2：透過 scan-to-map 和 scan-to-multiscan 方案建立 LiDAR 因子關聯。"
  - src: "/images/pubs/2023-glio-fig3-factor-graph.png"
    alt: "Two-stage factor graph structure with GNSS, INS, Doppler, scan-to-map, and scan-to-multiscan factors."
    context: "因子圖展示 GNSS、Doppler、IMU 和 LiDAR 約束如何組織到第一階段和第二階段最佳化中。"
    caption: "圖 3：第一階段融合與第二階段最佳化的因子圖結構。"
  - src: "/images/pubs/2023-glio-fig4-tst-trajectory.png"
    alt: "3D trajectory comparison in the Tsim Sha Tsui sequence."
    context: "結果從尖沙咀序列開始，比較 GLIO 變體和基線方法的軌跡一致性。"
    caption: "圖 4：RTKLIB、LIO、LIO-GNSS、GLIO-SS 和 GLIO-DS 在尖沙咀的軌跡比較。"
  - src: "/images/pubs/2023-glio-fig5-6-tst-errors.png"
    alt: "Tsim Sha Tsui positioning error plots comparing GLIO variants and baselines."
    context: "這些誤差圖量化同一序列，並顯示鬆耦合系統退化的位置以及緊耦合融合帶來的改進。"
    caption: "圖 5 和圖 6：尖沙咀定位誤差和 scan-to-multiscan 幀比較。"
  - src: "/images/pubs/2023-glio-fig7-8-whampoa-results.png"
    alt: "Whampoa table, trajectory, and positioning error plots for GLIO and baseline methods."
    context: "黃埔案例把評估擴展到更長的密集城市駕駛，包含隧道、交通和嚴峻的 GNSS/LiDAR 挑戰。"
    caption: "圖 7 和圖 8：黃埔密集城市駕駛下的軌跡和誤差結果。"
themes:
  - "urban-gnss-reliability"
  - "optimization-estimation"
  - "seamless-pnt-embodied"
tags: []
---

<aside class="translation-stub">本論文以英文發表。完整書目詳情、DOI / PDF 連結請見 <a href="/en/publications/2023-glio-tightly-coupled-gnsslidarimu-integration-for-continu/">英文頁面</a>。</aside>
