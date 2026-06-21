---
title: "完好性、故障检测与安全可信定位"
slug: "integrity-localization"
description: "既估计状态、也估计可信度 —— 故障检测、非高斯过界、保护级计算、完好性约束优化,服务于安全关键自主系统。"
keywords:
  - "导航完好性"
  - "故障检测"
  - "保护级"
  - "过界"
  - "非高斯误差"
  - "完好性约束 FGO"
  - "安全关键定位"
  - "欺骗检测"
weight: 5
lead: "penggao-yan"
---

对安全关键导航而言,仅有精度还不够:**一个错误位置上的确信回答,比一句诚实的"我不知道"更危险**。这条研究方向构建的系统既估计**自己在哪**,也估计**这个答案能否被信任** —— 同时输出状态估计与可量化的保护级。

<img src="/images/research/blueprint-integrity-localization.svg" alt="传统估计器只输出位置而没有可信度,对安全关键自主系统极其危险;IPNL 同时估计状态与可信度 —— 故障检测、非高斯过界、保护级 —— 输出可用于安全决策的结果。" style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

我们研发故障检测、非高斯误差过界、保护级计算与完好性约束优化。代表性工作:*重尾误差过界的主高斯过界方法*(Yan, Zhong, Hsu, IEEE TAES 2024)、*完好性约束因子图优化*(Xia, Wen, Hsu, NAVIGATION 2024)、*LiDAR/IMU 集成定位中高斯混合噪声的故障检测*(Yan 等, NAVIGATION 2025)。

这条研究方向也是 **2023 年 ION Per Enge 早期成就奖**与 **RGC 研究影响基金 R5009-21**(HK$4.43M 总额(其中 RGC HK$3.1M),项目协调人,2021–2026)的技术内核。
