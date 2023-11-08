import numpy as np
import pylab as plt
from scipy import interpolate
import pandas as pd
from sklearn.linear_model import LinearRegression

def coef(model):
    a2 = model.coef_[1]
    x0 = -model.coef_[0]/2/a2
    a0 = model.intercept_ - a2*x0**2
    
    return x0

def fx(model):
    a2 = model.coef_[1]
    x0 = -model.coef_[0]/2/a2
    a0 = model.intercept_ - a2*x0**2
    
    return a0

dI = 0.003
dx = 20
dk = 1

x=[5450, 5500, 5580, 5680, 5760, 5880, 6100, 6200, 6320, 6480, 6640, 6800, 6960, 7140, 7340, 7560, 7800, 8080, 8380, 8640, 8900, 9140, 9420, 9600, 9700, 9800, 9980]

k=[
    8,
9.2,
10.2,
11.4,
12.4,
13.8,
17,
18.6,
20.4,
22,
23.8,
25.2,
27,
28.6,
30,
32,
33.6,
35.4,
36.6,
38.4,
40.2,
41.8,
43.6,
44.5,
45,
46,
46.8
]

i=[
    0.06,
0.07,
0.07,
0.07,
0.07,
0.08,
0.11,
0.12,
0.14,
0.16,
0.19,
0.22,
0.26,
0.3,
0.36,
0.42,
0.49,
0.57,
0.65,
0.76,
0.85,
0.91,
0.93,
0.9,
0.84,
0.72,
0.53
]

u=[
    0.16,
0.19,
0.21,
0.25,
0.28,
0.32,
0.43,
0.5,
0.57,
0.67,
0.78,
0.93,
1.1,
1.32,
1.57,
1.82,
2.13,
2.49,
2.85,
3.24,
3.64,
4,
04.08,
3.96,
3.66,
3.11,
2.31
]

x=np.array(x)
i=np.array(i)
u=np.array(u)
k=np.array(k)

dI = i/k*np.sqrt(dI**2/i**2 + dk**2/k**2)
dU = u/k*np.sqrt(dI**2/u**2 + dk**2/k**2)


fig = plt.figure(figsize=(15,12))
df1 = pd.DataFrame(data={'I':x, 'N':i/k})
df1 = df1.sort_values(by=['I'], ignore_index=True)

df1_max = df1[-8: -2]
df1_max['I**2'] = df1_max['I']**2
max1 = LinearRegression()
X_max1 = np.array(df1_max.drop(df1_max.columns[[1]], axis=1))
Y_max1 = np.array(df1_max['N'])
max1.fit(X_max1, Y_max1)
print('\n\n\nlambda max =', coef(max1), '\n\n\n')

N_max1 = max1.predict(np.array([coef(max1), coef(max1)**2]).reshape(1, -1))

rang = np.linspace(min(df1_max['I']), max(df1_max['I']), 1000)
d = {'I':rang, 'I**2': rang**2}
df = pd.DataFrame(data=d)
plt.plot(rang, max1.predict(df), c='red', lw=2.5)
plt.scatter(coef(max1), fx(max1), s=1500, marker='|', c='r', lw=3, label='Максимум при ' + str(int(coef(max1))) + ' Å')
plt.scatter(df1['I'], df1['N'], c='blue', s=100, label='Измеренные данные')
plt.errorbar(df1['I'], df1['N'], xerr=dx, yerr=dI,fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.xlabel('Длина волны (Å)', fontsize=20)
plt.ylabel('Фототок (mA)', fontsize=20)
plt.legend(fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.grid()
plt.show()
fig.savefig('i.pdf')


fig = plt.figure(figsize=(15,12))
df1 = pd.DataFrame(data={'I':x, 'N':u/k})
df1 = df1.sort_values(by=['I'], ignore_index=True)

df1_max = df1[-8: -2]
df1_max['I**2'] = df1_max['I']**2
max1 = LinearRegression()
X_max1 = np.array(df1_max.drop(df1_max.columns[[1]], axis=1))
Y_max1 = np.array(df1_max['N'])
max1.fit(X_max1, Y_max1)
print('\n\n\nlambda max =', coef(max1), '\n\n\n')

N_max1 = max1.predict(np.array([coef(max1), coef(max1)**2]).reshape(1, -1))

rang = np.linspace(min(df1_max['I']), max(df1_max['I']), 1000)
d = {'I':rang, 'I**2': rang**2}
df = pd.DataFrame(data=d)
plt.plot(rang, max1.predict(df), c='red', lw=2.5)
plt.scatter(coef(max1), fx(max1), s=1500, marker='|', c='r', lw=3, label='Максимум при ' + str(int(coef(max1))) + ' Å')
plt.scatter(df1['I'], df1['N'], c='green', s=100, label='Измеренные данные')
plt.errorbar(df1['I'], df1['N'], xerr=dx, yerr=dU,fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.xlabel('Длина волны (Å)', fontsize=20)
plt.ylabel('ФотоЭДС (mV)', fontsize=20)
plt.legend(fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.grid()
plt.show()
fig.savefig('u.pdf')
