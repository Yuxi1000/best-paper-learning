# Appendix/hyperparams-implementation: Planning-Oriented Autonomous Driving

- id: `uniad`
- source: arXiv:2212.10156

## E.6. Training Details

Joint learning. UniAD is trained in two stages which we find more stable. In stage one, we pre-train perception tasks including tracking and online mapping to stabilize percep- tion predictions. Specifically, we load corresponding pre- trained BEVFormer [55] weights to UniAD for fast conver- gence including image backbone, FPN, BEV encoder and detection decoder except for object query embeddings (due to the additional ego-vehicle query). We stop the gradient back-propagation in the image backbone to reduce memory cost and train UniAD for 6 epochs with tracking and online mapping losses as follows: \ label { eq:all-loss-1} L_1 = L_{\text {track}} + L_{\text {map}}. (13) 18 Figure 7. Planner. Qego A and Qego ctx are the ego-vehicle query from the tracking and motion forecasting modules, respectively. Along with the high-level command, they are encoded with MLP layers followed by a max-pooling layer across the modality dimension, where the most salient modal features are selected and aggregated. The BEV feature interaction module is built with standard trans- former decoder layers, and it is stacked for N layers. In stage two, we keep the image backbone frozen as well, and…

## F.1. Protocols

We follow most of the basic training settings as in BEV- Former [55] for both two stages with a batch size of 1, a 19 learning rate of 2×10−4, learning rate multiplier of the back- bone 0.1 and AdamW optimizer [65] with a weight decay of 1×10−2. The default size of BEV size is 200×200, cover- ing BEV ranges of [-51.2m, 51.2m] for both X and Y axis with the interval as 0.512m. More hyperparameters related to feature dimensions are shown in Table 11. Experiments are conducted with 16 NVIDIA Tesla A100 GPUs.

## F.2. Metrics

Multi-object tracking. Following the standard evalua- tion protocols, we use AMOTA (Average Multi-object Tracking Accuracy), AMOTP (Average Multi-object Tracking Precision), Recall, and IDS (Identity Switches) to evaluate the 3D tracking performance of UniAD on nuScenes dataset. AMOTA and AMOTP are computed by integrating MOTA (Multi-object Tracking Accuracy) and MOTP (Multi-object Tracking Precision) values over all re- calls: \la b e l { e q:a m ota } \te xt {AMO TA} = \frac {1}{n-1}\sum _{r\in \{\frac {1}{n-1}, \frac {2}{n-1},...,1\}} \text {MOTA}_{r}, (17) \la b el {eq : m ota } \t e xt { M OT A }_{r } = \mathop {\max }(0, 1-\frac {\text {FP}_{r}+\text {FN}_{r}+\text {IDS}_{r}-(1-r)\text {GT}}{r\text {GT}}), (18) where FPr, FNr, and IDSr represent the number of false positives, false negatives and identity switches computed at the corresponding recall r, respectively. GT stands for the number of ground truth objects in this frame. AMOTP can be defined as: \la b e l { e q:a m otp } \te xt {AMO T P} = \frac {1}{n-1}\sum _{r\in \{\frac {1}{n-1}, \frac {2}{n-1},...,1\}} \frac {\sum _{i,t}d_{i,t}}{\text {TP}_r}, d (19) where di,t denotes the position error (in x and y axis) of…
