import tt
import numpy as np
import time
from tt.cross import rect_cross
import pandas as pd
import time

def genC(d):
    C = np.empty(shape=(d,d))
    for i in range(d):
        for j in range(d):
            if j >= i:
                C[i, j] = i+1
            else:
                C[i, j] = j+1
                
    return C
    
def con(d, C):
    return (2*np.pi)**(d/2)*np.sqrt(np.linalg.det(C))

def integrate(ind, h, C, a):
    coords = ind*h - a
    ans = coords @ C @ coords.T
    return np.exp(-1/2*np.diag(ans))
    
def solver(d, a, n, tol):
    C = genC(d)
    Cinv = np.linalg.inv(C)
    cons = con(d, C)
    
    h = 2*a / (n - 1)
    ones = tt.ones(n,d)
    
    func = rect_cross.cross(lambda arg: integrate(arg, h, Cinv, a),
                            tt.rand(n, d), nswp=7, eps=tol, kickrank=2, rf=1, verbose=True)
    integral = h**d/cons * tt.dot(ones, func)
    print(integral)

d = 2
tol = 1e-5
a = 10
n = 51

solver(d, a, n, tol)

As = [1, 5, 10, 15, 30]
ns = [5, 11, 21, 51, 71]
tols = [1e-3, 1e-5, 1e-7]
ds = [1, 2, 3]

table = pd.DataFrame(columns=['d', 'a', 'n', 'tol', 'integral', 'loss', 'time', 'rank'])

for d in ds:
    C = genC(d)
    Cinv = np.linalg.inv(C)
    cons = con(d, C)
    
    for a in As:
        for n in ns:
            h = 2*a / (n - 1)
            ones = tt.ones(n,d)
            for tol in tols:
                t_start= time.time()
                func = rect_cross.cross(lambda arg: integrate(arg, h, Cinv, a),
                            tt.rand(n, d), nswp=7, eps=tol, kickrank=2, rf=1, verbose=True)
                integral = h**d/cons * tt.dot(ones, func)
                loss = np.abs(1 - integral)
                t1 = time.time()
                new_row = pd.Series({'d': d, 'a' : a, 'n' : n, 'tol': tol, 'integral' : integral, 'loss': loss, 'time': t1-t_start, 'rank': np.max(func.r)})
                table = pd.concat([table, new_row.to_frame().T], ignore_index=True)
                table = table.sort_values(by=['loss'], ascending=True, ignore_index=True)
                table.to_csv("7th.csv")
