# VideoPoet: A Large Language Model for Zero-Shot Video Generation

- id: `videopoet`
- award: ICML 2024 Best Paper
- section_bucket: method-mechanism
- source: arXiv:2312.14125

## Excerpt (truncated; study the move, do not copy)

demonstrated the effectiveness of LLMs in text-to-image generation, e.g., DALL-E (Ramesh et al., 2022), Parti (Yu et al., 2022) and (Ding et al., 2021), and text-to-video, e.g., CogVideo (Hong et al., 2022)), language models have not reached a level of quality on par with video diffusion models in tasks like text-to-video generation as shown in previous studies (Nash et al., 2022; Villegas et al., 2022). In contrast to training exclusively for text-to-video tasks, the generative pretraining stage to learn a foundation (Bommasani et al., 2021) by examining pretraining tasks that extend beyond text-to-video generation. A notable advantage of employing LLMs in video generation lies in the ease of integrating existing LLM frameworks. This integration allows for reusing LLM infrastructure and leverages the optimizations our community has developed over many years for LLMs, including optimizations in learning recipes for model scaling (Brown et al., 2020; Chowdhery et al., 2022), training and inference infrastructure (Du et al., 2022), hardware, among other advancements. This couples with their flexibility in encoding many diverse tasks in the same model (Raffel et al., 2020), which stands in contrast to most diffusion models where architectural changes and adapter modules are the dominant approach used to adapt the model to more diverse tasks (Zhang et al., 2023b). In this paper,…
