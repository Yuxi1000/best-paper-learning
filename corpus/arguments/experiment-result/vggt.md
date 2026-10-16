# VGGT: Visual Geometry Grounded Transformer

- id: `vggt`
- award: CVPR 2025 Best Paper
- section_bucket: experiment-result
- source: arXiv:2503.11651

## Excerpt (truncated; study the move, do not copy)

RANSAC thresholds) from Roma [33]. Despite not being explicitly trained for two-view matching, Tab. 4 shows that VGGT achieves the highest accuracy among all baselines. 4.5. Ablation Studies Feature Backbone. We first validate the effectiveness of our proposed Alternating-Attention design by comparing it 8 w. Lcamera w. Ldepth w. Ltrack Acc.↓ Comp.↓ Overall↓ ✗ ✓ ✓ 1.042 0.627 0.834 ✓ ✗ ✓ 0.920 0.534 0.727 ✓ ✓ ✗ 0.976 0.603 0.790 ✓ ✓ ✓ 0.901 0.518 0.709 Table 6. Ablation Study for Multi-task Learning, which shows that simultaneous training with camera, depth and track estimation yields the highest accuracy in point map estimation on ETH3D. against two alternative attention architectures: (a) global self-attention only, and (b) cross-attention. To ensure a fair comparison, all model variants maintain an identical number of parameters, using a total of 2L attention layers. For the cross-attention variant, each frame independently attends to tokens from all other frames, maximizing cross-frame information fusion although significantly increasing the runtime, particularly as the number of input frames grows. The hyperparameters such as the hidden dimension and the number of heads are kept the same. Point map estimation accuracy is chosen as the evaluation metric for our ablation study, as it reflects the model’s joint understanding of scene geometry and camera parameters. Results…
