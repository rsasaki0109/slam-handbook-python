"""幾何計算ユーティリティ"""

import numpy as np


def skew_2d(v):
    """スカラー → 2×2歪対称行列"""
    return np.array([[0, -v], [v, 0]])


def skew_3d(v):
    """R^3 → 3×3歪対称行列"""
    return np.array([[0, -v[2], v[1]],
                     [v[2], 0, -v[0]],
                     [-v[1], v[0], 0]])


def rotation_matrix_2d(theta):
    """2D回転行列"""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])


def homogeneous(points):
    """(N, D) → (N, D+1) 同次座標に変換"""
    N = len(points)
    return np.column_stack([points, np.ones(N)])


def dehomogeneous(points_h):
    """(N, D+1) → (N, D) 同次座標から復元"""
    return points_h[:, :-1] / points_h[:, -1:]
