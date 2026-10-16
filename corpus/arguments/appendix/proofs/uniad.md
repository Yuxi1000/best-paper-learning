# Appendix/proofs: Planning-Oriented Autonomous Driving

- id: `uniad`
- source: arXiv:2212.10156

## C.1. Joint perception and prediction

Joint learning of perception and prediction is pro- posed to avoid the cascading error in traditional modular- independence pipelines. Similar to the motion forecasting task alone, it usually has two types of output representa- tions: agent-level bounding boxes and scene-level occu- pancy grid maps. Pioneering work FaF [66] predicts boxes in the future and aggregates past information to produce tracklets. IntentNet [10] extends it to reason about inten- tions and [25, 28] further predict future states in a refine- ment fashion. Some exploit detection first and utilize agent features in the second prediction stage [9, 53, 75]. Notic- ing that history information is ignored, PnPNet [57] en- riches it by estimating tracking association scores to avert the non-differentiable optimization process as adopted by the tracking-by-detection paradigm [54,64,85,98]. Yet, all these methods rely on non-maximum suppression (NMS) in detection which still leads to information loss. ViP3D [30] which is closely related to our work, employs agent queries in [104] to forecast, taking HD map as another input. We follow the philosophy of [30, 104] in agent track queries, but also develop non-linear…

## D. Notations

We provide a lookup table of notations and their shapes mentioned in this paper in Table 11 for reference.

## E.2. Online Mapping

Following [56], we decompose the map query set into thing queries and stuff queries. The thing queries model instance-wise map elements (i.e., lanes, boundaries, and 15 Notation Shape & Params. Description Qo 900 number of initial object queries D 256 embed dimensions B 200 × 200 × 256 BEV feature encoded by a multi-view framework N 6 number of transformer decoder layers for TrackFormer N 6 number of transformer decoder layers for MapFormer N 4 number of mask decoder layers for MapFormer N 3 number of transformer decoder layers for MotionFormer N 5 number of transformer decoder layers for OccFormer N 3 number of transformer decoder layers for Planner Na dynamic number of agents from TrackFormer Nm 300 number of map queries from MapFormer QA Na × 256 agent features from TrackFormer PA Na × 256 agent positions from TrackFormer QM Nm × 256 map features from MapFormer K 6 number of forecasting modality in MotionFormer ˜x T × 2 ground truth for one agent’s motion forecasting ˆx Na × T × 2 prediction of motion forecasting T 12 length of prediction timestamps in MotionFormer Qpos Na × K × 256 query position in MotionFormer Qctx Na × K × 256 query context in MotionFormer Qa Na × K × 256…

## F.5. Qualitative results

Attention mask visualization. To investigate the internal mechanism and show its explainability, we visualize the at- tention mask of the cross-attention module in the planner. As shown in Fig. 8, the predicted tracking bounding boxes, planned trajectory, and the ground truth HD Map are ren- dered for reference, and the attention mask is overlayered on top. From left to right, we show two consecutive frames in a time sequence but with different navigation commands. We can observe that the planned trajectory varies largely according to the command. Also, much attention is paid to the goal lane as well as the critical agents that are yielding to our ego vehicle. Visualization of different scenarios. We provide visual- izations for more scenarios, including cruising around the urban areas (Fig. 9), critical cases (Fig. 10), and obstacle avoidance scenarios (Fig. 11). One promising evidence for our planning-oriented design is shown in Fig. 12, where in- accurate results occur in prior modules while the later tasks could still recover. Similarly, we show results for all tasks in surround-view images, BEV, as well as the attention mask from the planner. A demo video3 is also provided…
