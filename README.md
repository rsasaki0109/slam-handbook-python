# SLAM Handbook Python

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/)

[SLAM Handbook](https://github.com/SLAM-Handbook-contributors/slam-handbook-public-release) (Cambridge University Press, 2026) の内容を **Python + Jupyter Notebook** で手を動かしながら学ぶためのリポジトリです。

> **注意**: 本リポジトリは学習目的の非公式な実装です。書籍の内容を忠実に再現することを目指していますが、書籍そのものの代替ではありません。

## 構成

### Part I: Foundations of SLAM

| Chapter | トピック | Colab | 主な実装 |
|---------|--------|-------|---------|
| Ch.1 | Factor Graphs for SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch01_factor_graphs/01_factor_graph_basics.ipynb) [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch01_factor_graphs/02_nonlinear_slam.ipynb) [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch01_factor_graphs/03_sparsity_and_elimination.ipynb) | Factor Graph, 1D/2D SLAM, GN/LM, Bayes Tree |
| Ch.2 | State Variable Representations | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch02_state_representations/01_rotations_and_poses.ipynb) [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch02_state_representations/02_lie_group_optimization.ipynb) [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch02_state_representations/03_continuous_trajectories.ipynb) | SO(3)/SE(3), Lie群Pose Graph, GP |
| Ch.3 | Robustness to Outliers | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch03_outlier_robustness/01_ransac_and_robust_losses.ipynb) | RANSAC, IRLS, GNC |
| Ch.4 | Differentiable Optimization | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch04_differentiable_optimization/01_differentiable_least_squares.ipynb) | Implicit/Unrolled Diff |
| Ch.5 | Dense Map Representations | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch05_dense_maps/01_occupancy_and_distance_fields.ipynb) | Occupancy Grid, SDF/TSDF |
| Ch.6 | Certifiably Optimal Solvers | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part1_foundations/ch06_certifiable_solvers/01_sdp_relaxation_and_sesync.ipynb) | SDP緩和, CRLB |

### Part II: SLAM in Practice

| Chapter | トピック | Colab | 主な実装 |
|---------|--------|-------|---------|
| Ch.7 | Visual SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part2_practice/ch07_visual_slam/01_camera_and_epipolar.ipynb) | Camera, Essential Matrix, BA |
| Ch.8 | LiDAR SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part2_practice/ch08_lidar_slam/01_icp_and_scan_matching.ipynb) | 2D ICP, LiDAR Odometry |
| Ch.9 | Radar SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part2_practice/ch09_radar_slam/01_radar_odometry.ipynb) | Doppler, Correlative Matching |
| Ch.10 | Event-based SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part2_practice/ch10_event_slam/01_event_camera_basics.ipynb) | Event Model, Time Surface |
| Ch.11 | Inertial Odometry | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part2_practice/ch11_inertial_odometry/01_imu_preintegration.ipynb) | IMU Preintegration |
| Ch.12 | Leg Odometry | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part2_practice/ch12_leg_odometry/01_legged_robot_kinematics.ipynb) | 脚FK, Leg Odometry |

### Part III: From SLAM to Spatial AI

| Chapter | トピック | Colab | 主な実装 |
|---------|--------|-------|---------|
| Ch.13 | Deep Learning for SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part3_spatial_ai/ch13_deep_learning_slam/01_learned_features_and_depth.ipynb) | 学習特徴量, 深度推定 |
| Ch.14 | NeRF & 3DGS | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part3_spatial_ai/ch14_differentiable_rendering/01_nerf_and_gaussian_splatting.ipynb) | Volume Rendering, Tiny NeRF |
| Ch.15 | Dynamic SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part3_spatial_ai/ch15_dynamic_slam/01_dynamic_object_handling.ipynb) | 動的物体除去 |
| Ch.16 | Metric-Semantic SLAM | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part3_spatial_ai/ch16_semantic_slam/01_metric_semantic_slam.ipynb) | セマンティック地図 |
| Ch.17 | Open-World Spatial AI | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part3_spatial_ai/ch17_open_world/01_foundation_models_for_slam.ipynb) | Open-vocab Query |
| Ch.18 | Computational Structure | [![][cb]](https://colab.research.google.com/github/rsasaki0109/slam-handbook-python/blob/main/part3_spatial_ai/ch18_computational_structure/01_spatial_ai_system.ipynb) | 計算DAG, システム設計 |

[cb]: https://colab.research.google.com/assets/colab-badge.svg

## セットアップ

### Google Colabで実行（推奨）

上のテーブルの [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](#) バッジをクリックするだけ！セットアップ不要。

### ローカルで実行

```bash
git clone https://github.com/rsasaki0109/slam-handbook-python.git
cd slam-handbook-python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

### 動作要件

- Python >= 3.10
- numpy, scipy, matplotlib, networkx
- 外部DLフレームワーク（PyTorch等）は不要 — 全てNumPyで実装

## 各Notebookの構成

各Notebookは以下の構成で統一されています:

1. タイトルと学習目標
2. 数式の解説（SLAM Handbookの対応セクション参照付き）
3. Pythonによるスクラッチ実装
4. 可視化（matplotlib）
5. 演習問題（発展的な実装課題）
6. まとめ

## 参考文献

- Carlone, Kim, Barfoot, Cremers, Dellaert (Eds.), *SLAM Handbook: From Localization and Mapping to Spatial Intelligence*, Cambridge University Press, 2026.
- 上田隆一, *詳解 確率ロボティクス Pythonによる基礎アルゴリズムの実装*, 講談社, 2019.
- Atsushi Sakai, [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
