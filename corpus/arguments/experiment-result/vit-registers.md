# Vision Transformers Need Registers

- id: `vit-registers`
- award: ICLR 2024 Outstanding Paper
- section_bucket: experiment-result
- source: arXiv:2309.16588

## Excerpt (truncated; study the move, do not copy)

As shown in Fig. 1, we get rid of the artifacts by training models with additional register tokens. In the appendix, we provide additional qualitative results for more images in Fig. 19. In order to quantitatively measure this effect, for each model, we probe the norm of features at the output of the model. We report these norms for all three algorithms with and without registers in Fig. 7. We see that when training with registers, models do not exhibit large-norm tokens at the output, which confirms the initial qualitative assessment. Performance regression. In the previous section, we have shown that the proposed approach removes artifacts from local feature maps. In this experiment, we want to check that the use of register tokens does not affect the representation quality of those features. We run linear probing on ImageNet classification, ADE20k Segmentation, and NYUd monocular depth estimation. We follow the experimental protocol outlined in Oquab et al. (2023). We summarize the performance of the models described in Sec. 3.1 with and without register tokens in Table 2a. We see that when using registers, models do not lose performance and sometimes even work better. For completeness, we also provided the zero-shot classification performance on ImageNet for OpenCLIP (Table 2b), which remains unchanged. Please note that the absolute performance of our OpenCLIP reproduction…
