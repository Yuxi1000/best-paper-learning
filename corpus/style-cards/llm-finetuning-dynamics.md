# Style card: llm-finetuning-dynamics

- title: Learning Dynamics of LLM Finetuning
- award: ICLR 2025 Outstanding Paper
- type: analysis-theory
- figures_extracted: 9 (analysis-diagram, qualitative)
- pages: 41

## What to steal (patterns, not sentences)

- Abstract shape: problem -> limitation of status quo -> this paper's move -> evidence of success.
- Match this paper when the user's draft is: mechanism-explanation, theory-to-fix, influence-analysis.
- Open the abstract file and 1-2 argument excerpts before imitating.

## Figure inventory

- `figures/analysis-diagram/llm-finetuning-dynamics-p03-01.png` (analysis-diagram, p.3) Figure 1: The per-step learning dynamics and the accumulated influence in an MNIST experiment. At(xo) = I −1π⊤ θt(xo) only depends on the model’s current predicted probability. The
- `figures/analysis-diagram/llm-finetuning-dynamics-p03-02.png` (analysis-diagram, p.3) Figure 1: The per-step learning dynamics and the accumulated influence in an MNIST experiment. At(xo) = I −1π⊤ θt(xo) only depends on the model’s current predicted probability. The
- `figures/analysis-diagram/llm-finetuning-dynamics-p03-03.png` (analysis-diagram, p.3) Figure 1: The per-step learning dynamics and the accumulated influence in an MNIST experiment. At(xo) = I −1π⊤ θt(xo) only depends on the model’s current predicted probability. The
- `figures/analysis-diagram/llm-finetuning-dynamics-p03-04.png` (analysis-diagram, p.3) Figure 1: The per-step learning dynamics and the accumulated influence in an MNIST experiment. At(xo) = I −1π⊤ θt(xo) only depends on the model’s current predicted probability. The
- `figures/analysis-diagram/llm-finetuning-dynamics-p03-05.png` (analysis-diagram, p.3) Figure 1: The per-step learning dynamics and the accumulated influence in an MNIST experiment. At(xo) = I −1π⊤ θt(xo) only depends on the model’s current predicted probability. The
- `figures/qualitative/llm-finetuning-dynamics-p08-06.png` (qualitative, p.8) Figure 3: First three: learning dynamics of SFT on different response types. Fourth: SFT 10 epochs then DPO. Last: the accumulated influence when SFT using different y (full result
- `figures/qualitative/llm-finetuning-dynamics-p36-07.png` (qualitative, p.36) Figure 5: Learning dynamics of the baseline and the proposed method with training data extension. Key trends to observe: 1.) Baseline and the extend method have similar behavior on
- `figures/qualitative/llm-finetuning-dynamics-p39-08.png` (qualitative, p.39) Figure 5. It is clear that the squeezing effect is mitigated, because the confidence of other responses all decays slower during DPO, and we also observe a big drop in the greedyde
- `figures/analysis-diagram/llm-finetuning-dynamics-p41-09.png` (analysis-diagram, p.41) Figure 2. By doing so, the big negative gradient no longer exists, and so does the squeezing effect. That is partly why this method is more stable and performs better. C THE “RELAT
