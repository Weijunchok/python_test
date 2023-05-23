# 导入
import gurobipy as gp

Condition = True
mu = 0
pho = 0.99
phi = 0.4
class LD():
    def __init__(self, mu):
        self.mu = mu
        self.m = gp.Model()
    def sub_problem(self):
        x = self.m.addVar(lb=0, name="x")
        self.m.setObjective(x * x - self.mu * x + 2*self.mu)
        self.m.optimize()
        solution = self.m.getAttr('X', self.m.getVars())
        print(solution)
        for v in self.m.getVars():
            print('%s %g' % (v.varName, v.x))
        print('Obj: %g' % self.m.objVal)
        obj_val = self.m.objVal
        x_val = solution[0]
        return x_val, obj_val
        
sp1_x, sp1_objVal = LD(mu).sub_problem()
sp2_y, sp2_objVal = LD(mu).sub_problem()
f_ini = sp1_objVal + sp2_objVal
while Condition:
    dmu = -sp1_x - sp2_y + 4  # 原函数对mu求偏导
    phi = phi * pho
    mu = mu + phi * dmu
    sp1_x, sp1_objVal = LD(mu).sub_problem()
    sp2_y, sp2_objVal = LD(mu).sub_problem()
    f_after = sp1_objVal + sp2_y
    print('current objective value is {0}'.format(sp1_x**2 + sp2_y**2))
    if abs(f_ini - f_after) <= 1e-20:
        Condition = False
    f_ini = f_after
print('optimal lagrangian multiplier is {0}'.format(mu))
print('optimal x = {0}, y = {1}'.format(sp1_x, sp2_y))
print('optimal objective value is {0}'.format(sp1_x**2 + sp2_y**2))