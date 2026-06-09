---
title: "Environment-Aware and 3D Map-Aided PNT"
description: "Using 3D city models, LiDAR maps, sky visibility, ray tracing, and digital twins to turn the urban environment from an obstacle into prior information for navigation."
keywords:
  - "3D mapping-aided GNSS"
  - "3DMA GNSS"
  - "3D city models"
  - "LiDAR maps"
  - "ray tracing"
  - "digital twins"
  - "sky visibility"
  - "skymask matching"
  - "environment-aware positioning"
weight: 3
lead: "guohao-zhang"
aliases:
  - /research/3d-mapping-aided/
---

The city becomes part of the navigation system. We use 3D city models, LiDAR maps, sky visibility, ray tracing, and digital twins to predict GNSS visibility, identify NLOS and multipath, improve accuracy, and assess reliability.

<img src="/images/research/blueprint-environment-aware-pnt.svg" alt="Conventional GNSS treats the city as obstruction and is blind to which satellites are NLOS, counting reflections as honest range; IPNL uses 3D city models and LiDAR maps with ray tracing to predict NLOS and multipath and produce a corrected, reliable position." style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

The urban environment is not only an obstacle; it can become **prior information** for trustworthy navigation. This pillar grew out of Prof. Hsu's postdoc work in Tokyo and the founding ION/IAG Working Group on Positioning at Asian Urban Canyons, and it is the technical core behind both the **US12123961B2 patent** on *3D LiDAR Aided GNSS NLOS Detection and Correction* and the long-running Huawei collaboration on 3DMA GNSS for mobile devices.
