# Appendix/other: VideoPoet: A Large Language Model for Zero-Shot Video Generation

- id: `videopoet`
- source: arXiv:2312.14125

## A. Appendix (opening)

VideoPoet: A Large Language Model for Zero-Shot Video Generation

## A.3. Additional Generated Examples

We include most generated videos in the supplementary materials for an enhanced visualization of motion and visual quality, in addition to Fig. 10 and Fig. 11.

## A.4. Video Stylization

To perform video stylization, we follow an approach inspired by (Zhang et al., 2023b; Chen et al., 2023b; Esser et al., 2023) to predict videos from the combination of text, optical flow, and depth signals. On a subset of steps, we also condition on the first video frame. As described in (Esser et al., 2023), the text will generally define the “content” or appearance of the output and the optical flow and depth control the “structure.” In contrast to the diffusion-based approaches that usually use external cross-attention networks (Zhang et al., 2023b) or latent blending (Meng et al., 2021) for stylization, our approach is more closely related to machine translation using large language models in that we only need to provide the structure and text as a prefix to a language model. To perform the task, we estimate optical flow from RAFT (Sun et al., 2022) and produce monocular depth maps from MIDAS (Ranftl et al., 2020), and then normalize and concatenate on the channel dimension. This conveniently produces the 15 VideoPoet: A Large Language Model for Zero-Shot Video Generation Camera Motion: Arc shot Camera Motion: FPV drone shot Figure 11: Examples of directed camera movement from…

## A.5.5. ZERO-SHOT TEXT-TO-VIDEO EVALUATION SETTINGS

We report the details of our zero-shot text-to-video settings here. We note that some details are missing in previous papers and different papers use different settings. Hence, we provide all the details and hope this evaluation setting can serve as a standard text-to-video generation benchmark. Our results are reported on the 8B model and we adopt classifier-free guidance (Ho & Salimans, 2022). All metrics are evaluated on generated videos containing 16 frames with a resolution of 256 x 256. We first generate videos of 128 x 128 resolution and then resize to 256 x 256 via bicubic upsampling. Zero-shot MSR-VTT. For CLIP score, we used all 59,794 captions from the MSR-VTT test set. We use CLIP ViT-B/16 model following Phenaki (Villegas et al., 2022). We note that some papers use other CLIP models, e.g., VideoLDM (Blattmann et al., 2023b) uses ViT-B/32. Our CLIP score evaluated on the ViT-B/32 backbone for MSR-VTT is 30.01. For the FVD metric, to evaluate on a wide range of captions as well as to be comparable with previous papers that evaluate on 2,048 videos, we evaluate on the first 40,960 captions in the MSR-VTT test set. More specifically, we report the FVD metrics on 2048…

## A.5.6. SELF-SUPERVISED TASKS EVALUATION SETTINGS

Self-supervised learning tasks include frame prediction on K600 with 5 frames as condition, as well as inpainting and outpainting on SSv2. FVD (Unterthiner et al., 2018) is used as the primary metric, calculated with 16 frames at 128×128 resolution. We follow MAGVIT (Yu et al., 2023a) in evaluating these tasks against the respective real distribution, using 50000×4 samples for K600 and 50000 samples for SSv2.
