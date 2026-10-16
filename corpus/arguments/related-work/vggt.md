# VGGT: Visual Geometry Grounded Transformer

- id: `vggt`
- award: CVPR 2025 Best Paper
- section_bucket: related-work
- source: arXiv:2503.11651

## Excerpt (truncated; study the move, do not copy)

Structure from Motion is a classic computer vision problem [45, 77, 80] that involves estimating camera parameters and reconstructing sparse point clouds from a set of images of a static scene captured from different viewpoints. The traditional SfM pipeline [2, 36, 70, 94, 103, 134] consists of multiple stages, including image matching, triangulation, and bundle adjustment. COLMAP [94] is the most popular framework based on the traditional pipeline. In recent years, deep learning has improved many components of the SfM pipeline, with keypoint detection [21, 31, 116, 149] and image matching [11, 67, 92, 99] being two primary areas of focus. Recent methods [5, 102, 109, 112, 113, 118, 122, 125, 131, 160] explored end-to-end differentiable SfM, where VGGSfM [125] started to outperform traditional algorithms on challenging phototourism scenarios. Multi-view Stereo aims to densely reconstruct the geometry of a scene from multiple overlapping images, typically assuming known camera parameters, which are often estimated with SfM. MVS methods can be divided into three categories: traditional handcrafted [38, 39, 96, 130], global optimization [37, 74, 133, 147], and learning-based methods [42, 72, 84, 145, 157]. As in SfM, learning-based MVS approaches have recently seen a lot of progress. Here, DUSt3R [129] and MASt3R [62] directly estimate aligned dense point clouds from a pair of…
