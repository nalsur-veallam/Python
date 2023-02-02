import tt
from tt.optimize import tt_min
import numpy as np
import time
import pandas as pd

d = 20
n0 = 2

Q = np.random.rand(d, d) - 1/2
Q = Q + Q.T

def func(x):
    if len(x.shape) > 1:
        ans = x@Q@(x.T)
        ans = np.diag(ans)
        return ans
    else:
        return x@Q@(x.T)
    
def brut(d):
    mi = 1e14
    x_mi = []
    for i in range(2**d):
        s = list("{:b}".format(i).zfill(d))
        x = np.array(list(map(int, s)))
        ans = x.T@Q@x
        if ans < mi:
            mi = ans
            x_min = x
    return mi


val, x_full = tt_min.min_func(func, 0, 1, d=d, n0=n0, rmax=10, nswp=30)

print(x_full)
print(func(x_full))

ds = np.array([2, 5, 10, 15, 20])
nswps = np.array([1, 7, 15, 20, 30])
rmaxs = np.array([1, 3, 5, 7, 10])

table = pd.DataFrame(columns=['d', 'nswp', 'rmax', 'accuracy', 'minimum', 'tt_min'])

for d in ds:
    Q = np.random.rand(d, d) - 1/2
    Q = Q + Q.T 
    
    mi = brut(d)
    print(brut(d))
    for nswp in nswps:
        for rmax in rmaxs:
            mini = 0
            for i in range(20):
                val, x_full = tt_min.min_func(func, 0, 1, d=d, n0=n0, rmax=rmax, nswp=nswp, verb=False)
                mini += x_full.T@Q@x_full
            mini = mini/20
            accuracy = 1 - np.abs((mini-mi)/mi)
            new_row = pd.Series({'minimum': mi, 'tt_min': mini, 'd': d, 'nswp': nswp, 'rmax': rmax, 'accuracy': accuracy})
            table = pd.concat([table, new_row.to_frame().T], ignore_index=True)
            
            
table = table.sort_values(by=['accuracy'], ascending=False, ignore_index=True)
table.to_csv("8th.csv")

