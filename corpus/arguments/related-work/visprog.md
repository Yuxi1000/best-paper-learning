# Visual Programming: Compositional Visual Reasoning Without Training

- id: `visprog`
- award: CVPR 2023 Best Paper
- section_bucket: related-work
- source: arXiv:2211.11559

## Excerpt (truncated; study the move, do not copy)

Neuro-symbolic approaches have seen renewed momentum owing to the incredible understanding, generation, and in-context learning capabilities of large language models (LLMs). We now discuss previous program generation and execution approaches for visual tasks, recent work in using LLMs for vision, and advances in reasoning methods for language tasks. Program generation and execution for visual tasks. Neural module networks (NMN) [2] pioneered modular and compositional approaches for the visual question answering (VQA) task. NMNs compose neural modules into an end-to-end differentiable network. While early attempts use off-the-shelf parsers [2], recent methods [9,10,12] learn the layout generation model jointly with the neural modules using REINFORCE [33] and weak answer supervision. While similar in spirit to NMNs, VISPROG has several advantages over NMNs. First, VISPROG generates high-level programs that invoke trained state-of-the-art neural models and other python functions at intermediate steps as opposed to generating end-to-end neural networks. This makes it easy to incorporate symbolic, non-differentiable modules. Second, VISPROG leverages the in-context learning ability of LLMs [5] to generate programs by prompting the LLM (GPT-3) with a natural language instruction (or a visual question or a statement to be veriﬁed) along with a few examples of similar instructions and…
