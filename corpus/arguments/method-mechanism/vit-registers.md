# Vision Transformers Need Registers

- id: `vit-registers`
- award: ICLR 2024 Outstanding Paper
- section_bucket: method-mechanism
- source: arXiv:2309.16588

## Excerpt (truncated; study the move, do not copy)

DINOv2 (Oquab et al., 2023) is a self-supervised method for learning visual features, following the DINO work. We apply our changes to this method as it is the main focus of our study. We run this method on ImageNet-22k with the ViT-L configuration. We use the official repository 3. 3.2 An additional interesting observation is that the norms of the registers appear to be quantized, compared to the previous outliers; we leave the investigation of this phenomenon for future work. D.2 INFORMATION HELD BY TOKENS We report on table 4 the linear probing performance of models trained with and without registers, when using different tokens as representations. We evaluate on the aircrafts dataset, as it showed clear conclusions in the similar table 1. We observe that adding a register does not significantly modify the scores obtained with the [CLS] or patch tokens. However, the outlier patches are removed, and their behavior is transferred to the newly added register. 14 Published as a conference paper at ICLR 2024 top-1 accuracy #registers [CLS] normal patch outlier patch register 0 84.6 15.5 73.3 N/A 1 85.2 14.5 N/A 71.1 Table 4: Linear probing of models with and without registers on the Aircraft dataset, using various tokens as representation. We observe that the behavior of the outlier tokens, aggregating global information, is absorbed into the register. We further conduct an…
