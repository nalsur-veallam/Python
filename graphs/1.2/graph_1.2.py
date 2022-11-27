import pylab as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

x = np.array([0,0.015, 0.06, 0.134,0.234, 0.357, 0.5, 0.658, 0.826, 1, 1.174])
xerr = np.array([0, 0.002, 0.003, 0.004, 0.006, 0.007, 0.008, 0.008, 0.009, 0.009, 0.009])
y = np.array([1.27, 1.3, 1.48, 1.58, 1.7, 1.9, 2.3, 2.5, 2.9, 3.1, 3.4])
yerr = np.array([0.02, 0.02, 0.05, 0.04, 0.1, 0.1, 0.2, 0.3, 0.3, 0.4, 0.6])

U = np.array([1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8])
uerr = 0.05*np.ones(len(U))
cou = np.array([16000, 51000, 63000, 63000, 71000, 69000, 71000])/60
cerr = 2000*np.ones(len(U))/60

df1 = pd.DataFrame(data={'x':x, 'y':y, 'xerr':xerr, 'yerr':yerr})
df1 = df1.sort_values(by=['x'], ignore_index=True)

model = LinearRegression()
model.fit(np.array(df1['x']).reshape(-1, 1), np.array(df1['y']))
rang = np.linspace(min(df1['x']), max(df1['x']), 1000).reshape(-1, 1)
plt.plot(rang, model.predict(rang), c='red', lw=2.5)
plt.scatter(df1['x'], df1['y'], c='g', label='w(V)', lw=2)
plt.errorbar(df1['x'], df1['y'], xerr=df1['xerr'], yerr=df1['yerr'],fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.plot()
plt.xlabel('1 - cos$\theta$', fontsize=20)
plt.ylabel('1/N*$10^3$', fontsize=20)
plt.legend(fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.grid()
plt.show()

print(model.coef_, model.intercept_)

df = pd.DataFrame({'cou':cou, 'U':U, 'xerr':uerr, 'yerr':cerr})
df = df.sort_values(by=['U'], ignore_index=True)

model = LinearRegression()
model.fit(np.exp(-10*df.drop(columns=['cou', 'xerr', 'yerr'])), df['cou'])
rang = np.linspace(min(df['U']), max(df['U']), 1000)
d = {'U':rang}
d = pd.DataFrame(data=d)
plt.plot(rang, model.predict(np.exp(-10*d)), c='red', lw=2.5)
plt.scatter(df['U'], df['cou'], c='g', lw=2)
plt.errorbar(df['U'], df['cou'], xerr=df['xerr'], yerr=df['yerr'],fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.plot()
plt.xlabel('U (kV)', fontsize=20)
plt.ylabel('Count per second', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.grid()
plt.show()
