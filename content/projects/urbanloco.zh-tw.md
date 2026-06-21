---
title: "UrbanLoco (城市定位資料集)"
slug: "urbanloco"
description: "面向高密度城市場景 (舊金山 + 香港) 建圖與定位演算法基準測試的全套感測器資料集。"
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

UrbanLoco 是一個多感測器資料集,服務於高密度城市環境下的建圖與定位演算法基準測試。它包含 <strong>13 條軌跡,總里程超過 40 km</strong>,跨舊金山與香港 —— 城市峽谷、橋樑、隧道、急轉彎 —— 同步採集 LiDAR、相機(舊金山 360°,香港魚眼天空相機)、IMU、GNSS 資料,採用 <strong>NovAtel SPAN CPT 7 + RTK</strong> 作為真值。

<strong>為什麼重要。</strong> 現有公開 AV 資料集要麼感測器覆蓋不全,要麼迴避了最具挑戰性的城市場景。UrbanLoco 捕捉到 <strong>GNSS 訊號被多徑嚴重退化、LiDAR / 相機方法又難以處理動態物體</strong> 的真實條件 —— 為自動駕駛導航演算法提供一個真實的壓力測試。

<strong>產出。</strong> 開源資料集(CC BY-NC-SA 4.0 協議)、[GitHub 倉庫](https://github.com/weisongwen/UrbanLoco)、配套 [ICRA 2020 論文](/zh-tw/news/2020-urbanloco-dataset/)(Wen, Zhou, Zhang, Fahandezh-Saadi, Bai, Zhan, Tomizuka, Hsu)。與 <strong>UC Berkeley 機械系統控制實驗室</strong> 聯合發布。
