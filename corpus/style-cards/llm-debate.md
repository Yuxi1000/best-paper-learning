# Style card: llm-debate

- title: Debating with More Persuasive LLMs Leads to More Truthful Answers
- award: ICML 2024 Best Paper
- type: empirical-science
- figures_extracted: 10 (analysis-diagram, qualitative, quantitative)
- pages: 72

## What to steal (patterns, not sentences)

- Abstract shape: problem -> limitation of status quo -> this paper's move -> evidence of success.
- Match this paper when the user's draft is: protocol-paper, human-study, claim-with-controls.
- Open the abstract file and 1-2 argument excerpts before imitating.

## Figure inventory

- `figures/quantitative/llm-debate-p02-01.png` (quantitative, p.2) Figure 1. Across all judges, using debate helps to answer questions better than baselines. Accuracy of non-expert judges using expert(s) to answer comprehension questions, and base
- `figures/analysis-diagram/llm-debate-p07-02.png` (analysis-diagram, p.7) Figure 2. An illustration of our set-up. We investigate three protocols for evaluating stronger models (experts) in the QuALITY dataset. Expert models, who can access the underlyin
- `figures/qualitative/llm-debate-p25-03.png` (qualitative, p.25) Figure 2. Furthermore, we introduce unsupervised metrics for evaluating the strength of the debaters. 2.1. Protocols Debate — We first introduce debate, a protocol in which two exp
- `figures/quantitative/llm-debate-p26-04.png` (quantitative, p.26) Figure 3. Stronger debaters result in better judge accuracy. We conduct a tournament between four different LLMs under best-of-n (boN) and critique-and-refinement (cN) optimisation
- `figures/quantitative/llm-debate-p27-05.png` (quantitative, p.27) Figure 4. Stronger consultants result in worse judge accuracy. (Left) Win rate vs best-of-N for consultants by assignment. Incorrect consultants become relatively more persuasive t
- `figures/quantitative/llm-debate-p28-06.png` (quantitative, p.28) Figure 5. Different judges produce different ratings and accuracies for the same self-play debates. We find that GPT-4-Turbo is the strongest judge, achieving higher accuracy for a
- `figures/quantitative/llm-debate-p29-07.png` (quantitative, p.29) Figure 6. Human judges, using debate, achieve high accuracy and are well-calibrated. (Left) Judge accuracy of different protocols: Debate and Interactive Debate outperform their re
- `figures/quantitative/llm-debate-p30-08.png` (quantitative, p.30) Figure 7. More persuasive debaters results in better judge accuracy whereas the opposite is true for consultants. (Left) Judge accuracy decreases with aggregate win rate for the co
- `figures/quantitative/llm-debate-p32-09.png` (quantitative, p.32) Figure 7. The data presented include only Claude 2.1 and GPT-4-Turbo experts employing the best-of-N augmentation strategy. For simplicity, results from the critique-and-refinement
- `figures/quantitative/llm-debate-p45-10.png` (quantitative, p.45) Figure 6. Figure 8 shows two main insights: 1. We find that debate is still a stronger oversight protocol over a larger set of questions than consultancy for each non-expert judge.
