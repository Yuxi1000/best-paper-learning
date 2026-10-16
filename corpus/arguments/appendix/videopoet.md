# Appendix: VideoPoet: A Large Language Model for Zero-Shot Video Generation

- id: `videopoet`
- award: ICML 2024 Best Paper
- arXiv: 2312.14125
- appendix_present: true
- start_page: 13
- appendix_pages: 8
- detection: override
- genres: hyperparams-implementation, other

## Table of contents

- `A` Appendix (opening) — *other* (p.13)
- `A.1` Responsible AI and Fairness Analysis — *hyperparams-implementation* (p.13)
- `A.2` Model Scale and Performance — *hyperparams-implementation* (p.13)
- `A.2.1` QUALITATIVE COMPARISON OF 1B AND 8B MODELS — *hyperparams-implementation* (p.13)
- `A.3` Additional Generated Examples — *other* (p.15)
- `A.4` Video Stylization — *other* (p.15)
- `A.5.1` ADDITIONAL IMPLEMENTATION DETAILS — *hyperparams-implementation* (p.17)
- `A.5.2` SUPER-RESOLUTION IMPLEMENTATION DETAILS — *hyperparams-implementation* (p.17)
- `A.5.3` ADDITIONAL EVALUATION DETAILS — *hyperparams-implementation* (p.18)
- `A.5.4` ADDITIONAL HUMAN EVALUATION DETAILS — *hyperparams-implementation* (p.18)
- `A.5.5` ZERO-SHOT TEXT-TO-VIDEO EVALUATION SETTINGS — *other* (p.18)
- `A.5.6` SELF-SUPERVISED TASKS EVALUATION SETTINGS — *other* (p.19)
- `A.5.7` STYLIZATION EVALUATION ON DAVIS — *hyperparams-implementation* (p.19)

## Excerpts (study the move, do not copy)

### A. Appendix (opening)

- genre: `other`
- start_page: 13

VideoPoet: A Large Language Model for Zero-Shot Video Generation

### A.1. Responsible AI and Fairness Analysis

- genre: `hyperparams-implementation`
- start_page: 13

We evaluate whether the generated outputs of our model are fair regarding protected attributes such as (1) Perceived Age (2) Perceived Gender Expression (3) Perceived Skin Tone. We construct 306 prompts with template — “a {profession or people descriptor} looking {adverb} at the camera” with “profession” being crawled from the US Bureau of Labor and Statistics and “people descriptors” including emotion state, socioeconomic class, etc. The “adverb” is used to generate semantically unchanged prompt templates such as “straightly” or “directly”. We generate 8 videos for each prompt and for each generated video we infer an approximation of the expressed attribute regarding the 3 protected attributes. Across 10 prompts that have the same semantic meaning but different “adverbs”, we observe our outputs generally introduced a stronger distribution shift toward “Young Adults” (age 18-35), “Male” and “Light Skin Tone”. However, we observe changing the “adverb” in the prompt template can significantly alter the output distributions. Therefore, our model can be prompted to produce outputs with non-uniform distributions across these groups, but also possess the ability of being prompted to…

### A.2. Model Scale and Performance

- genre: `hyperparams-implementation`
- start_page: 13

To analyze model performance versus model scale, we use a subset of the training set without text-paired data and a slightly different task prompt design. We evaluate the video generation quality using FVD (Unterthiner et al., 2018) and audio generation quality using the Fr´echet Audio Distance (FAD), which uses the VGGish model as the embedding function (Hershey et al., 2017). Both FVD and FAD metrics are calculated using a held-out subset of 25 thousand videos. Fig. 8 shows that as the model size grows and the amount of training data increases, performance improves across visual and audiovisual tasks. After obtaining the above results, we retrain our 1B and 8B models using the task design and text-paired training data discussed in Section 3. Appendix A.2.1 shows a qualitative comparison of the 1B and 8B pretrained models. Increasing the model size improved temporal consistency, prompt fidelity, and motion dynamics while adding capabilities for limited text rendering, spatial understanding, and counting. (a) Video generation quality in FVD (↓). (b) Audio generation quality in FAD (↓). Figure 8: Effects of model and data scale on video and audio generation quality. The…

### A.2.1. QUALITATIVE COMPARISON OF 1B AND 8B MODELS

- genre: `hyperparams-implementation`
- start_page: 13

