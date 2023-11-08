import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

hbar = 1.05457182e-34
c = 299792458


def eps(N_inf, N_v):
    return (N_inf - N_v) / N_inf


fig, ax = plt.subplots()

# Delta V = 2 * 0.25 = 0.5 V
# 1 раз
voltage = np.array([1.0, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5])
N_1 = np.array(
    [8.4, 18.8, 38.4, 51.8, 60.2, 74.4, 82.2, 107.2, 118.8, 114.0, 97.8, 74.4, 46.4, 19.4, 10.6, 4.6, 2.6, 0.6])

# 2 раз
N_2 = np.array([0, 0, 8.4, 17.8, 28.2, 33.6, 31.2, 41.2, 43.8, 52.8, 66.6, 80.8, 85.6, 70.8, 56.6, 35.0, 19.6, 8.4])

# 1 раз
"""v_neg_4 = np.array([0, 6.95, 6.56, 6.21, 5.73, 5.27, 4.78, 4.16, 3.50, 2.75, 2.17, 2.17, 1.68, 1.23, 0.58, 0.16, 0.95])
v_pos_4 = np.array([0, 5.02, 4.68, 4.48, 4.10, 3.82, 3.47, 2.96, 2.53, 1.95, 1.59, 2.27, 1.18, 1.70, 0.42, 0.13, 0.69])

int_neg_4 = np.array([6365, 9091, 9161, 9126, 9087, 9056, 9047, 8966, 8929, 8798, 8593, 8531, 8223, 7666, 6813, 6487, 7258])
int_pos_4 = np.array([6365, 9174, 9231, 9210, 9192, 9172, 9102, 9086, 9013, 8878, 8725, 8678, 8267, 7782, 6957, 6567, 7449])

v_neg_1 = np.array([6.98, 6.57, 6.19, 5.79, 5.26, 4.67, 4.12, 2.72, 1.95, 1.18, 0.24, 3.67,
           3.90, 3.82, 4.37, 3.23, 3.01, 3.56, 2.50])
v_pos_1 = np.array([5.00, 4.72, 4.47, 4.14, 3.77, 3.31, 2.95, 2.01, 1.43, 0.89, 0.24, 2.63,
            2.79, 2.76, 3.18, 2.32, 2.21, 2.56, 1.80])

int_neg_1 = np.array([8379, 8273, 8395, 8307, 8265, 8377, 8319, 8316, 8377, 8358, 8268, 8355,
             8311, 8360, 8297, 8313, 8450, 8393, 8345])
int_pos_1 = np.array([8401, 8369, 8388, 8362, 8295, 8147, 7878, 7953, 8263, 8338, 8396, 7565,
             7750, 7762, 8141, 7582, 7662, 7543, 8110])
"""
# 2 раз

v_neg_1 = np.array([7.00, 6.66, 6.28, 5.69, 5.24, 4.73, 4.09, 3.46, 2.78, 2.17, 2.11, 1.64, 2.25, 3.06,
                    3.33, 3.70, 3.89, 4.49])
v_pos_1 = np.array([4.96, 4.74, 4.47, 4.09, 3.77, 3.33, 2.93, 2.51, 1.99, 1.55, 3.05, 1.19, 1.62, 2.24,
                    2.37, 2.63, 2.86, 3.21])

int_neg_1 = np.array([7929, 7858, 7877, 7922, 7892, 7930, 7974, 7955, 7915, 7902, 7972, 7900, 7916,
                      7915, 7968, 7972, 7900, 7895])
int_pos_1 = np.array([8056, 8006, 7924, 7978, 7899, 7812, 7542, 7208, 7540, 7941, 7880, 7977, 7854,
                      7275, 7164, 7226, 7454, 7802])

v_neg_2 = np.array([6.86, 6.49, 6.13, 5.75, 5.25, 4.68, 4.26, 4.00, 3.79, 3.54, 3.38, 3.05, 2.75, 2.55,
                    2.14, 2.11, 2.09, 1.64, 1.25])
v_pos_2 = np.array([4.90, 7.44, 4.38, 4.09, 3.75, 3.35, 3.12, 2.91, 2.75, 2.58, 2.45, 2.29, 2.04, 1.90,
                    1.61, 1.53, 1.51, 1.20, 0.89])

int_neg_2 = np.array([3211, 3184, 3180, 3223, 3215, 3129, 3196, 3215, 3216, 3163, 3220, 3193, 3205,
                      3191, 3164, 3203, 3162, 3168, 3160])
int_pos_2 = np.array([3223, 3172, 3183, 3150, 3114, 3044, 2970, 2841, 2694, 2614, 2609, 2635, 2833,
                      2929, 3079, 3113, 3110, 3187, 3208])

v_neg_3 = np.array([6.67, 6.40, 6.01, 5.44, 4.95, 4.43, 4.17, 3.81, 3.61, 3.32, 3.07, 2.85, 2.65, 2.32,
                    2.04, 2.23, 2.06, 1.75, 1.22])
