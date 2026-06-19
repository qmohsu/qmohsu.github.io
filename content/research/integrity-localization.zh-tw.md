---
title: "完整性、故障偵測與安全可信定位"
slug: "integrity-localization"
description: "同時估計狀態與可信度 —— 故障偵測、非高斯過界、保護等級計算、完整性約束優化,服務於安全關鍵自主系統。"
keywords:
  - "導航完整性"
  - "故障偵測"
  - "保護等級"
  - "過界"
  - "非高斯誤差"
  - "完整性約束 FGO"
  - "安全關鍵定位"
  - "欺騙偵測"
weight: 5
lead: "penggao-yan"
---

對安全關鍵導航而言,僅有精度還不夠:**一個錯誤位置上的確信回答,比一句誠實的「我不知道」更危險**。這條研究方向構建的系統既估計**自己在哪**,也估計**這個答案能否被信任** —— 同時輸出狀態估計與可量化的保護等級。

<img src="/images/research/blueprint-integrity-localization.svg" alt="傳統估計器只輸出位置而沒有可信度;IPNL 同時估計狀態與可信度。" style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

我們研發故障偵測、非高斯誤差過界、保護等級計算與完整性約束優化。代表性工作:*重尾誤差過界的主高斯過界方法*(Yan, Zhong, Hsu, IEEE TAES 2024)、*完整性約束因子圖優化*(Xia, Wen, Hsu, NAVIGATION 2024)、*LiDAR/IMU 整合定位中高斯混合雜訊的故障偵測*(Yan 等, NAVIGATION 2025)。

這條研究方向也是 **2023 年 ION Per Enge 早期成就獎**與 **RGC 研究影響基金 R5009-21**(HK$4.5M, PI, 2021–2026)的技術內核。
