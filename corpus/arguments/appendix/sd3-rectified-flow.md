# Appendix: Scaling Rectified Flow Transformers for High-Resolution Image Synthesis

- id: `sd3-rectified-flow`
- award: ICML 2024 Best Paper
- arXiv: 2403.03206
- appendix_present: true
- start_page: 17
- appendix_pages: 12
- detection: override
- genres: datasets-protocol, hyperparams-implementation, other

## Table of contents

- `A` Appendix (opening) — *other* (p.17)
- `A` Background — *other* (p.17)
- `B.1` Details on Simulation-Free Training of Flows — *other* (p.20)
- `B.2` Details on Image and Text Representations — *other* (p.20)
- `B.4` Improving SNR Samplers for Rectified Flow Models — *other* (p.21)
- `C` Direct Preference Optimization — *other* (p.23)
- `D` Finetuning for instruction-based image editing — *other* (p.23)
- `E.1` Precomputing Image and Text Embeddings — *hyperparams-implementation* (p.24)
- `E.2` Preventing Image Memorization — *datasets-protocol* (p.24)
- `E.3` Assessing the Efficacy of our Deduplication Efforts — *other* (p.26)

## Excerpts (study the move, do not copy)

### A. Appendix (opening)

- genre: `other`
- start_page: 17

Scaling Rectified Flow Transformers for High-Resolution Image Synthesis

### A. Background

- genre: `other`
- start_page: 17

Diffusion Models (Sohl-Dickstein et al., 2015; Song et al., 2020; Ho et al., 2020) generate data by approximating the reverse ODE to a stochastic forward process which transforms data to noise. They have become the standard approach for generative modeling of images (Dhariwal & Nichol, 2021; Ramesh et al., 2022; Saharia et al., 2022b; Rombach et al., 2022; Balaji et al., 2022) and videos (Singer et al., 2022; Ho et al., 2022; Esser et al., 2023; Blattmann et al., 2023b; Gupta et al., 2023). Since these models can be derived both via a variational lower bound on the negative likelihood (Sohl-Dickstein et al., 2015) and score matching (Hyv¨arinen, 2005; Vincent, 2011; Song & Ermon, 2020), various formulations of forward- and reverse processes (Song et al., 2020; Dockhorn et al., 2021), model parameterizations (Ho et al., 2020; Ho & Salimans, 2022; Karras et al., 2022), loss weightings (Ho et al., 2020; Karras et al., 2022) and ODE solvers (Song et al., 2022; Lu et al., 2023; Dockhorn et al., 2022) have led to a large number of different training objectives and sampling procedures. More recently, the seminal works of Kingma & Gao (2023) and Karras et al. (2022) have proposed unified…

### B.1. Details on Simulation-Free Training of Flows

- genre: `other`
- start_page: 20

Following (Lipman et al., 2023), to see that ut(z) generates pt, we note that the continuity equation provides a necessary and sufficient condition (Villani, 2008): d dtpt(x) + ∇· [pt(x)vt(x)] = 0 ↔vt generates probability density path pt. (26) Therefore it suffices to show that −∇· [ut(z)pt(z)] = −∇· [Eϵ∼N(0,I)ut(z|ϵ)pt(z|ϵ) pt(z) pt(z)] (27) = Eϵ∼N(0,I) −∇· [ut(z|ϵ)pt(z|ϵ)] (28) = Eϵ∼N(0,I) d dtpt(z|ϵ) = d dtpt(z), (29) where we used the continuity equation Equation (26) for ut(z|ϵ) in line Equation (28) to Equation (29) since ut(z|ϵ) generates pt(z|ϵ) and the definition of Equation (6) in line Equation (27) The equivalence of objectives LF M ⇋LCF M (Lipman et al., 2023) follows from LF M(Θ) = Et,pt(z)||vΘ(z, t) −ut(z)||2 2 (30) = Et,pt(z)||vΘ(z, t)||2 2 −2Et,pt(z)⟨vΘ(z, t) | ut(z)⟩+ c (31) = Et,pt(z)||vΘ(z, t)||2 2 −2Et,pt(z|ϵ),p(ϵ)⟨vΘ(z, t) | ut(z|ϵ)⟩+ c (32) = Et,pt(z|ϵ),p(ϵ)||vΘ(z, t) −ut(z|ϵ)||2 2 + c′ = LCF M(Θ) + c′ (33) where c, c′ do not depend on Θ and line Equation (31) to line Equation (32) follows from: Ept(z|ϵ),p(ϵ)⟨vΘ(z, t) | ut(z|ϵ)⟩= Z dz Z dϵpt(z|ϵ)p(ϵ)⟨vΘ(z, t) | ut(z|ϵ)⟩ (34) = Z dzpt(z)⟨vΘ(z, t) | Z dϵpt(z|ϵ) pt(z) p(ϵ)ut(z|ϵ)⟩ (35) = Z dzpt(z)⟨vΘ(z, t) |…

