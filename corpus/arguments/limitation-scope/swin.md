# Swin Transformer: Hierarchical Vision Transformer using Shifted Windows

- id: `swin`
- award: ICCV 2021 Best Paper (Marr Prize)
- section_bucket: limitation-scope
- source: arXiv:2103.14030

## Excerpt (truncated; study the move, do not copy)

This paper presents Swin Transformer, a new vision Transformer which produces a hierarchical feature repre8 ImageNet COCO ADE20k Backbone top-1 top-5 APbox APmask mIoU sliding window Swin-T 81.4 95.6 50.2 43.5 45.8 Performer [14] Swin-T 79.0 94.2 shifted window Swin-T 81.3 95.6 50.5 43.7 46.1 Table 6. Accuracy of Swin Transformer using different methods for self-attention computation on three benchmarks. sentation and has linear computational complexity with respect to input image size. Swin Transformer achieves the state-of-the-art performance on COCO object detection and ADE20K semantic segmentation, signiﬁcantly surpassing previous best methods. We hope that Swin Transformer’s strong performance on various vision problems will encourage uniﬁed modeling of vision and language signals. As a key element of Swin Transformer, the shifted window based self-attention is shown to be effective and efﬁcient on vision problems, and we look forward to investigating its use in natural language processing as well. Acknowledgement We thank many colleagues at Microsoft for their help, in particular, Li Dong and Furu Wei for useful discussions; Bin Xiao, Lu Yuan and Lei Zhang for help on datasets. A1. Detailed Architectures The detailed architecture speciﬁcations are shown in Table 7, where an input image size of 224×224 is assumed for all architectures. “Concat n × n” indicates a…
