# Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors

- id: `never-train-from-scratch`
- award: ICLR 2024 Outstanding Paper
- section_bucket: method-mechanism
- source: arXiv:2310.02980

## Excerpt (truncated; study the move, do not copy)

Listops Text Retrieval Image Pathfinder PathX Avg. Transformer 36.37 64.27 57.46 42.44 71.40 ✗ 53.66 Local Attention 15.82 52.98 53.39 41.46 66.63 ✗ 46.71 Longformer 35.63 62.85 56.89 42.22 69.71 ✗ 52.88 Linformer 35.70 53.94 52.27 38.56 76.34 ✗ 51.14 Reformer 37.27 56.10 53.40 38.07 68.50 ✗ 50.56 BigBird 36.05 64.02 59.29 40.83 74.87 ✗ 54.17 Linear Trans. 16.13 65.90 53.09 42.34 75.30 ✗ 50.46 Performer 18.01 65.40 53.82 42.77 77.05 ✗ 51.18 Transformers + Masked SPT 59.75 89.27 88.64 74.22 88.45 87.73 81.34 Transformers + Causal SPT 59.15 88.81 90.38 76.00 88.49 88.05 81.81 tasks (Text, Retrieval) following Liu et al. (2019), and to 10% for ListOps. For Transformers, we use full attention as default with the hardware-optimized FLASH implementation (Dao et al., 2022). Due to computational constraints, for tasks with sequence length at least 16K we split the input to the attention layer into non-overlapping blocks of size 4096 and allow each block to attend to itself and its neighbour(s). Our codebase is built on the original S4 repository.1 For additional experimental details, such as computational resources for SPT and finetuning, please refer to Appendix C.1. 3 RESULTS In Section 3.1, we perform SPT for LRA tasks using the official model configurations. In Section 3.2, we perform SPT for Transformers and S4. Section 3.3 evaluates the role of design choices in SSMs in the…
