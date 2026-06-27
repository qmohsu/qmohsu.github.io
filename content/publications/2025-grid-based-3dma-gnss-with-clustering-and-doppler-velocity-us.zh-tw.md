---
title: Grid-based 3DMA GNSS with clustering and Doppler velocity using factor graph optimisation
slug: 2025-grid-based-3dma-gnss-with-clustering-and-doppler-velocity-us
authors:
- Ng, H. F.
- Zhong, Q.
- Groves, P.
- Hsu, L. T.
year: 2025
venue: The Journal of Navigation
type: journal
cv_number: 6
featured: false
quartile: Q1
doi: 10.1017/s0373463325000220
pdf: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4CA0FA5382164ABE5B9B6D4A7B4BB4E9/S0373463325000220a.pdf/grid-based-3dma-gnss-with-clustering-and-doppler-velocity-using-factor-graph-optimisation.pdf
code: ''
data: ''
summary: 這篇 grid-based 3DMA GNSS 論文把候選點 clustering、Doppler velocity 與 factor graph optimization 串在一起，用於改善深度城市場景中的 GNSS 定位。
highlights:
- 論文先以 region-growing clustering 分離多峰的 3DMA GNSS 候選位置，再進入 factor graph optimization。
- 實驗涵蓋 London 靜態資料與 Canary Wharf 車載資料，並比較 loosely coupled 與 hybrid-coupled FGO 版本。
hero_image: /images/pubs/2025-grid-3dma-fgo-fig1-flowchart.png
hero_alt: 包含 clustering、Doppler velocity estimation 與 factor graph optimization 的 grid-based 3DMA GNSS 演算法流程圖。
hero_caption: 圖 1：整體流程把 pseudorange 與 Doppler 資訊送入候選點分布、region-growing clustering 和 factor graph optimization。
figures:
- src: /images/pubs/2025-grid-3dma-fgo-fig2-region-growing.png
  alt: 以 sampled candidates、score ordering、thresholds 和 clustering results 說明 region-growing 的簡化範例。
  context: 在候選點分數計算後，論文用 region growing 把可能的位置分成不同 clusters，而不是強迫所有候選點形成單一解。
  caption: 圖 2：用於 clustering 3DMA GNSS sampled candidates 的 region-growing 簡化範例。
- src: /images/pubs/2025-grid-3dma-fgo-fig4-hybrid-factor-graph.png
  alt: 包含 state nodes、pseudorange factors、Doppler factors 與 selected 3DMA GNSS cluster factors 的 hybrid-coupled factor graph。
  context: 選出的 cluster 接著成為 hybrid-coupled graph 中的 measurement factor，並與 pseudorange 和 Doppler 資訊一起約束定位。
  caption: 圖 4：proposed hybrid-coupled 3DMA GNSS approach 的 factor graph 結構。
- src: /images/pubs/2025-grid-3dma-fgo-fig5-skymask-experiment.png
  alt: 顯示 building-boundary elevation angle、SNR、LOS satellites 與 NLOS satellites 的實驗統計與 sky masks。
  context: 在呈現定位精度前，論文先交代實驗中的城市遮蔽程度與衛星可見性條件。
  caption: 圖 5：代表性測試點的平均 building-boundary elevation、received SNR 與 sky masks。
- src: /images/pubs/2025-grid-3dma-fgo-fig7-clustering-result.png
  alt: 在困難街谷位置比較 clustered 與 non-clustered 3DMA GNSS FGO 方法的靜態定位結果圖。
  context: 靜態結果顯示 clustering 能降低沿街方向誤差，並把真值附近的候選 cluster 與其他 cluster 分開。
  caption: 圖 7：靜態城市測試點的 horizontal errors、map plots 與 multiple-cluster 範例。
- src: /images/pubs/2025-grid-3dma-fgo-fig9-vehicular-summary.png
  alt: 比較不同演算法在車載實驗中的 RMSE、50th、90th 與 95th percentile 定位誤差的柱狀圖。
  context: 車載結果把靜態觀察延伸到動態路線，並比較 conventional、grid-filter 與 FGO-based 方法的誤差分布。
  caption: 圖 9：車載實驗中的 RMSE 與 horizontal radial positioning error percentiles。
themes:
- urban-gnss-reliability
- environment-aware-pnt
- optimization-estimation
tags: []
---

<aside class="translation-stub">本論文以英文發表。完整書目詳情、DOI / PDF 連結請見 <a href="/en/publications/2025-grid-based-3dma-gnss-with-clustering-and-doppler-velocity-us/">英文頁面</a>。</aside>