v_pos_3 = np.array([4.86, 4.61, 4.30, 4.02, 3.67, 3.31, 3.08, 2.87, 2.69, 2.51, 2.30, 2.22, 2.05, 1.80,
                    1.55, 1.64, 1.46, 1.25, 0.89])

int_neg_3 = np.array([869, 868, 868, 888, 847, 850, 854, 878, 867, 877, 876, 878, 857.4, 861, 849, 861.3,
                      864, 851, 858])
int_pos_3 = np.array([830, 826.3, 821.4, 801.3, 817.9, 740.7, 735.8, 665.4, 656.7, 638.1, 649.9, 659.8,
                      698.1, 753.5, 781.3, 771.5, 782.7, 814.9, 827.3])

v_neg_4 = np.array([0.00, 6.80, 6.48, 6.00, 5.58, 5.06, 4.49, 4.26, 4.01, 3.38, 2.49, 2.11, 2.06, 1.56, 1.22, 0.57])
v_pos_4 = np.array([7.94, 4.71, 4.38, 4.04, 3.72, 3.20, 3.11, 2.92, 2.51, 1.88, 1.58, 1.46, 1.23, 0.90, 0.43])

int_neg_4 = np.array([6165, 8884, 8874, 8931, 8908, 8945, 8777, 8770, 8795, 8633, 8490, 8284, 8250, 7954, 7473, 6559])
int_pos_4 = np.array([9048, 8954, 8994, 8938, 8958, 8868, 8843, 8898, 8840, 8573, 8535, 8407, 8184, 7725, 6708])

# plt.plot(voltage, N_1, marker='*', linestyle='none')
# plt.plot(voltage, N_2, marker='+', linestyle='none')

v_1 = np.concatenate((-1 * v_neg_1, v_pos_1))
v_2 = np.concatenate((-1 * v_neg_2, v_pos_2))
v_3 = np.concatenate((-1 * v_neg_3, v_pos_3))
v_4 = np.concatenate((-1 * v_neg_4, v_pos_4))

n_1 = np.concatenate((int_neg_1, int_pos_1))
n_2 = np.concatenate((int_neg_2, int_pos_2))
n_3 = np.concatenate((int_neg_3, int_pos_3))
n_4 = np.concatenate((int_neg_4, int_pos_4))

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

n_inf = [7900, 3200, 870, 8900]
minimums = [7164, 2608, 638, 6160]

#plt.plot(v_1, n_1, marker='*', linestyle='none',
         #label='образец 1')
#plt.plot(v_2, n_2, marker='+', linestyle='none',
         #label='образец 2')
#plt.plot(v_3, n_3, marker='.', linestyle='none',
         #label='образец 3')
#plt.plot(v_4, n_4, marker='*', linestyle='none',
         #label='образец 4')

#ax.set(xlabel=r'v, mm / s', ylabel=r'Intensity, N')
#ax.legend()
#fig.set_size_inches(9, 7)
#plt.show()
#fig.savefig("1.png")

# амплитуда резонансного поглощения
#print("eps_1 = ", float('{:.3f}'.format(eps(n_inf[0], minimums[0]) * 100)), "%")
#print("eps_2 = ", float('{:.3f}'.format(eps(n_inf[1], minimums[1]) * 100)), "%")
#print("eps_3 = ", float('{:.3f}'.format(eps(n_inf[2], minimums[2]) * 100)), "%")
#print("eps_4 = ", float('{:.3f}'.format(eps(n_inf[3], minimums[3]) * 100)), "%")

vs = [2.43, 2.46423065, 2.54107032, -0.1442687]
Is = [7269.66, 2671.28191, 656.41275496, 6572.64494]

#df1 = pd.DataFrame(data={'I':v_1, 'N':n_1})
#df1 = df1.sort_values(by=['I'], ignore_index=True)

#df1_max = df1[19: 31]
#df1_max['I**2'] = df1_max['I']**2
#max1 = LinearRegression()
#X_max1 = np.array(df1_max.drop(df1_max.columns[[1]], axis=1))
#Y_max1 = np.array(df1_max['N'])
#max1.fit(X_max1, Y_max1)

#N_max1 = max1.predict(np.array([coef(max1), coef(max1)**2]).reshape(1, -1))

#rang = np.linspace(min(df1_max['I']), max(df1_max['I']), 1000)
#d = {'I':rang, 'I**2': rang**2}
#df = pd.DataFrame(data=d)
#fig = plt.figure(figsize=(10,7))
#plt.plot(rang, max1.predict(df), c='red', lw=2.5)
#plt.scatter(coef(max1), fx(max1), s=1000, marker='|', c='r', lw=3)
#plt.scatter(df1['I'], df1['N'], c='b')
#plt.xlabel('v (mm/s)', fontsize=20)
#plt.ylabel('Intensity (N)', fontsize=20)
#plt.tick_params(axis='both', which='major', labelsize=20)
#plt.grid()
#plt.show()
#fig.savefig("1.pdf")
#print(coef(max1), fx(max1))

