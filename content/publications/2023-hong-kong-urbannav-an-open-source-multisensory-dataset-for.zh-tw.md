---
title: "Hong Kong UrbanNav: An open-source multisensory dataset for benchmarking urban navigation algorithms"
slug: "2023-hong-kong-urbannav-an-open-source-multisensory-dataset-for"
authors:
  - "Hsu, L. T."
  - "Huang, F."
  - "Ng, H. F."
  - "Zhang, G."
  - "Zhong, Y."
  - "Bai, X."
  - "Wen, W."
year: 2023
venue: "NAVIGATION: Journal of the Institute of Navigation"
type: "journal"
cv_number: 37
featured: true
quartile: "Q1"
doi: "10.33012/navi.602"
pdf: ""
code: ""
data: ""
hero_image: "/images/pubs/2023-urbannav-fig1-overview.png"
hero_alt: "Overview montage of the UrbanNav dataset, including Hong Kong urban scenes, vehicle sensors, LiDAR point clouds, GNSS sky-view imagery, and skymasks."
hero_caption: "圖 1（UrbanNav 論文）：多感測器資料和具有挑戰性的香港城市場景，用於導航基準測試。"
figures:
  - src: "/images/pubs/2023-urbannav-fig2-platform.png"
    alt: "UrbanNav data collection vehicle and roof-mounted sensor kit with GNSS, IMU, LiDAR, and cameras."
    context: "資料集故事從實體採集平台開始，展示 GNSS、IMU、LiDAR 和相機如何一起搭載。"
    caption: "圖 2：資料採集平台和整合多感測器套件。"
  - src: "/images/pubs/2023-urbannav-fig3-hardware-flow.png"
    alt: "Hardware connection flowchart for synchronized UrbanNav sensor logging and postprocessing."
    context: "這進一步把感測器平台轉化為同步記錄流程，用於採集對齊的多感測器資料。"
    caption: "圖 3：資料採集平台的硬體連接與同步流程。"
  - src: "/images/pubs/2023-urbannav-fig4-sensor-installation.png"
    alt: "Sensor installation drawing with rack configuration, side view, and top view."
    context: "安裝幾何關係提供了把不同感測器資料流一起使用所需的校準基礎。"
    caption: "圖 4：UrbanNav 車輛的感測器安裝校準幾何。"
  - src: "/images/pubs/2023-urbannav-fig5-scenarios-reconstruction.png"
    alt: "UrbanNav scenario trajectories and environment reconstructions for middle-class, deep, harsh, and tunnel urban cases."
    context: "在平台定義完成後，論文介紹資料集要用於基準測試的城市場景。"
    caption: "圖 5：四個選定資料集的代表性軌跡和重建環境。"
  - src: "/images/pubs/2023-urbannav-fig6-skymasks.png"
    alt: "Skymask examples for middle-class urban, deep urban, and harsh urban scenarios."
    context: "天空遮罩量化這些場景對衛星的遮擋，把環境嚴重程度與 GNSS 難度連結起來。"
    caption: "圖 6：用於描述城市峽谷中衛星可見性約束的天空遮罩示例。"
  - src: "/images/pubs/2023-urbannav-fig16-benchmark-trajectories.png"
    alt: "Benchmark trajectories comparing ground truth with VINS-Mono, VINS-Fusion, and ORB-SLAM3."
    context: "基準測試部分隨後在選定場景中把視覺慣性和 SLAM 演算法與真值軌跡進行比較。"
    caption: "圖 16：將視覺慣性和 SLAM 方法與真值軌跡比較的基準軌跡。"
  - src: "/images/pubs/2023-urbannav-fig18-lessons-github.png"
    alt: "Lessons learned montage for UrbanNav, including sensor interference, start point, timing synchronization, and GitHub usage map."
    context: "最後一張圖把公開資料集發布與採集、同步和社群重複使用中的實務經驗連結起來。"
    caption: "圖 18：採集和發布 UrbanNav 資料集得到的經驗總結。"
project: "urbannav"
resources:
  - "urbannav-dataset"
repo: "https://github.com/IPNL-POLYU/UrbanNavDataset"
videos:
  - "https://www.youtube.com/watch?v=V94PAkkpwWs"
  - "https://www.youtube.com/watch?v=b1-lKmUttzc"
  - "https://www.youtube.com/watch?v=hQu8npoGad8"
themes:
  - "urban-gnss-reliability"
  - "optimization-estimation"
  - "seamless-pnt-embodied"
tags: []
---

<aside class="translation-stub">本論文以英文發表。完整書目詳情、DOI / PDF 連結請見 <a href="/en/publications/2023-hong-kong-urbannav-an-open-source-multisensory-dataset-for/">英文頁面</a>。</aside>
