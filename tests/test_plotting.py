import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from utils.plotting import (
    plot_2d_landmarks,
    plot_2d_poses,
    plot_covariance_ellipse,
    plot_factor_graph,
)


class TestPlot2DPoses:
    def test_returns_axes(self):
        poses = np.array([[0, 0, 0], [1, 0, 0.5], [2, 1, 1.0]])
        ax = plot_2d_poses(poses)
        assert isinstance(ax, matplotlib.axes.Axes)
        plt.close("all")

    def test_with_existing_axes(self):
        _, ax = plt.subplots()
        poses = np.array([[0, 0, 0], [1, 1, 0.5]])
        result = plot_2d_poses(poses, ax=ax)
        assert result is ax
        plt.close("all")


class TestPlot2DLandmarks:
    def test_returns_axes(self):
        landmarks = np.array([[1, 2], [3, 4]])
        ax = plot_2d_landmarks(landmarks)
        assert isinstance(ax, matplotlib.axes.Axes)
        plt.close("all")


class TestPlotFactorGraph:
    def test_returns_axes(self):
        variables = {"x0": (0, 0), "x1": (1, 0)}
        factors = [{"connected": ["x0", "x1"], "pos": (0.5, 0)}]
        ax = plot_factor_graph(variables, factors)
        assert isinstance(ax, matplotlib.axes.Axes)
        plt.close("all")


class TestPlotCovarianceEllipse:
    def test_returns_axes(self):
        mean = np.array([0, 0])
        cov = np.array([[1, 0], [0, 1]])
        ax = plot_covariance_ellipse(mean, cov)
        assert isinstance(ax, matplotlib.axes.Axes)
        plt.close("all")
