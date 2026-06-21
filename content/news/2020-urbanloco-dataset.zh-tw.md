---
title: "UrbanLoco 資料集發布"
slug: "2020-urbanloco-dataset"
date: 2020-03-30
category: "event"
summary: "IPNL 發布 UrbanLoco 資料集，供都市製圖與定位研究使用。"
image: "/images/news/20200330a.png"
source_type: "legacy_ipnl_migration"
source_site: "legacy-ipnl"
---

IPNL 與加州大學柏克萊分校機械系統控制實驗室（Mechanical Systems Control Lab）合作，發布了 UrbanLoco 資料集——一套完整感測器套組的基準資料集，專為高度都市化環境中的製圖與定位研究而設計。該資料集包含於舊金山與香港收集的 13 條軌跡，涵蓋超過 40 公里的多樣都市地形，包括都市峽谷、橋樑、隧道與急轉彎。

UrbanLoco 資料集提供來自光達（LiDAR）、相機（包括舊金山的 360 度環景與香港的魚眼天空相機）、IMU 與 GNSS 接收機的資料。真值（ground truth）由配備 RTK 修正的 NovAtel SPAN CPT 7 系統提供。該資料集直接填補了一項關鍵缺口：現有的公開資料集要嘛感測器涵蓋範圍有限，要嘛迴避最具挑戰性的都市情境，而 UrbanLoco 則捕捉了真實世界的狀況——GNSS 訊號因高樓的多路徑反射而嚴重劣化，且光達與相機方法在面對動態物體時難以應付。

![Dataset overview](/images/news/20200330b.png)
![Trajectory visualization](/images/news/20200330c.png)

隨附的論文由 Weisong Wen、Yiyang Zhou、Guohao Zhang、Saman Fahandezh-Saadi、Xiwei Bai、Wei Zhan、Masayoshi Tomizuka 與 Li-Ta Hsu 共同撰寫，並於法國巴黎舉行的 ICRA 2020 發表。該資料集以 Creative Commons Attribution-NonCommercial-ShareAlike 4.0 授權，公開託管於 [GitHub](https://github.com/weisongwen/UrbanLoco)，此後已被研究社群廣泛採用，作為光達 SLAM、視覺慣性導航與多感測器融合演算法的基準測試。
