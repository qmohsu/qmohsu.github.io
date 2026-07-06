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
hero_image: "/images/pubs/2023-glio-urban-trajectory-hero.png"
hero_alt: "GLIO 与其他 GNSS、LiDAR、IMU integration methods 的 3D trajectory 对比。"
hero_caption: "图 4 视觉细节：GNSS、LiDAR 与 IMU integration methods 的 3D trajectory 对比。"
figures:
  - src: "/images/pubs/2023-glio-fig2-lidar-association.png"
    alt: "Scan-to-map and scan-to-multiscan LiDAR association schemes."
    context: "在系统流程之后，这张图解释 LiDAR 约束设计如何支持更平滑且更具全局一致性的优化。"
    caption: "图 2：通过 scan-to-map 和 scan-to-multiscan 方案构建 LiDAR 因子关联。"
  - src: "/images/pubs/2023-glio-fig3-factor-graph.png"
    alt: "Two-stage factor graph structure with GNSS, INS, Doppler, scan-to-map, and scan-to-multiscan factors."
    context: "因子图展示 GNSS、Doppler、IMU 和 LiDAR 约束如何组织到第一阶段和第二阶段优化中。"
    caption: "图 3：第一阶段融合与第二阶段优化的因子图结构。"
  - src: "/images/pubs/2023-glio-fig4-tst-trajectory.png"
    alt: "3D trajectory comparison in the Tsim Sha Tsui sequence."
    context: "结果从尖沙咀序列开始，比较 GLIO 变体和基线方法的轨迹一致性。"
    caption: "图 4：RTKLIB、LIO、LIO-GNSS、GLIO-SS 和 GLIO-DS 在尖沙咀的轨迹比较。"
  - src: "/images/pubs/2023-glio-fig5-6-tst-errors.png"
    alt: "Tsim Sha Tsui positioning error plots comparing GLIO variants and baselines."
    context: "这些误差图量化同一序列，并显示松耦合系统退化的位置以及紧耦合融合带来的改进。"
    caption: "图 5 和图 6：尖沙咀定位误差和 scan-to-multiscan 帧比较。"
  - src: "/images/pubs/2023-glio-fig7-8-whampoa-results.png"
    alt: "Whampoa table, trajectory, and positioning error plots for GLIO and baseline methods."
    context: "黄埔案例把评估扩展到更长的密集城市驾驶，包含隧道、交通和严峻的 GNSS/LiDAR 挑战。"
    caption: "图 7 和图 8：黄埔密集城市驾驶下的轨迹和误差结果。"
themes:
  - "urban-gnss-reliability"
  - "optimization-estimation"
  - "seamless-pnt-embodied"
tags: []
---

<aside class="translation-stub">本论文以英文发表。完整书目详情、DOI / PDF 链接请见 <a href="/en/publications/2023-glio-tightly-coupled-gnsslidarimu-integration-for-continu/">英文页面</a>。</aside>
