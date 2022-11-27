import pylab as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

V1_ = np.array([132.34, 0.06, 0.07, 1.92, 6.96, 49.49, 132.89, 126.55, 101.4, 116.77, 131.3, 133.32, 132.84, 123.24, 132.45, 131.73, 129.69, 105.1, 88.73, 65.58, 56.08, 52.43, 50.7, 48.31, 46.29, 44.58, 42.3, 40.66, 38.91, 36.53, 35.07, 33.77, 33.29, 32.37, 32.01, 31.86, 31.68, 31.35, 31.61, 31.23, 31.49, 31.31, 31.23, 31.48, 31.42, 31.73, 32.02, 31.95, 32.12, 32.45, 33.34, 33.82, 34.28, 36.48, 38.87, 37.93, 35.69, 40.37, 41.79, 43.61, 44.81, 57.68, 54.63, 48.67])/100
V1 = np.array([1.796, 0.009, 0.022, 0.770, 0.890, 1.19, 1.951, 1.58, 2.368, 2.194, 2.126,1.968, 2.027, 2.157, 2.066, 2.081, 2.147, 2.35, 2.706, 3.168, 3.458, 3.596, 3.682, 3.807, 3.916, 4.017, 4.18, 4.333, 4.53, 4.803, 5.006, 5.237, 5.373, 5.648, 5.765, 5.957, 6.081, 6.3255, 6.209, 6.68, 6.517, 6.768, 6.649, 6.479, 7.01, 6.94, 7.273, 7.345, 7.483, 7.614, 7.823, 7.945, 8.036, 8.415, 8.832, 8.674, 8.205, 9.019, 9.314, 9.486, 9.544, 10.217, 9.930, 9.695])

V2_ = np.array([0.08, 6.41, 97.69, 140.39, 138.89, 140.37, 138.21, 115.39, 132.91, 140.92, 134.67, 102.67, 59.12, 49.84, 44.93, 37.72, 35.3, 33.62, 31.58, 30.88, 29, 28.23, 27.14, 26.2, 25.75, 25.34, 25.05, 24.78, 24.5, 24.53, 24.7, 24.22, 24.2, 24.79, 24.69, 26.46, 26.24, 26.19, 26.97, 27.26, 28.05, 28.55, 28.91, 29.33, 30.67, 31.5, 33.27, 38.55, 40.47, 45.45, 51.51])/100
V2 = [0.002, 0.914, 1.44, 1.821,1.903, 1.768, 1.626, 1.526, 1.565, 1.791, 2.003, 2.397, 3.159, 3.465, 3.675, 4.102, 4.315, 4.479, 4.686, 4.758, 5.049, 5.181, 5.403, 5.639, 5.774, 5.935, 6.033, 6.187, 6.34, 6.281, 6.142, 6.513, 6.763, 7.227, 6.985, 7.808, 7.657, 7.543, 7.833, 7.958, 8.214, 8.385, 8.472, 8.57, 8.873, 9.082, 9.449, 9.746, 9.938, 10.537, 11.047]


df1 = pd.DataFrame(data={'V':V1, 'I':V1_})
df1 = df1.sort_values(by=['V'], ignore_index=True)
pd.set_option('display.max_rows', None)


df2 = pd.DataFrame(data={'V':V2, 'I':V2_})
df2 = df2.sort_values(by=['V'], ignore_index=True)

df1_min = df1[25: 53]
df2_min = df2[15: 43]
df1_max = df1[5: 18]
df2_max = df2[2: 11]

df1_min['V**2'] = df1_min['V']**2
df2_min['V**2'] = df2_min['V']**2
df1_max['V**2'] = df1_max['V']**2
df2_max['V**2'] = df2_max['V']**2

min1 = LinearRegression()
min2 = LinearRegression()
max1 = LinearRegression()
max2 = LinearRegression()

X_min1 = np.array(df1_min.drop(df1_min.columns[[1]], axis=1))
Y_min1 = np.array(df1_min['I'])
X_min2 = np.array(df2_min.drop(df2_min.columns[[1]], axis=1))
Y_min2 = np.array(df2_min['I'])

