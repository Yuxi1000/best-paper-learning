# Appendix: Vision Transformers Need Registers

- id: `vit-registers`
- award: ICLR 2024 Outstanding Paper
- arXiv: 2309.16588
- appendix_present: true
- start_page: 12
- appendix_pages: 10
- detection: override
- genres: other

## Table of contents

- `A` Appendix (opening) — *other* (p.12)

## Excerpts (study the move, do not copy)

### A. Appendix (opening)

- genre: `other`
- start_page: 12

Published as a conference paper at ICLR 2024 Figure 10: Feature norms along locations: proportion of tokens with norm larger than the cutoff value at a given location. Left: official DINOv2 model (no antialiasing), right: our models (with antialiasing). At some positions, more than 20% of tokens have a high norm. Figure 11: Propagating unit gradients through a bicubic interpolation (16 × 16 →7 × 7) without antialiasing. We observe a striping pattern similar to the one of Fig. 10 (left). A INTERPOLATION ARTIFACTS AND OUTLIER POSITION DISTRIBUTION We plot in Figure 10 (left) the proportion of outlier tokens, characterized by a norm larger than the cutoff value defined manually, following the distribution of norms shown in Fig. 3 (main text). We make two observations: First, the distribution has a vertical-striped pattern. We investigate this phenomenon and notice that in the original DINOv2 implementation, during training the position embeddings are interpolated from a 16 × 16 map into a 7 × 7 map, without antialiasing. Propagating unit gradients through such an interpolation function (bicubic resize) leads to the following gradients, shown in Fig. 11. In this work, when producing…

## Page renders

- `figures/appendix/vit-registers/page-12.png`
- `figures/appendix/vit-registers/page-13.png`
- `figures/appendix/vit-registers/page-14.png`
- `figures/appendix/vit-registers/page-15.png`
- `figures/appendix/vit-registers/page-16.png`
- `figures/appendix/vit-registers/page-17.png`
- `figures/appendix/vit-registers/page-18.png`
- `figures/appendix/vit-registers/page-19.png`
