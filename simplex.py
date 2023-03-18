import numpy as np

def simplex(c, A, b):
    # c: coefficients of objective function (1 x n)
    # A: coefficients of constraints (m x n)
    # b: constants of constraints (m x 1)
    # returns: optimal solution x (n x 1) and optimal value z
    
    m, n = A.shape # number of constraints and variables
    N = list(range(n)) # list of non-basic variables
    B = list(range(n, n+m)) # list of basic variables
    z = 0 # initial objective value
    
    # append slack variables to get the canonical form
    A = np.hstack([A, np.eye(m)])
    c = np.hstack([c, np.zeros(m)])
    
    while True:
        # compute coefficients of objective function for non-basic variables
        cn = c[N] - np.dot(c[B], np.linalg.inv(A[:,B])) @ A[:,N]
        print(cn)
        # check if current solution is optimal
        if np.all(cn >= 0):
            x = np.zeros(n+m) 
            x[B] = np.dot(np.linalg.inv(A[:,B]), b) # compute basic variables
            print(x[:n], z)
            return x[:n], z
        
        # select entering variable with most negative coefficient
        e = N[np.argmin(cn)]
        
        # compute maximum step length for each basic variable
        Ab_inv_b = np.dot(np.linalg.inv(A[:,B]), b)
        Ab_inv_Ae = np.dot(np.linalg.inv(A[:,B]), A[:,e])
        
        theta = [] 
        for i in range(m):
            if Ab_inv_Ae[i] > 0:
                theta.append(Ab_inv_b[i] / Ab_inv_Ae[i])
            else:
                theta.append(np.inf)
                
        # check if problem is unbounded
        if min(theta) == np.inf:
            return None, None
        
        # select leaving variable with minimum step length
        l_index = np.argmin(theta)
        l = B[l_index]
        
        # update basic and non-basic variables lists
        B[l_index] = e 
        N[N.index(e)] = l
        
        # update objective value
        z += cn[N.index(l)] * theta[l_index]
c = np.array([3, 5]) # coefficients of objective function
A = np.array([[1, 0], [0, 2], [3, 2]]) # coefficients of constraints
b = np.array([4, 12, 18]) # constants of constraints
x, z = simplex(c, A, b)
print(x,z)