df1 = pd.DataFrame(data={'I':v_4, 'N':n_4})
df1 = df1.sort_values(by=['I'], ignore_index=True)

df1_max = df1[12: 20]
df1_max['I**2'] = df1_max['I']**2
max1 = LinearRegression()
X_max1 = np.array(df1_max.drop(df1_max.columns[[1]], axis=1))
Y_max1 = np.array(df1_max['N'])
max1.fit(X_max1, Y_max1)

N_max1 = max1.predict(np.array([coef(max1), coef(max1)**2]).reshape(1, -1))

rang = np.linspace(min(df1_max['I']), max(df1_max['I']), 1000)
d = {'I':rang, 'I**2': rang**2}
df = pd.DataFrame(data=d)
fig = plt.figure(figsize=(10,7))
plt.plot(rang, max1.predict(df), c='red', lw=2.5)
plt.scatter(coef(max1), fx(max1), s=1000, marker='|', c='r', lw=3)
plt.scatter(df1['I'], df1['N'], c='b')
plt.xlabel('v (mm/s)', fontsize=20)
plt.ylabel('Intensity (N)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.grid()
plt.show()
fig.savefig("4.pdf")
print(coef(max1), fx(max1))

#df1 = pd.DataFrame(data={'I':v_2, 'N':n_2})
#df1 = df1.sort_values(by=['I'], ignore_index=True)

#df1_max = df1[21: 33]
#df1_max['I**2'] = df1_max['I']**2
#max1 = LinearRegression()
#X_max1 = np.array(df1_max.drop(df1_max.columns[[1]], axis=1))
#Y_max1 = np.array(df1_max['N'])
#max1.fit(X_max1, Y_max1)

#N_max1 = max1.predict(np.array([coef(max1), coef(max1)**2]).reshape(1, -1))

#rang = np.linspace(min(df1_max['I']), max(df1_max['I']), 1000)
#d = {'I':rang, 'I**2': rang**2}
#df = pd.DataFrame(data=d)
#fig = plt.figure(figsize=(10,7))
#plt.plot(rang, max1.predict(df), c='red', lw=2.5)
#plt.scatter(coef(max1), fx(max1), s=1000, marker='|', c='r', lw=3)
#plt.scatter(df1['I'], df1['N'], c='b')
#plt.xlabel('v (mm/s)', fontsize=20)
#plt.ylabel('Intensity (N)', fontsize=20)
#plt.tick_params(axis='both', which='major', labelsize=20)
#plt.grid()
#plt.show()
#fig.savefig("2.pdf")
#print(coef(max1), fx(max1))

#df1 = pd.DataFrame(data={'I':v_3, 'N':n_3})
#df1 = df1.sort_values(by=['I'], ignore_index=True)

#df1_max = df1[22: 34]
#df1_max['I**2'] = df1_max['I']**2
#max1 = LinearRegression()
#X_max1 = np.array(df1_max.drop(df1_max.columns[[1]], axis=1))
#Y_max1 = np.array(df1_max['N'])
#max1.fit(X_max1, Y_max1)

#N_max1 = max1.predict(np.array([coef(max1), coef(max1)**2]).reshape(1, -1))

#rang = np.linspace(min(df1_max['I']), max(df1_max['I']), 1000)
#d = {'I':rang, 'I**2': rang**2}
#df = pd.DataFrame(data=d)
#fig = plt.figure(figsize=(10,7))
#plt.plot(rang, max1.predict(df), c='red', lw=2.5)
#plt.scatter(coef(max1), fx(max1), s=1000, marker='|', c='r', lw=3)
#plt.scatter(df1['I'], df1['N'], c='b')
#plt.xlabel('v (mm/s)', fontsize=20)
#plt.ylabel('Intensity (N)', fontsize=20)
#plt.tick_params(axis='both', which='major', labelsize=20)
#plt.grid()
#plt.show()
#fig.savefig("3.pdf")
#print(coef(max1), fx(max1))

print("dE_1 = ", vs[0]/c*23.8, "eV")
print("dE_2 = ", vs[1]/c*23.8, "eV")
print("dE_3 = ", vs[2]/c*23.8, "eV")
print("dE_4 = ", -vs[3]/c*23.8, "eV")

"""# величина хим сдвига
u_1 = 0
dE_1 = 23.8 * u_1 / c

print("dE_1 = ", dE_1, "eV")

# ширина линии экспериментальная
Gamma_est = 3 * 10 ** (-8)  # eV
Gamma_mes = 1 * 23.8 / c
print(Gamma_est, " ", Gamma_mes, " ", Gamma_mes / Gamma_est)"""
