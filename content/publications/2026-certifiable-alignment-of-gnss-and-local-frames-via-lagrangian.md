---
title: "Certifiable Alignment of GNSS and Local Frames via Lagrangian Duality"
slug: "2026-certifiable-alignment-of-gnss-and-local-frames-via-lagrangian"
authors:
  - "Baoshan Song"
  - "Matthew Giamou"
  - "Penggao Yan"
  - "Chunxi Xia"
  - "Li-Ta Hsu"
year: 2026
venue: "IEEE Robotics and Automation Letters"
type: "journal"
cv_number: 185
featured: false
quartile: "Q1"
doi: "10.1109/LRA.2026.3693943"
pdf: ""
code: ""
data: ""
themes:
  - "optimization-estimation"
  - "integrity-localization"
  - "seamless-pnt-embodied"
tags: []
---

<img src="/images/pubs/certifiable-alignment-pipeline.png" alt="Pipeline: the non-convex alignment problem is relaxed via rank-1 relaxation into a quadratic dual problem; after an observability check the dual is solved and rank tightness certifies whether the global optimum was found." style="max-width:560px;width:100%;height:auto;display:block;margin:1.25rem auto;" />

**Key idea.** Aligning the global GNSS frame with a local odometry/SLAM frame is a **non-convex** problem that local solvers can get silently wrong. The method applies a rank-1 relaxation and **Lagrangian duality**, checks observability (asking for more measurements when the problem is under-determined), and uses the **rank tightness** of the dual solution to *certify* when the recovered alignment is the global optimum.

**Why it matters.** Frame alignment underpins any fusion of GNSS with locally consistent navigation. A certificate of global optimality replaces "hope the solver converged" with a checkable guarantee. *(IEEE Robotics and Automation Letters, 2026, Q1.)*
