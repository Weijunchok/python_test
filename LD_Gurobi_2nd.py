# 导入
import gurobipy as gp
from gurobipy import GRB
import numpy as np
class LD():
    def __init__(self, mu,C,E,name):
        self.name = name
        self.mu = mu
        self.C = C
        self.E = E
        self.m = gp.Model()
    def sub_problem(self):
        x = self.m.addVar(vtype=GRB.CONTINUOUS,name="x")
        y = self.m.addVar(vtype=GRB.BINARY,name="y")
        self.m.addConstr(x >= self.E[0]*y)
        self.m.addConstr(x <= self.E[1]*y)
        self.m.setObjective(self.C[0] * x + self.C[1] * y - self.mu * x)
        self.m.optimize()
        self.m.write(self.name)
        solution = self.m.getAttr('X', self.m.getVars())
        print(solution)
        for v in self.m.getVars():
            print('%s %g' % (v.varName, v.x))
        print('Obj: %g' % self.m.objVal)
        obj_val = self.m.objVal
        x_val = solution[0]
        y_val = solution[1]
        return x_val, y_val,obj_val
Condition = True
mu = 9
pho = 0.99 # 越接近1越好
phi = 0.4 # 越接近于0越好
C1 = [10,15]
C2 = [12,20]
E1 = [10,50]
E2 = [5,30]
sp1_x, sp1_y, sp1_objVal = LD(mu,C1,E1,"Sub1.lp").sub_problem()
sp2_x, sp2_y, sp2_objVal = LD(mu,C2,E2,"Sub2.lp").sub_problem()
f_ini = sp1_objVal + sp2_objVal + 40 * mu
while Condition:
    dmu = -sp1_x - sp2_x + 40  # 原函数对mu求偏导
    phi = phi * pho
    mu = mu + phi * dmu

    sp1_x, sp1_y, sp1_objVal = LD(mu,C1,E1,"Sub1.lp").sub_problem()
    sp2_x, sp2_y, sp2_objVal = LD(mu,C2,E2,"Sub2.lp").sub_problem()
    f_after = sp1_objVal + sp2_objVal + 40 * mu
    print('current objective value is {0}'.format(f_after))
    if abs(f_ini - f_after) <= 0.05:
        Condition = False
    f_ini = f_after
    print('optimal lagrangian multiplier is {0}'.format(mu))
    print('optimal x1 = {0}, y1 = {1}'.format(sp1_x, sp1_y))
    print('optimal x2 = {0}, y2 = {1}'.format(sp2_x, sp2_y))
    print('optimal objective value is {0}'.format(f_after))
