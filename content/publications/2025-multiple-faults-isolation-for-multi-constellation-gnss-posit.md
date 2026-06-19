---
title: "Multiple Faults Isolation For Multi-Constellation GNSS Positioning through Incremental Expansion of Consistent Measurements"
slug: "2025-multiple-faults-isolation-for-multi-constellation-gnss-posit"
authors:
  - "Yan, P."
  - "Hu, Y."
  - "Wen, W."
  - "Hsu, L. T."
year: 2025
venue: "IEEE Sensors Journal"
type: "journal"
cv_number: 9
featured: false
quartile: "Q1"
doi: "10.1109/jsen.2024.3524434"
pdf: ""
code: ""
data: ""
themes:
  - "urban-gnss-reliability"
  - "optimization-estimation"
  - "integrity-localization"
tags: []
---

<img src="/images/pubs/multiple-faults-isolation.png" alt="Fault isolation first builds a minimum, fault-free 'basic set' from ordered studentized residuals, then incrementally admits measurements that pass a no-fault hypothesis test — measurements that never fit are isolated as faults." style="max-width:560px;width:100%;height:auto;display:block;margin:1.25rem auto;" />

**Key idea.** Multi-constellation GNSS supplies many redundant measurements, but also a higher chance of *several* simultaneous faults (multipath / NLOS). Instead of searching every measurement subset, the method first constructs a small **minimum basic set** assumed fault-free — selected via **ordered studentized residuals** — then **incrementally expands** it, admitting only measurements that pass a **no-fault hypothesis test**. Measurements that never fit are isolated as faults.

**Why it matters.** The conventional deletion-based greedy search method results in aggressive exclusion, which degrades satellite geometry and accuracy. The proposed method turns multiple-fault isolation from a combinatorial search into a tractable, incremental test, improving the reliability of multi-constellation positioning in challenging urban environments. *(IEEE Sensors Journal, 2025, Q1.)*
