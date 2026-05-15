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

Dense cities are not an exception case for GNSS; they are the stress test. We study how GNSS measurements fail through NLOS reception, multipath, diffraction, Doppler distortion, heavy-tailed errors, and measurement inconsistency — and how to detect and quantify these failures at the measurement layer before they corrupt downstream estimation.

The goal is not only to correct bad measurements, but to model their reliability so the rest of the navigation stack — estimator, fusion, integrity monitor — knows when to trust them. This pillar provides the measurement-layer foundation that the [Environment-Aware](/research/environment-aware-pnt/), [Optimization-Based Estimation](/research/optimization-estimation/), and [Integrity](/research/integrity-localization/) pillars build on.
