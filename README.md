# SLAM Handbook Python

[SLAM Handbook](https://github.com/SLAM-Handbook-contributors/slam-handbook-public-release) (Cambridge University Press, 2026) の内容を **Python + Jupyter Notebook** で手を動かしながら学ぶためのリポジトリです。

> **注意**: 本リポジトリは学習目的の非公式な実装です。書籍の内容を忠実に再現することを目指していますが、書籍そのものの代替ではありません。

## 構成

### Part I: Foundations of SLAM

| Chapter | トピック | Notebook | 主な実装 |
|---------|--------|----------|---------|
| Ch.1 | Factor Graphs for SLAM | [01](part1_foundations/ch01_factor_graphs/01_factor_graph_basics.ipynb) / [02](part1_foundations/ch01_factor_graphs/02_nonlinear_slam.ipynb) / [03](part1_foundations/ch01_factor_graphs/03_sparsity_and_elimination.ipynb) | Factor Graph可視化, 1D/2D SLAM, GN/LM法, スパース性, Bayes Tree |
| Ch.2 | State Variable Representations | [01](part1_foundations/ch02_state_representations/01_rotations_and_poses.ipynb) / [02](part1_foundations/ch02_state_representations/02_lie_group_optimization.ipynb) / [03](part1_foundations/ch02_state_representations/03_continuous_trajectories.ipynb) | SO(2)/SO(3)/SE(3), Lie群Pose Graph, GPモーションプライア |
| Ch.3 | Robustness to Outliers | [01](part1_foundations/ch03_outlier_robustness/01_ransac_and_robust_losses.ipynb) | RANSAC, Huber/GM/TQ Loss, IRLS, GNC |
| Ch.4 | Differentiable Optimization | [01](part1_foundations/ch04_differentiable_optimization/01_differentiable_least_squares.ipynb) | Implicit/Unrolled Diff, SO(3)ヤコビアン |
| Ch.5 | Dense Map Representations | [01](part1_foundations/ch05_dense_maps/01_occupancy_and_distance_fields.ipynb) | Occupancy Grid (log-odds), SDF/TSDF |
| Ch.6 | Certifiably Optimal Solvers | [01](part1_foundations/ch06_certifiable_solvers/01_sdp_relaxation_and_sesync.ipynb) | SDP緩和, Connection Laplacian, CRLB |

### Part II: SLAM in Practice

| Chapter | トピック | Notebook | 主な実装 |
|---------|--------|----------|---------|
| Ch.7 | Visual SLAM | [01](part2_practice/ch07_visual_slam/01_camera_and_epipolar.ipynb) | Pinhole Camera, Essential Matrix (8点法), Bundle Adjustment |
| Ch.8 | LiDAR SLAM | [01](part2_practice/ch08_lidar_slam/01_icp_and_scan_matching.ipynb) | 2D ICP (SVD+KD-tree), LiDAR Odometry |
| Ch.9 | Radar SLAM | [01](part2_practice/ch09_radar_slam/01_radar_odometry.ipynb) | Doppler速度推定, 相関スキャンマッチング |
| Ch.10 | Event-based SLAM | [01](part2_practice/ch10_event_slam/01_event_camera_basics.ipynb) | イベント生成モデル, Time Surface, Contrast Maximization |
| Ch.11 | Inertial Odometry | [01](part2_practice/ch11_inertial_odometry/01_imu_preintegration.ipynb) | IMUセンサモデル, Euler積分, Preintegration |
| Ch.12 | Leg Odometry | [01](part2_practice/ch12_leg_odometry/01_legged_robot_kinematics.ipynb) | 2リンク脚FK, 接触検出, Leg Odometry |

### Part III: From SLAM to Spatial AI

| Chapter | トピック | Notebook | 主な実装 |
|---------|--------|----------|---------|
| Ch.13 | Deep Learning for SLAM | [01](part3_spatial_ai/ch13_deep_learning_slam/01_learned_features_and_depth.ipynb) | 学習特徴量マッチング, 深度スケール曖昧性 |
| Ch.14 | NeRF & 3D Gaussian Splatting | [01](part3_spatial_ai/ch14_differentiable_rendering/01_nerf_and_gaussian_splatting.ipynb) | Volume Rendering, Tiny NeRF, 2D Gaussian Splatting |
| Ch.15 | Dynamic SLAM | [01](part3_spatial_ai/ch15_dynamic_slam/01_dynamic_object_handling.ipynb) | 動的物体検出, 残差ベース除去 |
| Ch.16 | Metric-Semantic SLAM | [01](part3_spatial_ai/ch16_semantic_slam/01_metric_semantic_slam.ipynb) | セマンティック地図, Object-level SLAM |
| Ch.17 | Open-World Spatial AI | [01](part3_spatial_ai/ch17_open_world/01_foundation_models_for_slam.ipynb) | CLIP風埋め込み, Open-vocab空間クエリ |
| Ch.18 | Computational Structure | [01](part3_spatial_ai/ch18_computational_structure/01_spatial_ai_system.ipynb) | 計算DAG, レイテンシ分析, 階層的認識 |

## セットアップ

```bash
git clone <this-repo>
cd slam-handbook-python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

### 動作要件

- Python >= 3.10
- numpy, scipy, matplotlib, networkx
- opencv-python, open3d (一部のNotebookで使用)
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
