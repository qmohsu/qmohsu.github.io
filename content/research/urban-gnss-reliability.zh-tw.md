---
title: "城市 GNSS 可靠性與訊號誤差建模"
slug: "urban-gnss-reliability"
description: "建模 GNSS 測量在密集城市中如何失效。"
keywords:
  - "城市 GNSS"
  - "多徑"
  - "NLOS"
  - "衍射"
  - "都卜勒一致性"
  - "重尾誤差"
  - "測量可靠性"
  - "不確定度建模"
weight: 2
lead: "li-ta-hsu"
video: "https://www.youtube.com/watch?v=Ys4xCbN9h1s"
aliases:
  - /research/urban-gnss/
---

密集城市不是 GNSS 的例外場景,而是它的壓力測試。我們研究 GNSS 測量如何失效 —— NLOS、多徑、衍射、都卜勒畸變、重尾誤差 —— 並在它們污染下游估計**之前**,在測量層偵測並量化這些失效。

<img src="/images/research/blueprint-urban-gnss-reliability.svg" alt="傳統 GNSS 等價對待所有測量;IPNL 在訊號層建模可靠性。" style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

目標不僅是修正「壞測量」,更要**建模它們的可靠性** —— 讓導航管線的其餘部分知道何時可以信任。這條方向是 [環境感知](/zh-tw/research/environment-aware-pnt/)、[優化估計](/zh-tw/research/optimization-estimation/) 和 [完整性](/zh-tw/research/integrity-localization/) 三條方向在測量層的共同基礎。
