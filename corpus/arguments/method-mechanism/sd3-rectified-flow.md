# Scaling Rectified Flow Transformers for High-Resolution Image Synthesis

- id: `sd3-rectified-flow`
- award: ICML 2024 Best Paper
- section_bucket: method-mechanism
- source: arXiv:2403.03206

## Excerpt (truncated; study the move, do not copy)

separate weights for the two modalities and enables a bidirectional flow of information between image and text tokens, improving text comprehension, typography, and human preference ratings. We demonstrate that this architecture follows predictable scaling trends and correlates lower validation loss to improved text-to-image synthesis as measured by various metrics and human evaluations. Our largest models outperform state-of-theart models, and we will make our experimental data, code, and model weights publicly available. 1 arXiv:2403.03206v1 [cs.CV] 5 Mar 2024 Scaling Rectified Flow Transformers for High-Resolution Image Synthesis outperforms the model that only utilizes original captions. We thus use the 50/50 synthetic/original caption mix for the remainder of this work. 5.2.3. IMPROVED TEXT-TO-IMAGE BACKBONES In this section, we compare the performance of existing transformer-based diffusion backbones with our novel multimodal transformer-based diffusion backbone, MM-DiT, as introduced in Section 4. MM-DiT is specifically designed to handle different domains, here text and image tokens, using (two) different sets of trainable model weights. More specifically, we follow the experimental setup from Section 5.1 and compare text-to-image performance on CC12M of DiT, CrossDiT (DiT but with cross-attending to the text tokens instead of sequence-wise concatenation (Chen et al.,…
