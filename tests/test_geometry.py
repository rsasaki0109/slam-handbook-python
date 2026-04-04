import numpy as np
import numpy.testing as npt

from utils.geometry import (
    dehomogeneous,
    homogeneous,
    rotation_matrix_2d,
    skew_2d,
    skew_3d,
)


class TestSkew2D:
    def test_shape(self):
        assert skew_2d(1.0).shape == (2, 2)

    def test_antisymmetric(self):
        S = skew_2d(2.0)
        npt.assert_array_equal(S, -S.T)

    def test_known_value(self):
        S = skew_2d(3.0)
        npt.assert_array_equal(S, [[0, -3], [3, 0]])


class TestSkew3D:
    def test_shape(self):
        assert skew_3d([1, 2, 3]).shape == (3, 3)

    def test_antisymmetric(self):
        v = np.array([1.0, 2.0, 3.0])
        S = skew_3d(v)
        npt.assert_array_almost_equal(S, -S.T)

    def test_cross_product(self):
        v = np.array([1.0, 2.0, 3.0])
        w = np.array([4.0, 5.0, 6.0])
        npt.assert_array_almost_equal(skew_3d(v) @ w, np.cross(v, w))


class TestRotationMatrix2D:
    def test_identity(self):
        npt.assert_array_almost_equal(rotation_matrix_2d(0), np.eye(2))

    def test_orthogonal(self):
        R = rotation_matrix_2d(0.7)
        npt.assert_array_almost_equal(R @ R.T, np.eye(2))

    def test_det_one(self):
        R = rotation_matrix_2d(1.2)
        npt.assert_almost_equal(np.linalg.det(R), 1.0)

    def test_90_degrees(self):
        R = rotation_matrix_2d(np.pi / 2)
        npt.assert_array_almost_equal(R, [[0, -1], [1, 0]])


class TestHomogeneous:
    def test_shape(self):
        pts = np.array([[1, 2], [3, 4]])
        assert homogeneous(pts).shape == (2, 3)

    def test_last_column_ones(self):
        pts = np.array([[1, 2], [3, 4], [5, 6]])
        npt.assert_array_equal(homogeneous(pts)[:, -1], [1, 1, 1])

    def test_roundtrip(self):
        pts = np.array([[1.0, 2.0], [3.0, 4.0]])
        npt.assert_array_almost_equal(dehomogeneous(homogeneous(pts)), pts)


class TestDehomogeneous:
    def test_non_unit_weight(self):
        pts_h = np.array([[2.0, 4.0, 2.0], [3.0, 9.0, 3.0]])
        expected = np.array([[1.0, 2.0], [1.0, 3.0]])
        npt.assert_array_almost_equal(dehomogeneous(pts_h), expected)
