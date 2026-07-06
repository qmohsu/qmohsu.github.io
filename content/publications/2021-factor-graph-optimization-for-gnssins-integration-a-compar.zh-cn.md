---
title: "Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter"
slug: "2021-factor-graph-optimization-for-gnssins-integration-a-compar"
authors:
  - "Wen W."
  - "Pfeifer T."
  - "Bai X."
  - "Hsu L. T."
year: 2021
venue: "NAVIGATION: Journal of the Institute of Navigation"
type: "journal"
cv_number: 80
featured: true
quartile: "Q1"
doi: "10.1002/navi.421"
pdf: ""
code: ""
data: ""
project: "graphgnsslib"
resources:
  - "graphgnsslib-software"
repo: "https://github.com/weisongwen/GraphGNSSLib"
video: "https://www.youtube.com/watch?v=f5bIh96SRsk"
hero_image: "/images/pubs/2021-fgo-urban-vehicle-hero.png"
hero_alt: "用于 GNSS/INS factor graph 实验的测试车辆与 urban canyon 场景。"
hero_caption: "图 3 视觉细节：测试车辆与 urban canyon 实验设置，用于比较 FGO 与 EKF。"
figures:
  - src: "/images/pubs/2021-fgo-fig1-flowchart.png"
    alt: "Flowchart of loosely coupled and tightly coupled GNSS/INS integrations implemented using EKF."
    context: "在提出因子图模型前，论文先建立 EKF 的松耦合与紧耦合基线，作为新 formulation 的比较对象。"
    caption: "图 1（论文）：基于 EKF 实现的松耦合与紧耦合 GNSS/INS 集成流程图。"
  - src: "/images/pubs/2021-fgo-fig3-experiment-setup.png"
    alt: "Experimental vehicle sensor setup and Hong Kong urban canyon test scene."
    context: "在定义估计结构后，论文转向香港车辆实验平台和城市峡谷路线，用于比较 EKF 与 FGO。"
    caption: "图 3（论文）：实验车辆传感器配置和香港城市峡谷测试场景。"
  - src: "/images/pubs/2021-fgo-fig5-tc-results.png"
    alt: "Tightly coupled GNSS/INS trajectory and two-dimensional error results comparing EKF and FGO."
    context: "第一组主要结果把方法转化为轨迹证据，对比紧耦合 EKF 和 FGO 与参考轨迹的差异。"
    caption: "图 5（论文）：紧耦合 GNSS/INS 轨迹以及 EKF 与 FGO 的 2D 定位误差比较。"
  - src: "/images/pubs/2021-fgo-fig8-window-size.png"
    alt: "Two-dimensional positioning error under different FGO window sizes."
    context: "窗口长度分析说明 FGO 的性能为何取决于同时优化多少历史信息。"
    caption: "图 8（论文）：紧耦合 FGO 在不同滑动窗口长度下的 2D 定位误差。"
  - src: "/images/pubs/2021-fgo-fig9-skyview.png"
    alt: "Sky-view images showing line-of-sight and non-line-of-sight satellite visibility at selected epochs."
    context: "这些天空视图时刻通过展示困难时段的 LOS/NLOS 卫星条件来解释窗口长度结果。"
    caption: "图 9（论文）：鱼眼天空视图和所选时刻的 LOS/NLOS 卫星可见性。"
  - src: "/images/pubs/2021-fgo-fig10-pseudorange-gmm.png"
    alt: "GPS and BeiDou pseudorange error histograms with fitted Gaussian mixture models."
    context: "伪距直方图把定位表现与城市测量噪声的非高斯特性联系起来。"
    caption: "图 10（论文）：GPS 和北斗伪距误差直方图及对应的高斯混合模型拟合。"
  - src: "/images/pubs/2021-fgo-fig13-computation-time.png"
    alt: "Computational time comparison between tightly coupled FGO and tightly coupled iSAM."
    context: "最后的比较检查用 FGO 与 iSAM 求解紧耦合图优化的实际计算代价。"
    caption: "图 13（论文）：紧耦合 FGO 与紧耦合 iSAM 的计算时间比较。"
themes:
  - "urban-gnss-reliability"
  - "optimization-estimation"
tags: []
---

<aside class="translation-stub">本论文以英文发表。完整书目详情、DOI / PDF 链接请见 <a href="/en/publications/2021-factor-graph-optimization-for-gnssins-integration-a-compar/">英文页面</a>。</aside>
