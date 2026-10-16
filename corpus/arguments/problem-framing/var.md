# Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction

- id: `var`
- award: NeurIPS 2024 Best Paper
- section_bucket: problem-framing
- source: arXiv:2404.02905

## Excerpt (truncated; study the move, do not copy)

Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction Keyu Tian1,2, Yi Jiang2,†, Zehuan Yuan2,∗, Bingyue Peng2, Liwei Wang1,∗ 1Peking University 2Bytedance Inc keyutian@stu.pku.edu.cn, jiangyi.enjoy@bytedance.com, yuanzehuan@bytedance.com, bingyue.peng@bytedance.com, wanglw@pku.edu.cn Try and explore our online demo at: https://var.vision Codes and models: https://github.com/FoundationVision/VAR Figure 1: Generated samples from Visual AutoRegressive (VAR) transformers trained on ImageNet. We show 512×512 samples (top), 256×256 samples (middle), and zero-shot image editing results (bottom). Abstract We present Visual AutoRegressive modeling (VAR), a new generation paradigm that redefines the autoregressive learning on images as coarse-to-fine “next-scale prediction” or “next-resolution prediction”, diverging from the standard raster-scan “next-token prediction”. This simple, intuitive methodology allows autoregressive (AR) transformers to learn visual distributions fast and can generalize well: VAR, for the first time, makes GPT-style AR models surpass diffusion transformers in image generation. On ImageNet 256×256 benchmark, VAR significantly improve AR baseline by improving Fréchet inception distance (FID) from 18.65 to 1.73, inception score (IS) from 80.4 to 350.2, with 20× faster inference speed. It is also empirically verified that VAR…
