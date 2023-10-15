import gurobipy as gp

# Create a new model
model = gp.Model()

# Create decision variables
x = model.addVar(lb=0, ub=1, vtype=gp.GRB.CONTINUOUS, name="x")
y = model.addVar(lb=0, ub=1, vtype=gp.GRB.CONTINUOUS, name="y")

# Set objective function
model.setObjective(2*x + 3*y, gp.GRB.MAXIMIZE)

# Add constraints
model.addConstr(x + y <= 1, "c1")
model.addConstr(2*x - y >= 1, "c2")

# Optimize the model
model.optimize()

# Print the optimal solution
if model.status == gp.GRB.OPTIMAL:
    print("Optimal solution found!")
    print("x =", x.x)
    print("y =", y.x)
    print("Objective value =", model.objVal)
else:
    print("No solution found.")