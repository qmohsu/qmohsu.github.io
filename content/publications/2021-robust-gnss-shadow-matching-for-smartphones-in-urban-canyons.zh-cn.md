---
title: "Robust GNSS Shadow Matching for Smartphones in Urban Canyons"
slug: "2021-robust-gnss-shadow-matching-for-smartphones-in-urban-canyons"
authors:
  - "Ng H.F."
  - "Zhang G."
  - "Hsu L. T."
year: 2021
venue: "IEEE Sensors Journal"
type: "journal"
cv_number: 79
featured: true
quartile: "Q1"
doi: "10.1109/jsen.2021.3083801"
pdf: ""
code: ""
data: ""
hero_image: "/images/pubs/2021-shadow-matching-urban-skymask-hero.png"
hero_alt: "用于 smartphone GNSS shadow matching 的 urban canyon 测试点与预测 sky mask。"
hero_caption: "图 6 视觉细节：urban canyon 测试点与预测 sky mask，用于 smartphone shadow matching。"
figures:
  - src: "/images/pubs/2021-shadow-matching-fig1-skymask-format.png"
    alt: "Skymask storage format beside a polar skymask visualization."
    context: "在给候选位置评分前，论文先定义由 3D 建筑预测 LOS/NLOS 可见性的天空遮罩表示。"
    caption: "图 1：用于可见性预测的天空遮罩数据格式和天空图可视化。"
  - src: "/images/pubs/2021-shadow-matching-fig2-nlos-example.png"
    alt: "NLOS reception example showing LOS, reflected, and NLOS paths around buildings."
    context: "这个例子说明为何需要鲁棒方法：NLOS 接收会让街道两侧候选位置看起来同样可信。"
    caption: "图 2：NLOS 接收影响 GNSS 阴影匹配的示例。"
  - src: "/images/pubs/2021-shadow-matching-fig4-key-satellite.png"
    alt: "Key satellite classification diagram with LOS, NLOS, skymask, and key satellite area."
    context: "在基本阴影匹配流程之后，可靠性规则关注建筑边缘附近的关键卫星，以判断几何是否足够有辨识度。"
    caption: "图 4：建筑天空遮罩边缘附近的关键卫星分类。"
  - src: "/images/pubs/2021-shadow-matching-fig6-environment-skymask.png"
    alt: "Urban experiment environment panels paired with skymasks."
    context: "评估随后把这些规则应用到不同建筑几何和接收机类型的真实街道实验。"
    caption: "图 6：实验环境及对应天空遮罩。"
  - src: "/images/pubs/2021-shadow-matching-fig11-candidate-skymask.png"
    alt: "Position candidate heatmap and skymasks showing satellite classification at selected candidates."
    context: "这个诊断案例说明，当多个候选位置产生相似的天空遮罩证据时，歧义为何仍然存在。"
    caption: "图 11：用于解释阴影匹配歧义案例的候选热力图和天空遮罩诊断。"
  - src: "/images/pubs/2021-shadow-matching-fig14-reliability-cdf.png"
    alt: "CDF of across-street positioning error before and after reliability evaluation."
    context: "最终结果显示，排除不可靠的阴影匹配历元可以改善横街方向误差分布。"
    caption: "图 14：可靠性评估改善横街方向误差分布。"
project: "3dma-gnss"
themes:
  - "urban-gnss-reliability"
  - "environment-aware-pnt"
  - "seamless-pnt-embodied"
tags: []
---

<aside class="translation-stub">本论文以英文发表。完整书目详情、DOI / PDF 链接请见 <a href="/en/publications/2021-robust-gnss-shadow-matching-for-smartphones-in-urban-canyons/">英文页面</a>。</aside>
