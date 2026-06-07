---
title: "Urban GNSS Reliability and Signal Error Modeling"
description: "Modeling how GNSS measurements fail in dense cities — NLOS, multipath, diffraction, heavy-tailed errors — so downstream estimation and integrity systems know when to trust them."
keywords:
  - "urban GNSS"
  - "multipath"
  - "NLOS"
  - "diffraction"
  - "Doppler consistency"
  - "heavy-tailed errors"
  - "measurement reliability"
  - "uncertainty modeling"
weight: 2
lead: "li-ta-hsu"
video: "https://www.youtube.com/watch?v=Ys4xCbN9h1s"
aliases:
  - /research/urban-gnss/
---

Dense cities are not an exception case for GNSS; they are the stress test. We study how GNSS measurements fail — NLOS reception, multipath, diffraction, Doppler distortion, heavy-tailed errors — and detect and quantify these failures at the measurement layer before they corrupt downstream estimation.

<img src="/images/research/blueprint-urban-gnss-reliability.svg" alt="Blueprint: satellite signals pass through urban hazards (NLOS, multipath, diffraction, Doppler distortion, heavy-tailed errors), producing measurements that each carry a reliability tag." style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

The goal is not only to correct bad measurements but to **model their reliability**, so the rest of the navigation stack knows when to trust them. This pillar is the measurement-layer foundation for the [Environment-Aware](/research/environment-aware-pnt/), [Optimization-Based Estimation](/research/optimization-estimation/), and [Integrity](/research/integrity-localization/) pillars.
