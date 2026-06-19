---
title: "接收機層 GNSS 訊號處理與 SDR"
slug: "receiver-sdr"
description: "軟體無線電接收機、向量追蹤、訊號品質分析。"
keywords:
  - "GNSS SDR"
  - "向量追蹤"
  - "捕獲 / 追蹤"
  - "L1 / L5"
  - "直接位置估計"
  - "C/N0"
  - "相關器特徵"
  - "接收機層不確定度"
weight: 1
lead: "bing-xu"
aliases:
  - /research/gnss-sdr/
---

可信導航必須在位置估計**之前**就開始。許多城市 GNSS 失效從接收機層就埋下種子 —— 弱訊號、相關峰畸變、多徑、NLOS、都卜勒不一致、追蹤環失鎖 —— 下游估計器都無法完全彌補。

<img src="/images/research/blueprint-receiver-sdr.svg" alt="傳統純量追蹤接收機輸出黑盒測量;IPNL 用軟體無線電 + 向量追蹤輸出帶不確定度的測量。" style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

我們研究接收機層演算法,把弱、畸變訊號轉化為可用的測量、似然與不確定度模型 —— 軟體無線電接收機、向量追蹤、捕獲 / 追蹤、GPS L1/L5 處理、直接位置估計、相關器層特徵、城市 / 植被 / 高動態環境下的 C/N0 評估。

這是 IPNL 自許立達博士讀博起就奠定的基礎,代表作是開源 MATLAB 向量追蹤接收機 [GPS_VT_SDR](/zh-tw/projects/gps-vt-sdr/),由 NOAA GPS Toolbox 收錄。
