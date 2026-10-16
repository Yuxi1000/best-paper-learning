# VideoPoet: A Large Language Model for Zero-Shot Video Generation

- id: `videopoet`
- award: ICML 2024 Best Paper
- section_bucket: related-work
- source: arXiv:2312.14125

## Excerpt (truncated; study the move, do not copy)

Video diffusion models. Recently, numerous video generation methods use diffusion-based methods for text-tovideo (Ho et al., 2022a; Blattmann et al., 2023b; Zhang et al., 2023a; Blattmann et al., 2023a; He et al., 2023; Zhou et al., 2022; Wang et al., 2023a; Ge et al., 2023; Wang et al., 2023d;c; Singer et al., 2022; Zhang et al., 2023a; Zeng et al., 2023) and video-to-video editing (Liew et al., 2023; Feng et al., 2023; Esser et al., 2023; Chen et al., 2023b). As video diffusion models are usually derived from text-toimage diffusion models (Ramesh et al., 2021; Saharia et al., 2022), additional tasks and modalities are added via inference tricks (Meng et al., 2021), architectural changes (Esser et al., 2023; Liew et al., 2023) and adapter layers (Zhang et al., 2023b; Guo et al., 2023). Although these models are composable after training, they are not trained end-to-end in a unified framework. Our multitask pretraining strategy in a single model improves performance and provides zero-shot video generation capabilities. 2 VideoPoet: A Large Language Model for Zero-Shot Video Generation Figure 2: Sequence layout for VideoPoet. We encode all modalities into the discrete token space, so that we can directly use large language model architectures for video generation. We denote special tokens in <> (see Table 4 for definitions). The modality agnostic tokens are in darker red; the…
