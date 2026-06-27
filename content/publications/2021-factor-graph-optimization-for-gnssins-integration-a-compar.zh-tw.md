---
title: "Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter"
slug: "2021-factor-graph-optimization-for-gnssins-integration-a-compar"
authors:
  - "Wen W."
  - "Pfeifer T."
  - "Bai X."
  - "Hsu L. T."
year: 2021
venue: "NAVIGATION: Journal of the Institute of Navigation"
type: "journal"
cv_number: 80
featured: true
quartile: "Q1"
doi: "10.1002/navi.421"
pdf: ""
code: ""
data: ""
project: "graphgnsslib"
resources:
  - "graphgnsslib-software"
repo: "https://github.com/weisongwen/GraphGNSSLib"
video: "https://www.youtube.com/watch?v=f5bIh96SRsk"
hero_image: "/images/pubs/2021-fgo-fig2-factor-graph.png"
hero_alt: "Factor graph structure for loosely coupled and tightly coupled GNSS/INS integration."
hero_caption: "圖 2（論文）：用於鬆耦合和緊耦合 GNSS/INS 整合的因子圖結構。"
figures:
  - src: "/images/pubs/2021-fgo-fig1-flowchart.png"
    alt: "Flowchart of loosely coupled and tightly coupled GNSS/INS integrations implemented using EKF."
    context: "在提出因子圖模型前，論文先建立 EKF 的鬆耦合與緊耦合基線，作為新 formulation 的比較對象。"
    caption: "圖 1（論文）：基於 EKF 實現的鬆耦合與緊耦合 GNSS/INS 整合流程圖。"
  - src: "/images/pubs/2021-fgo-fig3-experiment-setup.png"
    alt: "Experimental vehicle sensor setup and Hong Kong urban canyon test scene."
    context: "在定義估計結構後，論文轉向香港車輛實驗平台和城市峽谷路線，用於比較 EKF 與 FGO。"
    caption: "圖 3（論文）：實驗車輛感測器配置和香港城市峽谷測試場景。"
  - src: "/images/pubs/2021-fgo-fig5-tc-results.png"
    alt: "Tightly coupled GNSS/INS trajectory and two-dimensional error results comparing EKF and FGO."
    context: "第一組主要結果把方法轉化為軌跡證據，對比緊耦合 EKF 和 FGO 與參考軌跡的差異。"
    caption: "圖 5（論文）：緊耦合 GNSS/INS 軌跡以及 EKF 與 FGO 的 2D 定位誤差比較。"
  - src: "/images/pubs/2021-fgo-fig8-window-size.png"
    alt: "Two-dimensional positioning error under different FGO window sizes."
    context: "視窗長度分析說明 FGO 的性能為何取決於同時最佳化多少歷史資訊。"
    caption: "圖 8（論文）：緊耦合 FGO 在不同滑動視窗長度下的 2D 定位誤差。"
  - src: "/images/pubs/2021-fgo-fig9-skyview.png"
    alt: "Sky-view images showing line-of-sight and non-line-of-sight satellite visibility at selected epochs."
    context: "這些天空視圖時刻透過展示困難時段的 LOS/NLOS 衛星條件來解釋視窗長度結果。"
    caption: "圖 9（論文）：魚眼天空視圖和所選時刻的 LOS/NLOS 衛星可見性。"
  - src: "/images/pubs/2021-fgo-fig10-pseudorange-gmm.png"
    alt: "GPS and BeiDou pseudorange error histograms with fitted Gaussian mixture models."
    context: "偽距直方圖把定位表現與城市測量雜訊的非高斯特性連結起來。"
    caption: "圖 10（論文）：GPS 和北斗偽距誤差直方圖及對應的高斯混合模型擬合。"
  - src: "/images/pubs/2021-fgo-fig13-computation-time.png"
    alt: "Computational time comparison between tightly coupled FGO and tightly coupled iSAM."
    context: "最後的比較檢查用 FGO 與 iSAM 求解緊耦合圖最佳化的實際計算代價。"
    caption: "圖 13（論文）：緊耦合 FGO 與緊耦合 iSAM 的計算時間比較。"
themes:
  - "urban-gnss-reliability"
  - "optimization-estimation"
tags: []
---

<aside class="translation-stub">本論文以英文發表。完整書目詳情、DOI / PDF 連結請見 <a href="/en/publications/2021-factor-graph-optimization-for-gnssins-integration-a-compar/">英文頁面</a>。</aside>
