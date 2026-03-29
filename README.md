# SLAM Handbook Python

[SLAM Handbook](https://github.com/SLAM-Handbook-contributors/slam-handbook-public-release) (Cambridge University Press, 2026) の内容を **Python + Jupyter Notebook** で手を動かしながら学ぶためのリポジトリです。

> **注意**: 本リポジトリは学習目的の非公式な実装です。書籍の内容を忠実に再現することを目指していますが、書籍そのものの代替ではありません。

## 構成

### Part I: Foundations of SLAM

| Chapter | トピック | Notebook |
|---------|--------|----------|
| Ch.1 | Factor Graphs for SLAM | [factor_graphs](part1_foundations/ch01_factor_graphs/) |
| Ch.2 | Advanced State Variable Representations | [state_representations](part1_foundations/ch02_state_representations/) |
| Ch.3 | Robustness to Outliers | [outlier_robustness](part1_foundations/ch03_outlier_robustness/) |
| Ch.4 | Differentiable Optimization | [differentiable_optimization](part1_foundations/ch04_differentiable_optimization/) |
| Ch.5 | Dense Map Representations | [dense_maps](part1_foundations/ch05_dense_maps/) |
| Ch.6 | Certifiably Optimal Solvers | [certifiable_solvers](part1_foundations/ch06_certifiable_solvers/) |

### Part II: SLAM in Practice

| Chapter | トピック | Notebook |
|---------|--------|----------|
| Ch.7 | Visual SLAM | [visual_slam](part2_practice/ch07_visual_slam/) |
| Ch.8 | LiDAR SLAM | [lidar_slam](part2_practice/ch08_lidar_slam/) |
| Ch.9 | Radar SLAM | [radar_slam](part2_practice/ch09_radar_slam/) |
| Ch.10 | Event-based SLAM | [event_slam](part2_practice/ch10_event_slam/) |
| Ch.11 | Inertial Odometry | [inertial_odometry](part2_practice/ch11_inertial_odometry/) |
| Ch.12 | Leg Odometry | [leg_odometry](part2_practice/ch12_leg_odometry/) |

### Part III: From SLAM to Spatial AI

| Chapter | トピック | Notebook |
|---------|--------|----------|
| Ch.13 | Deep Learning for SLAM | [deep_learning_slam](part3_spatial_ai/ch13_deep_learning_slam/) |
| Ch.14 | NeRF & 3D Gaussian Splatting | [differentiable_rendering](part3_spatial_ai/ch14_differentiable_rendering/) |
| Ch.15 | Dynamic and Deformable SLAM | [dynamic_slam](part3_spatial_ai/ch15_dynamic_slam/) |
| Ch.16 | Metric-Semantic SLAM | [semantic_slam](part3_spatial_ai/ch16_semantic_slam/) |
| Ch.17 | Open-World Spatial AI | [open_world](part3_spatial_ai/ch17_open_world/) |
| Ch.18 | Computational Structure | [computational_structure](part3_spatial_ai/ch18_computational_structure/) |

## セットアップ

```bash
git clone <this-repo>
cd slam-handbook-python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## 参考文献

- Carlone, Kim, Barfoot, Cremers, Dellaert (Eds.), *SLAM Handbook: From Localization and Mapping to Spatial Intelligence*, Cambridge University Press, 2026.
- 上田隆一, *詳解 確率ロボティクス Pythonによる基礎アルゴリズムの実装*, 講談社, 2019.
- Atsushi Sakai, [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
