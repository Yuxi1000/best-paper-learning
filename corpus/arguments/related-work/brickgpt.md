# Generating Physically Stable and Buildable Brick Structures from Text

- id: `brickgpt`
- award: ICCV 2025 Best Paper (Marr Prize)
- section_bucket: related-work
- source: arXiv:2505.05469

## Excerpt (truncated; study the move, do not copy)

Text-to-3D Generation. Text-to-3D generation has seen remarkable progress recently, driven by advances in neural rendering and generative models. Dreamfusion [60] and Score Jacobian Chaining [78] pioneer zero-shot text-to-3D generation by optimizing neural radiance fields [53] with pretrained diffusion models [64]. Subsequent work has explored alternative 3D representations [3, 34, 36, 43, 49, 52, 68] and improved loss functions [26, 45, 48, 76, 80, 86]. Rather than relying on iterative optimization, a promising alternative direction trains generative models directly on 3D asset datasets, with various backbones including diffusion models [21, 33, 35, 55, 62, 65, 88, 89, 92], large reconstruction models [22, 32, 75, 84], U-Nets [37, 70], and autoregressive models [4–6, 19, 56, 66, 69, 82]. However, these existing methods cannot be directly applied to generating brick structures as they do not account for the unique physical and assembly constraints of real-world designs [47]. We bridge this gap by introducing a method for generating physically stable and buildable brick structures directly from text prompts. Autoregressive 3D Modeling. Recent research has successfully used autoregressive models to generate 3D meshes [4– 6, 9, 19, 56, 66, 69, 82], often conditioned on input text or images. Most recently, LLaMA-Mesh [81] demonstrates that large language models (LLMs) can be…
