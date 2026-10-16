# Scaling Rectified Flow Transformers for High-Resolution Image Synthesis

- id: `sd3-rectified-flow`
- award: ICML 2024 Best Paper
- section_bucket: problem-framing
- source: arXiv:2403.03206

## Excerpt (truncated; study the move, do not copy)

Scaling Rectified Flow Transformers for High-Resolution Image Synthesis Patrick Esser * Sumith Kulal Andreas Blattmann Rahim Entezari Jonas M¨uller Harry Saini Yam Levi Dominik Lorenz Axel Sauer Frederic Boesel Dustin Podell Tim Dockhorn Zion English Kyle Lacey Alex Goodwin Yannik Marek Robin Rombach * Stability AI Figure 1. High-resolution samples from our 8B rectified flow model, showcasing its capabilities in typography, precise prompt following and spatial reasoning, attention to fine details, and high image quality across a wide variety of styles. Abstract Diffusion models create data from noise by inverting the forward paths of data towards noise and have emerged as a powerful generative modeling technique for high-dimensional, perceptual data such as images and videos. Rectified flow is a recent generative model formulation that connects data and noise in a straight line. Despite its better theoretical properties and conceptual simplicity, it is not yet decisively established as standard practice. In this work, we improve existing noise sampling techniques for training rectified flow models by biasing them towards perceptually relevant scales. Through a large-scale study, we demon*Equal contribution . <first.last>@stability.ai. strate the superior performance of this approach compared to established diffusion formulations for high-resolution text-to-image synthesis.…
