# Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction

- id: `var`
- award: NeurIPS 2024 Best Paper
- section_bucket: method-mechanism
- source: arXiv:2404.02905

## Excerpt (truncated; study the move, do not copy)

3.1 Preliminary: autoregressive modeling via next-token prediction Formulation. Consider a sequence of discrete tokens x = (x1, x2, . . . , xT ), where xt ∈[V ] is an integer from a vocabulary of size V . The next-token autoregressive posits the probability of observing the current token xt depends only on its prefix (x1, x2, . . . , xt−1). This unidirectional token dependency assumption allows for the factorization of the sequence x’s likelihood: p(x1, x2, . . . , xT ) = T Y t=1 p(xt | x1, x2, . . . , xt−1). (1) Training an autoregressive model pθ involves optimizing pθ(xt | x1, x2, . . . , xt−1) over a dataset. This is known as the “next-token prediction”, and the trained pθ can generate new sequences. Tokenization. Images are inherently 2D continuous signals. To apply autoregressive modeling to images via next-token prediction, we must: 1) tokenize an image into several discrete tokens, and 2) define a 1D order of tokens for unidirectional modeling. For 1), a quantized autoencoder such as [30] is often used to convert the image feature map f ∈Rh×w×C to discrete tokens q ∈[V ]h×w: f = E(im), q = Q(f), (2) where im denotes the raw image, E(·) a encoder, and Q(·) a quantizer. The quantizer typically includes a learnable codebook Z ∈RV ×C containing V vectors. The quantization process q = Q(f) will map each feature vector f (i,j) to the code index q(i,j) of its nearest code in…
