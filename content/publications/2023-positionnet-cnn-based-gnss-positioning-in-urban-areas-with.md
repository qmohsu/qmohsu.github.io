---
title: "PositionNet: CNN-based GNSS positioning in urban areas with residual maps"
slug: "2023-positionnet-cnn-based-gnss-positioning-in-urban-areas-with"
authors:
  - "Xu, P."
  - "Zhang, G."
  - "Yang, B."
  - "Hsu, L. T."
year: 2023
venue: "Applied Soft Computing"
type: "journal"
cv_number: 41
featured: true
quartile: "Q1"
doi: "10.2139/ssrn.4194604"
pdf: ""
code: ""
data: ""
summary: "PositionNet uses CNNs and residual maps to learn urban GNSS position corrections."
hero_image: "/images/pubs/2023-positionnet-fig3-network.png"
hero_alt: "Network structure of PositionNet with encoder, decoder, mean pooling, and residual connection."
hero_caption: "Figure 3 from the PositionNet paper: CNN architecture for turning residual maps into a positioning heat map."
figures:
  - src: "/images/pubs/2023-positionnet-fig1-res-map-geometry.png"
    alt: "Geometry of the range residual map with satellite direction, sampling location, and user location."
    context: "Before the CNN architecture, the paper defines how satellite range residuals become image-like maps around the least-squares solution."
    caption: "Figure 1: geometry of the residual map used as PositionNet input."
  - src: "/images/pubs/2023-positionnet-fig2-sdres-map.png"
    alt: "Single-differenced residual map layers intersecting at the user location."
    context: "The SDRes map removes receiver clock bias by differencing with a master satellite, creating a clearer location pattern for the network."
    caption: "Figure 2: SDRes maps strengthen the location pattern when multiple LOS satellites agree."
  - src: "/images/pubs/2023-positionnet-fig4-validation-map.png"
    alt: "Validation and testing PositionNet results over Tsim Sha Tsui, Whampoa, Mong Kok, and Kowloon Bay maps."
    context: "The first result maps PositionNet outputs across urban districts to show validation and testing behavior beyond a single scene."
    caption: "Figure 4: validation and testing results displayed on urban maps."
  - src: "/images/pubs/2023-positionnet-fig5-case1-solution.png"
    alt: "Case 1 PositionNet solution map and output heat map."
    context: "The case study then zooms into one large least-squares error to show how the output heat map points to a corrected location."
    caption: "Figure 5: Case 1 positioning solution and output heat map."
  - src: "/images/pubs/2023-positionnet-fig6-case1-saliency.png"
    alt: "Case 1 saliency map grid showing residual maps, SDRes maps, C/N0 maps, and saliency responses."
    context: "The saliency maps explain that case by showing which satellite residual, SDRes, and C/N0 layers influenced the network."
    caption: "Figure 6: Case 1 saliency map explaining which satellite residual patterns influenced the network."
  - src: "/images/pubs/2023-positionnet-fig11-saliency-weighting.png"
    alt: "Scatter plots of saliency map weighting versus pseudorange error for validation and testing data."
    context: "The aggregate saliency plot ties the case-level explanation back to measurement quality across validation and testing data."
    caption: "Figure 11: saliency map weighting versus pseudorange error for validation and testing data."
themes:
  - "urban-gnss-reliability"
  - "environment-aware-pnt"
  - "optimization-estimation"
tags: []
---

**Key idea.** **PositionNet** learns to correct urban GNSS errors with a CNN that reads **residual maps** — turning the spatial pattern of pseudorange residuals into a learned position correction.

**Impact.** Shows that data-driven methods can complement model-based 3D-mapping-aided GNSS, an early thread in the lab's AI-for-positioning direction.
