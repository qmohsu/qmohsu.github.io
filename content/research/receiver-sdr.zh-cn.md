---
title: "接收机层 GNSS 信号处理与 SDR"
slug: "receiver-sdr"
description: "软件无线电接收机、矢量跟踪、信号质量分析,把退化的卫星信号转化为带明确不确定度的可用测量。"
keywords:
  - "GNSS SDR"
  - "矢量跟踪"
  - "捕获 / 跟踪"
  - "L1 / L5"
  - "直接位置估计"
  - "C/N0"
  - "相关器特征"
  - "接收机层不确定度"
weight: 1
lead: "bing-xu"
aliases:
  - /research/gnss-sdr/
---

可信导航必须在位置估计**之前**就开始。许多城市 GNSS 失效从接收机层就埋下种子 —— 弱信号、相关峰畸变、多径、NLOS、多普勒不一致、跟踪环失锁 —— 下游估计器都无法完全弥补。

<img src="/images/research/blueprint-receiver-sdr.svg" alt="传统标量跟踪接收机输出黑盒测量,弱信号或畸变信号会失锁;IPNL 用软件无线电 + 矢量跟踪输出带明确不确定度的测量。" style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

我们研究接收机层算法,把弱、畸变信号转化为可用的测量、似然与不确定度模型 —— 软件无线电接收机、矢量跟踪、捕获 / 跟踪、GPS L1/L5 处理、直接位置估计、相关器层特征、城市 / 植被 / 高动态环境下的 C/N0 评估。

这是 IPNL 自许立达博士读博起就奠定的基础,代表作是开源 MATLAB 矢量跟踪接收机 [GPS_VT_SDR](/zh-cn/projects/gps-vt-sdr/),由 NOAA GPS Toolbox 收录。
