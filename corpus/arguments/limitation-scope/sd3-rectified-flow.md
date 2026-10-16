# Scaling Rectified Flow Transformers for High-Resolution Image Synthesis

- id: `sd3-rectified-flow`
- award: ICML 2024 Best Paper
- section_bucket: limitation-scope
- source: arXiv:2403.03206

## Excerpt (truncated; study the move, do not copy)

Figure 5. Effects of QK-normalization. Normalizing the Q- and K-embeddings before calculating the attention matrix prevents the attention-logit growth instability (left), which causes the attention entropy to collapse (right) and has been previously reported in the discriminative ViT literature (Dehghani et al., 2023; Wortsman et al., 2023). In contrast with these previous works, we observe this instability in the last transformer blocks of our networks. Maximum attention logits and attention entropies are shown averaged over the last 5 blocks of a 2B (d=24) model. 5.3.2. FINETUNING ON HIGH RESOLUTIONS QK-Normalization In general, we pretrain all of our models on low-resolution images of size 2562 pixels. Next, we finetune our models on higher resolutions with mixed aspect ratios (see next paragraph for details). We find that, when moving to high resolutions, mixed precision training can become unstable and the loss diverges. This can be remedied by switching to full precision training — but comes with a ∼2× performance drop compared to mixedprecision training. A more efficient alternative is reported in the (discriminative) ViT literature: Dehghani et al. (2023) observe that the training of large vision transformer models diverges because the attention entropy grows uncontrollably. To avoid this, Dehghani et al. (2023) propose to normalize Q and K before the attention…
