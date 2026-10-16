# Appendix: Generating Physically Stable and Buildable Brick Structures from Text

- id: `brickgpt`
- award: ICCV 2025 Best Paper (Marr Prize)
- arXiv: 2505.05469
- appendix_present: true
- start_page: 13
- appendix_pages: 4
- detection: override
- genres: failure-cases, hyperparams-implementation, other

## Table of contents

- `A` BRICKGPT Implementation Details — *hyperparams-implementation* (p.13)
- `B` Robotic Assembly — *other* (p.14)
- `C` Manual Assembly — *other* (p.14)
- `D` Limitations — *failure-cases* (p.15)

## Excerpts (study the move, do not copy)

### A. BRICKGPT Implementation Details

- genre: `hyperparams-implementation`
- start_page: 13

Captioning Details. The complete prompt template used for GPT-4o caption generation is as follows: “This is a rendering of a 3D object built with LEGO bricks with 24 different views. The object belongs to the category of {CATEGORY_NAME}. You will generate five different captions for this {CATEGORY_NAME} that: 1. Describes the core object/subject and its key geometric features 2. Focuses on structure, geometry, and layout information 3. Uses confident, concrete, and declarative language 4. Omits color and texture information 5. Excludes medium-related terms (model, render, design) 6. Do not describe or reference each view individually. 7. Focus on form over function. Describe the physical appearance of components rather than their purpose. 8. Describe components in detail, including size, shape, and position relative to other components. 9. The five captions should be from coarse to fine, with the first one being the most coarse-grained (e.g., a general description of the object, within 10 words) and the last one being the most fine-grained (e.g., a detailed description of the object, within 50 words). The five captions should be dif- ferent from each other. Do not include any…

### B. Robotic Assembly

- genre: `other`
- start_page: 14

We demonstrate automated assembly using a dual-robot- arm system as shown in Figure 10. The system consists of two Yaskawa GP4 robots, each equipped with an ATI force-torque sensor. A calibrated baseplate is placed between them, and the robots use the bricks initially placed on the plate to construct the brick structure. Given a brick struc- ture B = [b1, b2, . . . , bN], we employ the action mask in [40] with assembly-by-disassembly search [73] to generate a physically executable assembly sequence for the robots, i.e., reordering the brick sequence so that 1) each intermediate structure is physically stable by itself, 2) each intermediate structure is stable under the robot operation, and 3) each as- sembly step is executable within the system’s dexterity. With the executable assembly sequence, an asynchronous planner [24] distributes the assembly tasks to the robots, plans the robots’ movements, and coordinates the bimanual system to construct the brick structure. The robots use the end-of-arm tool and the manipulation policy presented in [24, 39] with closed-loop force control to robustly manipulate bricks and construct the structure.

### C. Manual Assembly

- genre: `other`
- start_page: 14

As shown in Figure 11, human users can assemble our gen- erated structures, demonstrating their physical stability and buildability. Notably, since our method outputs a sequence of intermediate steps, it naturally serves as an intuitive as- sembly guide. … … … … … … Figure 10. Automated Assembly. We demonstrate robotic assembly of generated structures using LEGO bricks.

### D. Limitations

- genre: `failure-cases`
- start_page: 15

Though our method outperforms existing methods, it still has several limitations. First, due to limited computational resources, we have not explored the largest 3D dataset. As a result, our method is restricted to producing designs within a 20 × 20 × 20 grid across 21 categories, while recent 3D generation methods can create a wider variety of objects. Future work includes scaling up model training at higher grid resolutions on larger, more diverse datasets, such as Objaverse-XL [7]. Training on large-scale datasets can also improve generalization to out-of-distribution text prompts. Second, our method currently supports a fixed set of com- monly used toy bricks. In future work, we plan to expand the brick library to include a broader range of dimensions and brick types, such as slopes and tiles, allowing for more diverse and intricate designs. "A backless bench with armrest." “An acoustic guitar with an hourglass shape […]” "A two-seater bench with a straight backrest and an open rectangular design on the sides, […]" "A rectangular bookshelf featuring three horizontal shelves with open sides, supported by four […]" "A cylindrical bottle with a long, narrow neck tapering upwards…

## Page renders

- `figures/appendix/brickgpt/page-13.png`
- `figures/appendix/brickgpt/page-14.png`
- `figures/appendix/brickgpt/page-15.png`
- `figures/appendix/brickgpt/page-16.png`
