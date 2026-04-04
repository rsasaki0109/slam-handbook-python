import numpy as np
import numpy.testing as npt

from utils.lie_groups import (
    normalize_angle,
    se2_exp,
    se2_from_xyt,
    se2_inv,
    se2_log,
    se2_ominus,
    se2_oplus,
    se3_exp,
    se3_from_Rt,
    se3_inv,
    se3_log,
    se3_ominus,
    se3_oplus,
    se3_vee,
    se3_wedge,
    so2_exp,
    so2_log,
    so3_exp,
    so3_log,
    so3_vee,
    so3_wedge,
)

# =============================================================
# SO(2)
# =============================================================


class TestSO2:
    def test_exp_identity(self):
        npt.assert_array_almost_equal(so2_exp(0), np.eye(2))

    def test_exp_log_roundtrip(self):
        for theta in [0.5, -1.0, np.pi / 3]:
            R = so2_exp(theta)
            npt.assert_almost_equal(so2_log(R), theta)

    def test_known_90deg(self):
        R = so2_exp(np.pi / 2)
        npt.assert_array_almost_equal(R, [[0, -1], [1, 0]])


# =============================================================
# SO(3)
# =============================================================


class TestSO3:
    def test_exp_identity(self):
        npt.assert_array_almost_equal(so3_exp([0, 0, 0]), np.eye(3))

    def test_exp_log_roundtrip(self):
        v = np.array([0.1, -0.2, 0.3])
        npt.assert_array_almost_equal(so3_log(so3_exp(v)), v)

    def test_orthogonal(self):
        v = np.array([0.5, 0.3, -0.7])
        R = so3_exp(v)
        npt.assert_array_almost_equal(R @ R.T, np.eye(3), decimal=10)

    def test_det_one(self):
        R = so3_exp([1.0, 0.0, 0.0])
        npt.assert_almost_equal(np.linalg.det(R), 1.0)

    def test_wedge_vee_roundtrip(self):
        v = np.array([1.0, 2.0, 3.0])
        npt.assert_array_almost_equal(so3_vee(so3_wedge(v)), v)

    def test_wedge_antisymmetric(self):
        W = so3_wedge([1, 2, 3])
        npt.assert_array_almost_equal(W, -W.T)

    def test_near_zero_rotation(self):
        v = np.array([1e-12, 0, 0])
        R = so3_exp(v)
        npt.assert_array_almost_equal(R, np.eye(3), decimal=8)


# =============================================================
# SE(2)
# =============================================================


class TestSE2:
    def test_from_xyt(self):
        T = se2_from_xyt(1, 2, 0)
        expected = np.array([[1, 0, 1], [0, 1, 2], [0, 0, 1]])
        npt.assert_array_almost_equal(T, expected)

    def test_inv(self):
        T = se2_from_xyt(1, 2, 0.5)
        npt.assert_array_almost_equal(T @ se2_inv(T), np.eye(3))

    def test_exp_log_roundtrip(self):
        xi = np.array([1.0, 0.5, 0.3])
        npt.assert_array_almost_equal(se2_log(se2_exp(xi)), xi)

    def test_exp_pure_translation(self):
        xi = np.array([2.0, 3.0, 0.0])
        T = se2_exp(xi)
        npt.assert_array_almost_equal(T[:2, 2], [2.0, 3.0])
        npt.assert_array_almost_equal(T[:2, :2], np.eye(2))

    def test_oplus_ominus(self):
        T = se2_from_xyt(1, 2, 0.5)
        xi = np.array([0.1, -0.2, 0.05])
        T2 = se2_oplus(T, xi)
        npt.assert_array_almost_equal(se2_ominus(T2, T), xi)


# =============================================================
# SE(3)
# =============================================================


class TestSE3:
    def test_from_Rt(self):
        R = np.eye(3)
        t = np.array([1, 2, 3])
        T = se3_from_Rt(R, t)
        npt.assert_array_almost_equal(T[:3, :3], R)
        npt.assert_array_almost_equal(T[:3, 3], t)
        npt.assert_array_almost_equal(T[3, :], [0, 0, 0, 1])

    def test_inv(self):
        R = so3_exp([0.1, 0.2, 0.3])
        T = se3_from_Rt(R, [1, 2, 3])
        npt.assert_array_almost_equal(T @ se3_inv(T), np.eye(4))

    def test_exp_log_roundtrip(self):
        xi = np.array([0.1, -0.2, 0.3, 0.05, 0.1, -0.05])
        npt.assert_array_almost_equal(se3_log(se3_exp(xi)), xi)

    def test_wedge_vee_roundtrip(self):
        xi = np.array([1.0, 2.0, 3.0, 0.1, 0.2, 0.3])
        npt.assert_array_almost_equal(se3_vee(se3_wedge(xi)), xi)

    def test_oplus_ominus(self):
        R = so3_exp([0.1, 0.2, 0.3])
        T = se3_from_Rt(R, [1, 2, 3])
        xi = np.array([0.01, -0.02, 0.03, 0.005, 0.01, -0.005])
        T2 = se3_oplus(T, xi)
        npt.assert_array_almost_equal(se3_ominus(T2, T), xi, decimal=5)


# =============================================================
# normalize_angle
# =============================================================


class TestNormalizeAngle:
    def test_within_range(self):
        assert normalize_angle(0.5) == 0.5

    def test_wrap_positive(self):
        npt.assert_almost_equal(normalize_angle(2.5 * np.pi), 0.5 * np.pi)

    def test_wrap_negative(self):
        npt.assert_almost_equal(normalize_angle(-3 * np.pi), -np.pi)
