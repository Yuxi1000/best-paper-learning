# Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction

- id: `var`
- award: NeurIPS 2024 Best Paper
- section_bucket: limitation-scope
- source: arXiv:2404.02905

## Excerpt (truncated; study the move, do not copy)

1) The mathematical premise is satisfied if we constrain each rk to depend only on its prefix, that is, the process of getting rk is solely related to r≤k. This constraint is acceptable as it aligns with the natural, coarse-to-fine progression characteristics like human visual perception and artistic drawing (as we discussed in Sec. 1). Further details are provided in the Tokenization below. 2) The spatial locality is preserved as (i) there is no flattening operation in VAR, and (ii) tokens in each rk are fully correlated. The multi-scale design additionally reinforces the spatial structure. 3) The complexity for generating an image with n × n latent is significantly reduced to O(n4), see Appendix for proof. This efficiency gain arises from the parallel token generation in each rk. Tokenization. We develope a new multi-scale quantization autoencoder to encode an image to K multi-scale discrete token maps R = (r1, r2, . . . , rK) necessary for VAR learning (6). We employ the same architecture as VQGAN [30] but with a modified multi-scale quantization layer. The encoding and decoding procedures with residual design on f or ˆf are detailed in algorithms 1 and 2. We empirically find this residual-style design, akin to [50], can perform better than independent interpolation. Algorithm 1 shows that each rk would depend only on its prefix (r1, r2, . . . , rk−1). Note that a shared…
