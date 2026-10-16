# Learning Dynamics of LLM Finetuning

- id: `llm-finetuning-dynamics`
- award: ICLR 2025 Outstanding Paper
- section_bucket: limitation-scope
- source: arXiv:2407.10490

## Excerpt (truncated; study the move, do not copy)

Learning dynamics, which depict how the model’s prediction changes when it learns new examples, provide a powerful tool to analyze the behavior of models trained with gradient descent. To better utilize this tool in the context of LLM finetuning, we first derive the step-wise decomposition of LLM finetuning for various common algorithms. Then, we propose a unified framework for understanding LLM predictions’ behaviors across different finetuning methods. The proposed analysis successfully explains various phenomena during LLM’s instruction tuning and preference tuning, some of them are quite counter-intuitive. We also shed light on how specific hallucinations are introduced in the SFT stage, as previously observed (Gekhman et al. 2024), and where the improvements of some new RL-free algorithms come from compared with the vanilla off-policy DPO. The analysis of the squeezing effect also has the potential to be applied to other deep learning systems which apply big negative gradients to already-unlikely outcomes. Finally, inspired by this analysis, we propose a simple (but counter-intuitive) method that is effective in improving the alignment of models. 10 Published as a conference paper at ICLR 2025 ACKNOWLEDGEMENTS This research was enabled in part by support provided by the Canada CIFAR AI Chairs program, WestGrid, and Compute Canada. We thank Shangmin Guo, Noam Razin, Wonho…
