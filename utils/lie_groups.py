"""Lie群ユーティリティ: SO(2), SO(3), SE(2), SE(3) の Exp/Log/wedge/vee"""

import numpy as np

# =============================================================
# SO(2)
# =============================================================


def so2_exp(theta):
    """スカラー → 2×2回転行列"""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])


def so2_log(R):
    """2×2回転行列 → スカラー"""
    return np.arctan2(R[1, 0], R[0, 0])


# =============================================================
# SO(3)
# =============================================================


def so3_wedge(v):
    """R^3 → 3×3歪対称行列"""
    return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


def so3_vee(W):
    """3×3歪対称行列 → R^3"""
    return np.array([W[2, 1], W[0, 2], W[1, 0]])


def so3_exp(v):
    """R^3 → SO(3) (Rodrigues公式)"""
    v = np.asarray(v, dtype=float)
    phi = np.linalg.norm(v)
    if phi < 1e-10:
        return np.eye(3) + so3_wedge(v)
    a = v / phi
    aw = so3_wedge(a)
    return np.eye(3) + np.sin(phi) * aw + (1 - np.cos(phi)) * (aw @ aw)


def so3_log(R):
    """SO(3) → R^3"""
    cos_phi = np.clip((np.trace(R) - 1) / 2, -1, 1)
    phi = np.arccos(cos_phi)
    if phi < 1e-10:
        return so3_vee(R - np.eye(3))
    return phi / (2 * np.sin(phi)) * so3_vee(R - R.T)


# =============================================================
# SE(2)
# =============================================================


def se2_from_xyt(x, y, theta):
    """(x, y, θ) → 3×3同次変換行列"""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, x], [s, c, y], [0, 0, 1]])


def se2_inv(T):
    """SE(2)の逆行列"""
    R = T[:2, :2]
    t = T[:2, 2]
    Ti = np.eye(3)
    Ti[:2, :2] = R.T
    Ti[:2, 2] = -R.T @ t
    return Ti


def se2_exp(xi):
    """R^3 → SE(2)"""
    rho, theta = xi[:2], xi[2]
    if abs(theta) < 1e-10:
        return np.array([[1, 0, rho[0]], [0, 1, rho[1]], [0, 0, 1]])
    c, s = np.cos(theta), np.sin(theta)
    V = np.array([[s / theta, -(1 - c) / theta], [(1 - c) / theta, s / theta]])
    t = V @ rho
    T = np.eye(3)
    T[:2, :2] = np.array([[c, -s], [s, c]])
    T[:2, 2] = t
    return T


def se2_log(T):
    """SE(2) → R^3"""
    theta = np.arctan2(T[1, 0], T[0, 0])
    t = T[:2, 2]
    if abs(theta) < 1e-10:
        return np.array([t[0], t[1], theta])
    c, s = np.cos(theta), np.sin(theta)
    V = np.array([[s / theta, -(1 - c) / theta], [(1 - c) / theta, s / theta]])
    rho = np.linalg.solve(V, t)
    return np.array([rho[0], rho[1], theta])


# =============================================================
# SE(3)
# =============================================================


def se3_from_Rt(R, t):
    """回転行列と並進ベクトルから4×4同次変換行列"""
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = t
    return T


def se3_inv(T):
    """SE(3)の逆行列"""
    R = T[:3, :3]
    t = T[:3, 3]
    Ti = np.eye(4)
    Ti[:3, :3] = R.T
    Ti[:3, 3] = -R.T @ t
    return Ti


def se3_wedge(xi):
    """R^6 → 4×4行列 (se(3)の要素)  xi = [rho(3), theta(3)]"""
    rho, theta = xi[:3], xi[3:]
    Xi = np.zeros((4, 4))
    Xi[:3, :3] = so3_wedge(theta)
    Xi[:3, 3] = rho
    return Xi


def se3_vee(Xi):
    """4×4行列 → R^6"""
    rho = Xi[:3, 3]
    theta = so3_vee(Xi[:3, :3])
    return np.concatenate([rho, theta])


def se3_exp(xi):
    """R^6 → SE(3)"""
    from scipy.linalg import expm

    return expm(se3_wedge(xi))


def se3_log(T):
    """SE(3) → R^6"""
    from scipy.linalg import logm

    return se3_vee(logm(T))


# =============================================================
# ⊕ / ⊖ 演算子
# =============================================================


def se2_oplus(T, xi):
    """T ⊕ ξ = T · Exp(ξ)"""
    return T @ se2_exp(xi)


def se2_ominus(T1, T2):
    """T1 ⊖ T2 = Log(T2^{-1} · T1)"""
    return se2_log(se2_inv(T2) @ T1)


def se3_oplus(T, xi):
    """T ⊕ ξ = T · Exp(ξ)"""
    return T @ se3_exp(xi)


def se3_ominus(T1, T2):
    """T1 ⊖ T2 = Log(T2^{-1} · T1)"""
    return se3_log(se3_inv(T2) @ T1)


# =============================================================
# ヘルパー
# =============================================================


def normalize_angle(a):
    """角度を [-π, π] に正規化"""
    return (a + np.pi) % (2 * np.pi) - np.pi
