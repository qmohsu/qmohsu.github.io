---
title: "基于优化的估计与因子图"
slug: "optimization-estimation"
description: "因子图优化作为 GNSS / INS / 载波相位 / 多普勒 / 地图 / 感知 / 完好性的统一框架,跨异质测量在时间维度上推理。"
keywords:
  - "因子图优化"
  - "FGO"
  - "GNSS/INS"
  - "RTK"
  - "PPP-RTK"
  - "平滑"
  - "非线性优化"
  - "稳健估计"
  - "传感器融合"
weight: 4
lead: "weisong-wen"
video: "https://www.youtube.com/watch?v=f5bIh96SRsk"
aliases:
  - /research/factor-graph-optimization/
---

因子图优化是连接信号、测量、地图、传感器与完好性的数学引擎。我们用它作为统一框架 —— 让导航系统在时间维度推理、融合异质测量、比经典纯滤波管线更灵活地处理离群值。

<img src="/images/research/blueprint-optimization-estimation.svg" alt="EKF 把所有历史压缩到单一当前状态、单点线性化,处理离群值很差;IPNL 用 FGO 联合优化时间窗内的状态序列,稳健融合异质测量。" style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

奠基论文 *Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter*(Wen, Pfeifer, Bai, Hsu, NAVIGATION 2021)被评为 **2024 年 NAVIGATION: Journal of the Institute of Navigation 最高引用论文**。后续工作把 FGO 拓展至完好性约束估计、智能手机仅 IMU 室内 SLAM(IEEE TAES 2024)、3D 视觉辅助 GNSS RTK(NAVIGATION 2023)、自监督权重学习(AutoW, ION GNSS+ 2024)。开源库 [GraphGNSSLib](/zh-cn/projects/graphgnsslib/) 是这条研究方向面向社区的代表作。
