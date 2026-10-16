# Appendix/hyperparams-implementation: Scaling Rectified Flow Transformers for High-Resolution Image Synthesis

- id: `sd3-rectified-flow`
- source: arXiv:2403.03206

## E.1. Precomputing Image and Text Embeddings

Our model uses the output of multiple pretrained, frozen networks as inputs (autoencoder latents and text encoder repre- sentations). Since these outputs are constant during training, we precompute them once for the entire dataset. This comes with two main advantages: (i) The encoders do not need to be available on the GPU during training, lowering the required memory. (ii) The forward encoding pass is skipped during training, saving time and total needed compute after the first epoch, see Tab. 7. This approach has two disadvantages: First, random augmentation for each sample every epoch is not possible and we use square-center cropping during precomputation of image latents. For finetuning our model at higher resolutions, we specify a number of aspect ratio buckets, and resize and crop to the closest bucket first and then precompute in that aspect ratio. Second, the dense output of the text encoders is particularly large, creating additional storage cost and longer loading times during training (c.f. Tab. 7). We save the embeddings of the language models in half precision, as we do not observe a deterioration in performance in practice.
