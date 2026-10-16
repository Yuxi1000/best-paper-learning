# Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction

- id: `var`
- award: NeurIPS 2024 Best Paper
- section_bucket: related-work
- source: arXiv:2404.02905

## Excerpt (truncated; study the move, do not copy)

2.1 Properties of large autoregressive language models Scaling laws are found and studied in autoregressive language models [43, 35], which describe a power-law relationship between the scale of model (or dataset, computation, etc.) and the crossentropy loss value on the test set. Scaling laws allow us to directly predict the performance of a larger model from smaller ones [1], thus guiding better resource allocation. More pleasingly, they show that the performance of LLMs can scale well with the growth of model, data, and computation and never saturate, which is considered a key factor in the success of [15, 82, 83, 98, 90, 38]. The success brought by scaling laws has inspired the vision community to explore more similar methods for multimodality understanding and generation [53, 2, 88, 27, 96, 77, 21, 23, 41, 31, 32, 80, 87]. Zero-shot generalization. Zero-shot generalization [72] refers to the ability of a model, particularly a Large Language Model, to perform tasks that it has not been explicitly trained on. Within the realm of the computer vision, there is a burgeoning interest in the zero-shot and in-context learning abilities of foundation models, CLIP [64], SAM [48], Dinov2 [61]. Innovations like Painter [89] and LVM [6] extend visual prompters [40, 11] to achieve in-context learning in vision. 2.2 Visual generation Raster-scan autoregressive models for visual…
