# Vision Transformers Need Registers

- id: `vit-registers`
- award: ICLR 2024 Outstanding Paper
- section_bucket: limitation-scope
- source: arXiv:2309.16588

## Excerpt (truncated; study the move, do not copy)

In this work, we exposed artifacts in the feature maps of DINOv2 models, and found this phenomenon to be present in multiple existing popular models. We have described a simple method to detect these artifacts by observing that they correspond to tokens with an outlier norm value at the output of the Transformer model. Studying their location, we have proposed an interpretation that models naturally recycle tokens from low-informative areas and repurpose them into a different role for inference. Following this interpretation, we have proposed a simple fix, consisting of appending additional tokens to the input sequence that are not used as outputs, and have found that this entirely removes the artifacts, improving the performance in dense prediction and object discovery. Moreover, we have shown that the proposed solution also removes the same artifacts present in supervised models such as DeiT-III and OpenCLIP, confirming the generality of our solution. 9 Published as a conference paper at ICLR 2024 ACKNOWLEDGMENTS We thank Hu Xu, Oriane Sim´eoni, Mido Assran and Armand Joulin for their insightful discussions and help during the course of this work. We thank Pyrrhus for posing for fig 8. Julien Mairal was supported by ANR 3IA MIAI@Grenoble Alpes (ANR-19-P3IA-0003) and by ERC grant number 101087696 (APHELEIA project). REFERENCES Hangbo Bao, Li Dong, and Furu Wei. Beit: Bert…
