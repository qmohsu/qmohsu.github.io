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
hero_caption: "圖 3（PositionNet 論文）：把殘差圖轉換為定位熱力圖的 CNN 架構。"
figures:
  - src: "/images/pubs/2023-positionnet-fig1-res-map-geometry.png"
    alt: "Geometry of the range residual map with satellite direction, sampling location, and user location."
    context: "在 CNN 架構之前，論文先定義衛星距離殘差如何變成圍繞最小平方法解的影像式輸入。"
    caption: "圖 1：PositionNet 輸入殘差圖的幾何關係。"
  - src: "/images/pubs/2023-positionnet-fig2-sdres-map.png"
    alt: "Single-differenced residual map layers intersecting at the user location."
    context: "SDRes 圖透過與主衛星做差來去除接收機鐘差，為網路形成更清晰的位置模式。"
    caption: "圖 2：當多個 LOS 衛星一致時，SDRes 圖會強化位置模式。"
  - src: "/images/pubs/2023-positionnet-fig4-validation-map.png"
    alt: "Validation and testing PositionNet results over Tsim Sha Tsui, Whampoa, Mong Kok, and Kowloon Bay maps."
    context: "第一組結果把 PositionNet 輸出映射到多個城市區域，展示其在單一場景之外的驗證和測試表現。"
    caption: "圖 4：顯示在城市地圖上的驗證和測試結果。"
  - src: "/images/pubs/2023-positionnet-fig5-case1-solution.png"
    alt: "Case 1 PositionNet solution map and output heat map."
    context: "案例研究進一步放大一個最小平方法誤差較大的樣例，展示輸出熱力圖如何指向修正後的位置。"
    caption: "圖 5：案例 1 的定位解和輸出熱力圖。"
  - src: "/images/pubs/2023-positionnet-fig6-case1-saliency.png"
    alt: "Case 1 saliency map grid showing residual maps, SDRes maps, C/N0 maps, and saliency responses."
    context: "顯著性圖解釋該案例中哪些衛星殘差、SDRes 和 C/N0 圖層影響了網路判斷。"
    caption: "圖 6：案例 1 的顯著性圖，解釋哪些衛星殘差模式影響了網路。"
  - src: "/images/pubs/2023-positionnet-fig11-saliency-weighting.png"
    alt: "Scatter plots of saliency map weighting versus pseudorange error for validation and testing data."
    context: "彙總顯著性圖把案例級解釋擴展到驗證和測試資料中的測量品質。"
    caption: "圖 11：驗證和測試資料中顯著性圖權重與偽距誤差的關係。"
themes:
  - "urban-gnss-reliability"
  - "environment-aware-pnt"
  - "optimization-estimation"
tags: []
---

<aside class="translation-stub">本論文以英文發表。完整書目詳情、DOI / PDF 連結請見 <a href="/en/publications/2023-positionnet-cnn-based-gnss-positioning-in-urban-areas-with/">英文頁面</a>。</aside>
