# Appendix/other: Vision Transformers Need Registers

- id: `vit-registers`
- source: arXiv:2309.16588

## A. Appendix (opening)

Published as a conference paper at ICLR 2024 Figure 10: Feature norms along locations: proportion of tokens with norm larger than the cutoff value at a given location. Left: official DINOv2 model (no antialiasing), right: our models (with antialiasing). At some positions, more than 20% of tokens have a high norm. Figure 11: Propagating unit gradients through a bicubic interpolation (16 × 16 →7 × 7) without antialiasing. We observe a striping pattern similar to the one of Fig. 10 (left). A INTERPOLATION ARTIFACTS AND OUTLIER POSITION DISTRIBUTION We plot in Figure 10 (left) the proportion of outlier tokens, characterized by a norm larger than the cutoff value defined manually, following the distribution of norms shown in Fig. 3 (main text). We make two observations: First, the distribution has a vertical-striped pattern. We investigate this phenomenon and notice that in the original DINOv2 implementation, during training the position embeddings are interpolated from a 16 × 16 map into a 7 × 7 map, without antialiasing. Propagating unit gradients through such an interpolation function (bicubic resize) leads to the following gradients, shown in Fig. 11. In this work, when producing…
