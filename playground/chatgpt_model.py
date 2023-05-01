from pyomo.environ import *

ok_data = [
    ((1, 3), 1),
    ((1, 4), 1),
    ((2, 3), 1),
    ((2, 4), 1),
]

dist_data = [
    ((1, 3), 10),
    ((1, 4), 15),
    ((2, 3), 12),
    ((2, 4), 8),
]

group_data = [
    ((1, 1), 1),
    ((2, 1), 1),
    ((3, 2), 1),
    ((4, 2), 1),
]

# Assuming the data is provided in the following format:
# ok, dist, and group are dictionaries with keys (i, j), (i, j), and (i, g) respectively
ok = {(i, j): value for (i, j), value in ok_data}
dist = {(i, j): value for (i, j), value in dist_data}
group = {(i, g): value for (i, g), value in group_data}

# Create a Pyomo model
model = ConcreteModel()

# Define sets
model.I = Set(initialize=set([i for i, _ in ok.keys()]))
model.J = Set(initialize=set([j for _, j in ok.keys()]))
model.G = Set(initialize=set([g for _, g in group.keys()]))

# Define variables
model.x = Var(model.I, within=Binary)
model.z = Var(model.I, model.J, within=Binary)


# Define objective function
def obj_rule(m):
    return sum(dist[i, j] * m.z[i, j] for i, j in ok.keys())


model.obj = Objective(rule=obj_rule, sense=minimize)


# Define constraints
def group_constraint_rule(m, g):
    return sum(m.x[i] for i in m.I if (i, g) in group.keys()) == 1


model.group_constraint = Constraint(model.G, rule=group_constraint_rule)


def z_le_xi_constraint_rule(m, i, j):
    if (i, j) in ok.keys():
        return m.z[i, j] <= m.x[i]
    else:
        return Constraint.Skip


model.z_le_xi_constraint = Constraint(model.I, model.J, rule=z_le_xi_constraint_rule)


def z_le_xj_constraint_rule(m, i, j):
    if (i, j) in ok.keys():
        return m.z[i, j] <= m.x[j]
    else:
        return Constraint.Skip


model.z_le_xj_constraint = Constraint(model.I, model.J, rule=z_le_xj_constraint_rule)


def z_ge_xi_plus_xj_constraint_rule(m, i, j):
    if (i, j) in ok.keys():
        return m.z[i, j] >= m.x[i] + m.x[j] - 1
    else:
        return Constraint.Skip


model.z_ge_xi_plus_xj_constraint = Constraint(model.I, model.J, rule=z_ge_xi_plus_xj_constraint_rule)

# Solve the model using a solver (e.g., GLPK, CPLEX, or Gurobi)
solver = SolverFactory('glpk')
result = solver.solve(model)

# Print the results
print("Status:", result.solver.status)
print("Termination condition:", result.solver.termination_condition)
print("Objective value:", model.obj())

for i in model.x:
    print(f"x[{i}] =", model.x[i].value)

for i, j in model.z:
    print(f"z[{i},{j}] =", model.z[i, j].value)
