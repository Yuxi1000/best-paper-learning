# Vision Transformers Need Registers

- id: `vit-registers`
- award: ICLR 2024 Outstanding Paper
- section_bucket: related-work
- source: arXiv:2309.16588

## Excerpt (truncated; study the move, do not copy)

Feature extraction with pretrained models. Using pretrained neural network models for extracting visual features has stood the test of time since the AlexNet (Krizhevsky et al., 2012) CNN model pretrained on ImageNet-1k (Russakovsky et al., 2015). More recent models have upgraded the same setup with modern architectures, such as ResNets (used in, e.g., DETR, Carion et al., 2020) or even Vision Transformers. As Transformers are easily able to handle different modalities during training, off-the-shelf backbones are now commonly trained on label supervision (e.g., DeiT-III on ImageNet22k, Touvron et al., 2022) or text supervision (e.g., CLIP (Radford et al., 2021)), providing strong visual foundation models, scaling well with model sizes, and enabling excellent performance on a variety of tasks including detection (Carion et al., 2020) and segmentation (Zheng et al., 2021; Kirillov et al., 2023). In this context, supervision relies on annotations in the form of labels or text alignment; the dataset biases (Torralba & Efros, 2011) are not well characterized, yet they drive 8 Published as a conference paper at ICLR 2024 learning and shape the learned models. An alternative approach consists of not using supervision and letting the models learn from the data via a pretext task that is designed to require understanding the content of images (Doersch et al., 2015). This…
