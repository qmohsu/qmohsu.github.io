---
title: "UrbanLoco 数据集发布"
slug: "2020-urbanloco-dataset"
date: 2020-03-30
category: "event"
summary: "IPNL 发布了用于城市建图与定位研究的 UrbanLoco 数据集。"
image: "/images/news/20200330a.png"
source_type: "legacy_ipnl_migration"
source_site: "legacy-ipnl"
---

IPNL 与加州大学伯克利分校机械系统控制实验室 (Mechanical Systems Control Lab, University of California, Berkeley) 合作，发布了 UrbanLoco 数据集——这是一个面向高度城市化环境中建图与定位研究而设计的全传感器套件基准数据集。该数据集包含在旧金山与香港采集的 13 条轨迹，覆盖超过 40 公里的多样化城市地形，包括城市峡谷、桥梁、隧道与急转弯。

UrbanLoco 数据集提供来自 LiDAR、相机（包括旧金山的 360 度环视相机与香港的鱼眼朝天相机）、IMU 与 GNSS 接收机的数据。真值由配备 RTK 改正的 NovAtel SPAN CPT 7 系统提供。该数据集直接填补了一项关键空白：现有的公开数据集要么传感器覆盖有限，要么回避了最具挑战性的城市场景，而 UrbanLoco 捕捉了真实世界的状况——其中 GNSS 信号因高层建筑的多径反射而严重退化，且基于 LiDAR 与相机的方法在面对动态物体时举步维艰。

![Dataset overview](/images/news/20200330b.png)
![Trajectory visualization](/images/news/20200330c.png)

配套论文由 Weisong Wen、Yiyang Zhou、Guohao Zhang、Saman Fahandezh-Saadi、Xiwei Bai、Wei Zhan、Masayoshi Tomizuka 与 Li-Ta Hsu 共同撰写，并在法国巴黎举行的 ICRA 2020 上发表。该数据集以 Creative Commons Attribution-NonCommercial-ShareAlike 4.0 许可协议公开发布于 [GitHub](https://github.com/weisongwen/UrbanLoco)，此后已被研究界广泛采用，用于对 LiDAR SLAM、视觉惯性导航与多传感器融合算法进行基准测试。
