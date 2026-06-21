---
title: "GraphGNSSLib (因子图 GNSS 库)"
slug: "graphgnsslib"
description: "基于因子图优化的开源 GNSS 定位、RTK 与 GNSS/INS 研究平台 (C/C++)。"
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

GraphGNSSLib 是一个开源 C/C++ 平台,用于基于因子图优化 (FGO) 的 GNSS 定位、RTK 与 GNSS/INS 研究。它把原始 GNSS 数据(伪距、多普勒、载波相位、整周模糊度解算)连接到非线性优化,以及基于 ROS 的机器人系统。

<strong>为什么重要。</strong> GraphGNSSLib 给导航与机器人研究人员<strong>一条从 GNSS 测量到现代优化估计的实用桥梁</strong>,用一个能融合异质测量、更灵活处理离群值、跨时间推理的统一框架,替代经典 EKF 管线。

<strong>产出。</strong> [GitHub 仓库](https://github.com/weisongwen/GraphGNSSLib)、代码示例、ROS 演示、与 [UrbanNav](/zh-cn/projects/urbannav/) 的集成,以及奠基性论文 *Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter*(Wen, Pfeifer, Bai, Hsu)—— <strong>2024 年 NAVIGATION 期刊最高引用论文奖</strong>。
