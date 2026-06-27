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
summary: Integrity-constrained FGO 通过 switchable pseudorange 与 chi-square-test factors 重新加权故障 GNSS measurements，同时保留 protection-level calculation 所需的 geometry。
highlights:
- factor graph 同时包含 switchable pseudorange、switch prior、switch reliable 与 chi-square test factors。
- UrbanNav 实验把方法连到真实中等与严苛城市场景，包含 HPE、HPL、skyplot 与 trajectory results。
hero_image: /images/pubs/2024-integrity-fgo-fig1-method-flowchart.png
hero_alt: 包含 switchable pseudorange modeling、chi-square testing、measurement reweighting 与 protection-level calculation 的 integrity-constrained factor graph optimization 流程图。
hero_caption: 图 1：proposed method 连接 switchable factors、chi-square testing、measurement reweighting 与 HPL calculation。
figures:
- src: /images/pubs/2024-integrity-fgo-fig2-factor-graph.png
  alt: 包含 satellite nodes、switch variables、pseudorange factors、switch priors、switch reliable factors 与 chi-square test factor 的 integrity-constrained factor graph。
  context: 流程图落到 factor graph 后，方法跨 epochs 估计 switch variables，而不是直接移除卫星。
  caption: 图 2：proposed integrity-constrained factor graph 的 graph structure。
- src: /images/pubs/2024-integrity-fgo-fig6-hpe-hpl.png
  alt: 在 bias-injection period 中比较 FGO、RAIM-FGO、SW-FGO 与 SWFDE-FGO 的 HPE 与 HPL 曲线。
  context: controlled bias test 显示 chi-square-test factor 在 fault period 中如何影响 horizontal position error 与 protection level。
  caption: 图 6：四种方法在 injected satellite biases 期间的 HPE 与 HPL。
- src: /images/pubs/2024-integrity-fgo-fig7-skyplot-switch-values.png
  alt: 比较 FGO、RAIM-FGO、SW-FGO 与 SWFDE-FGO 在 epoch A 的 switch values skyplots。
  context: skyplot 说明核心设计：faulty satellites 通过 switch values 被降权，以保留有用 geometry。
  caption: 图 7：四种方法在 epoch A 的 switch values skyplot。
- src: /images/pubs/2024-integrity-fgo-fig8-urbannav-trajectories.png
  alt: UrbanNav-Medium 与 UrbanNav-Harsh datasets 的 bird's-eye-view trajectories。
  context: 真实 UrbanNav trajectories 把评估从 controlled bias injection 推进到中等与严苛的城市路线。
  caption: 图 8：UrbanNav-Medium 与 UrbanNav-Harsh datasets 的 bird's-eye-view trajectories。
- src: /images/pubs/2024-integrity-fgo-fig9-urban-medium-results.png
  alt: 不同算法的 snapshot test statistic、HPE 与 HPL UrbanNav result curves。
  context: UrbanNav result curves 把 trajectory behavior 接到用于方法比较的 integrity metrics。
  caption: 图 9：UrbanNav experiment 中的 snapshot test statistic、HPE 与 HPL。
- src: /images/pubs/2024-integrity-fgo-fig13-pseudorange-error-distribution.png
  alt: FGO、SW-FGO 与 SWFDE-FGO 的 switchable pseudorange errors distribution。
  context: pseudorange-error distribution 说明 switch values 如何收窄或重塑 residuals，同时保留 geometry information。
  caption: 图 13：FGO、SW-FGO 与 SWFDE-FGO 的 switchable pseudorange error distribution。
themes:
- urban-gnss-reliability
- optimization-estimation
- integrity-localization
tags: []
---

<aside class="translation-stub">本论文以英文发表。完整书目详情、DOI / PDF 链接请见 <a href="/en/publications/2024-integrity-constrained-factor-graph-optimization-for-gnss-pos/">英文页面</a>。</aside>
