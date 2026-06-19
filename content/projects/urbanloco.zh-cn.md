---
title: "UrbanLoco (城市定位数据集)"
slug: "urbanloco"
description: "面向高密度城市场景 (旧金山 + 香港) 建图与定位算法基准测试的全套传感器数据集。"
category: "open-platform"
status: "maintained"
flagship: false
start_date: 2020
repo: "https://github.com/weisongwen/UrbanLoco"
video: "https://www.youtube.com/watch?v=3axr7ICggRw"
themes: ["urban-gnss-reliability", "environment-aware-pnt", "seamless-pnt-embodied"]
people: ["weisong-wen", "guohao-zhang", "xiwei-bai"]
tags: ["dataset", "benchmark", "LiDAR", "camera", "autonomous-vehicles"]
weight: 2
---

UrbanLoco 是一个多传感器数据集,服务于高密度城市环境下的建图与定位算法基准测试。它包含 <strong>13 条轨迹,总里程超过 40 km</strong>,跨旧金山与香港 —— 城市峡谷、桥梁、隧道、急转弯 —— 同步采集 LiDAR、相机(旧金山 360°,香港鱼眼天空相机)、IMU、GNSS 数据,采用 <strong>NovAtel SPAN CPT 7 + RTK</strong> 作为真值。

<strong>为什么重要。</strong> 现有公开 AV 数据集要么传感器覆盖不全,要么回避了最具挑战性的城市场景。UrbanLoco 捕捉到 <strong>GNSS 信号被多径严重退化、LiDAR / 相机方法又难以处理动态物体</strong> 的真实条件 —— 为自动驾驶导航算法提供一个真实的压力测试。

<strong>产出。</strong> 开源数据集(CC BY-NC-SA 4.0 协议)、[GitHub 仓库](https://github.com/weisongwen/UrbanLoco)、配套 [ICRA 2020 论文](/zh-cn/news/2020-urbanloco-dataset/)(Wen, Zhou, Zhang, Fahandezh-Saadi, Bai, Zhan, Tomizuka, Hsu)。与 <strong>UC Berkeley 机械系统控制实验室</strong> 联合发布。
