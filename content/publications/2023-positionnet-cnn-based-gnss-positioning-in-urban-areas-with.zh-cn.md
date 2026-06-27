---
title: "PositionNet: CNN-based GNSS positioning in urban areas with residual maps"
slug: "2023-positionnet-cnn-based-gnss-positioning-in-urban-areas-with"
authors:
  - "Xu, P."
  - "Zhang, G."
  - "Yang, B."
  - "Hsu, L. T."
year: 2023
venue: "Applied Soft Computing"
type: "journal"
cv_number: 41
featured: true
quartile: "Q1"
doi: "10.2139/ssrn.4194604"
pdf: ""
code: ""
data: ""
hero_image: "/images/pubs/2023-positionnet-fig3-network.png"
hero_alt: "Network structure of PositionNet with encoder, decoder, mean pooling, and residual connection."
hero_caption: "图 3（PositionNet 论文）：把残差图转换为定位热力图的 CNN 架构。"
figures:
  - src: "/images/pubs/2023-positionnet-fig1-res-map-geometry.png"
    alt: "Geometry of the range residual map with satellite direction, sampling location, and user location."
    context: "在 CNN 架构之前，论文先定义卫星距离残差如何变成围绕最小二乘解的图像式输入。"
    caption: "图 1：PositionNet 输入残差图的几何关系。"
  - src: "/images/pubs/2023-positionnet-fig2-sdres-map.png"
    alt: "Single-differenced residual map layers intersecting at the user location."
    context: "SDRes 图通过与主卫星做差来去除接收机钟差，为网络形成更清晰的位置模式。"
    caption: "图 2：当多个 LOS 卫星一致时，SDRes 图会强化位置模式。"
  - src: "/images/pubs/2023-positionnet-fig4-validation-map.png"
    alt: "Validation and testing PositionNet results over Tsim Sha Tsui, Whampoa, Mong Kok, and Kowloon Bay maps."
    context: "第一组结果把 PositionNet 输出映射到多个城市区域，展示其在单一场景之外的验证和测试表现。"
    caption: "图 4：显示在城市地图上的验证和测试结果。"
  - src: "/images/pubs/2023-positionnet-fig5-case1-solution.png"
    alt: "Case 1 PositionNet solution map and output heat map."
    context: "案例研究进一步放大一个最小二乘误差较大的样例，展示输出热力图如何指向修正后的位置。"
    caption: "图 5：案例 1 的定位解和输出热力图。"
  - src: "/images/pubs/2023-positionnet-fig6-case1-saliency.png"
    alt: "Case 1 saliency map grid showing residual maps, SDRes maps, C/N0 maps, and saliency responses."
    context: "显著性图解释该案例中哪些卫星残差、SDRes 和 C/N0 图层影响了网络判断。"
    caption: "图 6：案例 1 的显著性图，解释哪些卫星残差模式影响了网络。"
  - src: "/images/pubs/2023-positionnet-fig11-saliency-weighting.png"
    alt: "Scatter plots of saliency map weighting versus pseudorange error for validation and testing data."
    context: "汇总显著性图把案例级解释扩展到验证和测试数据中的测量质量。"
    caption: "图 11：验证和测试数据中显著性图权重与伪距误差的关系。"
themes:
  - "urban-gnss-reliability"
  - "environment-aware-pnt"
  - "optimization-estimation"
tags: []
---

<aside class="translation-stub">本论文以英文发表。完整书目详情、DOI / PDF 链接请见 <a href="/en/publications/2023-positionnet-cnn-based-gnss-positioning-in-urban-areas-with/">英文页面</a>。</aside>
