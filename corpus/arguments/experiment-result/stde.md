# Stochastic Taylor Derivative Estimator: Efficient Amortization for Arbitrary Differential Operators

- id: `stde`
- award: NeurIPS 2024 Best Paper
- section_bucket: experiment-result
- source: arXiv:2412.00088

## Excerpt (truncated; study the move, do not copy)

Each experiment is run with five different random seeds, and the average and the standard deviations of these runs are reported. To get an accurate reading of memory usage, we use a separate run where GPU memory pre-allocation for JAX is disabled through setting the environment variable XLA_PYTHON_CLIENT_ALLOCATOR=platform, and the test data set is stored on the CPU memory. The GPU memory usage was obtained via NVIDIA-smi and peak memory was reported. All the experiments were done on a single NVIDIA A100 GPU with 40GB memory and CUDA 12.2. with driver 535.129.03 and JAX version 0.4.23. Network architecture and training hyperparameters For the semilinear parabolic PDEs tested in Appendix I.2 we follow the network architecture of the original SDGD [13]: • The network is a 4-layer multi-layer perceptron (MLP) with 128 hidden units activated by Tanh. • The network is trained with Adam [20] for 10K steps, with an initial learning rate of 1e-3 that linearly decays to 0 in 10K steps, where at each step we calculate the model parameters gradient with 100 uniformly sampled random residual points. • The model is evaluated using 20K uniformly sampled random points fixed throughout the training. 20 • The zero boundary condition is satisfied via the following parameterization uθ(x) = (1 −∥x∥2 2)uMLP θ (x) (55) where uMLP θ is the MLP network, and uθ is the PDE ansatz, as described in [26].…
