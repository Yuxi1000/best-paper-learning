# Rich Human Feedback for Text-to-Image Generation

- id: `richhf`
- award: CVPR 2024 Best Paper
- section_bucket: experiment-result
- source: arXiv:2312.10240

## Excerpt (truncated; study the move, do not copy)

For score prediction tasks, we report the Pearson linear correlation coefficient (PLCC) and Spearman rank correlation coefficient (SRCC), which are typical evaluation metrics for score predictions [29]. For heatmap prediction tasks, a straightforward way to evaluate the results would be to borrow standard saliency heatmap metrics cannot be applied directly in our case as all these metrics assume the ground truth heatmap is not empty; yet in our case, empty ground truth is possible (e.g., for artifact/implausibility heatmap, it means the image does not have any artifact/implausibility). As such, we report MSE on all samples and on those with empty ground truth, respectively, and report saliency heatmap evaluation metrics like NSS/KLD/AUC-Judd/SIM/CC [5] for the samples with non-empty ground truth. For the misaligned keyword sequence prediction, we adopt the token-level precision, recall, and F1-score. Specifically, the precision/recall/F1 scores are computed for the misaligned keywords over all the samples. Baselines For comparison, we finetune two ResNet-50 models [18], with multiple fully connected layers and deconvolution heads to predict the scores and heatmaps, respectively. We also use the off-the-shelf…
