# Appendix: Planning-Oriented Autonomous Driving

- id: `uniad`
- award: CVPR 2023 Best Paper
- arXiv: 2212.10156
- appendix_present: true
- start_page: 13
- appendix_pages: 12
- detection: override
- genres: hyperparams-implementation, other, proofs

## Table of contents

- `A` Task Definition — *other* (p.13)
- `B` The Necessity of Each Task — *other* (p.14)
- `C.1` Joint perception and prediction — *proofs* (p.14)
- `C.2` Joint prediction and planning — *other* (p.15)
- `C.3` End-to-end motion planning — *other* (p.15)
- `D` Notations — *proofs* (p.15)
- `E.1` Detection and Tracking — *other* (p.15)
- `E.2` Online Mapping — *proofs* (p.15)
- `E.3` Motion Forecasting — *other* (p.17)
- `E.4` Occupancy Prediction — *other* (p.17)
- `E.5` Planning — *other* (p.18)
- `E.6` Training Details — *hyperparams-implementation* (p.18)
- `F.1` Protocols — *hyperparams-implementation* (p.19)
- `F.2` Metrics — *hyperparams-implementation* (p.20)
- `F.3` Model complexity and Computational cost — *other* (p.20)
- `F.4` Model scale — *other* (p.20)
- `F.5` Qualitative results — *proofs* (p.21)

## Excerpts (study the move, do not copy)

### A. Task Definition

- genre: `other`
- start_page: 13

Detection and tracking. Detection and tracking are two crucial perception tasks for autonomous driving, and we fo- cus on representing them in the 3D space to facilitate down- stream usage. 3D Detection is responsible for locating sur- rounding objects (coordinates, length, width, height, etc.) at each time stamp; tracking aims at finding the correspon- dences between different objects across time stamps and as- sociating them temporally (i.e., assigning a consistent track ID for each agent). In the paper, we use multi-object track- ing in some cases to denote the detection and tracking pro- cess. The final output is a series of associated 3D boxes in each frame, and their corresponding features QA are for- warded to the motion module. Additionally, note that we have one special query named ego-vehicle query for down- stream tasks, which would not be included in the prediction- ground truth matching process and it regresses the location of ego-vehicle accordingly. Online mapping. Map intuitively embodies the geomet- ric and semantic information of the environment, and on- line mapping is to segment meaningful road elements with onboard sensor data (multi-view images in our case)…

### B. The Necessity of Each Task

- genre: `other`
- start_page: 14

In terms of perception, tracking in the loop as does in PnPNet [57] and ViP3D [30] is proven to complement spatial-temporal features and provide history tracks for oc- cluded agents, refraining from catastrophic decisions for downstream planning. With the aid of HD maps [30,57,82, 101] and motion forecasting, planning becomes more accu- rate toward higher-level intelligence. However, such infor- mation is expensive to construct and prone to be outdated, raising the demand for online mapping without HD maps. As for prediction, motion forecasting [10, 29, 41, 42, 107] generates long-term future behaviors and preserves agent identity in form of sparse waypoint outputs. Nonetheless, there exists the challenge to integrate non-differentiable box representation into subsequent planning module [30, 57]. Some recent literature investigates another type of predic- tion task named occupancy [88] prediction to assist end- to-end planning, in form of cost maps. However, the lack of agent identity and dynamics in occupancy makes it im- practical to model social interactions for safe planning. The large computational consumption of modeling multi-step dense features also leads to a much shorter…

### C.1. Joint perception and prediction

- genre: `proofs`
- start_page: 14

