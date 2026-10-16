# Appendix/datasets-protocol: Scaling Rectified Flow Transformers for High-Resolution Image Synthesis

- id: `sd3-rectified-flow`
- source: arXiv:2403.03206

## E.2. Preventing Image Memorization

In the context of generative image models memorization of training samples can lead to a number of issues (Somepalli et al., 2023a; Carlini et al., 2023; Somepalli et al., 2023b). To avoid verbatim copies of images by our trained models, we carefully scan our training dataset for duplicated examples and remove them. 24 Scaling Rectified Flow Transformers for High-Resolution Image Synthesis Input Output 1 Output 2 Write ”go small go home” instead GO BIG OR GO UNET is written on the blackboard change the word to UNOT make the sign say MMDIT rules Figure 15. Zero Shot Text manipulation and insertion with the 2B Edit model Details on Deduplication In accordance with the methods outlined by Carlini et al. (2023) and Somepalli et al. (2023a), we opt for SSCD (Pizzi et al., 2022) as the backbone for the deduplication process. The SSCD algorithm is a state-of-the-art technique for detecting near-duplicate images at scale, and it generates high-quality image embeddings that can be used for clustering and other downstream tasks. We also decided to follow Nichol (2022) to decide on a number of clusters N. For our experiments, we use N = 16, 000. We utilize autofaiss (2023) for clustering.…
