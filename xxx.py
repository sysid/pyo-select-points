import pyomo.environ as pyo
from pyomo.core import Objective
from math import sqrt
import random

# Given n points in g groups, select g points (one in each group)
# such that total distance between the selected points is minimized.

# Size of the problem
n = 50
g = 5

points = [f"i{i + 1}" for i in range(n)]
groups = [f"g{j + 1}" for j in range(g)]

# Group membership: random groups
group_membership = [(f"i{random.randint(1, n)}", f"g{random.randint(1, g)}") for _ in range(n)]

# Distances from random locations
locations = {f"i{i + 1}": (random.uniform(0, 100), random.uniform(0, 100)) for i in range(n)}

# Distances
distances = {(f"i{i + 1}", f"i{j + 1}"): sqrt((locations[f"i{i + 1}"][0] - locations[f"i{j + 1}"][0]) ** 2 + (
        locations[f"i{i + 1}"][1] - locations[f"i{j + 1}"][1]) ** 2) for i in range(n) for j in range(n) if i < j}

# Create Pyomo Model
model = pyo.ConcreteModel()

# Variables
model.x = pyo.Var(points, domain=pyo.Binary)
model.pair = pyo.Var([(i, j) for i in points for j in points if i != j], domain=pyo.Binary)


# Objective Function
def total_distance_rule(m):
    return sum(m.pair[i, j] * distances.get((i, j), distances.get((j, i), 0)) for i in points for j in points if i < j)


model.total_distance = Objective(rule=total_distance_rule, sense=pyo.minimize)


# Constraints
def one_point_per_group_rule(m, g):
    return sum(m.x[i] for i, j in group_membership if j == g) == 1


model.one_point_per_group = pyo.Constraint(groups, rule=one_point_per_group_rule)


def both_selected_rule(m, i, j):
    return m.pair[i, j] >= m.x[i] + m.x[j] - 1


model.both_selected = pyo.Constraint([(i, j) for i in points for j in points if i < j], rule=both_selected_rule)

# Solve
solver = pyo.SolverFactory('cbc', executable="/Users/Q187392/dev/bin/coinbrew/dist/bin/cbc")
solver.solve(model, tee=True)

# Display Results
for i in points:
    if model.x[i].value > 0.5:
        print(f"Selected Point: {i}")
