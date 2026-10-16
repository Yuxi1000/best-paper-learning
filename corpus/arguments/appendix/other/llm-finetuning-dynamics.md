# Appendix/other: Learning Dynamics of LLM Finetuning

- id: `llm-finetuning-dynamics`
- source: arXiv:2407.10490

## A. SIMPLE METHOD TO IMPROVE ALIGNMENT

F.1 PINPOINTING THE DRAWBACK OF OFF-POLICY DPO Based on our observations and analysis above, we speculate that “imposing big negative gradients on the valley region” is one of the bottlenecks of off-policy RL-free methods. Starting from this hypothesis, we believe introducing on-policy sampling has the potential to mitigate this problem, as demonstrated in SPIN (Z. Chen et al. 2024) and other online algorithms (S. Guo, B. Zhang, et al. 2024). However, we also speculate 38 Published as a conference paper at ICLR 2025 that these methods improve the model’s performance not only by mitigating the squeezing effect. Hence to figure out to what extent the squeezing effect can harm the model’s performance, we propose a simple yet effective method to isolate its influence. As this method can directly mitigate this effect, it can also be considered as an ablation study of this interesting phenomenon. Figure 21: Illustration of the proposed method and baseline. “E” is short for the “dataset extension”. F.2
