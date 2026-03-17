---
title: "UrbanLoco Dataset Released"
date: 2020-03-30
category: "event"
summary: "IPNL released the UrbanLoco dataset for urban mapping and localization research."
image: "/images/news/20200330a.png"
source_type: "legacy_ipnl_migration"
source_site: "legacy-ipnl"
---

IPNL, in collaboration with the Mechanical Systems Control Lab at the University of California, Berkeley, released the UrbanLoco dataset — a full sensor-suite benchmark designed for mapping and localization research in highly urbanized environments. The dataset includes 13 trajectories collected in San Francisco and Hong Kong, covering over 40 kilometers of diverse urban terrain including urban canyons, bridges, tunnels, and sharp turns.

The UrbanLoco dataset provides data from LiDAR, cameras (including a 360-degree view in San Francisco and a fish-eye sky camera in Hong Kong), IMU, and GNSS receivers. Ground truth is provided by a NovAtel SPAN CPT 7 system with RTK corrections. The dataset directly addresses a critical gap: while existing public datasets offered limited sensor coverage or avoided the most challenging urban scenarios, UrbanLoco captures real-world conditions where GNSS signals are severely degraded by multipath reflections from high-rise buildings, and where LiDAR and camera-based methods struggle with dynamic objects.

![Dataset overview](/images/news/20200330b.png)
![Trajectory visualization](/images/news/20200330c.png)

The accompanying paper, authored by Weisong Wen, Yiyang Zhou, Guohao Zhang, Saman Fahandezh-Saadi, Xiwei Bai, Wei Zhan, Masayoshi Tomizuka, and Li-Ta Hsu, was presented at ICRA 2020 in Paris, France. The dataset is publicly available on [GitHub](https://github.com/weisongwen/UrbanLoco) under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license and has since been widely adopted by the research community for benchmarking LiDAR SLAM, visual-inertial navigation, and multi-sensor fusion algorithms.
