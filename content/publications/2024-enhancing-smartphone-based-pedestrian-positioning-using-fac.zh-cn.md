---
title: 'Enhancing Smartphone-based Pedestrian Positioning: Using Factor Graph Optimization with Indoor/Outdoor Detection for 3DMA GNSS/Visual-Inertial State Estimation'
slug: 2024-enhancing-smartphone-based-pedestrian-positioning-using-fac
authors:
- Ho, H. Y.
- Ng, H. F.
- Wen, W.
- Gu, Y.
- Hsu, L. T.
year: 2024
venue: Journal of Data Science and Intelligent Systems
type: journal
cv_number: 11
featured: true
quartile: Q?
doi: 10.47852/bonviewjdsis42022961
pdf: https://ojs.bonviewpress.com/index.php/jdsis/article/download/2961/1145/24389
code: https://github.com/queenie-ho/3DMAGNSSVINS-IOFGO
data: ''
summary: 这篇论文在 factor graph optimization 中用 indoor/outdoor switching factor 融合 smartphone 3DMA GNSS 与 visual-inertial estimates。
highlights:
- 系统用 SVM-based indoor/outdoor detection 决定 GNSS 与 VINS measurements 在 graph 中的权重。
- 香港行人实验在 indoor/outdoor transitions 下，把 smartphone trajectories 与 LIO-SAM ground truth 进行比较。
hero_image: "/images/pubs/2024-smartphone-fgo-field-trajectory-hero.png"
hero_alt: "用于 indoor/outdoor pedestrian positioning 的 LIO-SAM ground-truth point clouds、smartphone 实景图与 trajectory comparison。"
hero_caption: "图 5、6、14 视觉组合：LIO-SAM ground truth、field image matching 与 trajectory comparison。"
figures:
- src: /images/pubs/2024-smartphone-fgo-fig3-io-svm-flow.png
  alt: 使用 training data、validation data、GNSS features 与 test data 的 indoor/outdoor classification SVM flowchart。
  context: SVM classifier 把 GNSS features 转成 indoor/outdoor label，后续用来控制 switching factor。
  caption: 图 3：indoor/outdoor classification 的 SVM flowchart。
- src: /images/pubs/2024-smartphone-fgo-fig4-factor-graph.png
  alt: 连接 VINS factors、3DMA GNSS factors、switching factors 与 state nodes 的 factor graph。
  context: factor graph 说明 VINS、3DMA GNSS 与 indoor/outdoor switching factor 在 optimization problem 中如何汇合。
  caption: 图 4：用 indoor/outdoor switching factor loosely coupling GNSS 与 VINS 的 FGO structure。
- src: /images/pubs/2024-smartphone-fgo-fig5-experiment-trajectories.png
  alt: experiment trajectories A、B 与 C 的 Google Earth views。
  context: experiment routes 定义了后续比较算法所需的 indoor/outdoor transition scenarios。
  caption: 图 5：trajectories A、B 与 C 的 Google Earth views。
- src: /images/pubs/2024-smartphone-fgo-fig6-lio-sam-ground-truth.png
  alt: trajectories A、B 与 C 的 LIO-SAM ground-truth maps。
  context: LIO-SAM ground truth 为后面的 trajectory comparisons 与 error plots 提供基准。
  caption: 图 6：LIO-SAM 生成的 trajectories A、B 与 C ground truth。
- src: /images/pubs/2024-smartphone-fgo-fig13-b2-error.png
  alt: 含 3DMA GNSS standard deviation 与 indoor/outdoor indicator 的 B2 absolute positioning error plot。
  context: B2 error plot 凸显 transition period：加入 indoor/outdoor switch 后，可抑制没有 switch 的方法中出现的 error growth。
  caption: 图 13：含 estimated 3DMA GNSS standard deviation 与 IO indicator 的 B2 absolute positioning error comparison。
- src: /images/pubs/2024-smartphone-fgo-fig14-b2-trajectory.png
  alt: B2 trajectory comparison，包含 GT、VINSMONO、3DMA GNSS、3DMA GNSS/VINS FGO 与 3DMA GNSS/VINS-IO FGO。
  context: 配对的 trajectory plot 从空间上呈现同一件事：switching version 在 transition 期间更贴近 ground truth。
  caption: 图 14：B2 trajectory comparison。
themes:
- optimization-estimation
- seamless-pnt-embodied
tags: []
---

<aside class="translation-stub">本论文以英文发表。完整书目详情、DOI / PDF 链接请见 <a href="/en/publications/2024-enhancing-smartphone-based-pedestrian-positioning-using-fac/">英文页面</a>。</aside>