Joint learning of perception and prediction is pro- posed to avoid the cascading error in traditional modular- independence pipelines. Similar to the motion forecasting task alone, it usually has two types of output representa- tions: agent-level bounding boxes and scene-level occu- pancy grid maps. Pioneering work FaF [66] predicts boxes in the future and aggregates past information to produce tracklets. IntentNet [10] extends it to reason about inten- tions and [25, 28] further predict future states in a refine- ment fashion. Some exploit detection first and utilize agent features in the second prediction stage [9, 53, 75]. Notic- ing that history information is ignored, PnPNet [57] en- riches it by estimating tracking association scores to avert the non-differentiable optimization process as adopted by the tracking-by-detection paradigm [54,64,85,98]. Yet, all these methods rely on non-maximum suppression (NMS) in detection which still leads to information loss. ViP3D [30] which is closely related to our work, employs agent queries in [104] to forecast, taking HD map as another input. We follow the philosophy of [30, 104] in agent track queries, but also develop non-linear…

### C.2. Joint prediction and planning

- genre: `other`
- start_page: 15

PRECOG [81] proposes a recurrent model that condi- tions forecasting on the goal position of the ego vehicle, while PiP [86] generates agents’ motion considering com- plete presumed planning trajectories. However, producing a rough future trajectory is still challenging in the real world, toward which [62] presents a deep structured model to de- rive both prediction and planning from the same set of learn- able costs. [39,40] couple the prediction model with classic optimization methods. Meanwhile, some motion forecast- ing methods implicitly include the planning task by produc- ing their future trajectories simultaneously [12,45,70]. Sim- ilarly, we encode possible behaviors of the ego vehicle in the scene-centric motion forecasting module, but the inter- pretable occupancy map is utilized to further optimize the plan to stay safe.

### C.3. End-to-end motion planning

- genre: `other`
- start_page: 15

End-to-end motion planning has been an active research domain since Pomerleau [77] uses a single neural network that directly predicts control signals. Subsequent studies make great advances especially in closed-loop simulation with deeper networks [4], multi-modal inputs [2, 21, 78], multi-task learning [20,97], reinforcement learning [13,14, 46, 59, 89] and distillation from certain privilege knowl- edge [16,103,106]. However, for such methods of directly generating control outputs from sensor data, the transfer from the synthetic environment to realistic application re- mains a problem considering their robustness and safety assurance [22, 38]. Thus researchers aim at explicitly de- signing the intermediate representations of the network to prompt safety, where predicting how the scene evolves at- tracts broad interest. Some works [19,34,83] jointly decode planning and BEV semantic predictions to enhance inter- pretability, while PLOP [5] adopts a polynomial formula- tion to provide smooth planning results for both ego vehi- cle and neighbors. Cui et al. [24] introduce a contingency planner with diverse sets of future predictions and LAV [15] trains the planner with all…

### D. Notations

- genre: `proofs`
- start_page: 15

We provide a lookup table of notations and their shapes mentioned in this paper in Table 11 for reference.

### E.1. Detection and Tracking

- genre: `other`
- start_page: 15

We inherit most of the detection designs from BEV- Former [55] which takes a BEV encoder to transform im- age features into BEV feature B and adopts a Deformable DETR head [109] to perform detection on B. To further conduct end-to-end tracking without heavy post association, we introduce another group of queries named track queries as in MOTR [100] which continuously tracks previously ob- served instances according to its assigned track ID. We in- troduce the tracking process in detail below. Training stage: At the beginning (i.e., first frame) of each training sequence, all queries are considered detection queries and predict all newborn objects, which is actually the same as BEVFormer. Detection queries are matched to the ground truth by the Hungarian algorithm [8]. They will be stored and updated via the query interaction module (QIM) for the next timestamp serving as track queries fol- lowing MOTR [100]. In the next timestamp, track queries will be directly matched with a part of ground-truth ob- jects according to the corresponding track ID, and detection queries will be matched with the remaining ground-truth objects (newborn objects). To stabilize training, we adopt the 3D…

### E.2. Online Mapping

- genre: `proofs`
- start_page: 15

