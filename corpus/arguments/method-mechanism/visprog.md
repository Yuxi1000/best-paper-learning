# Visual Programming: Compositional Visual Reasoning Without Training

- id: `visprog`
- award: CVPR 2023 Best Paper
- section_bucket: method-mechanism
- source: arXiv:2211.11559

## Excerpt (truncated; study the move, do not copy)

makes it challenging to scale to the inﬁnitely long tail of complex tasks we would eventually like these systems to perform. In this work, we explore the use of large language models to tackle the long tail of complex tasks by decomposing these tasks described in natural language into simpler steps that may be handled by specialized end-to-end trained models or other programs. Imagine instructing a vision system to “Tag the 7 main characters on the TV show Big Bang Theory in this image.” To perform this task, the system ﬁrst needs to understand the intent of the instruction and then perform a sequence of steps - detect the faces, retrieve list of main characters on Big Bang Theory from a knowledge base, classify faces using the list of characters, and tag the image with recognized character’s faces and names. While different vision and language systems exist to perform each of these steps, executing this task described in natural language is beyond the scope of end-to-end trained systems. We introduce VISPROG which inputs visual data (a single image or a set of images) along with a natural language instruction, generates a sequence of steps, a visual program if you will, and then executes these steps to produce the desired output. Each line in a visual program invokes one among a wide range of modules currently supported by the system. Modules may be off-the-shelf computer…
