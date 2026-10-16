# Style card: train-for-the-worst

- title: Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions
- award: ICML 2025 Outstanding Paper
- type: analysis-theory
- figures_extracted: 5 (qualitative, quantitative, teaser)
- pages: 21

## What to steal (patterns, not sentences)

- Abstract shape: problem -> limitation of status quo -> this paper's move -> evidence of success.
- Match this paper when the user's draft is: train-test-mismatch, theory-plus-simple-fix, headline-jump.
- Open the abstract file and 1-2 argument excerpts before imitating.

## Figure inventory

- `figures/teaser/train-for-the-worst-p03-01.png` (teaser, p.3) Figure 1. (Top) MDM training can be seen as learning multiple masked prediction problems, where some are harder to learn, leading to performance imbalance (Section 3). (Bottom) Dur
- `figures/qualitative/train-for-the-worst-p03-02.png` (qualitative, p.3) Figure 1. (Top) MDM training can be seen as learning multiple masked prediction problems, where some are harder to learn, leading to performance imbalance (Section 3). (Bottom) Dur
- `figures/qualitative/train-for-the-worst-p05-03.png` (qualitative, p.5) Figure 2. Left: MDMs train on hard problems (Section 3.2). x-axis and y-axis correspond to log(FLOPs) and −log pθ(x), respectively. MDM (Blue) is worse than ARM (Orange) in likelih
- `figures/qualitative/train-for-the-worst-p07-04.png` (qualitative, p.7) Figure 3. Generative Perplexity. We compare the resulting generative perplexity (GenPPL) of adaptive vs. vanilla MDM inference. We employ a pretrained 170M MDM and LLaMA-7B (Touvro
- `figures/quantitative/train-for-the-worst-p16-05.png` (quantitative, p.16) Figure 4. Overlap achieved by belief propagation initialized at ground truth versus random for planted CSP with k = 3, m = 3, and g = NAE, for N = 10000 and varying choices of aver
