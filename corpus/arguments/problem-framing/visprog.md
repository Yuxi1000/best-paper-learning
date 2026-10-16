# Visual Programming: Compositional Visual Reasoning Without Training

- id: `visprog`
- award: CVPR 2023 Best Paper
- section_bucket: problem-framing
- source: arXiv:2211.11559

## Excerpt (truncated; study the move, do not copy)

Visual Programming: Compositional visual reasoning without training Tanmay Gupta, Aniruddha Kembhavi PRIOR @ Allen Institute for AI https://prior.allenai.org/projects/visprog Figure 1. VISPROG is a modular and interpretable neuro-symbolic system for compositional visual reasoning. Given a few examples of natural language instructions and the desired high-level programs, VISPROG generates a program for any new instruction using incontext learning in GPT-3 and then executes the program on the input image(s) to obtain the prediction. VISPROG also summarizes the intermediate outputs into an interpretable visual rationale (Fig. 4). We demonstrate VISPROG on tasks that require composing a diverse set of modules for image understanding and manipulation, knowledge retrieval, and arithmetic and logical operations. Abstract We present VISPROG, a neuro-symbolic approach to solving complex and compositional visual tasks given natural language instructions. VISPROG avoids the need for any task-speciﬁc training. Instead, it uses the incontext learning ability of large language models to generate python-like modular programs, which are then executed to get both the solution and a comprehensive and interpretable rationale. Each line of the generated program may invoke one of several off-the-shelf computer vision models, image processing subroutines, or python functions to produce intermediate…
