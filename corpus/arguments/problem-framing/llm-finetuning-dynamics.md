# Learning Dynamics of LLM Finetuning

- id: `llm-finetuning-dynamics`
- award: ICLR 2025 Outstanding Paper
- section_bucket: problem-framing
- source: arXiv:2407.10490

## Excerpt (truncated; study the move, do not copy)

arXiv:2407.10490v4 [cs.LG] 29 Jun 2025 Published as a conference paper at ICLR 2025 LEARNING DYNAMICS OF LLM FINETUNING Yi Ren University of British Columbia renyi.joshua@gmail.com Danica J. Sutherland University of British Columbia & Amii dsuth@cs.ubc.ca ABSTRACT Learning dynamics, which describes how the learning of specific training examples influences the model’s predictions on other examples, gives us a powerful tool for understanding the behavior of deep learning systems. We study the learning dynamics of large language models during different types of finetuning, by analyzing the step-wise decomposition of how influence accumulates among different potential responses. Our framework allows a uniform interpretation of many interesting observations about the training of popular algorithms for both instruction tuning and preference tuning. In particular, we propose a hypothetical explanation of why specific types of hallucination are strengthened after finetuning, e.g., the model might use phrases or facts in the response for question B to answer question A, or the model might keep repeating similar simple phrases when generating responses. We also extend our framework and highlight a unique “squeezing effect” to explain a previously observed phenomenon in off-policy direct preference optimization (DPO), where running DPO for too long makes even the desired outputs less…
