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
hero_image: "/images/pubs/2021-shadow-matching-fig3-flowchart.png"
hero_alt: "Flowchart of the proposed robust GNSS shadow matching method."
hero_caption: "圖 3（論文）：穩健 GNSS 陰影匹配流程，包含觀測、候選位置、天空遮罩、評分和可靠性評估。"
figures:
  - src: "/images/pubs/2021-shadow-matching-fig1-skymask-format.png"
    alt: "Skymask storage format beside a polar skymask visualization."
    context: "在給候選位置評分前，論文先定義由 3D 建築預測 LOS/NLOS 可見性的天空遮罩表示。"
    caption: "圖 1：用於可見性預測的天空遮罩資料格式和天空圖視覺化。"
  - src: "/images/pubs/2021-shadow-matching-fig2-nlos-example.png"
    alt: "NLOS reception example showing LOS, reflected, and NLOS paths around buildings."
    context: "這個例子說明為何需要穩健方法：NLOS 接收會讓街道兩側候選位置看起來同樣可信。"
    caption: "圖 2：NLOS 接收影響 GNSS 陰影匹配的示例。"
  - src: "/images/pubs/2021-shadow-matching-fig4-key-satellite.png"
    alt: "Key satellite classification diagram with LOS, NLOS, skymask, and key satellite area."
    context: "在基本陰影匹配流程之後，可靠性規則關注建築邊緣附近的關鍵衛星，以判斷幾何是否足夠有辨識度。"
    caption: "圖 4：建築天空遮罩邊緣附近的關鍵衛星分類。"
  - src: "/images/pubs/2021-shadow-matching-fig6-environment-skymask.png"
    alt: "Urban experiment environment panels paired with skymasks."
    context: "評估隨後把這些規則應用到不同建築幾何和接收機類型的真實街道實驗。"
    caption: "圖 6：實驗環境及對應天空遮罩。"
  - src: "/images/pubs/2021-shadow-matching-fig11-candidate-skymask.png"
    alt: "Position candidate heatmap and skymasks showing satellite classification at selected candidates."
    context: "這個診斷案例說明，當多個候選位置產生相似的天空遮罩證據時，歧義為何仍然存在。"
    caption: "圖 11：用於解釋陰影匹配歧義案例的候選熱力圖和天空遮罩診斷。"
  - src: "/images/pubs/2021-shadow-matching-fig14-reliability-cdf.png"
    alt: "CDF of across-street positioning error before and after reliability evaluation."
    context: "最終結果顯示，排除不可靠的陰影匹配歷元可以改善橫街方向誤差分布。"
    caption: "圖 14：可靠性評估改善橫街方向誤差分布。"
project: "3dma-gnss"
themes:
  - "urban-gnss-reliability"
  - "environment-aware-pnt"
  - "seamless-pnt-embodied"
tags: []
---

<aside class="translation-stub">本論文以英文發表。完整書目詳情、DOI / PDF 連結請見 <a href="/en/publications/2021-robust-gnss-shadow-matching-for-smartphones-in-urban-canyons/">英文頁面</a>。</aside>
