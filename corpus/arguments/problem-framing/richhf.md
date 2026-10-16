# Rich Human Feedback for Text-to-Image Generation

- id: `richhf`
- award: CVPR 2024 Best Paper
- section_bucket: problem-framing
- source: arXiv:2312.10240

## Excerpt (truncated; study the move, do not copy)

Rich Human Feedback for Text-to-Image Generation Youwei Liang*†1, Junfeng He*‡2, Gang Li*‡2, Peizhao Li†5, Arseniy Klimovskiy2, Nicholas Carolan2, Jiao Sun†§3, Jordi Pont-Tuset2, Sarah Young2, Feng Yang2, Junjie Ke2, Krishnamurthy Dj Dvijotham2, Katherine M. Collins†4, Yiwen Luo2, Yang Li2, Kai J Kohlhoff2, Deepak Ramachandran2, and Vidhya Navalpakkam2 1University of California, San Diego 2Google Research 3University of Southern California 4University of Cambridge 5Brandeis University Abstract Recent Text-to-Image (T2I) generation models such as Stable Diffusion and Imagen have made significant progress in generating high-resolution images based on text descriptions. However, many generated images still suffer from issues such as artifacts/implausibility, misalignment with text descriptions, and low aesthetic quality. Inspired by the success of Reinforcement Learning with Human Feedback (RLHF) for large language models, prior works collected human-provided scores as feedback on generated images and trained a reward model to improve the T2I generation. In this paper, we enrich the feedback signal by (i) marking image regions that are implausible or misaligned with the text, and (ii) annotating which words in the text prompt are misrepresented or missing on the image. We collect such rich human feedback on 18K generated images (RichHF18K) and train a multimodal transformer to…