In Figure 9, we show outputs of 1B and 8B parameter models on the same prompts. Four frames from the best video output of each model in a batch of four text-to-video samples were selected to represent the model. In the first row, the 1B model is unstable with large changes to the subject over time and misses elements from the complex prompt. This prompt was originally used for scaling comparisons in (Yu et al., 2022), and compared to a dedicated image-only model, our model does 13 VideoPoet: A Large Language Model for Zero-Shot Video Generation prompt: A portrait photo of a kangaroo wearing an orange hoodie and blue sunglasses standing on the grass in front of the Sydney Opera House holding a sign on the chest that says Welcome Friends! prompt: A kangaroo holding a sign with the letter A on it prompt: A photo of an astronaut riding a horse in the forest. There is a river in front of them with water lilies prompt: A zoomed out map of the United States made out of sushi. It is on a table next to a glass of red wine. Pieces of sushi disappear one by one prompt: Rotating around a vase holding a dozen roses Figure 9: A comparison of a 1B (left) and 8B (right) parameter models on the…

### A.3. Additional Generated Examples

- genre: `other`
- start_page: 15

We include most generated videos in the supplementary materials for an enhanced visualization of motion and visual quality, in addition to Fig. 10 and Fig. 11.

### A.4. Video Stylization

- genre: `other`
- start_page: 15

To perform video stylization, we follow an approach inspired by (Zhang et al., 2023b; Chen et al., 2023b; Esser et al., 2023) to predict videos from the combination of text, optical flow, and depth signals. On a subset of steps, we also condition on the first video frame. As described in (Esser et al., 2023), the text will generally define the “content” or appearance of the output and the optical flow and depth control the “structure.” In contrast to the diffusion-based approaches that usually use external cross-attention networks (Zhang et al., 2023b) or latent blending (Meng et al., 2021) for stylization, our approach is more closely related to machine translation using large language models in that we only need to provide the structure and text as a prefix to a language model. To perform the task, we estimate optical flow from RAFT (Sun et al., 2022) and produce monocular depth maps from MIDAS (Ranftl et al., 2020), and then normalize and concatenate on the channel dimension. This conveniently produces the 15 VideoPoet: A Large Language Model for Zero-Shot Video Generation Camera Motion: Arc shot Camera Motion: FPV drone shot Figure 11: Examples of directed camera movement from…

### A.5.1. ADDITIONAL IMPLEMENTATION DETAILS

- genre: `hyperparams-implementation`
- start_page: 17

The unified vocabulary is constructed as follows: the initial 256 codes are reserved for special tokens and task prompts. Table 4 lists some examples of special tokens. Subsequently, the next 262,144 codes are allocated for image and video tokenization. This is followed by 4,096 audio codes. We also include a small text vocabulary of English words. Overall, this produces a total vocabulary size of approximately 300,000. Since the first frame is tokenized separately, MAGVIT-v2 allows images to be represented in the same vocabulary as video. In addition to being more compact, images provide many learnable characteristics that are not typically represented in videos, such as strong visual styles (e.g., art paintings), objects which are infrequently seen in video, rich captions, and significantly more text-image paired training data. When training on images, we resize the images to 128×128 which are then tokenized to a latent shape of (1, 16, 16), or 256 tokens. We scale the MAGVIT-v2 model’s size and train it on the datasets discussed in Section 5.1. The training follows two steps: image training, inflation (Yu et al., 2024) and video training. Due to images requiring fewer tokens,…

### A.5.2. SUPER-RESOLUTION IMPLEMENTATION DETAILS

- genre: `hyperparams-implementation`
- start_page: 17

We use a 1B model for the first 2× spatial super-resolution stage and a 500M model for the second 2× stage. The first super-resolution stage models videos of 17 × 448 × 256 pixels with a token sequence of shape (5, 56, 32). The second stage models videos of 17 × 896 × 512 pixels with a token sequence of shape (5, 112, 64). The token sequences are obtained with the same MAGVIT-v2 (Yu et al., 2024) tokenizer used for the base language model. The custom super-resolution transformer has local self-attention windows for vertical, horizontal and temporal layers of shape (1, 56, 4), (1, 8, 32), (5, 8, 8) in the first stage and (1, 112, 2), (1, 4, 64), (5, 8, 8) in the second stage, respectively (Fig. 3). The cross-attention layers attend to local windows in the low-resolution sequence isomorphic to self-attention windows but with half the spatial size. We train the super-resolution stages on a dataset of 64M high-quality text-video pairs using the masked modeling objective of MAGVIT (Yu et al., 2023a), with token factorization into k = 2 groups (Yu et al., 2024). During inference, we use the sampling algorithm of MAGVIT-v2 (Yu et al., 2024) with 24 sampling steps for each stage and…

