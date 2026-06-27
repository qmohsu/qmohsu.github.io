---
title: Integrity-Constrained Factor Graph Optimization for GNSS Positioning in Urban Canyons
slug: 2024-integrity-constrained-factor-graph-optimization-for-gnss-pos
authors:
- Xia, X.
- Wen, W.
- Hsu, L. T.
year: 2024
venue: 'NAVIGATION: Journal of the Institute of Navigation'
type: journal
cv_number: 15
featured: false
quartile: Q1
doi: 10.33012/navi.660
pdf: https://ira.lib.polyu.edu.hk/bitstream/10397/111854/1/navi.660.full.pdf
code: ''
data: ''
summary: Integrity-constrained FGO 透過 switchable pseudorange 與 chi-square-test factors 重新加權故障 GNSS measurements，同時保留 protection-level calculation 所需的 geometry。
highlights:
- factor graph 同時包含 switchable pseudorange、switch prior、switch reliable 與 chi-square test factors。
- UrbanNav 實驗把方法連到真實中等與嚴苛城市場景，包含 HPE、HPL、skyplot 與 trajectory results。
hero_image: /images/pubs/2024-integrity-fgo-fig1-method-flowchart.png
hero_alt: 包含 switchable pseudorange modeling、chi-square testing、measurement reweighting 與 protection-level calculation 的 integrity-constrained factor graph optimization 流程圖。
hero_caption: 圖 1：proposed method 連接 switchable factors、chi-square testing、measurement reweighting 與 HPL calculation。
figures:
- src: /images/pubs/2024-integrity-fgo-fig2-factor-graph.png
  alt: 包含 satellite nodes、switch variables、pseudorange factors、switch priors、switch reliable factors 與 chi-square test factor 的 integrity-constrained factor graph。
  context: 流程圖落到 factor graph 後，方法跨 epochs 估計 switch variables，而不是直接移除衛星。
  caption: 圖 2：proposed integrity-constrained factor graph 的 graph structure。
- src: /images/pubs/2024-integrity-fgo-fig6-hpe-hpl.png
  alt: 在 bias-injection period 中比較 FGO、RAIM-FGO、SW-FGO 與 SWFDE-FGO 的 HPE 與 HPL 曲線。
  context: controlled bias test 顯示 chi-square-test factor 在 fault period 中如何影響 horizontal position error 與 protection level。
  caption: 圖 6：四種方法在 injected satellite biases 期間的 HPE 與 HPL。
- src: /images/pubs/2024-integrity-fgo-fig7-skyplot-switch-values.png
  alt: 比較 FGO、RAIM-FGO、SW-FGO 與 SWFDE-FGO 在 epoch A 的 switch values skyplots。
  context: skyplot 說明核心設計：faulty satellites 透過 switch values 被降權，以保留有用 geometry。
  caption: 圖 7：四種方法在 epoch A 的 switch values skyplot。
- src: /images/pubs/2024-integrity-fgo-fig8-urbannav-trajectories.png
  alt: UrbanNav-Medium 與 UrbanNav-Harsh datasets 的 bird's-eye-view trajectories。
  context: 真實 UrbanNav trajectories 把評估從 controlled bias injection 推進到中等與嚴苛的城市路線。
  caption: 圖 8：UrbanNav-Medium 與 UrbanNav-Harsh datasets 的 bird's-eye-view trajectories。
- src: /images/pubs/2024-integrity-fgo-fig9-urban-medium-results.png
  alt: 不同演算法的 snapshot test statistic、HPE 與 HPL UrbanNav result curves。
  context: UrbanNav result curves 把 trajectory behavior 接到用於方法比較的 integrity metrics。
  caption: 圖 9：UrbanNav experiment 中的 snapshot test statistic、HPE 與 HPL。
- src: /images/pubs/2024-integrity-fgo-fig13-pseudorange-error-distribution.png
  alt: FGO、SW-FGO 與 SWFDE-FGO 的 switchable pseudorange errors distribution。
  context: pseudorange-error distribution 說明 switch values 如何收窄或重塑 residuals，同時保留 geometry information。
  caption: 圖 13：FGO、SW-FGO 與 SWFDE-FGO 的 switchable pseudorange error distribution。
themes:
- urban-gnss-reliability
- optimization-estimation
- integrity-localization
tags: []
---

<aside class="translation-stub">本論文以英文發表。完整書目詳情、DOI / PDF 連結請見 <a href="/en/publications/2024-integrity-constrained-factor-graph-optimization-for-gnss-pos/">英文頁面</a>。</aside>
