import numpy as np
import numpy.testing as npt

from utils.factor_graph import BetweenFactor, FactorGraph, PriorFactor


class TestFactorGraph:
    def test_add_variable(self):
        fg = FactorGraph()
        fg.add_variable("x0", [0.0, 0.0])
        assert "x0" in fg.variables

    def test_add_factor(self):
        fg = FactorGraph()
        f = PriorFactor("x0", [1.0], [1.0])
        fg.add_factor(f)
        assert len(fg.factors) == 1

    def test_get_state_vector(self):
        fg = FactorGraph()
        fg.add_variable("x0", [1.0, 2.0])
        fg.add_variable("x1", [3.0, 4.0])
        sv = fg.get_state_vector()
        npt.assert_array_equal(sv, [1.0, 2.0, 3.0, 4.0])

    def test_get_state_vector_custom_order(self):
        fg = FactorGraph()
        fg.add_variable("x0", [1.0])
        fg.add_variable("x1", [2.0])
        sv = fg.get_state_vector(var_order=["x1", "x0"])
        npt.assert_array_equal(sv, [2.0, 1.0])


class TestPriorFactor:
    def test_residual(self):
        f = PriorFactor("x0", [1.0, 2.0], [0.5, 0.5])
        variables = {"x0": np.array([1.5, 2.5])}
        npt.assert_array_almost_equal(f.residual(variables), [1.0, 1.0])

    def test_cost_zero_residual(self):
        f = PriorFactor("x0", [1.0], [1.0])
        variables = {"x0": np.array([1.0])}
        npt.assert_almost_equal(f.cost(variables), 0.0)

    def test_cost_known_value(self):
        f = PriorFactor("x0", [0.0], [1.0])
        variables = {"x0": np.array([2.0])}
        npt.assert_almost_equal(f.cost(variables), 2.0)


class TestBetweenFactor:
    def test_residual(self):
        f = BetweenFactor("x0", "x1", [1.0], [0.5])
        variables = {"x0": np.array([0.0]), "x1": np.array([1.5])}
        npt.assert_array_almost_equal(f.residual(variables), [1.0])

    def test_cost_zero_residual(self):
        f = BetweenFactor("x0", "x1", [2.0], [1.0])
        variables = {"x0": np.array([1.0]), "x1": np.array([3.0])}
        npt.assert_almost_equal(f.cost(variables), 0.0)


class TestTotalCost:
    def test_sum_of_costs(self):
        fg = FactorGraph()
        fg.add_variable("x0", [0.0])
        fg.add_variable("x1", [3.0])
        fg.add_factor(PriorFactor("x0", [0.0], [1.0]))
        fg.add_factor(BetweenFactor("x0", "x1", [2.0], [1.0]))
        # prior cost: 0.5 * (0-0)^2 = 0
        # between cost: 0.5 * (3-0-2)^2 = 0.5
        npt.assert_almost_equal(fg.total_cost(), 0.5)
