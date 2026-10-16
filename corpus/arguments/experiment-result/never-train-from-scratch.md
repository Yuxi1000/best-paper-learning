# Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors

- id: `never-train-from-scratch`
- award: ICLR 2024 Outstanding Paper
- section_bucket: experiment-result
- source: arXiv:2310.02980

## Excerpt (truncated; study the move, do not copy)

Range Arena), where models are randomly initialized and trained to predict a target label from an input sequence. In this work, we show that random initialization leads to gross overestimation of the differences between architectures and that pretraining with standard denoising objectives, using only the downstream task data, leads to dramatic gains across multiple architectures and to very small gaps between Transformers and state space models (SSMs). In stark contrast to prior works, we find vanilla Transformers to match the performance of S4 on Long Range Arena when properly pretrained, and we improve the best reported results of SSMs on the PathX-256 task by 20 absolute points. Subsequently, we analyze the utility of previously-proposed structured parameterizations for SSMs and show they become mostly redundant in the presence of data-driven initialization obtained through pretraining. Our work shows that, when evaluating different architectures on supervised tasks, incorporation of data-driven priors via pretraining is essential for reliable performance estimation, and can be done efficiently. 1 (ii) We report large empirical gains over the previously-reported performances on LRA across a range of architectures and, in particular, improve upon the best reported accuracy on the challenging PathX-256 task by 20 absolute points (67 →87). (iii) We demonstrate how…
