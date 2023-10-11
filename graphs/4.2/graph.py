import pylab as plt
import numpy as np
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

Nf = 0.88
k = 1013.5/3.25 # From conversion momentum
dI = 0.11
dN = 0.14
dp = k*dI
c = 3e8
m = 0.5e3

Ns = np.array([1.123, 1.409, 6.623, 14.531, 16.602, 10.053, 4.391, 6.598, 0.786, 0.524, 1.335, 2.357, 13.920, 25.619, 24.958, 13.945, 14.032, 15.628, 10.764, 4.789]) - Nf

Is = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 3.7, 3.6, 3.4, 3.3, 3.2, 3.1, 2.2, 1.75, 1.25, 2.75])

ps = k*Is
Ts = np.sqrt(ps**2 + m**2) - m
Terr = Ts*dp/ps

Y = np.sqrt(Ns)/ps
Yerr = Y*np.sqrt(dp**2/ps**2 + dN**2/Ns**2)

df2 = pd.DataFrame(data={'T':Ts, 'Y':Y})
df2 = df2.sort_values(by=['T'], ignore_index=True)

df2_lin = df2[4: 11]

lin = LinearRegression()
X_lin = np.array(df2_lin.drop(df2_lin.columns[[1]], axis=1))
Y_lin = np.array(df2_lin['Y'])
lin.fit(X_lin, Y_lin)
rang = np.linspace(min(df2_lin['T']), 660, 1000)
d = {'T':rang}
df = pd.DataFrame(data=d)
plt.plot(rang, lin.predict(df), c='red', lw=2.5)
plt.scatter(Ts, Y, c='b')
plt.errorbar(Ts, Y, xerr=Terr, yerr=Yerr,fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.xlabel('T (keV)', fontsize=20)
plt.ylabel('mkFermi', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.grid()
plt.show()
print('\n\n\nEe is ', -1*lin.intercept_/lin.coef_, '\n\n\n')



df1 = pd.DataFrame(data={'I':Is, 'N':Ns})
df1 = df1.sort_values(by=['I'], ignore_index=True)

df1_max = df1[11: 15]
df1_max['I**2'] = df1_max['I']**2
max1 = LinearRegression()
X_max1 = np.array(df1_max.drop(df1_max.columns[[1]], axis=1))
Y_max1 = np.array(df1_max['N'])
max1.fit(X_max1, Y_max1)
print('\n\n\nI max =', coef(max1), '\n\n\n')

N_max1 = max1.predict(np.array([coef(max1), coef(max1)**2]).reshape(1, -1))

rang = np.linspace(min(df1_max['I']), max(df1_max['I']), 1000)
d = {'I':rang, 'I**2': rang**2}
df = pd.DataFrame(data=d)
plt.plot(rang, max1.predict(df), c='red', lw=2.5)
plt.scatter(coef(max1), fx(max1), s=1000, marker='|', c='r', lw=3)
plt.scatter(df1['I'], df1['N'], c='b')
plt.errorbar(df1['I'], df1['N'], xerr=dI, yerr=dN,fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.xlabel('I (A)', fontsize=20)
plt.ylabel('N ($c^{-1}$)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.grid()
plt.show()

plt.scatter(Ts, Ns, c='b')
plt.errorbar(Ts, Ns, xerr=Terr, yerr=dN,fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.xlabel('T (keV)', fontsize=20)
plt.ylabel('N ($c^{-1}$)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.grid()
plt.show()