X_max1 = np.array(df1_max.drop(df1_max.columns[[1]], axis=1))
Y_max1 = np.array(df1_max['I'])
X_max2 = np.array(df2_max.drop(df2_max.columns[[1]], axis=1))
Y_max2 = np.array(df2_max['I'])

min1.fit(X_min1, Y_min1)
min2.fit(X_min2, Y_min2)

max1.fit(X_max1, Y_max1)
max2.fit(X_max2, Y_max2)

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

print('V min1 =', coef(min1))
print('V min2 =', coef(min2))
print('V min =', coef(min1)/2 + coef(min2)/2)
print('V max1 =', coef(max1))
print('V max2 =', coef(max2))
print('V max =', coef(max1)/2 + coef(max2)/2)

I_max1 = max1.predict(np.array([coef(max1), coef(max1)**2]).reshape(1, -1))
I_max2 = max2.predict(np.array([coef(max2), coef(max2)**2]).reshape(1, -1))

rang = np.linspace(min(df1_min['V']), max(df1_min['V']), 1000)
d = {'V':rang, 'V**2': rang**2}
df = pd.DataFrame(data=d)
plt.plot(rang, min1.predict(df), c='red', lw=2.5)
rang = np.linspace(min(df2_min['V']), max(df2_min['V']), 1000)
d = {'V':rang, 'V**2': rang**2}
df = pd.DataFrame(data=d)
plt.plot(rang, min2.predict(df), c='red', lw=2.5)
rang = np.linspace(min(df1_max['V']), max(df1_max['V']), 1000)
d = {'V':rang, 'V**2': rang**2}
df = pd.DataFrame(data=d)
plt.plot(rang, max1.predict(df), c='red', lw=2.5)
rang = np.linspace(min(df2_max['V']), max(df2_max['V']), 1000)
d = {'V':rang, 'V**2': rang**2}
df = pd.DataFrame(data=d)
plt.plot(rang, max2.predict(df), c='red', lw=2.5)

plt.scatter(coef(min1), fx(min1), s=1000, marker='|', c='r', lw=3)
plt.scatter(coef(min2), fx(min2), s=1000, marker='|', c='r', lw=3)
plt.scatter(coef(max1), fx(max1), s=1000, marker='|', c='r', lw=3)
plt.scatter(coef(max2), fx(max2), s=1000, marker='|', c='r', lw=3)

plt.plot(df1['V'], df1['I'], c='b', label='V = 2.620V', lw=1)
plt.plot(df2['V'], df2['I'], c='g', label='V = 2.537V', lw=1)
plt.xlabel('V (V)', fontsize=20)
plt.ylabel('I ($\mu$A)', fontsize=20)
plt.legend(fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.grid()
plt.show()

w = -1*np.log(V1_/I_max1)
V = V1

xerr = 0.08*np.ones(V.shape)
yerr = 0.0005*np.sqrt((I_max1*np.ones(V.shape))**(-2) + V1_**(-2)) + 0.2

df = pd.DataFrame({'w':w, 'V':V})
df = df.sort_values(by=['V'], ignore_index=True)

for i in range(2, 6):
    df['V**'+str(i)] = df['V']**i
    
model = LinearRegression()
model.fit(df.drop(columns=['w']), df['w'])
rang = np.linspace(min(df['V']), max(df['V']), 1000)
d = {'V':rang}
d = pd.DataFrame(data=d)
for i in range(2, 6):
    d['V**'+str(i)] = d['V']**i
plt.plot(rang, model.predict(d), c='red', lw=2.5)
plt.scatter(df['V'], df['w'], c='g', label='w(V)', lw=2)
plt.errorbar(df['V'], df['w'], xerr=xerr, yerr=yerr,fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.plot()
plt.xlabel('V (V)', fontsize=20)
plt.ylabel('w(V)', fontsize=20)
plt.legend(fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.grid()
plt.show()
