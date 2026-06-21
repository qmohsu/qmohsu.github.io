---
title: "Multiple Faulty GNSS Measurement Exclusion based on Consistency Check in Urban Canyons"
slug: "2017-multiple-faulty-gnss-measurement-exclusion-based-on-consiste"
authors:
  - "Hsu L. T."
  - "Tokura H."
  - "Kubo N."
  - "Gu Y."
  - "Kamijo S."
year: 2017
venue: "IEEE Sensors Journal"
type: "journal"
cv_number: 124
featured: false
quartile: "Q1"
doi: "10.1109/jsen.2017.2654359"
pdf: ""
code: ""
data: ""
themes:
  - "urban-gnss-reliability"
  - "integrity-localization"
tags: []
---

<img src="/images/pubs/consistency-check-flowchart.png" alt="Greedy search flowchart: starting from all satellites in view, subsets are generated and tested by a second-layer fault detection until a consistent subset passes and is used for weighted least squares positioning." style="max-width:560px;width:100%;height:auto;display:block;margin:1.25rem auto;" />

**Key idea.** Urban canyons routinely corrupt **several satellites at once**. A greedy consistency check searches subsets of the satellites in view — excluding the worst offender each round — until the remaining set passes fault detection and is used for positioning (figure).

**Why it matters.** Classical RAIM assumes a single fault; dense cities break that assumption daily. This deletion-based exclusion restored usable urban positioning under simultaneous faults — and its known limitation (aggressive exclusion degrading geometry) is what the lab's later incremental fault-isolation work improves on. *(IEEE Sensors Journal, 2017, Q1.)*
