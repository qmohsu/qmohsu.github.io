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
featured: false
quartile: Q?
doi: 10.47852/bonviewjdsis42022961
pdf: https://ojs.bonviewpress.com/index.php/jdsis/article/download/2961/1145/24389
code: https://github.com/queenie-ho/3DMAGNSSVINS-IOFGO
data: ''
summary: 這篇論文在 factor graph optimization 中用 indoor/outdoor switching factor 融合 smartphone 3DMA GNSS 與 visual-inertial estimates。
highlights:
- 系統用 SVM-based indoor/outdoor detection 決定 GNSS 與 VINS measurements 在 graph 中的權重。
- 香港行人實驗在 indoor/outdoor transitions 下，把 smartphone trajectories 與 LIO-SAM ground truth 進行比較。
hero_image: /images/pubs/2024-smartphone-fgo-fig2-system-flow.png
hero_alt: 含 indoor/outdoor switching 的 smartphone 3DMA GNSS/VINS factor graph optimization 系統流程圖。
hero_caption: 圖 2：proposed framework 結合 camera、IMU、GNSS、3DMA GNSS、SVM indoor/outdoor classification 與 factor graph optimization。
figures:
- src: /images/pubs/2024-smartphone-fgo-fig3-io-svm-flow.png
  alt: 使用 training data、validation data、GNSS features 與 test data 的 indoor/outdoor classification SVM flowchart。
  context: SVM classifier 把 GNSS features 轉成 indoor/outdoor label，後續用來控制 switching factor。
  caption: 圖 3：indoor/outdoor classification 的 SVM flowchart。
- src: /images/pubs/2024-smartphone-fgo-fig4-factor-graph.png
  alt: 連接 VINS factors、3DMA GNSS factors、switching factors 與 state nodes 的 factor graph。
  context: factor graph 說明 VINS、3DMA GNSS 與 indoor/outdoor switching factor 在 optimization problem 中如何匯合。
  caption: 圖 4：用 indoor/outdoor switching factor loosely coupling GNSS 與 VINS 的 FGO structure。
- src: /images/pubs/2024-smartphone-fgo-fig5-experiment-trajectories.png
  alt: experiment trajectories A、B 與 C 的 Google Earth views。
  context: experiment routes 定義了後續比較演算法所需的 indoor/outdoor transition scenarios。
  caption: 圖 5：trajectories A、B 與 C 的 Google Earth views。
- src: /images/pubs/2024-smartphone-fgo-fig6-lio-sam-ground-truth.png
  alt: trajectories A、B 與 C 的 LIO-SAM ground-truth maps。
  context: LIO-SAM ground truth 為後面的 trajectory comparisons 與 error plots 提供基準。
  caption: 圖 6：LIO-SAM 產生的 trajectories A、B 與 C ground truth。
- src: /images/pubs/2024-smartphone-fgo-fig13-b2-error.png
  alt: 含 3DMA GNSS standard deviation 與 indoor/outdoor indicator 的 B2 absolute positioning error plot。
  context: B2 error plot 凸顯 transition period：加入 indoor/outdoor switch 後，可抑制沒有 switch 的方法中出現的 error growth。
  caption: 圖 13：含 estimated 3DMA GNSS standard deviation 與 IO indicator 的 B2 absolute positioning error comparison。
- src: /images/pubs/2024-smartphone-fgo-fig14-b2-trajectory.png
  alt: B2 trajectory comparison，包含 GT、VINSMONO、3DMA GNSS、3DMA GNSS/VINS FGO 與 3DMA GNSS/VINS-IO FGO。
  context: 配對的 trajectory plot 從空間上呈現同一件事：switching version 在 transition 期間更貼近 ground truth。
  caption: 圖 14：B2 trajectory comparison。
themes:
- optimization-estimation
- seamless-pnt-embodied
tags: []
---

<aside class="translation-stub">本論文以英文發表。完整書目詳情、DOI / PDF 連結請見 <a href="/en/publications/2024-enhancing-smartphone-based-pedestrian-positioning-using-fac/">英文頁面</a>。</aside>
