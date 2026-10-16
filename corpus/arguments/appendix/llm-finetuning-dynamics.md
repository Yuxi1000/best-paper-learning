# Appendix: Learning Dynamics of LLM Finetuning

- id: `llm-finetuning-dynamics`
- award: ICLR 2025 Outstanding Paper
- arXiv: 2407.10490
- appendix_present: true
- start_page: 16
- appendix_pages: 26
- detection: override
- genres: datasets-protocol, other

## Table of contents

- `A` SIMPLE METHOD TO IMPROVE ALIGNMENT — *other* (p.38)
- `A` SIMPLE METHOD INSPIRED BY LEARNING DYNAMICS — *datasets-protocol* (p.39)

## Excerpts (study the move, do not copy)

### A. SIMPLE METHOD TO IMPROVE ALIGNMENT

- genre: `other`
- start_page: 38

F.1 PINPOINTING THE DRAWBACK OF OFF-POLICY DPO Based on our observations and analysis above, we speculate that “imposing big negative gradients on the valley region” is one of the bottlenecks of off-policy RL-free methods. Starting from this hypothesis, we believe introducing on-policy sampling has the potential to mitigate this problem, as demonstrated in SPIN (Z. Chen et al. 2024) and other online algorithms (S. Guo, B. Zhang, et al. 2024). However, we also speculate 38 Published as a conference paper at ICLR 2025 that these methods improve the model’s performance not only by mitigating the squeezing effect. Hence to figure out to what extent the squeezing effect can harm the model’s performance, we propose a simple yet effective method to isolate its influence. As this method can directly mitigate this effect, it can also be considered as an ablation study of this interesting phenomenon. Figure 21: Illustration of the proposed method and baseline. “E” is short for the “dataset extension”. F.2

### A. SIMPLE METHOD INSPIRED BY LEARNING DYNAMICS

- genre: `datasets-protocol`
- start_page: 39

As illustrated in Figure 21, where the baseline method is a standard SFT-then-DPO pipeline. The proposed method is very simple. We only need to augment the dataset used in SFT by adding (x, y− u ) pairs for each sample into it. All other settings are unchanged. The motivation for this method is also quite simple: as SFT can pull up the region of supervised ˆy and we don’t want the model to impose big negative gradients on a valley region, we can just pull up those y− u before DPO. Furthermore, as demonstrated in the third panel in Figure 19 and Equation (15), the negative gradient in DPO would be strong enough to push down πθt(y− u ), because the gradient will be large if the model cannot separate y+ u and y− u well. In other words, under DPO’s loss, there is no need to worry about the model overfitting those y− u during SFT. F.3 EXPERIMENTAL VERIFICATION To verify our analysis, we conduct experiments by finetuning a pretrained Qwen1.5-1.8B (J. Bai et al. 2023) model using Antropic-HH dataset (Y. Bai et al. 2022) (we use a subset containing 5000 random examples from the training split). The pipelines of different methods are demonstrated in Figure 21. In this experiment, we call…

## Page renders

- `figures/appendix/llm-finetuning-dynamics/page-16.png`
- `figures/appendix/llm-finetuning-dynamics/page-17.png`
- `figures/appendix/llm-finetuning-dynamics/page-18.png`
- `figures/appendix/llm-finetuning-dynamics/page-19.png`
- `figures/appendix/llm-finetuning-dynamics/page-20.png`
- `figures/appendix/llm-finetuning-dynamics/page-21.png`
- `figures/appendix/llm-finetuning-dynamics/page-22.png`
- `figures/appendix/llm-finetuning-dynamics/page-23.png`
