---
title: "GraphGNSSLib (因子圖 GNSS 庫)"
slug: "graphgnsslib"
description: "基於因子圖優化的開源 GNSS 定位、RTK 與 GNSS/INS 研究平台 (C/C++)。"
category: "open-platform"
status: "active"
flagship: true
start_date: 2020
repo: "https://github.com/weisongwen/GraphGNSSLib"
video: "https://www.youtube.com/playlist?list=PLw8Oypadak9PjlbVn8tpnlP2Xs-cNHLYj"
themes: ["urban-gnss-reliability", "environment-aware-pnt", "optimization-estimation", "integrity-localization", "seamless-pnt-embodied"]
people: ["weisong-wen"]
tags: ["factor graph", "GNSS", "optimization", "C++", "ROS", "open-source"]
weight: 3
---

GraphGNSSLib 是一個開源 C/C++ 平台,用於基於因子圖優化 (FGO) 的 GNSS 定位、RTK 與 GNSS/INS 研究。它把原始 GNSS 資料(偽距、都卜勒、載波相位、整週模糊度解算)連接到非線性優化,以及基於 ROS 的機器人系統。

<strong>為什麼重要。</strong> GraphGNSSLib 給導航與機器人研究人員<strong>一條從 GNSS 測量到現代優化估計的實用橋樑</strong>,用一個能融合異質測量、更靈活處理離群值、跨時間推理的統一框架,替代經典 EKF 管線。

<strong>產出。</strong> [GitHub 倉庫](https://github.com/weisongwen/GraphGNSSLib)、程式碼範例、ROS 示範、與 [UrbanNav](/zh-tw/projects/urbannav/) 的整合,以及奠基性論文 *Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter*(Wen, Pfeifer, Bai, Hsu)—— <strong>2024 年 NAVIGATION 期刊最高引用論文獎</strong>。
