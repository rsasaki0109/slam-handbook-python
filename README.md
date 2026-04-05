# SLAM Handbook Python

[日本語](README_ja.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/)
[![CI](https://github.com/rsasaki0109/slam-handbook-python/actions/workflows/ci.yml/badge.svg)](https://github.com/rsasaki0109/slam-handbook-python/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Jupyter Book](https://img.shields.io/badge/Jupyter%20Book-live-orange)](https://rsasaki0109.github.io/slam-handbook-python/)

Hands-on Python + Jupyter Notebook implementations for the [SLAM Handbook](https://github.com/SLAM-Handbook-contributors/slam-handbook-public-release) (Cambridge University Press, 2026).

> **Note**: This is an unofficial, educational implementation. It aims to faithfully reproduce the book's content but is not a substitute for the book itself.

## Contents

### Part I: Foundations of SLAM

| Chapter | Topic | Colab | Key Implementations |
|---------|-------|-------|---------------------|
| Ch.1 | Factor Graphs for SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch01_factor_graphs/01_factor_graph_basics.ipynb) [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch01_factor_graphs/02_nonlinear_slam.ipynb) [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch01_factor_graphs/03_sparsity_and_elimination.ipynb) | Factor Graph, 1D/2D SLAM, GN/LM, Bayes Tree |
| Ch.2 | State Variable Representations | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch02_state_representations/01_rotations_and_poses.ipynb) [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch02_state_representations/02_lie_group_optimization.ipynb) [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch02_state_representations/03_continuous_trajectories.ipynb) | SO(3)/SE(3), Lie Group Pose Graph, GP |
| Ch.3 | Robustness to Outliers | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch03_outlier_robustness/01_ransac_and_robust_losses.ipynb) | RANSAC, IRLS, GNC |
| Ch.4 | Differentiable Optimization | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch04_differentiable_optimization/01_differentiable_least_squares.ipynb) | Implicit/Unrolled Diff |
| Ch.5 | Dense Map Representations | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch05_dense_maps/01_occupancy_and_distance_fields.ipynb) | Occupancy Grid, SDF/TSDF |
| Ch.6 | Certifiably Optimal Solvers | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch06_certifiable_solvers/01_sdp_relaxation_and_sesync.ipynb) | SDP Relaxation, CRLB |

### Part II: SLAM in Practice

| Chapter | Topic | Colab | Key Implementations |
|---------|-------|-------|---------------------|
| Ch.7 | Visual SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part2_practice/ch07_visual_slam/01_camera_and_epipolar.ipynb) | Camera, Essential Matrix, BA |
| Ch.8 | LiDAR SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part2_practice/ch08_lidar_slam/01_icp_and_scan_matching.ipynb) | 2D ICP, LiDAR Odometry |
| Ch.9 | Radar SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part2_practice/ch09_radar_slam/01_radar_odometry.ipynb) | Doppler, Correlative Matching |
| Ch.10 | Event-based SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part2_practice/ch10_event_slam/01_event_camera_basics.ipynb) | Event Model, Time Surface |
| Ch.11 | Inertial Odometry | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part2_practice/ch11_inertial_odometry/01_imu_preintegration.ipynb) | IMU Preintegration |
| Ch.12 | Leg Odometry | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part2_practice/ch12_leg_odometry/01_legged_robot_kinematics.ipynb) | Leg FK, Leg Odometry |

### Part III: From SLAM to Spatial AI

| Chapter | Topic | Colab | Key Implementations |
|---------|-------|-------|---------------------|
| Ch.13 | Deep Learning for SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part3_spatial_ai/ch13_deep_learning_slam/01_learned_features_and_depth.ipynb) | Learned Features, Depth Estimation |
| Ch.14 | NeRF & 3DGS | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part3_spatial_ai/ch14_differentiable_rendering/01_nerf_and_gaussian_splatting.ipynb) | Volume Rendering, Tiny NeRF |
| Ch.15 | Dynamic SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part3_spatial_ai/ch15_dynamic_slam/01_dynamic_object_handling.ipynb) | Dynamic Object Removal |
| Ch.16 | Metric-Semantic SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part3_spatial_ai/ch16_semantic_slam/01_metric_semantic_slam.ipynb) | Semantic Map |
| Ch.17 | Open-World Spatial AI | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part3_spatial_ai/ch17_open_world/01_foundation_models_for_slam.ipynb) | Open-vocab Query |
| Ch.18 | Computational Structure | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part3_spatial_ai/ch18_computational_structure/01_spatial_ai_system.ipynb) | Computation DAG, System Design |

[cb]: https://colab.research.google.com/assets/colab-badge.svg

## Setup

### Google Colab (Recommended)

Click any [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](#) badge above. No setup required.

### Local

```bash
git clone https://github.com/rsasaki0109/slam-handbook-python.git
cd slam-handbook-python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

### Requirements

- Python >= 3.10
- numpy, scipy, matplotlib, networkx
- No external DL frameworks (e.g., PyTorch) required — everything is implemented in NumPy

## Notebook Structure

Each notebook follows a consistent structure:

1. Title and learning objectives
2. Mathematical background (with references to the SLAM Handbook)
3. From-scratch Python implementation
4. Visualization (matplotlib)
5. Exercises (advanced implementation challenges)
6. Summary

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## References

- Carlone, Kim, Barfoot, Cremers, Dellaert (Eds.), *SLAM Handbook: From Localization and Mapping to Spatial Intelligence*, Cambridge University Press, 2026.
- Atsushi Sakai, [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
