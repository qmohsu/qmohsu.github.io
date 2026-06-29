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
featured: true
quartile: Q1
doi: 10.1017/s0373463325000220
pdf: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4CA0FA5382164ABE5B9B6D4A7B4BB4E9/S0373463325000220a.pdf/grid-based-3dma-gnss-with-clustering-and-doppler-velocity-using-factor-graph-optimisation.pdf
code: ''
data: ''
summary: 这篇 grid-based 3DMA GNSS 论文把候选点 clustering、Doppler velocity 与 factor graph optimization 串在一起，用于改善深度城市场景中的 GNSS 定位。
highlights:
- 论文先用 region-growing clustering 分离多峰的 3DMA GNSS 候选位置，再进入 factor graph optimization。
- 实验涵盖 London 静态数据与 Canary Wharf 车载数据，并比较 loosely coupled 与 hybrid-coupled FGO 版本。
hero_image: /images/pubs/2025-grid-3dma-fgo-fig1-flowchart.png
hero_alt: 包含 clustering、Doppler velocity estimation 与 factor graph optimization 的 grid-based 3DMA GNSS 算法流程图。
hero_caption: 图 1：整体流程把 pseudorange 与 Doppler 信息送入候选点分布、region-growing clustering 和 factor graph optimization。
figures:
- src: /images/pubs/2025-grid-3dma-fgo-fig2-region-growing.png
  alt: 用 sampled candidates、score ordering、thresholds 和 clustering results 说明 region-growing 的简化示例。
  context: 在候选点分数计算后，论文用 region growing 把可能的位置分成不同 clusters，而不是强迫所有候选点形成单一解。
  caption: 图 2：用于 clustering 3DMA GNSS sampled candidates 的 region-growing 简化示例。
- src: /images/pubs/2025-grid-3dma-fgo-fig4-hybrid-factor-graph.png
  alt: 包含 state nodes、pseudorange factors、Doppler factors 与 selected 3DMA GNSS cluster factors 的 hybrid-coupled factor graph。
  context: 选出的 cluster 接着成为 hybrid-coupled graph 中的 measurement factor，并与 pseudorange 和 Doppler 信息一起约束定位。
  caption: 图 4：proposed hybrid-coupled 3DMA GNSS approach 的 factor graph 结构。
- src: /images/pubs/2025-grid-3dma-fgo-fig5-skymask-experiment.png
  alt: 显示 building-boundary elevation angle、SNR、LOS satellites 与 NLOS satellites 的实验统计与 sky masks。
  context: 在呈现定位精度前，论文先交代实验中的城市遮蔽程度与卫星可见性条件。
  caption: 图 5：代表性测试点的平均 building-boundary elevation、received SNR 与 sky masks。
- src: /images/pubs/2025-grid-3dma-fgo-fig7-clustering-result.png
  alt: 在困难街谷位置比较 clustered 与 non-clustered 3DMA GNSS FGO 方法的静态定位结果图。
  context: 静态结果显示 clustering 能降低沿街方向误差，并把真值附近的候选 cluster 与其他 cluster 分开。
  caption: 图 7：静态城市测试点的 horizontal errors、map plots 与 multiple-cluster 示例。
- src: /images/pubs/2025-grid-3dma-fgo-fig9-vehicular-summary.png
  alt: 比较不同算法在车载实验中的 RMSE、50th、90th 与 95th percentile 定位误差的柱状图。
  context: 车载结果把静态观察延伸到动态路线，并比较 conventional、grid-filter 与 FGO-based 方法的误差分布。
  caption: 图 9：车载实验中的 RMSE 与 horizontal radial positioning error percentiles。
themes:
- urban-gnss-reliability
- environment-aware-pnt
- optimization-estimation
tags: []
---

<aside class="translation-stub">本论文以英文发表。完整书目详情、DOI / PDF 链接请见 <a href="/en/publications/2025-grid-based-3dma-gnss-with-clustering-and-doppler-velocity-us/">英文页面</a>。</aside>
