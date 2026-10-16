# Swin Transformer: Hierarchical Vision Transformer using Shifted Windows

- id: `swin`
- award: ICCV 2021 Best Paper (Marr Prize)
- section_bucket: method-mechanism
- source: arXiv:2103.14030

## Excerpt (truncated; study the move, do not copy)

3.1. Overall Architecture An overview of the Swin Transformer architecture is presented in Figure 3, which illustrates the tiny version (SwinT). It ﬁrst splits an input RGB image into non-overlapping patches by a patch splitting module, like ViT. Each patch is treated as a “token” and its feature is set as a concatenation of the raw pixel RGB values. In our implementation, we use a patch size of 4 × 4 and thus the feature dimension of each patch is 4 × 4 × 3 = 48. A linear embedding layer is applied on this raw-valued feature to project it to an arbitrary dimension (denoted as C). Several Transformer blocks with modiﬁed self-attention computation (Swin Transformer blocks) are applied on these patch tokens. The Transformer blocks maintain the number of tokens ( H 4 × W 4 ), and together with the linear embedding are referred to as “Stage 1”. To produce a hierarchical representation, the number of tokens is reduced by patch merging layers as the network gets deeper. The ﬁrst patch merging layer concatenates the features of each group of 2 × 2 neighboring patches, and applies a linear layer on the 4C-dimensional concatenated features. This reduces the number of tokens by a multiple of 2×2 = 4 (2× downsampling of resolution), and the output dimension is set to 2C. Swin Transformer blocks are applied afterwards for feature transformation, with the resolution kept at H 8 × W 8 .…
