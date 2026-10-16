# Rich Human Feedback for Text-to-Image Generation

- id: `richhf`
- award: CVPR 2024 Best Paper
- section_bucket: method-mechanism
- source: arXiv:2312.10240

## Excerpt (truncated; study the move, do not copy)

The architecture of our model is shown in Fig. 3. We adopt a vision-language model based on ViT [14] and T5X [41] models, inspired by the Spotlight model architecture [34], but modifying both the model and pretraining datasets to better suit our tasks. We use a self-attention module [50] among the concatenated image tokens and text tokens, similar to PaLI [7], as our tasks require bidirectional information propagation. The text information is propagated to image tokens for text misalignment score and heatmap prediction, while the vision information is propagated to text tokens for better vision-aware text encoding to decode the text misalignment sequence. To pretrain the model on more diverse images, we add the natural image captioning task on the WebLI dataset [7] to the pretraining task mixture. Specifically, the ViT takes the generated image as input and outputs image tokens as high-level representations. The text prompt tokens are embedded into dense vectors. The image tokens and embedded text tokens are concatenated and encoded by the Transformer self-attention encoder in T5X. On top of the encoded fused text and image tokens, we use three kinds of predictors to predict different outputs. For heatmap prediction, the image tokens are reshaped into a feature map and sent through convolution layers, deconvolution layers, and sigmoid activation, and outputs implausibility and…
