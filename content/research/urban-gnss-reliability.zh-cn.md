---
title: "城市 GNSS 可靠性与信号误差建模"
slug: "urban-gnss-reliability"
description: "建模 GNSS 测量在密集城市环境中如何失效 —— NLOS、多径、衍射、重尾误差 —— 让下游估计与完好性系统知道何时可信。"
keywords:
  - "城市 GNSS"
  - "多径"
  - "NLOS"
  - "衍射"
  - "多普勒一致性"
  - "重尾误差"
  - "测量可靠性"
  - "不确定度建模"
weight: 2
lead: "li-ta-hsu"
video: "https://www.youtube.com/watch?v=Ys4xCbN9h1s"
aliases:
  - /research/urban-gnss/
---

密集城市不是 GNSS 的例外场景,而是它的压力测试。我们研究 GNSS 测量如何失效 —— NLOS、多径、衍射、多普勒畸变、重尾误差 —— 并在它们污染下游估计**之前**,在测量层检测并量化这些失效。

<img src="/images/research/blueprint-urban-gnss-reliability.svg" alt="传统 GNSS 等价对待所有测量,城市 NLOS / 多径 / 衍射污染定位结果;IPNL 在信号层建模可靠性,让每个测量都带可信度标签。" style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

目标不仅是修正"坏测量",更要**建模它们的可靠性** —— 让导航管线的其余部分知道何时可以信任。这条方向是 [环境感知](/zh-cn/research/environment-aware-pnt/)、[优化估计](/zh-cn/research/optimization-estimation/) 和 [完好性](/zh-cn/research/integrity-localization/) 三条方向在测量层的共同基础。
