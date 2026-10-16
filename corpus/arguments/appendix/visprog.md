# Appendix: Visual Programming: Compositional Visual Reasoning Without Training

- id: `visprog`
- award: CVPR 2023 Best Paper
- arXiv: 2211.11559
- appendix_present: true
- start_page: 12
- appendix_pages: 2
- detection: override
- genres: hyperparams-implementation

## Table of contents

- `A` Appendix — *hyperparams-implementation* (p.12)
- `A.1` Task Prompts — *hyperparams-implementation* (p.12)
- `A.2` Module Details — *hyperparams-implementation* (p.12)

## Excerpts (study the move, do not copy)

### A. Appendix

- genre: `hyperparams-implementation`
- start_page: 12

This appendix includes • Task prompts for VISPROG(Sec. A.1) • Module implementation details (Sec. A.2) • Many more qualitative results with visual rationales for both successful and failure cases can be found at https://prior.allenai.org/projects/visprog.

### A.1. Task Prompts

- genre: `hyperparams-implementation`
- start_page: 12

We show the prompt structures for GQA (Figure 10), NLVR (Figure 11), knowledge tagging (Figure 13), and language-guided image editing (Figure 12) tasks with 3 in- context examples each. Figure 10. GQA prompt

### A.2. Module Details

- genre: `hyperparams-implementation`
- start_page: 12

To help understand the generated programs better, we now provide a few implementation details about some of the modules. Select. The module takes a query and a category argu- ment. When the category is provided, the selection is only performed over the regions that have been identiﬁed as belonging to that category by a previous module in the program (typically the Seg module). If category is None, the selection is performed over all regions. The query is the text to be used for region-text scoring to perform the selection. We use CLIP-ViT [23] to select the region with the maximum score for the query. When the query contains multiple phrases separated by commas, the highest-scoring region is selected for each phrase. Figure 11. NLVR prompt Figure 12. Image editing prompt. Note that the prompt includes a mapping of emojis to their names in the AugLy [22] library that is used to implement Emoji module. The third example shows how to provide the category value for the Select module. Classify. The Classify module takes lists of object regions and categories and tries to assign one of the categories to each region. For simplicity, we assume the images in the tagging task has at most 1…

## Page renders

- `figures/appendix/visprog/page-12.png`
- `figures/appendix/visprog/page-13.png`
