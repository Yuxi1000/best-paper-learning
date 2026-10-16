# Generative Image Dynamics

- id: `generative-image-dynamics`
- award: CVPR 2024 Best Paper
- section_bucket: method-mechanism
- source: arXiv:2309.07906

## Excerpt (truncated; study the move, do not copy)

seamless looping videos, editing the generated motions, and enabling interactive dynamic images via image-space modal bases, i.e., simulating the response of object dynamics to user-applied forces [22]. whereas these prior methods required a video as input. Image Synthesis Video Synthesis FID KID FVD FVD32 DTFVD DTFVD32 TATS [35] 65.8 1.67 265.6 419.6 22.6 40.7 Stochastic I2V [27] 68.3 3.12 253.5 320.9 16.7 41.7 MCVD [93] 63.4 2.97 208.6 270.4 19.5 53.9 LFDM [67] 47.6 1.70 187.5 254.3 13.0 45.6 DMVFN [48] 37.9 1.09 206.5 316.3 11.2 54.5 Endo et al. [29] 10.4 0.19 166.0 231.6 5.35 65.1 Holynski et al. [46] 11.2 0.20 179.0 253.7 7.23 46.8 Ours 4.03 0.08 47.1 62.9 2.53 6.75 Table 1. Quantitative comparisons on the test set. We report both image synthesis and video synthesis quality. Here, KID is scaled by 100. Lower is better for all error. See Sec. 7.1 for descriptions of baselines and error metrics. 7. Experiments Implementation details. We use an LDM [74] as the backbone for predicting spectral volumes, for which we use a VAE with a continuous latent space of dimension 4. We train the VAE with an L1 reconstruction loss, a multi-scale gradient consistency loss [54–56], and a KL-divergence loss with respective weights of 1, 0.2, 10−6. We train the same 2D U-Net used in the original LDM work to perform iterative denosing with a simple MSE loss [44], and adopt the attention layers…
