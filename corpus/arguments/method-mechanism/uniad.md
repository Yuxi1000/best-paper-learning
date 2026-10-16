# Planning-Oriented Autonomous Driving

- id: `uniad`
- award: CVPR 2023 Best Paper
- section_bucket: method-mechanism
- source: arXiv:2212.10156

## Excerpt (truncated; study the move, do not copy)

Perception Prediction Plan Det. Track Map Motion Occ. (b) NMP [101] ✓ ✓ ✓ NEAT [19] ✓ ✓ BEVerse [105] ✓ ✓ ✓ (c.1) [14,16,78,97] ✓ (c.2) PnPNet† [57] ✓ ✓ ✓ ViP3D† [30] ✓ ✓ ✓ P3 [82] ✓ ✓ MP3 [11] ✓ ✓ ✓ ST-P3 [38] ✓ ✓ ✓ LAV [15] ✓ ✓ ✓ ✓ (c.3) UniAD (ours) ✓ ✓ ✓ ✓ ✓ ✓ Table 1. Tasks comparison and taxonomy. “Design” column is classified as in Fig. 1. “Det.” denotes 3D object detection, “Map” stands for online mapping, and “Occ.” is occupancy map prediction. †: these works are not proposed directly for planning, yet they still share the spirit of joint perception and prediction. UniAD conducts five essential driving tasks to facilitate planning. erse [105], and industrialized products, e.g., Mobileye [68], Tesla [87], Nvidia [71], etc. In MTL, the co-training strategy across tasks could leverage feature abstraction; it could effortlessly extend to additional tasks, and save computation cost for onboard chips. However, such a scheme may cause undesirable “negative transfer” [23,64]. By contrast, the emergence of end-to-end autonomous driving [11,15,19,38,97] unites all nodes from perception, prediction and planning as a whole. The choice and priority of preceding tasks should be determined in favor of planning. The system should be planning-oriented, exquisitely designed with certain components involved, such that there are few accumulative error as in the standalone option or…
