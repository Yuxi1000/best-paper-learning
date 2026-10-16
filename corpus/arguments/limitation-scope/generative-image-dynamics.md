# Generative Image Dynamics

- id: `generative-image-dynamics`
- award: CVPR 2024 Best Paper
- section_bucket: limitation-scope
- source: arXiv:2309.07906

## Excerpt (truncated; study the move, do not copy)

Limitations. Since our approach only predicts lower frequencies of a spectral volume, it can fail to model nonoscillating motions or high-frequency vibrations—this may be resolved by using learned motion bases. Furthermore, the quality of generated videos relies on the quality of underlying motion trajectories, which may degrade in scenes with thin moving objects or objects with large displacements. Even if correct, motions that require generating large amounts of new unseen content may also cause degradations (Fig. 8). We present a new approach for modeling natural oscillation dynamics from a single still picture. Our image-space motion prior is represented with spectral volumes, a frequency representation of per-pixel motion trajectories, which we find to be efficient and effective for prediction with diffusion models, and which we learn from collections of real world videos. Spectral volumes are predicted using frequency-coordinated latent diffusion model and are used to animate future video frames through an image-based rendering module. We show that our approach produces photo-realistic animations from a single picture and significantly outperforms prior baselines, and that it can enable several downstream applications such as creating seamlessly looping or interactive image dynamics. Acknowledgements. We thank Abe Davis, Rick Szeliski, Andrew Liu, Boyang Deng, Qianqian…
