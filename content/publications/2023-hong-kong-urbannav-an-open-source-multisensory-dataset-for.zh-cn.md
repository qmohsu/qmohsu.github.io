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
hero_caption: "图 1（UrbanNav 论文）：多传感器数据和具有挑战性的香港城市场景，用于导航基准测试。"
figures:
  - src: "/images/pubs/2023-urbannav-fig2-platform.png"
    alt: "UrbanNav data collection vehicle and roof-mounted sensor kit with GNSS, IMU, LiDAR, and cameras."
    context: "数据集故事从实体采集平台开始，展示 GNSS、IMU、LiDAR 和相机如何一起搭载。"
    caption: "图 2：数据采集平台和集成多传感器套件。"
  - src: "/images/pubs/2023-urbannav-fig3-hardware-flow.png"
    alt: "Hardware connection flowchart for synchronized UrbanNav sensor logging and postprocessing."
    context: "这进一步把传感器平台转化为同步记录流程，用于采集对齐的多传感器数据。"
    caption: "图 3：数据采集平台的硬件连接与同步流程。"
  - src: "/images/pubs/2023-urbannav-fig4-sensor-installation.png"
    alt: "Sensor installation drawing with rack configuration, side view, and top view."
    context: "安装几何关系提供了把不同传感器数据流一起使用所需的标定基础。"
    caption: "图 4：UrbanNav 车辆的传感器安装标定几何。"
  - src: "/images/pubs/2023-urbannav-fig5-scenarios-reconstruction.png"
    alt: "UrbanNav scenario trajectories and environment reconstructions for middle-class, deep, harsh, and tunnel urban cases."
    context: "在平台定义完成后，论文介绍数据集要用于基准测试的城市场景。"
    caption: "图 5：四个选定数据集的代表性轨迹和重建环境。"
  - src: "/images/pubs/2023-urbannav-fig6-skymasks.png"
    alt: "Skymask examples for middle-class urban, deep urban, and harsh urban scenarios."
    context: "天空遮罩量化这些场景对卫星的遮挡，把环境严重程度与 GNSS 难度联系起来。"
    caption: "图 6：用于描述城市峡谷中卫星可见性约束的天空遮罩示例。"
  - src: "/images/pubs/2023-urbannav-fig16-benchmark-trajectories.png"
    alt: "Benchmark trajectories comparing ground truth with VINS-Mono, VINS-Fusion, and ORB-SLAM3."
    context: "基准测试部分随后在选定场景中把视觉惯性和 SLAM 算法与真值轨迹进行比较。"
    caption: "图 16：将视觉惯性和 SLAM 方法与真值轨迹比较的基准轨迹。"
  - src: "/images/pubs/2023-urbannav-fig18-lessons-github.png"
    alt: "Lessons learned montage for UrbanNav, including sensor interference, start point, timing synchronization, and GitHub usage map."
    context: "最后一张图把公开数据集发布与采集、同步和社区复用中的实践经验联系起来。"
    caption: "图 18：采集和发布 UrbanNav 数据集得到的经验总结。"
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

<aside class="translation-stub">本论文以英文发表。完整书目详情、DOI / PDF 链接请见 <a href="/en/publications/2023-hong-kong-urbannav-an-open-source-multisensory-dataset-for/">英文页面</a>。</aside>