### B.2. Details on Image and Text Representations

- genre: `other`
- start_page: 20

Latent Image Representation We follow LDM (Rombach et al., 2022) and use a pretrained autoencoder to represent RGB images X ∈RH×W ×3 in a smaller latent space x = E(X) ∈Rh×w×d. We use a spatial downsampling factor of 8, such that h = H 8 and w = W 8 , and experiment with different values for d in Section 5.2.1. We always apply the forward process from Equation 2 in the latent space, and when sampling a representation x via Equation 1, we decode it back into pixel space X = D(x) via the decoder D. We follow Rombach et al. (2022) and normalize the latents by their mean and standard deviation, which are globally computed over a subset of the training data. Figure 10 shows how generative model training for different d evolves as a function of model capacity, as discussed in Section 5.2.1. Text Representation Similar to the encoding of images to latent representations, we also follow previous approaches (Saharia et al., 2022b; Balaji et al., 2022) and encode the text conditioning c using pretrained, frozen text models. In particular, for all experiments, we use a combination of CLIP (Radford et al., 2021) models and a encoder-decoder text model. Specifically, we encode c with the text…

### B.4. Improving SNR Samplers for Rectified Flow Models

- genre: `other`
- start_page: 21

As described in Section 2, we introduce novel densities π(t) for the timesteps that we use to train our rectified flow models. Figure 11 visualizes the distributions of the logit-normal sampler and the mode sampler introduced in Section 3.1. Notably, as we demonstrate in Section 5.1, the logit-normal sampler outperforms the classic uniform rectified flow formulation (Liu et al., 2022) and established diffusion baselines such as EDM (Karras et al., 2022) and LDM-Linear (Rombach et al., 2022). 21 Scaling Rectified Flow Transformers for High-Resolution Image Synthesis Figure 11. The mode (left) and logit-normal (right) distributions that we explore for biasing the sampling of training timesteps. “A raccoon wearing formal clothes, wearing a tophat and holding a cane. The raccoon is holding a garbage bag. Oil painting in the style of abstract cubism.” “A bowl of soup that looks like a monster made out of plasticine” “Two cups of coffee, one with latte art of a heart. The other has latte art of stars.” “A smiling sloth is wearing a leather jacket, a cowboy hat, a kilt and a bowtie. The sloth is holding a quarterstaff and a big book. The sloth is standing on grass a few feet in front of…

### C. Direct Preference Optimization

- genre: `other`
- start_page: 23

“a peaceful lakeside landscape with migrating herd of sauropods” “a book with the words ‘Don’t Panic¡, written on it” 2B base 2B w/ DPO 8b base 8b w/ DPO Figure 13. Comparison between base models and DPO-finetuned models. DPO-finetuning generally results in more aesthetically pleasing samples with better spelling. Direct Preference Optimization (DPO) (Rafailov et al., 2023) is a technique to finetune LLMs with preference data. Recently, this method has been adapted to preference finetuning of text-to-image diffusion models (Wallace et al., 2023). In this section, we verify that our model is also amenable to preference optimization. In particular, we apply the method introduced in Wallace et al. (2023) to our 2B and 8B parameter base model. Rather than finetuning the entire model, we introduce learnable Low-Rank Adaptation (LoRA) matrices (of rank 128) for all linear layers as is common practice. We finetune these new parameters for 4k and 2k iteration for the 2B and 8B base model, respectively. We then evaluate the resulting model in a human preference study using a subset of 128 captions from the Partiprompts set (Yu et al., 2022) (roughly three voter per prompt and comparison).…

### D. Finetuning for instruction-based image editing

- genre: `other`
- start_page: 23

