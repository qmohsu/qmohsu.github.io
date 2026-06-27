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
summary: "Open multisensory GNSS, LiDAR, camera, and IMU benchmark captured in Hong Kong urban canyons."
hero_image: "/images/pubs/2023-urbannav-fig1-overview.png"
hero_alt: "Overview montage of the UrbanNav dataset, including Hong Kong urban scenes, vehicle sensors, LiDAR point clouds, GNSS sky-view imagery, and skymasks."
hero_caption: "Figure 1 from the UrbanNav paper: multisensory data and challenging Hong Kong urban scenarios for navigation benchmarking."
figures:
  - src: "/images/pubs/2023-urbannav-fig2-platform.png"
    alt: "UrbanNav data collection vehicle and roof-mounted sensor kit with GNSS, IMU, LiDAR, and cameras."
    context: "The dataset story starts from the physical collection platform that carries GNSS, IMU, LiDAR, and camera sensors together."
    caption: "Figure 2: data collection platform and integrated multisensor kit."
  - src: "/images/pubs/2023-urbannav-fig3-hardware-flow.png"
    alt: "Hardware connection flowchart for synchronized UrbanNav sensor logging and postprocessing."
    context: "This turns the sensor platform into a synchronized logging pipeline for collecting aligned multisensor data."
    caption: "Figure 3: hardware connection and synchronization flow for the data collection platform."
  - src: "/images/pubs/2023-urbannav-fig4-sensor-installation.png"
    alt: "Sensor installation drawing with rack configuration, side view, and top view."
    context: "The installation geometry provides the calibration basis needed to use the different sensor streams together."
    caption: "Figure 4: calibrated sensor installation geometry for the UrbanNav vehicle."
  - src: "/images/pubs/2023-urbannav-fig5-scenarios-reconstruction.png"
    alt: "UrbanNav scenario trajectories and environment reconstructions for middle-class, deep, harsh, and tunnel urban cases."
    context: "After the platform is defined, the paper introduces the urban scenarios that the dataset is designed to benchmark."
    caption: "Figure 5: representative trajectories and reconstructed environments for the four selected datasets."
  - src: "/images/pubs/2023-urbannav-fig6-skymasks.png"
    alt: "Skymask examples for middle-class urban, deep urban, and harsh urban scenarios."
    context: "The skymasks quantify how those scenarios obstruct satellites, connecting environment severity to GNSS difficulty."
    caption: "Figure 6: skymask examples used to describe satellite visibility constraints in urban canyons."
  - src: "/images/pubs/2023-urbannav-fig16-benchmark-trajectories.png"
    alt: "Benchmark trajectories comparing ground truth with VINS-Mono, VINS-Fusion, and ORB-SLAM3."
    context: "The benchmark section then runs visual-inertial and SLAM algorithms against ground truth across the selected scenarios."
    caption: "Figure 16: benchmark trajectories comparing visual-inertial and SLAM methods against ground truth."
  - src: "/images/pubs/2023-urbannav-fig18-lessons-github.png"
    alt: "Lessons learned montage for UrbanNav, including sensor interference, start point, timing synchronization, and GitHub usage map."
    context: "The final figure connects the public dataset release to practical lessons from collection, synchronization, and community reuse."
    caption: "Figure 18: lessons learned from collecting and releasing the UrbanNav dataset."
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

**Key idea.** A high-quality **open-source multi-sensor dataset** (GNSS, LiDAR, camera, IMU) captured in Hong Kong's deep urban canyons, with accurate ground truth — purpose-built for benchmarking urban navigation algorithms.

**Impact.** UrbanNav has become a widely used community benchmark for urban GNSS and sensor-fusion research, lowering the barrier for groups worldwide to test in genuinely challenging conditions. Community-facing infrastructure, not just a paper.
