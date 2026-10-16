# Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions

- id: `train-for-the-worst`
- award: ICML 2025 Outstanding Paper
- section_bucket: method-mechanism
- source: arXiv:2502.06768

## Excerpt (truncated; study the move, do not copy)

# Param Accuracy ARM (w/o ordering) 42M 9.73% ARM (with ordering) 87.18% MDM (vanilla) 6M 6.88% MDM (Top probability) 18.51% MDM (Top prob. margin) 89.49% on L&O-NAE-SAT and text data, before turning to our primary application to logic puzzles. L&O-NAE-SAT and text data. For the L&O-NAE-SAT distribution defined in Section 3.3, we evaluate the effectiveness of adaptive inference by measuring the accuracy in predicting the observation tokens. Table 1 in the appendix reveals a clear improvement over vanilla inference. For the text dataset, we evaluate using the standard metric of generative perplexity, by which likelihood is measured by a large language model. We also compute the entropy of the generated samples to ensure both inference strategies exhibit similar levels of diversity. As shown in Fig. 3, we observe a substantial decrease in generative perplexity using adaptive inference. We defer further experimental details to Appendix D.1. Logic puzzles. We consider two different types of logic puzzles: Sudoku and Zebra (Einstein) puzzles. Intuitively, for Sudoku, some empty (masked) cells are significantly easier to predict than others and we want to choose the cells that are easier to predict during the inference. We evaluate the effectiveness of adaptive MDM inference over vanilla MDM inference in selecting such cells.2 To measure the performance of an inference method, we…
