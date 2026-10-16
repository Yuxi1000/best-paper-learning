# Visual Programming: Compositional Visual Reasoning Without Training

- id: `visprog`
- award: CVPR 2023 Best Paper
- section_bucket: experiment-result
- source: arXiv:2211.11559

## Excerpt (truncated; study the move, do not copy)

4.1. Compositional Visual Question Answering VISPROG is compositional by construction which makes it suitable for the compositional, multi-step visual question answering task: GQA [11]. Modules for the GQA task include those for open vocabulary localization, a VQA module, functions for cropping image regions given bounding box co-ordinates or spatial prepositions (such as above, left, etc.), module to count boxes, and a module to evaluate Python expressions. For example, consider the question: “Is the small truck to the left or to the right of the people that are wearing helmets?”. VISPROG ﬁrst localizes “people wearing helmets”, crops the region to the left (or right) of these people, checks if there is a “small truck” on that side, and return “left” if so and “right” otherwise. VISPROG uses the question answering module based on VILT [16], but instead of simply passing the complex original question to VILT, VISPROG invokes it for simpler tasks like identifying the contents within an image patch. As a result, our resulting VISPROG for GQA is not only more interpretable than VILT but also more accurate (Tab. 1). Alternatively, one could completely eliminate the need for a QA model like ViLT and use other systems like CLIP and object detectors, but we leave that for future investigation. Evaluation. In order to limit the money spent on generating programs with GPT-3, we create…
