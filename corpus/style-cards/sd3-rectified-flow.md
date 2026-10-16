# Style card: sd3-rectified-flow

- title: Scaling Rectified Flow Transformers for High-Resolution Image Synthesis
- award: ICML 2024 Best Paper
- type: method-scaling
- figures_extracted: 16 (architecture, qualitative, quantitative, teaser)
- pages: 28

## What to steal (patterns, not sentences)

- Abstract shape: problem -> limitation of status quo -> this paper's move -> evidence of success.
- Match this paper when the user's draft is: scaling-study, architecture-ablation, industrial-scale-writing.
- Open the abstract file and 1-2 argument excerpts before imitating.

## Figure inventory

- `figures/teaser/sd3-rectified-flow-p01-01.png` (teaser, p.1) Figure 1. High-resolution samples from our 8B rectified flow model, showcasing its capabilities in typography, precise prompt following and spatial reasoning, attention to fine det
- `figures/qualitative/sd3-rectified-flow-p08-02.png` (qualitative, p.8) Figure 2. Our general setup follows LDM (Rombach et al., 2022) for training text-to-image models in the latent space of a pretrained autoencoder. Similar to the encoding of images 
- `figures/architecture/sd3-rectified-flow-p08-03.png` (architecture, p.8) Figure 2. Our model architecture. Concatenation is indicated by ⊙and element-wise multiplication by ∗. The RMS-Norm for Q and K can be added to stabilize training runs. Best viewed
- `figures/quantitative/sd3-rectified-flow-p08-04.png` (quantitative, p.8) Figure 3. Rectified flows are sample efficient. Rectified Flows perform better then other formulations when sampling fewer steps. For 25 and more steps, only rf/lognorm(0.00, 1.00)
- `figures/quantitative/sd3-rectified-flow-p08-05.png` (quantitative, p.8) Figure 3. Rectified flows are sample efficient. Rectified Flows perform better then other formulations when sampling fewer steps. For 25 and more steps, only rf/lognorm(0.00, 1.00)
- `figures/quantitative/sd3-rectified-flow-p08-06.png` (quantitative, p.8) Figure 3. Rectified flows are sample efficient. Rectified Flows perform better then other formulations when sampling fewer steps. For 25 and more steps, only rf/lognorm(0.00, 1.00)
- `figures/quantitative/sd3-rectified-flow-p08-07.png` (quantitative, p.8) Figure 3. Rectified flows are sample efficient. Rectified Flows perform better then other formulations when sampling fewer steps. For 25 and more steps, only rf/lognorm(0.00, 1.00)
- `figures/quantitative/sd3-rectified-flow-p08-08.png` (quantitative, p.8) Figure 3. Rectified flows are sample efficient. Rectified Flows perform better then other formulations when sampling fewer steps. For 25 and more steps, only rf/lognorm(0.00, 1.00)
- `figures/quantitative/sd3-rectified-flow-p08-09.png` (quantitative, p.8) Figure 3. Rectified flows are sample efficient. Rectified Flows perform better then other formulations when sampling fewer steps. For 25 and more steps, only rf/lognorm(0.00, 1.00)
- `figures/quantitative/sd3-rectified-flow-p08-10.png` (quantitative, p.8) Figure 3. Rectified flows are sample efficient. Rectified Flows perform better then other formulations when sampling fewer steps. For 25 and more steps, only rf/lognorm(0.00, 1.00)
- `figures/quantitative/sd3-rectified-flow-p08-11.png` (quantitative, p.8) Figure 3. Rectified flows are sample efficient. Rectified Flows perform better then other formulations when sampling fewer steps. For 25 and more steps, only rf/lognorm(0.00, 1.00)
- `figures/qualitative/sd3-rectified-flow-p09-12.png` (qualitative, p.9) Figure 2. As demonstrated in Figure 5, the additional normalization prevents the attention logit growth instability, confirming findings by Dehghani et al. (2023) and Wortsman et a
- `figures/qualitative/sd3-rectified-flow-p09-13.png` (qualitative, p.9) Figure 2. As demonstrated in Figure 5, the additional normalization prevents the attention logit growth instability, confirming findings by Dehghani et al. (2023) and Wortsman et a
- `figures/qualitative/sd3-rectified-flow-p09-14.png` (qualitative, p.9) Figure 2. As demonstrated in Figure 5, the additional normalization prevents the attention logit growth instability, confirming findings by Dehghani et al. (2023) and Wortsman et a
- `figures/qualitative/sd3-rectified-flow-p09-15.png` (qualitative, p.9) Figure 2. As demonstrated in Figure 5, the additional normalization prevents the attention logit growth instability, confirming findings by Dehghani et al. (2023) and Wortsman et a
- `figures/qualitative/sd3-rectified-flow-p10-16.png` (qualitative, p.10) Figure 6. Finally, note that Equation 23 implies a log-SNR shift of log n m similar to (Hoogeboom et al., 2023): λtm = 2 log 1 −tn p m n tn (24) = λtn −2 log α = λtn −log m n . (25
