"""簡易Factor Graph実装"""

import numpy as np


class FactorGraph:
    """最小限のFactor Graph（学習用）"""

    def __init__(self):
        self.variables = {}  # {name: initial_value}
        self.factors = []    # list of Factor

    def add_variable(self, name, initial_value):
        self.variables[name] = np.asarray(initial_value, dtype=float)

    def add_factor(self, factor):
        self.factors.append(factor)

    def get_state_vector(self, var_order=None):
        if var_order is None:
            var_order = sorted(self.variables.keys())
        return np.concatenate([self.variables[v] for v in var_order])

    def total_cost(self):
        return sum(f.cost(self.variables) for f in self.factors)


class PriorFactor:
    """単項ファクター: ||x - z||^2_Σ"""

    def __init__(self, var_name, measurement, sigma):
        self.var_name = var_name
        self.measurement = np.asarray(measurement, dtype=float)
        self.sigma = np.asarray(sigma, dtype=float)

    def residual(self, variables):
        return (variables[self.var_name] - self.measurement) / self.sigma

    def cost(self, variables):
        r = self.residual(variables)
        return 0.5 * np.dot(r, r)


class BetweenFactor:
    """二項ファクター: ||x_j - x_i - z||^2_Σ"""

    def __init__(self, var_i, var_j, measurement, sigma):
        self.var_i = var_i
        self.var_j = var_j
        self.measurement = np.asarray(measurement, dtype=float)
        self.sigma = np.asarray(sigma, dtype=float)

    def residual(self, variables):
        delta = variables[self.var_j] - variables[self.var_i]
        return (delta - self.measurement) / self.sigma

    def cost(self, variables):
        r = self.residual(variables)
        return 0.5 * np.dot(r, r)
