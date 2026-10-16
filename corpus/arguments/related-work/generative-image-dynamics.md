# Generative Image Dynamics

- id: `generative-image-dynamics`
- award: CVPR 2024 Best Paper
- section_bucket: related-work
- source: arXiv:2309.07906

## Excerpt (truncated; study the move, do not copy)

Generative synthesis. Recent advances in generative models have enabled photorealistic synthesis of images conditioned on text prompts [16, 17, 24, 73–75]. These text-toimage models can be augmented to synthesize video sequences by extending the generated image tensors along a time dimension [7, 9, 43, 62, 84, 106, 106, 111]. While these methods can produce video sequences that capture the spatiotemporal statistics of real footage, these videos often suffer from artifacts like incoherent motion, unrealistic temporal variation in textures, and violations of physical constraints like preservation of mass. Animating images. Instead of generating videos entirely from text, other techniques take as input a still picture and animate it. Many recent deep learning methods adopt a 3DUnet architecture to produce video volumes directly [27, 36, 40, 47, 53, 93]. These models are effectively the same video generation models (but conditioned on image information instead of text), and exhibit similar artifacts to those mentioned above. One way to overcome these limitations is to not directly generate the video content itself, but instead animate an input source image through image-based rendering, i.e., moving the image content around according to motion derived from external sources such as a driving video [51, 80–82, 99], motion or 3D geometry priors [8, 29, 46, 63–65, 67, 90, 97, 101,…
