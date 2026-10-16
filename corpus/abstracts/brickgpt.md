# Generating Physically Stable and Buildable Brick Structures from Text

- id: `brickgpt`
- award: ICCV 2025 Best Paper (Marr Prize)
- venue: ICCV 2025
- arXiv: [2505.05469](https://arxiv.org/abs/2505.05469)
- authors: Ava Pun, Kangle Deng, Ruixuan Liu, Deva Ramanan, Changliu Liu, Jun-Yan Zhu
- posted: 2025-05-08
- license: see arXiv page
- paper_type: method-system
- use_for: constraint-in-decoding, qualitative, dataset-plus-method

## Abstract

We introduce BrickGPT, the first approach for generating physically stable interconnecting brick assembly models from text prompts. To achieve this, we construct a large-scale, physically stable dataset of brick structures, along with their associated captions, and train an autoregressive large language model to predict the next brick to add via next-token prediction. To improve the stability of the resulting designs, we employ an efficient validity check and physics-aware rollback during autoregressive inference, which prunes infeasible token predictions using physics laws and assembly constraints. Our experiments show that BrickGPT produces stable, diverse, and aesthetically pleasing brick structures that align closely with the input text prompts. We also develop a text-based brick texturing method to generate colored and textured designs. We show that our designs can be assembled manually by humans and automatically by robotic arms. We release our new dataset, StableText2Brick, containing over 47,000 brick structures of over 28,000 unique 3D objects accompanied by detailed captions, along with our code and models at the project website: https://avalovelace1.github.io/BrickGPT/.
