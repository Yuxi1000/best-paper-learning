# Appendix/hyperparams-implementation: Generating Physically Stable and Buildable Brick Structures from Text

- id: `brickgpt`
- source: arXiv:2505.05469

## A. BRICKGPT Implementation Details

Captioning Details. The complete prompt template used for GPT-4o caption generation is as follows: “This is a rendering of a 3D object built with LEGO bricks with 24 different views. The object belongs to the category of {CATEGORY_NAME}. You will generate five different captions for this {CATEGORY_NAME} that: 1. Describes the core object/subject and its key geometric features 2. Focuses on structure, geometry, and layout information 3. Uses confident, concrete, and declarative language 4. Omits color and texture information 5. Excludes medium-related terms (model, render, design) 6. Do not describe or reference each view individually. 7. Focus on form over function. Describe the physical appearance of components rather than their purpose. 8. Describe components in detail, including size, shape, and position relative to other components. 9. The five captions should be from coarse to fine, with the first one being the most coarse-grained (e.g., a general description of the object, within 10 words) and the last one being the most fine-grained (e.g., a detailed description of the object, within 50 words). The five captions should be dif- ferent from each other. Do not include any…
