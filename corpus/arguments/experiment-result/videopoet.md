# VideoPoet: A Large Language Model for Zero-Shot Video Generation

- id: `videopoet`
- award: ICML 2024 Best Paper
- section_bucket: experiment-result
- source: arXiv:2312.14125

## Excerpt (truncated; study the move, do not copy)

We employ a zero-shot generation the training data of target benchmarks. Specifically, the datasets, MSR-VTT (Xu et al., 2016) and UCF-101 (Soomro et al., 2012), as well as the frame prediction task on Kinetics 600 (K600) (Carreira et al., 2018), in which the first 5 frames are provided as the condition to predict the next 11 frames. We also include inpainting and outpainting tasks (Yu et al., 2023a) on Something-Something V2 (SSv2) (Goyal et al., 2017). We employ widely used metrics such as Fr´echet Video Distance (FVD) (Unterthiner et al., 2018), CLIP similarity score (Wu et al., 2021), and Inception Score (IS) (Saito et al., 2020) for evaluation. Note that the specific metrics and evaluation methods vary across different datasets. Detailed information on these variations can be found in Appendix A.5.5. We include examples of the generated videos in the supplementary materials. 5.2. Pretraining Task Analysis We investigate the learning capabilities of different combinations of pretraining tasks using a model with 300 million parameters. All task combinations are trained using a learning rate of 10−3 for the same number of steps (300k) with a batch size of 1024. For the analysis of pretraining tasks, we consider text-tovideo (T2V), text-to-image (T2I), and four self-supervised learning (SSL) tasks: frame prediction (FP), central inpainting and central outpainting (Painting)…
