# Appendix/other: Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution

- id: `sedd`
- source: arXiv:2310.16834

## A. Appendix (opening)

Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution

## C.1. Diffusion Details

The geometric noise distribution is σ(t) = σ1−t minσt max. The log linear noise schedule is σ(t) = −log(1 −(1 −ϵt)) for some small epsilon for numerical stability as t →1, commonly 10−3 or 10−4. These noise schedules were chosen such that the prior loss DKL(pT |0(·x0) ∥π) and the approximation of pdata with pσ(0) are negligible. We typically scale the uniform transition matrix down by 1 N and take pbase to be uniform. For the absorbing state, we take pbase to be the MASK state with some leakage of probability to a random non-MASK state (to avoid inf KL divergence, although this is negligible and is not used for generation in practice).

## C.2. Model Details

Our model train with flash attention (Dao et al., 2022) with fused kernels wherever applicable. We also use the adaLN-zero time information network of (Peebles & Xie, 2023) with 128 hidden dimension. Following previous work, we parameterize the network with the total noise level instead of the time t. We also found it easier to postprocess the output of our network to form sθ, rather than outputting it directly. Concretely, we exponentiate (which maintains positivity) to be beneficial to avoid numerical errors and also found that scaling by eσ −1 helps for absorbing diffusion. SEDD models have the same hidden dimensions, number of blocks, and number of heads as their corresponding GPT-2 models. However, SEDD models also use a separate word embedding matrix and output matrix. In total, SEDD small and SEDD medium have around 90M parameters and 320M non embedding parameters respectively (compared to GPT-2 small 86M and GPT-2 medium 304M non-embedding parameters respectively). 15 Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution

## C.5.1. TEXT8

The baselines are taken from Graves et al. (2023), with many coming from Austin et al. (2021). In particular, they are IAF/SCF (Ziegler & Rush, 2019), the Autoregressive Argmax Flow (Hoogeboom et al., 2021), and the discrete flow (Tran et al., 2019) for autoregressive models. The non-autoregressive baselines are, in order, Multinomial Diffusion (Hoogeboom et al., 2021), MAC (Shih et al., 2022), Bayesian Flow Networks (Graves et al., 2023), and D3PM (Austin et al., 2021).

## C.5.2. ONE BILLION WORDS PERPLEXITY

The baselines are taken from He et al. (2022). They are D3PM (Austin et al., 2021), Diffusion-LM (Li et al., 2022), BERT-mouth (Wang & Cho, 2019), and DiffusionBert (He et al., 2022).

## C.7. Unconditional Generation Details

We generate using the Tweedie denoiser, which performed slightly better than the Euler sampling (typically by 1-4 perplexity points). We generated 1000 samples for all models.

## C.8. Conditional Generation Details

We follow Han et al. (2022) and generate 5 samples for each ground truth sample before calculating MAUVE. Note that this implies that we compare 5000 generated samples and 1000 ground truth samples. We sample by conditioning on 50 tokens and generating a new 50. For autoregressive-type sampling, this means we take the first 50 tokens. For SEDD with infilling, this means we clamp all input text sizes to a max of 100 tokens and condition on the first and last 25 tokens. 16 Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution Figure 2: Generative Perplexity for SEDD Uniform.

## D.2. Further Evaluation of Generative Perplexity

We further evaluate our generative perplexity for uniform models as well as different sampling schemes (analytic sampling based on Tweedie’s vs Euler sampling based off of reverse diffusion). Results are shown in Figure 2. Generally, we find that uniform does not produce the same linear tradeoff curve as absorbing (most likely due to a bottleneck in generation quality). Futhermore, analytic generally outperforms Euler sampling, and this is a major factor for the uniform model. We also generated on our trained baselines (Austin et al., 2021; Gulrajani & Hashimoto, 2023), finding both performed substantially worse than our SEDD Absorb baseline but slightly better than our SEDD Uniform.

## D.3. Additional Samples

Continued on next page. 18 Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution ; Koopong and Kozullo each received annual stipends of $500 for regular parking. Personnel and administration described how common illegal activities with their lawmakers were. Koopong had our neighbors respond as politically incorrect. Koltak adds, ”People said their taxes were too high.” Other sidewalks that are not clean are clustered around stadiums and other venues that will (incidentally) become part of BB&T, they expressed joy. Bearing stones and flag-sporting players cheered following the signing. Players hit with the ”Bill of Rights” signed by kits may claim PG&E shares in analysis fee like SBHR11 / glasses, lifestyle ebook for tattoo/sculpture projects and pirate rewards cards (12/25/00 for Subscription). Keiley, BA said there are six sitting Summons Vendors. Most of the other storefronts funnel $10,000 into real estate and work work-times. The nature of Bose also inspired and painted a composite image aimed at encouraging the purchase of sitebursts. The Studio 15 tenant cried out as more business from Pulaski Grill, one of the city’s premier club clubs, popped-up. I…
