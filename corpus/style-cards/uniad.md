# Style card: uniad

- title: Planning-oriented Autonomous Driving
- award: CVPR 2023 Best Paper
- type: method-system
- figures_extracted: 16 (analysis-diagram, architecture, qualitative)
- pages: 24

## What to steal (patterns, not sentences)

- Abstract shape: problem -> limitation of status quo -> this paper's move -> evidence of success.
- Match this paper when the user's draft is: task-reframing, system-architecture, metric-story.
- Open the abstract file and 1-2 argument excerpts before imitating.

## Figure inventory

- `figures/architecture/uniad-p01-01.png` (architecture, p.1) Figure 1. Comparison on the various designs of autonomous driving framework. (a) Most industrial solutions deploy separate models for different tasks. (b) The multi-task learning s
- `figures/architecture/uniad-p03-02.png` (architecture, p.3) Figure 2. Pipeline of Unified Autonomous Driving (UniAD). It is exquisitely devised following planning-oriented philosophy. Instead of a simple stack of tasks, we investigate the e
- `figures/qualitative/uniad-p08-03.png` (qualitative, p.8) Figure 3. Visualization results. We show results for all tasks in surround-view images and BEV. Predictions from motion and occupancy modules are consistent, and the ego vehicle is
- `figures/qualitative/uniad-p08-04.png` (qualitative, p.8) Figure 3. Visualization results. We show results for all tasks in surround-view images and BEV. Predictions from motion and occupancy modules are consistent, and the ego vehicle is
- `figures/qualitative/uniad-p08-05.png` (qualitative, p.8) Figure 3. Visualization results. We show results for all tasks in surround-view images and BEV. Predictions from motion and occupancy modules are consistent, and the ego vehicle is
- `figures/qualitative/uniad-p08-06.png` (qualitative, p.8) Figure 3. Visualization results. We show results for all tasks in surround-view images and BEV. Predictions from motion and occupancy modules are consistent, and the ego vehicle is
- `figures/qualitative/uniad-p08-07.png` (qualitative, p.8) Figure 3. Visualization results. We show results for all tasks in surround-view images and BEV. Predictions from motion and occupancy modules are consistent, and the ego vehicle is
- `figures/qualitative/uniad-p08-08.png` (qualitative, p.8) Figure 3. Visualization results. We show results for all tasks in surround-view images and BEV. Predictions from motion and occupancy modules are consistent, and the ego vehicle is
- `figures/qualitative/uniad-p08-09.png` (qualitative, p.8) Figure 3. Visualization results. We show results for all tasks in surround-view images and BEV. Predictions from motion and occupancy modules are consistent, and the ego vehicle is
- `figures/analysis-diagram/uniad-p17-10.png` (analysis-diagram, p.17) Figure 5. Illustration of agent-goal interaction Module. The BEV visual feature is sampled near each agent’s goal points with deformable cross-attention. pedestrian crossings) and 
- `figures/analysis-diagram/uniad-p17-11.png` (analysis-diagram, p.17) Figure 5. Illustration of agent-goal interaction Module. The BEV visual feature is sampled near each agent’s goal points with deformable cross-attention. pedestrian crossings) and 
- `figures/qualitative/uniad-p19-12.png` (qualitative, p.19) Figure 7. Planner. Qego A and Qego ctx are the ego-vehicle query from the tracking and motion forecasting modules, respectively. Along with the high-level command, they are encoded
- `figures/qualitative/uniad-p22-13.png` (qualitative, p.22) Figure 9. Visualization for cruising around the urban areas. UniAD can generate high-quality interpretable perceptual and prediction results, and make a safe maneuver. The first th
- `figures/qualitative/uniad-p22-14.png` (qualitative, p.22) Figure 9. Visualization for cruising around the urban areas. UniAD can generate high-quality interpretable perceptual and prediction results, and make a safe maneuver. The first th
- `figures/qualitative/uniad-p23-15.png` (qualitative, p.23) Figure 11. Obstacles avoidance visualization. In these two scenarios, the ego vehicle is changing lanes attentively to avoid the obstacle vehicle. From the attention mask, we can o
- `figures/qualitative/uniad-p23-16.png` (qualitative, p.23) Figure 11. Obstacles avoidance visualization. In these two scenarios, the ego vehicle is changing lanes attentively to avoid the obstacle vehicle. From the attention mask, we can o
