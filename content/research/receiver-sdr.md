---
title: "Receiver-Level GNSS Signal Processing and SDR"
description: "Software-defined receivers, vector tracking, and signal-quality analysis that turn distorted satellite signals into usable measurements with explicit uncertainty."
keywords:
  - "GNSS SDR"
  - "vector tracking"
  - "acquisition / tracking"
  - "L1 / L5"
  - "direct position estimation"
  - "C/N0"
  - "correlator features"
  - "receiver-aware uncertainty"
weight: 1
lead: "bing-xu"
aliases:
  - /research/gnss-sdr/
---

Reliable navigation starts before position estimation. Many urban GNSS failures begin at the receiver level — weak signals, distorted correlation peaks, multipath, NLOS reception, Doppler inconsistency, poor tracking — none of which a downstream estimator can fully recover.

<img src="/images/research/blueprint-receiver-sdr.svg" alt="Blueprint: RF/IF samples from a software-defined receiver flow through acquisition and tracking (vector tracking) and correlator-feature analysis to yield measurements with explicit uncertainty." style="max-width:660px;width:100%;height:auto;display:block;margin:1.5rem auto;" />

We study receiver-level algorithms that turn weak, distorted signals into usable measurements, likelihoods, and uncertainty models — software-defined receivers, vector tracking, acquisition/tracking, GPS L1/L5 processing, direct position estimation, correlator-level features, and C/N0 assessment in urban, vegetated, and high-dynamic environments.

This is the foundation IPNL has built since Prof. Hsu's PhD work, anchored by the open-source [GPS_VT_SDR](/projects/gps-vt-sdr/) MATLAB vector-tracking receiver hosted on the NOAA GPS Toolbox.