Following [56], we decompose the map query set into thing queries and stuff queries. The thing queries model instance-wise map elements (i.e., lanes, boundaries, and 15 Notation Shape & Params. Description Qo 900 number of initial object queries D 256 embed dimensions B 200 × 200 × 256 BEV feature encoded by a multi-view framework N 6 number of transformer decoder layers for TrackFormer N 6 number of transformer decoder layers for MapFormer N 4 number of mask decoder layers for MapFormer N 3 number of transformer decoder layers for MotionFormer N 5 number of transformer decoder layers for OccFormer N 3 number of transformer decoder layers for Planner Na dynamic number of agents from TrackFormer Nm 300 number of map queries from MapFormer QA Na × 256 agent features from TrackFormer PA Na × 256 agent positions from TrackFormer QM Nm × 256 map features from MapFormer K 6 number of forecasting modality in MotionFormer ˜x T × 2 ground truth for one agent’s motion forecasting ˆx Na × T × 2 prediction of motion forecasting T 12 length of prediction timestamps in MotionFormer Qpos Na × K × 256 query position in MotionFormer Qctx Na × K × 256 query context in MotionFormer Qa Na × K × 256…

### E.3. Motion Forecasting

- genre: `other`
- start_page: 17

To better illustrate the details, we provide a diagram as shown in Fig. 4. Our MotionFormer takes Ia T , Is T , ˆx0, ˆxl−1 T ∈RK×2 to embed query position, and takes Ql−1 ctx as query context. Specifically, the anchors are clustered among training data of all agents by the k-means algorithm, and we set K = 6 which is compatible with our output modali- ties. To embed the scene-level prior, the anchor Ia T is rotated and translated into the global coordinate frame according to each agent’s current location and heading angle, which is denoted as Is T , as shown in Eq. (12), \la b el { e q :sl-anchors} I_{i, T}^{s} = R_{i} I_{T}^{a} + T_{i}, (12) where i is the index of the agent, and it is omitted later for brevity. To facilitate the coarse-to-fine paradigm, we also adopt the goal point predicted from the previous layer ˆxl−1 T . In the meantime, the agent’s current position is broadcast across the modality, denoted as ˆx0. Then, MLPs and si- nusoidal positional embeddings are applied for each of the prior positional knowledge and we summarize them as the query position Qpos ∈RK×D, which is of the same shape as the query context Qctx. Qpos and Qctx together build up our motion query.…

### E.4. Occupancy Prediction

- genre: `other`
- start_page: 17

Given the BEV feature from upstream modules, we first downsample it by /4 with convolutional layers for efficient multi-step prediction, then pass it to our proposed Occ- Former. OccFormer is composed of To sequential blocks shown in Fig. 6, where To = 5 is the temporal horizon (including current and future frames) and each block is re- sponsible for generating occupancy of one specific frame. 17 Different from prior works which are short of agent-level knowledge, our proposed method incorporates both dense scene features and sparse agent features when unrolling the future representations. The dense scene feature is from the output of the last block (or the observed feature for cur- rent frame) and it’s further downscaled (/8) by a convolu- tion layer to reduce computation for pixel-agent interac- tion. The sparse agent feature is derived from the con- catenation of track query QA, agent positions PA, and mo- tion query QX, and it is then passed to a temporal-specific MLP for temporal sensitivity. We conduct pixel-level self- attention to model the long-term dependency required in some rapidly changing scenes, then perform scene-agent incorporation by attending each pixel of the…

### E.5. Planning

- genre: `other`
- start_page: 18

As shown in Fig. 7, our planner takes the ego-vehicle query generated from the tracking and motion forecasting module, which is symbolized with the blue triangle and yellow rectangle respectively. These two queries, along with the command embedding, are encoded with MLP lay- ers followed by a max-pooling layer across the modality dimension, where the most salient modal features are se- lected and aggregated. The BEV feature interaction module is built with standard transformer decoder layers, and it is stacked for N layers, where we set N = 3 here. Specif- ically, it cross-attends the dense BEV feature with the ag- gregated plan query. More qualitative results can be found in Appendix F.5 showing the effectiveness of this mod- ule. To embed location information, we fuse the plan- query with learned position embedding and the BEV fea- ture with sinusoidal positional embedding. We then regress the planning trajectory with MLP layers, which is denoted as ˆτ ∈RTp×2. Here we set Tp = 6 (3 seconds). Finally, MLP K & V Mask Flatten Unflatten × T! Dec F"#$ 𝑂,% " F" Block t Q C 𝑄% 𝑃% 𝑄& MLPt MLP Cross-attn Self-attn Downscale Upscale Figure 6. OccFormer. It is composed of To sequential…

### E.6. Training Details

- genre: `hyperparams-implementation`
- start_page: 18

Joint learning. UniAD is trained in two stages which we find more stable. In stage one, we pre-train perception tasks including tracking and online mapping to stabilize percep- tion predictions. Specifically, we load corresponding pre- trained BEVFormer [55] weights to UniAD for fast conver- gence including image backbone, FPN, BEV encoder and detection decoder except for object query embeddings (due to the additional ego-vehicle query). We stop the gradient back-propagation in the image backbone to reduce memory cost and train UniAD for 6 epochs with tracking and online mapping losses as follows: \ label { eq:all-loss-1} L_1 = L_{\text {track}} + L_{\text {map}}. (13) 18 Figure 7. Planner. Qego A and Qego ctx are the ego-vehicle query from the tracking and motion forecasting modules, respectively. Along with the high-level command, they are encoded with MLP layers followed by a max-pooling layer across the modality dimension, where the most salient modal features are selected and aggregated. The BEV feature interaction module is built with standard trans- former decoder layers, and it is stacked for N layers. In stage two, we keep the image backbone frozen as well, and…

### F.1. Protocols

- genre: `hyperparams-implementation`
- start_page: 19

We follow most of the basic training settings as in BEV- Former [55] for both two stages with a batch size of 1, a 19 learning rate of 2×10−4, learning rate multiplier of the back- bone 0.1 and AdamW optimizer [65] with a weight decay of 1×10−2. The default size of BEV size is 200×200, cover- ing BEV ranges of [-51.2m, 51.2m] for both X and Y axis with the interval as 0.512m. More hyperparameters related to feature dimensions are shown in Table 11. Experiments are conducted with 16 NVIDIA Tesla A100 GPUs.

### F.2. Metrics

- genre: `hyperparams-implementation`
- start_page: 20

Multi-object tracking. Following the standard evalua- tion protocols, we use AMOTA (Average Multi-object Tracking Accuracy), AMOTP (Average Multi-object Tracking Precision), Recall, and IDS (Identity Switches) to evaluate the 3D tracking performance of UniAD on nuScenes dataset. AMOTA and AMOTP are computed by integrating MOTA (Multi-object Tracking Accuracy) and MOTP (Multi-object Tracking Precision) values over all re- calls: \la b e l { e q:a m ota } \te xt {AMO TA} = \frac {1}{n-1}\sum _{r\in \{\frac {1}{n-1}, \frac {2}{n-1},...,1\}} \text {MOTA}_{r}, (17) \la b el {eq : m ota } \t e xt { M OT A }_{r } = \mathop {\max }(0, 1-\frac {\text {FP}_{r}+\text {FN}_{r}+\text {IDS}_{r}-(1-r)\text {GT}}{r\text {GT}}), (18) where FPr, FNr, and IDSr represent the number of false positives, false negatives and identity switches computed at the corresponding recall r, respectively. GT stands for the number of ground truth objects in this frame. AMOTP can be defined as: \la b e l { e q:a m otp } \te xt {AMO T P} = \frac {1}{n-1}\sum _{r\in \{\frac {1}{n-1}, \frac {2}{n-1},...,1\}} \frac {\sum _{i,t}d_{i,t}}{\text {TP}_r}, d (19) where di,t denotes the position error (in x and y axis) of…

### F.3. Model complexity and Computational cost

- genre: `other`
- start_page: 20

We measure the complexity of UniAD and runtime on an Nvidia Tesla A100 GPU, as depicted in Table 13. Though the decoder part of tasks brings a certain amount of param- eters, the computational complexity mainly comes from the encoder part, compared to the original BEVFormer detec- tor (ID. 1). We also provide a comparison with the recent BEVerse [105]. UniAD owns more tasks, achieves superior performance, and has lower FLOPs - indicating affordable budget to additional computation cost.

### F.4. Model scale

- genre: `other`
- start_page: 20

We provide three variations of UniAD under different model scales as shown in Table 12. The chosen image 20 Methods Encoder Tracking Mapping Motion Forecasting Occupancy Prediction Planning AMOTA↑ AMOTP↓ IDS↓ IoU-lane↑ IoU-road↑ minADE↓ minFDE↓ MR↓ EPA↑ IoU-n.↑ IoU-f.↑ VPQ-n.↑ VPQ-f.↑ avg.L2↓ avg.Col.↓ UniAD-S R50 0.241 1.488 958 0.315 0.689 0.788 1.126 0.156 0.381 59.4 35.6 49.2 28.9 1.04 0.32 UniAD-B R101 0.359 1.320 906 0.313 0.691 0.708 1.025 0.151 0.456 63.4 40.2 54.7 33.5 1.03 0.31 UniAD-L V2-99∗ 0.409 1.259 1583 0.323 0.709 0.723 1.067 0.158 0.508 64.1 42.6 55.8 36.9 1.03 0.29 Table 12. Comparisons between three variations of UniAD. ∗: pre-trained with extra depth data [73]. ID Det. Track Map Motion Occ. Plan #Params FLOPs FPS 0 [105] ✓ ✓ ✓ 102.5M 1921G - 1 ✓ 65.9M 1324G 4.2 2 ✓ ✓ 68.2M 1326G 2.7 3 ✓ ✓ ✓ 95.8M 1520G 2.2 4 ✓ ✓ ✓ ✓ 108.6M 1535G 2.1 5 ✓ ✓ ✓ ✓ ✓ 122.5M 1701G 2.0 6 ✓ ✓ ✓ ✓ ✓ ✓ 125.0M 1709G 1.8 Table 13. Computational complexity and runtime with different modules incorporated. ID.1 is similar to original BEVFormer [55], and ID. 0 (BEVerse-Tiny) [105] is an MTL framework. backbones for image-view feature extraction are ResNet- 50 [32], ResNet-101 and VoVNet 2-99…

### F.5. Qualitative results

- genre: `proofs`
- start_page: 21

Attention mask visualization. To investigate the internal mechanism and show its explainability, we visualize the at- tention mask of the cross-attention module in the planner. As shown in Fig. 8, the predicted tracking bounding boxes, planned trajectory, and the ground truth HD Map are ren- dered for reference, and the attention mask is overlayered on top. From left to right, we show two consecutive frames in a time sequence but with different navigation commands. We can observe that the planned trajectory varies largely according to the command. Also, much attention is paid to the goal lane as well as the critical agents that are yielding to our ego vehicle. Visualization of different scenarios. We provide visual- izations for more scenarios, including cruising around the urban areas (Fig. 9), critical cases (Fig. 10), and obstacle avoidance scenarios (Fig. 11). One promising evidence for our planning-oriented design is shown in Fig. 12, where in- accurate results occur in prior modules while the later tasks could still recover. Similarly, we show results for all tasks in surround-view images, BEV, as well as the attention mask from the planner. A demo video3 is also provided…

## Page renders

- `figures/appendix/uniad/page-13.png`
- `figures/appendix/uniad/page-14.png`
- `figures/appendix/uniad/page-15.png`
- `figures/appendix/uniad/page-16.png`
- `figures/appendix/uniad/page-17.png`
- `figures/appendix/uniad/page-18.png`
- `figures/appendix/uniad/page-19.png`
- `figures/appendix/uniad/page-20.png`
