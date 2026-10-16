# Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction

- id: `var`
- award: NeurIPS 2024 Best Paper
- section_bucket: experiment-result
- source: arXiv:2404.02905

## Excerpt (truncated; study the move, do not copy)

This section first compares VAR with other image generative model families in Sec. 5.1. Evaluations on the scalability and generalizability of VAR models are presented in Sec. 5.2 and Appendix 6. For implementation details and ablation study, please see Appendix 4 and Appendix 7. 5.1 State-of-the-art image generation Setup. We test VAR models with depths 16, 20, 24, and 30 on ImageNet 256×256 and 512×512 conditional generation benchmarks and compare them with the state-of-the-art image generation model families. Among all VQVAE-based AR or VAR models, VQGAN [30] and ours use the same architecture (CNN) and training data (OpenImages [49]) for VQVAE, while ViT-VQGAN [92] uses a ViT autoencoder, and both it and RQTransformer [50] trains the VQVAE directly on ImageNet. The results are summaried in Tab. 1 and Tab. 2. 3Due to resource limitation, we use a single shared adaptive layernorm (AdaLN) acorss all attention blocks in 512×512 synthesis. In this case, the parameter count would be reduced to around 12dw2 + 6w2 ≈49152 d3. 6 Table 1: Generative model family comparison on class-conditional ImageNet 256×256. “↓” or “↑” indicate lower or higher values are better. Metrics include Fréchet inception distance (FID), inception score (IS), precision (Pre) and recall (rec). “#Step”: the number of model runs needed to generate an image. Wall-clock inference time relative to VAR is…
