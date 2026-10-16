# VGGT: Visual Geometry Grounded Transformer

- id: `vggt`
- award: CVPR 2025 Best Paper
- venue: CVPR 2025
- arXiv: [2503.11651](https://arxiv.org/abs/2503.11651)
- authors: Jianyuan Wang, Minghao Chen, Nikita Karaev, Andrea Vedaldi, Christian Rupprecht, David Novotny
- posted: 2025-03-14
- license: see arXiv page
- paper_type: method-system
- use_for: architecture-figure, system-method, strong-abstract, multi-task-claim

## Abstract

We present VGGT, a feed-forward neural network that directly infers all key 3D attributes of a scene, including camera parameters, point maps, depth maps, and 3D point tracks, from one, a few, or hundreds of its views. This approach is a step forward in 3D computer vision, where models have typically been constrained to and specialized for single tasks. It is also simple and efficient, reconstructing images in under one second, and still outperforming alternatives that require post-processing with visual geometry optimization techniques. The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking. We also show that using pretrained VGGT as a feature backbone significantly enhances downstream tasks, such as non-rigid point tracking and feed-forward novel view synthesis. Code and models are publicly available at https://github.com/facebookresearch/vggt.