### A.5.3. ADDITIONAL EVALUATION DETAILS

- genre: `hyperparams-implementation`
- start_page: 18

We measure CLIP similarity scores (Wu et al., 2021) following an implementation given by Villegas et al. (2022), measure FVD (Unterthiner et al., 2018) following Yu et al. (2023a) on UCF101 dataset and following Zhang et al. (2023a) on MSR-VTT, and measure Inception Score (IS) (Saito et al., 2020). When the evaluation protocol is on 16 frames, we discard the generated last frame to make a 16-frame video.

### A.5.4. ADDITIONAL HUMAN EVALUATION DETAILS

- genre: `hyperparams-implementation`
- start_page: 18

Figure 13 shows an example screenshot of our side-by-side UI for comparing models. We used a team of 7 human raters to complete all ratings. To achieve best results, we call VideoPoet using the negative prompt “a still shot of an ugly cartoon, slideshow of an empty scene, low resolution, distorted and disfigured” and rewrite the given prompt by appending the string highly detailed, cinematic, arc shot, high contrast, soft lighting, 8k.

### A.5.5. ZERO-SHOT TEXT-TO-VIDEO EVALUATION SETTINGS

- genre: `other`
- start_page: 18

We report the details of our zero-shot text-to-video settings here. We note that some details are missing in previous papers and different papers use different settings. Hence, we provide all the details and hope this evaluation setting can serve as a standard text-to-video generation benchmark. Our results are reported on the 8B model and we adopt classifier-free guidance (Ho & Salimans, 2022). All metrics are evaluated on generated videos containing 16 frames with a resolution of 256 x 256. We first generate videos of 128 x 128 resolution and then resize to 256 x 256 via bicubic upsampling. Zero-shot MSR-VTT. For CLIP score, we used all 59,794 captions from the MSR-VTT test set. We use CLIP ViT-B/16 model following Phenaki (Villegas et al., 2022). We note that some papers use other CLIP models, e.g., VideoLDM (Blattmann et al., 2023b) uses ViT-B/32. Our CLIP score evaluated on the ViT-B/32 backbone for MSR-VTT is 30.01. For the FVD metric, to evaluate on a wide range of captions as well as to be comparable with previous papers that evaluate on 2,048 videos, we evaluate on the first 40,960 captions in the MSR-VTT test set. More specifically, we report the FVD metrics on 2048…

### A.5.6. SELF-SUPERVISED TASKS EVALUATION SETTINGS

- genre: `other`
- start_page: 19

Self-supervised learning tasks include frame prediction on K600 with 5 frames as condition, as well as inpainting and outpainting on SSv2. FVD (Unterthiner et al., 2018) is used as the primary metric, calculated with 16 frames at 128×128 resolution. We follow MAGVIT (Yu et al., 2023a) in evaluating these tasks against the respective real distribution, using 50000×4 samples for K600 and 50000 samples for SSv2.

### A.5.7. STYLIZATION EVALUATION ON DAVIS

- genre: `hyperparams-implementation`
- start_page: 19

To evaluate the CLIP similarity score and human preference on video stylization, we use the following set of videos and prompts. We select 20 videos from DAVIS 2016 (Perazzi et al., 2016), and for each video we take 16 frames starting from the initial frame specified below and evaluate stylization on the two text prompts specified below. To be easily reproducible, we use a central square crop at the height of the video and evaluate the output videos at 256x256 resolution. We use CLIP-B/16 for the similarity score. Several prompts below are used in or inspired by previous work (Esser et al., 2023; Chen et al., 2023b; Liew et al., 2023). 19 VideoPoet: A Large Language Model for Zero-Shot Video Generation video name starting frame first text prompt elephant 10 oil painting of an elephant walking away elephant 10 cartoon animation of an elephant walking through dirt surrounded by boulders car-turn 40 car on a snowcovered road in the countryside car-turn 40 8-bit pixelated car driving down the road dog-agility 0 a dog in the style of a comic book dog-agility 0 a dog running through a field of poles in the style of cyberpunk bmx-bumps 10 riding a bicycle on a rainbow track in space with…

## Page renders

- `figures/appendix/videopoet/page-13.png`
- `figures/appendix/videopoet/page-14.png`
- `figures/appendix/videopoet/page-15.png`
- `figures/appendix/videopoet/page-16.png`
- `figures/appendix/videopoet/page-17.png`
- `figures/appendix/videopoet/page-18.png`
- `figures/appendix/videopoet/page-19.png`
- `figures/appendix/videopoet/page-20.png`
