import gurobipy as grb
import numpy as np

m = grb.Model("LP")
m.setParam('OutputFlag',1)
x = m.addMVar(2,lb=0,ub=grb.GRB.INFINITY)
c = np.array([[3,5]])
A = np.array([[1,0],
              [0,2],
              [3,2]])
b = np.array([4,12,18])
m.addConstr(A@x <=b)
m.Params.timelimit = 99999999999999999999
m.setObjective(c@x,grb.GRB.MAXIMIZE)
m.update()
m.optimize()
print('x_1={}'.format(x[0].x))
print('x_2={}'.format(x[1].x))
m.write('model.lp')