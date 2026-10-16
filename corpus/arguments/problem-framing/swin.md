# Swin Transformer: Hierarchical Vision Transformer using Shifted Windows

- id: `swin`
- award: ICCV 2021 Best Paper (Marr Prize)
- section_bucket: problem-framing
- source: arXiv:2103.14030

## Excerpt (truncated; study the move, do not copy)

Swin Transformer: Hierarchical Vision Transformer using Shifted Windows Ze Liu†* Yutong Lin†* Yue Cao* Han Hu*‡ Yixuan Wei† Zheng Zhang Stephen Lin Baining Guo Microsoft Research Asia {v-zeliu1,v-yutlin,yuecao,hanhu,v-yixwe,zhez,stevelin,bainguo}@microsoft.com Abstract This paper presents a new vision Transformer, called Swin Transformer, that capably serves as a general-purpose backbone for computer vision. Challenges in adapting Transformer from language to vision arise from differences between the two domains, such as large variations in the scale of visual entities and the high resolution of pixels in images compared to words in text. To address these differences, we propose a hierarchical Transformer whose representation is computed with Shifted windows. The shifted windowing scheme brings greater efﬁciency by limiting self-attention computation to non-overlapping local windows while also allowing for cross-window connection. This hierarchical architecture has the ﬂexibility to model at various scales and has linear computational complexity with respect to image size. These qualities of Swin Transformer make it compatible with a broad range of vision tasks, including image classiﬁcation (87.3 top-1 accuracy on ImageNet-1K) and dense prediction tasks such as object detection (58.7 box AP and 51.1 mask AP on COCO testdev) and semantic segmentation (53.5 mIoU on ADE20K val).…
