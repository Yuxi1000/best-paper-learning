# Generative Image Dynamics

- id: `generative-image-dynamics`
- award: CVPR 2024 Best Paper
- venue: CVPR 2024
- arXiv: [2309.07906](https://arxiv.org/abs/2309.07906)
- authors: Zhengqi Li, Richard Tucker, Noah Snavely, Aleksander Holynski
- posted: 2023-09-14
- license: see arXiv page
- paper_type: method-system
- use_for: teaser, qualitative-grid, problem-reframing

## Abstract

We present an approach to modeling an image-space prior on scene motion. Our prior is learned from a collection of motion trajectories extracted from real video sequences depicting natural, oscillatory dynamics such as trees, flowers, candles, and clothes swaying in the wind. We model this dense, long-term motion prior in the Fourier domain:given a single image, our trained model uses a frequency-coordinated diffusion sampling process to predict a spectral volume, which can be converted into a motion texture that spans an entire video. Along with an image-based rendering module, these trajectories can be used for a number of downstream applications, such as turning still images into seamlessly looping videos, or allowing users to realistically interact with objects in real pictures by interpreting the spectral volumes as image-space modal bases, which approximate object dynamics.
