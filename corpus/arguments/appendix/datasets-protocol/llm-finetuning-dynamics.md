# Appendix/datasets-protocol: Learning Dynamics of LLM Finetuning

- id: `llm-finetuning-dynamics`
- source: arXiv:2407.10490

## A. SIMPLE METHOD INSPIRED BY LEARNING DYNAMICS

As illustrated in Figure 21, where the baseline method is a standard SFT-then-DPO pipeline. The proposed method is very simple. We only need to augment the dataset used in SFT by adding (x, y− u ) pairs for each sample into it. All other settings are unchanged. The motivation for this method is also quite simple: as SFT can pull up the region of supervised ˆy and we don’t want the model to impose big negative gradients on a valley region, we can just pull up those y− u before DPO. Furthermore, as demonstrated in the third panel in Figure 19 and Equation (15), the negative gradient in DPO would be strong enough to push down πθt(y− u ), because the gradient will be large if the model cannot separate y+ u and y− u well. In other words, under DPO’s loss, there is no need to worry about the model overfitting those y− u during SFT. F.3 EXPERIMENTAL VERIFICATION To verify our analysis, we conduct experiments by finetuning a pretrained Qwen1.5-1.8B (J. Bai et al. 2023) model using Antropic-HH dataset (Y. Bai et al. 2022) (we use a subset containing 5000 random examples from the training split). The pipelines of different methods are demonstrated in Figure 21. In this experiment, we call…
