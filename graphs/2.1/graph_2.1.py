import numpy as np
import pylab as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


V_4 = [0.04, 5.74, 9.47, 11.75, 13.34, 14.45, 16.20, 20.56, 22.05, 21.83, 23.35, 23.87, 25.32, 26.77, 28.83, 27.40, 25.83, 29.61, 31.02, 33.45, 37.95, 38.90, 36.42, 34.91, 35.76, 37.50, 39.93, 40.77, 42.19, 45.05, 47.64, 50.34, 46.89, 45.55, 44.14]
I_4 = [1.76, 31.91, 55.03, 67.81, 76.71, 82.97, 92.09, 97.27, 93.22, 94.71, 61.87, 59.97, 68.46, 82.06, 101.17, 88.23, 73.90, 108.89, 123.01, 145.36, 166.95, 168.30, 170.11, 160.92, 168.04, 171.72, 164.72, 158.28, 151.22, 146.72, 152.89, 163.69, 151.23, 147.95, 147.96]

V_6 = [37.87, 19.84, 1.35, 10.72, 7.16, 16.60, 13.22, 17.62, 19.22, 18.58, 21.98, 20.40, 21.38, 22.56, 24.71, 25.48, 23.59, 25.04, 29.40, 33.52, 38.62, 36.77, 37.28, 41.64, 40.56, 39.80, 39.32, 44.36, 42.44, 45.41, 47.08, 48.15, 46.67, 47.5, 49.16, 52.23, 57.72]
I_6 = [145.36, 101.22, 0.2, 54.45, 30.4, 90.73, 70.46, 96.49, 101.53, 100.21, 90.81, 99.70, 95.04, 86.09, 35.13, 35.35, 44.63, 34.76, 79.01, 118.52, 144.45, 144.15, 144.67, 127.17, 134.65, 140.45, 143.29, 114.1, 123.8, 111.59, 109.37, 110.6, 109.77, 110.02, 113.13, 124.8, 154.45]

V_8 = [21.32, 38.98, 5.26, 11.81, 3.98, 14.93, 18.82, 20.60, 19.61, 22.68, 21.76, 20.15, 21.16, 22, 23.06, 26.53, 24.88, 26.23, 25.22, 26.09, 26.83, 28.15, 27.47, 29.31, 32.75, 35.62, 37.17, 38.24, 37.85, 37.04, 38.53, 40.74, 40.04, 39.27, 41.74, 42.20, 43.88, 44.46, 46.76, 47.52, 48.98, 50.45, 49.62, 48.10, 52.44, 54.05, 51.38]
I_8 = [94.90, 115.6, 7.38, 51.58, 1.4, 72.15, 94.06, 96, 95.9, 86.06, 92.61, 95.9, 94.62, 91.23, 72.47, 14.6, 18.66, 14.22, 16.2, 14.1, 15.9, 24.2, 19.3, 37.12, 77.8, 107.76, 115.33, 116.2, 116, 115.4, 116.88, 107.6, 112.7, 116.7, 101.97, 99.86, 91.04, 88, 77.6, 75.63, 73.7, 75.30, 73.82, 74.81, 80.97, 87.44, 79.05]


d_4 = {'V': V_4, 'I': I_4}
df_4 = pd.DataFrame(data=d_4)
df_4 = df_4.sort_values(by=['V'])
df_4 = df_4.drop(20)

d_6 = {'V': V_6, 'I': I_6}
df_6 = pd.DataFrame(data=d_6)
df_6 = df_6.sort_values(by=['V'])

d_8 = {'V': V_8, 'I': I_8}
df_8 = pd.DataFrame(data=d_8)
df_8 = df_8.sort_values(by=['V'])


#plt.scatter(df_4['V'], df_4['I'], label="$V_{3}$ = 4 V", c='g', marker='o', s=40)
#plt.plot(df_4['V'], df_4['I'], c='g', lw=3)

#plt.scatter(df_6['V'], df_6['I'], label="$V_{3}$ = 6 V", c='r', marker='*', s=60)
#plt.plot(df_6['V'], df_6['I'], c='r', lw=3)

plt.scatter(df_8['V'], df_8['I'], label="$V_{3}$ = 8 V", c='b', marker='s', s=60)
#plt.plot(df_8['V'], df_8['I'], c='b', lw=3)



df_8_min1 = df_8[14: 21]
df_8_min2 = df_8[38: 44]
df_8_max1 = df_8[4: 12]
df_8_max2 = df_8[25: 33]

min1 = LinearRegression()
min2 = LinearRegression()
max1 = LinearRegression()
max2 = LinearRegression()

df_8_min1['V**2'] = df_8_min1['V']**2
df_8_min2['V**2'] = df_8_min2['V']**2
df_8_max1['V**2'] = df_8_max1['V']**2
df_8_max2['V**2'] = df_8_max2['V']**2

X_min1 = np.array(df_8_min1.drop(df_8_min1.columns[[1]], axis=1))
Y_min1 = np.array(df_8_min1['I'])
X_min2 = np.array(df_8_min2.drop(df_8_min2.columns[[1]], axis=1))
Y_min2 = np.array(df_8_min2['I'])

X_max1 = np.array(df_8_max1.drop(df_8_max1.columns[[1]], axis=1))
Y_max1 = np.array(df_8_max1['I'])
X_max2 = np.array(df_8_max2.drop(df_8_max2.columns[[1]], axis=1))
Y_max2 = np.array(df_8_max2['I'])

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

print('$\Delta$ V min =', coef(min2) - coef(min1))
print('$\Delta$ V max =', coef(max2) - coef(max1))
print('$\Delta$ V =', (coef(min2) - coef(min1) + coef(max2) - coef(max1))/2)


rang = np.linspace(min(df_8_min1['V']), max(df_8_min1['V']), 1000)
d = {'V':rang, 'V**2': rang**2}
df = pd.DataFrame(data=d)
plt.plot(rang, min1.predict(df), c='red', lw=2.5)
rang = np.linspace(min(df_8_min2['V']), max(df_8_min2['V']), 1000)
d = {'V':rang, 'V**2': rang**2}
df = pd.DataFrame(data=d)
plt.plot(rang, min2.predict(df), c='red', lw=2.5)
rang = np.linspace(min(df_8_max1['V']), max(df_8_max1['V']), 1000)
d = {'V':rang, 'V**2': rang**2}
df = pd.DataFrame(data=d)
plt.plot(rang, max1.predict(df), c='red', lw=2.5)
rang = np.linspace(min(df_8_max2['V']), max(df_8_max2['V']), 1000)
d = {'V':rang, 'V**2': rang**2}
df = pd.DataFrame(data=d)
plt.plot(rang, max2.predict(df), c='red', lw=2.5)

plt.scatter(coef(min1), fx(min1), s=1000, marker='|', c='r', lw=3)
plt.scatter(coef(min2), fx(min2), s=1000, marker='|', c='r', lw=3)
plt.scatter(coef(max1), fx(max1), s=1000, marker='|', c='r', lw=3)
plt.scatter(coef(max2), fx(max2), s=1000, marker='|', c='r', lw=3)

plt.xlabel('V (V)', fontsize=20)
plt.ylabel('I ($\mu$A)', fontsize=20)
plt.grid()
plt.legend(fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xlim([0, max(V_8)])
plt.show()