A common approach for training instruction based image editing and general image-to-image diffusion models is to concatenate the latents of the input image to the noised latents of the diffusion target along the channel dimension before feeding the input into a U-Net (Brooks et al., 2023; Sheynin et al., 2023; Saharia et al., 2022a;c). We follow the same approach, concatenating input and target along the channels before patching, and demonstrate that the same method is applicable to our proposed architecture. We finetune the 2B parameter base model on a dataset consisting of image-to-image editing tasks similar to the distribution of the InstructPix2Pix dataset (Brooks et al., 2023) as well as inpainting, segmentation, colorization, deblurring and controlnet tasks similar to Emu Edit and Palette (Sheynin et al., 2023; Saharia et al., 2022a). As shown in Fig 15 we observe that the resulting 2B Edit model has the capability to manipulate text in a given image, even 23 Scaling Rectified Flow Transformers for High-Resolution Image Synthesis Prompt Quality 0 10 20 30 40 50 60 Human Preference [ % ] depth=24 (2B) base w/ DPO Prompt Quality depth=38 (8B) base w/ DPO Figure 14. Human…

### E.1. Precomputing Image and Text Embeddings

- genre: `hyperparams-implementation`
- start_page: 24

Our model uses the output of multiple pretrained, frozen networks as inputs (autoencoder latents and text encoder repre- sentations). Since these outputs are constant during training, we precompute them once for the entire dataset. This comes with two main advantages: (i) The encoders do not need to be available on the GPU during training, lowering the required memory. (ii) The forward encoding pass is skipped during training, saving time and total needed compute after the first epoch, see Tab. 7. This approach has two disadvantages: First, random augmentation for each sample every epoch is not possible and we use square-center cropping during precomputation of image latents. For finetuning our model at higher resolutions, we specify a number of aspect ratio buckets, and resize and crop to the closest bucket first and then precompute in that aspect ratio. Second, the dense output of the text encoders is particularly large, creating additional storage cost and longer loading times during training (c.f. Tab. 7). We save the embeddings of the language models in half precision, as we do not observe a deterioration in performance in practice.

### E.2. Preventing Image Memorization

- genre: `datasets-protocol`
- start_page: 24

In the context of generative image models memorization of training samples can lead to a number of issues (Somepalli et al., 2023a; Carlini et al., 2023; Somepalli et al., 2023b). To avoid verbatim copies of images by our trained models, we carefully scan our training dataset for duplicated examples and remove them. 24 Scaling Rectified Flow Transformers for High-Resolution Image Synthesis Input Output 1 Output 2 Write ”go small go home” instead GO BIG OR GO UNET is written on the blackboard change the word to UNOT make the sign say MMDIT rules Figure 15. Zero Shot Text manipulation and insertion with the 2B Edit model Details on Deduplication In accordance with the methods outlined by Carlini et al. (2023) and Somepalli et al. (2023a), we opt for SSCD (Pizzi et al., 2022) as the backbone for the deduplication process. The SSCD algorithm is a state-of-the-art technique for detecting near-duplicate images at scale, and it generates high-quality image embeddings that can be used for clustering and other downstream tasks. We also decided to follow Nichol (2022) to decide on a number of clusters N. For our experiments, we use N = 16, 000. We utilize autofaiss (2023) for clustering.…

### E.3. Assessing the Efficacy of our Deduplication Efforts

- genre: `other`
- start_page: 26

Carlini et al. (2023) devise a two-stage data extraction attack that generates images using standard approaches, and flags those that exceed certain membership inference scoring criteria. Carlini et al. (2023) bias their search towards duplicated training examples because these are orders of magnitude more likely to be memorized than non-duplicated examples (Somepalli et al., 2023a;a; Lee et al., 2021). To assess how well our SSCD-based deduplication works, we follow Carlini et al. (2023) to extract memorized samples from small, specifically for this purpose trained models and compare them before and after deduplication. Two main step of the mentioned procedure include: 1) Generate many examples using the diffusion model in the standard sampling manner and with the known prompts. 2) Perform membership inference to separate the model’s novel generations from those generations which are memorized training examples. Algorithm 2 shows the steps to find the memorized samples based on Carlini et al. (2023). Note that we run this techniques two times; one for SD-2.1 model with only exact dedup removal as baseline, and for a model with the SD2.1 architecture but trained on removed exact…

## Page renders

- `figures/appendix/sd3-rectified-flow/page-17.png`
- `figures/appendix/sd3-rectified-flow/page-18.png`
- `figures/appendix/sd3-rectified-flow/page-19.png`
- `figures/appendix/sd3-rectified-flow/page-20.png`
- `figures/appendix/sd3-rectified-flow/page-21.png`
- `figures/appendix/sd3-rectified-flow/page-22.png`
- `figures/appendix/sd3-rectified-flow/page-23.png`
- `figures/appendix/sd3-rectified-flow/page-24.png`
