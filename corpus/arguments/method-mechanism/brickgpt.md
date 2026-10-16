# Generating Physically Stable and Buildable Brick Structures from Text

- id: `brickgpt`
- award: ICCV 2025 Best Paper (Marr Prize)
- section_bucket: method-mechanism
- source: arXiv:2505.05469

## Excerpt (truncated; study the move, do not copy)

• Physically stable: Built on a baseplate with strong structural integrity, without floating or collapsing bricks. • Buildable: Compatible with standard toy brick pieces and able to be assembled brick-by-brick by humans or robots. In this work, we introduce BRICKGPT with the key insight of repurposing autoregressive large language models, originally trained for next-token prediction, for next-brick prediction. We formulate the problem of brick structure design as an autoregressive text generation task, where the next-brick dimension and placement are specified with a simple textual format. To ensure generated structures are both stable and buildable, we enforce physics-aware assembly constraints during both training and inference. During training, we construct a large-scale dataset of physically stable brick structures paired with captions. During autoregressive inference, we enforce feasibility with an efficient validity check and physics-aware rollback to ensure that the final tokens adhere to physics laws and assembly constraints. Our experiments show that the generated designs are stable, diverse, and visually appealing while adhering to input prompts. Our method outperforms pre-trained LLMs with or without in-context learning, and previous approaches based on 3D mesh generation. Finally, we explore applications such as text-driven brick texturing, as well as manual…
