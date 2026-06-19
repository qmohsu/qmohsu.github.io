---
title: "UrbanNav (城市导航数据集)"
slug: "urbannav"
description: "面向城市导航算法基准测试的开源多传感器数据集。"
category: "open-platform"
status: "active"
flagship: true
start_date: 2019
funding: "Google, RGC, and other sources"
repo: "https://github.com/IPNL-POLYU/UrbanNavDataset"
videos:
  - "https://www.youtube.com/watch?v=V94PAkkpwWs"
  - "https://www.youtube.com/watch?v=b1-lKmUttzc"
  - "https://www.youtube.com/watch?v=hQu8npoGad8"
themes: ["urban-gnss-reliability", "environment-aware-pnt", "optimization-estimation", "seamless-pnt-embodied"]
people: ["weisong-wen", "guohao-zhang", "hoi-fung-ng"]
tags: ["dataset", "benchmark", "GNSS", "LiDAR", "IMU", "open-source"]
weight: 1
---

UrbanNav 是一个开源多传感器基准数据集,服务于在密集城市环境下测试导航算法。它提供来自亚洲城市峡谷的原始 GNSS、IMU、LiDAR、相机、真值数据 —— 支持 GNSS 定位、传感器融合、SLAM、完好性监测等方向的研究。

<strong>为什么重要。</strong> 真实城市导航失败的原因是 GNSS、感知、低成本传感器<strong>一起</strong>失效。UrbanNav 给社区提供了一个共享的"联合失败"基准,被定位导航社区广泛采纳为参考数据集。

<strong>产出。</strong> 开源数据集、[GitHub 仓库](https://github.com/IPNL-POLYU/UrbanNavDataset)、基准论文(NAVIGATION 2023;ION GNSS+ 2021)、教程,以及与 [GraphGNSSLib](/zh-cn/projects/graphgnsslib/) 因子图平台的集成。
