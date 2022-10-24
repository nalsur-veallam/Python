import numpy as np
import pylab as plt
import pandas as pd
from scipy.optimize import minimize
from sklearn.linear_model import LinearRegression


Neon = np.array([2952, 2924, 2856, 2844, 2828, 2797, 2786, 2748, 2741, 2723, 2712, 2696, 2675, 2656, 2646, 2623, 2614, 2592, 2566, 2558, 2522, 2510, 2248, 2206]).reshape(1, -1)
Hydr = np.array([2915, 2684, 2483, 2468, 2288, 1866, 1200, 651]).reshape(1, -1)

Neon_ = np.array([7032, 6929, 6717, 6678, 6599, 6533, 6507, 6402, 6383, 6334, 6305, 6267, 6217, 6164, 6143, 6096, 6074, 6030, 5976, 5945, 5882, 5852, 5401, 5341]).reshape(1, -1)
Hydr_ = np.array([6907, 6234, 5791, 5770, 5461, 4916, 4358, 4047]).reshape(1, -1)

H = (np.array([6570, 4840, 4310, 4110.0])**(-1)).reshape(-1, 1)
I = np.array([2600, 2496, 2137]).reshape(1, -1)

m = np.array([3,4,5,6])

ix = (1/2*np.ones(4) - np.ones(4)/m**2).reshape(-1, 1)

lambd = np.concatenate((Neon_, Hydr_), axis=1)
phi = np.concatenate((Neon, Hydr), axis=1)

x0 = [2317, -6.3e6, 4291]

size = 32
fun = lambda x: np.sum((phi - np.ones(size)*x[0] + np.ones(size)*x[1]/(np.ones(size)*x[2] - lambd))**2)

res = minimize(fun, x0)
consts = res.x

print(res)
# 

x = np.arange(500, 3000, 1)
y = np.ones(len(x))*consts[2] + np.ones(len(x))*consts[1]/(x - np.ones(len(x))*consts[0])

plt.scatter(phi, lambd)
plt.plot(x, y)
plt.xlabel('$\phi$', fontsize=20)
plt.ylabel('$\lambda$, (Å)', fontsize=20)
plt.grid()
plt.legend(fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.show()


rang = np.linspace(0.35, 0.5, 1000).reshape(-1, 1)
lr = LinearRegression()
lr.fit(ix, H)

yerr = (H*0.027).reshape(4)
print(lr.intercept_, lr.coef_)

plt.plot(rang,lr.predict(rang), c='r')
plt.scatter(ix, H)
plt.errorbar(ix.reshape(4), H.reshape(4), xerr=np.zeros(4), yerr=yerr,fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.xlabel('1/2 - 1/m^2', fontsize=20)
plt.ylabel('1/$\lambda$, (1/Å)', fontsize=20)
plt.grid()
plt.legend(fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.show()
