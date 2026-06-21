---
title: "环境感知与 3D 地图辅助 PNT"
slug: "environment-aware-pnt"
description: "用 3D 城市模型、LiDAR 地图、天空可视性、光线追踪、数字孪生,把城市环境从障碍转化为导航的先验信息。"
keywords:
  - "3D 地图辅助 GNSS"
  - "3DMA GNSS"
  - "3D 城市模型"
  - "LiDAR 地图"
  - "光线追踪"
  - "数字孪生"
  - "天空可视性"
  - "Skymask 匹配"
  - "环境感知定位"
weight: 3
lead: "guohao-zhang"
aliases:
  - /research/3d-mapping-aided/
---

城市本身成为导航系统的一部分。我们用 3D 城市模型、LiDAR 地图、天空可视性、光线追踪与数字孪生预测 GNSS 卫星可见性、识别 NLOS 与多径、提升精度并评估可靠性。

<img src="/images/research/blueprint-environment-aware-pnt.svg" alt="传统 GNSS 把城市视作障碍,无法分辨哪颗卫星是 NLOS;IPNL 用 3D 城市模型 + LiDAR 地图 + 光线追踪预测 NLOS / 多径,得到经修正的可信定位。" style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

城市环境不仅是障碍,更可以变成**可信导航的先验信息**。这条研究方向源自许立达教授在东京的博士后工作,以及由他创办的 ION/IAG 亚洲城市峡谷定位导航工作组,也是 **US12123961B2 专利**(*3D LiDAR 辅助 GNSS NLOS 检测与修正*)与长期华为 3DMA GNSS 移动端合作的技术内核。
