# Appendix/failure-cases: Generating Physically Stable and Buildable Brick Structures from Text

- id: `brickgpt`
- source: arXiv:2505.05469

## D. Limitations

Though our method outperforms existing methods, it still has several limitations. First, due to limited computational resources, we have not explored the largest 3D dataset. As a result, our method is restricted to producing designs within a 20 × 20 × 20 grid across 21 categories, while recent 3D generation methods can create a wider variety of objects. Future work includes scaling up model training at higher grid resolutions on larger, more diverse datasets, such as Objaverse-XL [7]. Training on large-scale datasets can also improve generalization to out-of-distribution text prompts. Second, our method currently supports a fixed set of com- monly used toy bricks. In future work, we plan to expand the brick library to include a broader range of dimensions and brick types, such as slopes and tiles, allowing for more diverse and intricate designs. "A backless bench with armrest." “An acoustic guitar with an hourglass shape […]” "A two-seater bench with a straight backrest and an open rectangular design on the sides, […]" "A rectangular bookshelf featuring three horizontal shelves with open sides, supported by four […]" "A cylindrical bottle with a long, narrow neck tapering upwards…
