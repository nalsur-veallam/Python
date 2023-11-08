import pylab as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

V = np.array([95, 86.2, 80.7, 75.3, 70.4, 65.5, 59.6, 53.9])
E = np.array([16.6, 15.1, 14.1, 13.2, 12.4, 11.4, 10.4, 9.4])
dV = 0.3

df = pd.DataFrame(data={'V':V, 'E':E})
X_lin = np.array(df.drop(df.columns[[1]], axis=1))
Y_lin = np.array(df['E'])

lin = LinearRegression(fit_intercept=False)
lin.fit(X_lin, Y_lin)

rang = np.linspace(min(V), max(V), 1000)
d = {'V':rang}
df = pd.DataFrame(data=d)
plt.plot(rang, lin.predict(df), c='red', lw=2.5)
plt.scatter(V, E, c='b')
plt.errorbar(V, E, xerr=dV, yerr=dV,fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.xlabel('V (mV)', fontsize=20)
plt.ylabel('Epsilon (mV)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.grid()
plt.show()
print(lin.coef_)
# [0.17492772]
