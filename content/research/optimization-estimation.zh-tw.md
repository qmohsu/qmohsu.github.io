---
title: "基於優化的估計與因子圖"
slug: "optimization-estimation"
description: "因子圖優化作為 GNSS / INS / 載波相位 / 都卜勒 / 地圖 / 感知 / 完整性的統一框架。"
keywords:
  - "因子圖優化"
  - "FGO"
  - "GNSS/INS"
  - "RTK"
  - "PPP-RTK"
  - "平滑"
  - "非線性優化"
  - "穩健估計"
  - "感測器融合"
weight: 4
lead: "weisong-wen"
video: "https://www.youtube.com/watch?v=f5bIh96SRsk"
aliases:
  - /research/factor-graph-optimization/
---

因子圖優化是連接訊號、測量、地圖、感測器與完整性的數學引擎。我們用它作為統一框架 —— 讓導航系統在時間維度推理、融合異質測量、比經典純濾波管線更靈活地處理離群值。

<img src="/images/research/blueprint-optimization-estimation.svg" alt="EKF 把所有歷史壓縮到單一當前狀態、單點線性化;IPNL 用 FGO 聯合優化時間窗內的狀態序列。" style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

奠基論文 *Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter*(Wen, Pfeifer, Bai, Hsu, NAVIGATION 2021)被評為 **2024 年 NAVIGATION 期刊最高引用論文**。後續工作把 FGO 拓展至完整性約束估計、智慧型手機僅 IMU 室內 SLAM(IEEE TAES 2024)、3D 視覺輔助 GNSS RTK(NAVIGATION 2023)、自監督權重學習(AutoW, ION GNSS+ 2024)。開源庫 [GraphGNSSLib](/zh-tw/projects/graphgnsslib/) 是這條研究方向面向社群的代表作。
