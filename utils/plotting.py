"""可視化ヘルパー関数"""

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np


def plot_2d_poses(poses, ax=None, color="blue", label=None, arrow_length=0.3):
    """2Dポーズ (x, y, theta) のリストをプロット

    Parameters
    ----------
    poses : array-like, shape (N, 3)
        各行が [x, y, theta] のポーズ
    ax : matplotlib.axes.Axes, optional
    color : str
    label : str, optional
    arrow_length : float
    """
    poses = np.asarray(poses)
    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=(8, 8))

    ax.plot(poses[:, 0], poses[:, 1], "o-", color=color, label=label, markersize=4)
    for x, y, theta in poses:
        dx = arrow_length * np.cos(theta)
        dy = arrow_length * np.sin(theta)
        ax.arrow(x, y, dx, dy, head_width=0.08, head_length=0.05, fc=color, ec=color)

    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    if label:
        ax.legend()
    return ax


def plot_2d_landmarks(landmarks, ax=None, color="red", marker="*", label=None):
    """2Dランドマーク (x, y) をプロット"""
    landmarks = np.asarray(landmarks)
    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.scatter(
        landmarks[:, 0], landmarks[:, 1], c=color, marker=marker, s=100, label=label, zorder=5
    )
    if label:
        ax.legend()
    return ax


def plot_factor_graph(variables, factors, ax=None):
    """Factor Graphをシンプルに描画

    Parameters
    ----------
    variables : dict
        {name: (x, y)} 変数ノードの位置
    factors : list of dict
        各factorは {"connected": [var1, var2, ...], "pos": (x, y)} 形式
    ax : matplotlib.axes.Axes, optional
    """
    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=(10, 4))

    # 変数ノード（丸）
    for name, (x, y) in variables.items():
        circle = patches.Circle(
            (x, y), 0.2, fill=True, facecolor="lightblue", edgecolor="black", linewidth=2, zorder=3
        )
        ax.add_patch(circle)
        ax.text(x, y, name, ha="center", va="center", fontsize=10, fontweight="bold", zorder=4)

    # ファクターノード（四角）とエッジ
    for f in factors:
        fx, fy = f["pos"]
        rect = patches.Rectangle(
            (fx - 0.12, fy - 0.12), 0.24, 0.24, fill=True, facecolor="black", zorder=3
        )
        ax.add_patch(rect)

        for var_name in f["connected"]:
            vx, vy = variables[var_name]
            ax.plot([fx, vx], [fy, vy], "k-", linewidth=1.5, zorder=1)

    ax.set_aspect("equal")
    ax.set_xlim(-1, max(x for x, y in variables.values()) + 1.5)
    ax.set_ylim(-2, 2)
    ax.axis("off")
    return ax


def plot_covariance_ellipse(mean, cov, ax=None, n_std=2.0, color="blue", alpha=0.3):
    """2D共分散楕円をプロット"""
    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=(8, 8))

    eigenvalues, eigenvectors = np.linalg.eigh(cov[:2, :2])
    angle = np.degrees(np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0]))
    width, height = 2 * n_std * np.sqrt(eigenvalues)

    ellipse = patches.Ellipse(
        mean[:2],
        width,
        height,
        angle=angle,
        fill=True,
        facecolor=color,
        alpha=alpha,
        edgecolor=color,
        linewidth=2,
    )
    ax.add_patch(ellipse)
    return ax
