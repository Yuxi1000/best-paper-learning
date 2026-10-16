# Generative Image Dynamics

- id: `generative-image-dynamics`
- award: CVPR 2024 Best Paper
- section_bucket: problem-framing
- source: arXiv:2309.07906

## Excerpt (truncated; study the move, do not copy)

Generative Image Dynamics Zhengqi Li Richard Tucker Noah Snavely Aleksander Holynski Google Research … Input Picture X coefficients Spectral Volume (Image-Space Modal Basis) 0.2Hz 0.4Hz 3.0Hz Looping video Interactive dynamics … Y coefficients Figure 1. We model a generative image-space prior on scene motion: from a single RGB image, our method generates a spectral volume [23], a motion representation that models dense, long-term pixel trajectories in the Fourier domain. Our learned motion priors can be used to turn a single picture into a seamlessly looping video, or into an interactive simulation of dynamics that responds to user inputs like dragging and releasing points. On the right, we visualize output videos as space-time X-t slices (along the input scanline shown on the left). Abstract We present an approach to modeling an image-space prior on scene motion. Our prior is learned from a collection of motion trajectories extracted from real video sequences depicting natural, oscillatory dynamics of objects such as trees, flowers, candles, and clothes swaying in the wind. We model dense, long-term motion in the Fourier domain as spectral volumes, which we find are well-suited to prediction with diffusion models. Given a single image, our trained model uses a frequency-coordinated diffusion sampling process to predict a spectral volume, which can be converted into a motion…
