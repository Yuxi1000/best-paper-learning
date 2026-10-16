# Style card: shallow-safety

- title: Safety Alignment Should Be Made More Than Just a Few Tokens Deep
- award: ICLR 2025 Outstanding Paper
- type: analysis-method
- figures_extracted: 7 (qualitative, quantitative, teaser)
- pages: 25

## What to steal (patterns, not sentences)

- Abstract shape: problem -> limitation of status quo -> this paper's move -> evidence of success.
- Match this paper when the user's draft is: unifying-explanation, case-study-structure, mitigation-from-diagnosis.
- Open the abstract file and 1-2 argument excerpts before imitating.

## Figure inventory

- `figures/teaser/shallow-safety-p04-01.png` (teaser, p.4) Figure 1: Per-token KL Divergence between Aligned and Unaligned Models on Harmful HEx-PHI. Current Safety-aligned Models Exploit This Shortcut. We provide evidence that current saf
- `figures/qualitative/shallow-safety-p04-02.png` (qualitative, p.4) Figure 2: ASR vs. Number of Prefilled Harmful Tokens, with ˆy ∼ πθ(·|x, y≤k) on Harmful HEx-PHI. Prefilling Attacks. A simple exploit is to prefill the first few tokens with a non-
- `figures/qualitative/shallow-safety-p05-03.png` (qualitative, p.5) Figure 2. As shown, when conditioned on an increasing number of harmful tokens, the aligned models’ likelihood of generating harmful content increases quickly from near zero to ove
- `figures/qualitative/shallow-safety-p05-04.png` (qualitative, p.5) Figure 3: Then per-token dynamics when fine-tuning Llama-2-7B-Chat on the 100 Harmful Examples from Qi et al. [22]. Note: 1) ASR of initially aligned model = 1.5%; 2) After 2 gradi
- `figures/qualitative/shallow-safety-p05-05.png` (qualitative, p.5) Figure 3: Then per-token dynamics when fine-tuning Llama-2-7B-Chat on the 100 Harmful Examples from Qi et al. [22]. Note: 1) ASR of initially aligned model = 1.5%; 2) After 2 gradi
- `figures/quantitative/shallow-safety-p07-06.png` (quantitative, p.7) Figure 4: The data augmentation induces larger KL divergence on Harmful HEx-PHI (Section 2.2) over the later tokens of harmful responses. Effects of The Data Augmentation. 1) Align
- `figures/qualitative/shallow-safety-p18-07.png` (qualitative, p.18) Figure 5: Per-token Gradient Norm When Fine-tuning Llama-2-7B-Chat on Benign Downstream Tasks Datasets. Note: 1) ASR of initially aligned model = 1.5%; 2) After 10 gradient steps o
