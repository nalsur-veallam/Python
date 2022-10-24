from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp

yerr = 0.3
xerr = 0.01
N0 = 93088

Y_al = [[52419, 51820, 50989], [32817, 33008, 33342], [20808, 20998, 20774], [13267, 13290, 13564], [8625, 8593, 8709], [5795, 5730, 5934], [3885, 3755, 3958], [2596, 2717, 2700]]
Y_fe = [[43460, 43416, 43199], [23679, 23495, 23151], [12533, 12532, 12919], [6987, 7047, 7107], [3961, 4044, 3980], [2303, 2338, 2296], [1340, 1321, 1326], [835, 808, 801]]
Y_pb = [[47880, 47270, 47260], [25770, 25480, 25670], [14010,14509, 16076], [6704, 6575, 6612], [3755, 3613, 3460], [2120, 2244, 2254], [1305, 1373, 1352], [857, 815, 833], [568, 591, 599], [401, 411, 416]]

X_al = np.array([2, 3.95, 5.95, 7.94, 9.95, 11.91, 13.88, 15.89]).reshape(-1, 1)
X_fe = np.array([1, 2, 3, 3.99, 4.99, 6, 7, 8]).reshape(-1, 1)
X_pb = np.array([0.48, 0.96, 1.44, 1.96, 2.48, 2.96, 3.49, 3.95, 4.40, 4.84]).reshape(-1, 1)

yerr_al = np.sqrt(0.5*np.sum((Y_al - (np.sum(np.array(Y_al), axis=1)/3).reshape(8,1))**2, axis=1))
yerr_fe = np.sqrt(0.5*np.sum((Y_fe - (np.sum(np.array(Y_fe), axis=1)/3).reshape(8,1))**2, axis=1))
yerr_pb = np.sqrt(0.5*np.sum((Y_pb - (np.sum(np.array(Y_pb), axis=1)/3).reshape(10,1))**2, axis=1))

al_copy = np.sum(np.array(Y_al), axis=1)/3
fe_copy = np.sum(np.array(Y_fe), axis=1)/3
pb_copy = np.sum(np.array(Y_pb), axis=1)/3

mu_al = np.ones(8)/X_al.reshape(8)*np.log(N0*np.ones(8)/al_copy)
mu_fe = np.ones(8)/X_fe.reshape(8)*np.log(N0*np.ones(8)/fe_copy)
mu_pb = np.ones(10)/X_pb.reshape(10)*np.log(N0*np.ones(10)/pb_copy)

mu_a = np.sum(mu_al)/8
mu_f = np.sum(mu_fe)/8
mu_p = np.sum(mu_pb)/10

mu_a_er = np.sqrt(1/7*np.sum((mu_al - mu_a*np.ones(8))**2))
mu_f_er = np.sqrt(1/7*np.sum((mu_fe - mu_f*np.ones(8))**2))
mu_p_er = np.sqrt(1/9*np.sum((mu_pb - mu_p*np.ones(10))**2))

print(mu_a, " +- ", mu_a_er, "; ", mu_f, " +- ", mu_f_er, "; ", mu_p, " +- ", mu_p_er)

Y_al = np.log(np.sum(np.array(Y_al), axis=1)/3)
Y_fe = np.log(np.sum(np.array(Y_fe), axis=1)/3)
Y_pb = np.log(np.sum(np.array(Y_pb), axis=1)/3)

yerr_al = yerr_al*Y_al/al_copy
yerr_fe = yerr_fe*Y_fe/fe_copy
yerr_pb = yerr_pb*Y_pb/pb_copy

rang = np.linspace(0, 16, 1000).reshape(-1, 1)

lr_al = LinearRegression()
lr_fe = LinearRegression()
lr_pb = LinearRegression()

lr_al.fit(X_al, Y_al)
lr_fe.fit(X_fe, Y_fe)
lr_pb.fit(X_pb, Y_pb)

plt.scatter(X_pb,Y_pb, c='b', label="Plumbum")
plt.plot(rang,lr_pb.predict(rang), c='b')
plt.scatter(X_al,Y_al,c='r', label="Aluminium")
plt.plot(rang,lr_al.predict(rang), c='r')
plt.scatter(X_fe,Y_fe,c='g', label="Ferrum")
plt.plot(rang,lr_fe.predict(rang), c='g')
plt.xlabel('l (cm)', fontsize=20)
plt.ylabel('log(N)', fontsize=20)
plt.xlim([0, 16])
plt.ylim([0, 12])
plt.tick_params(axis='both', which='major', labelsize=16)

X_al = np.array([2, 3.95, 5.95, 7.94, 9.95, 11.91, 13.88, 15.89])
X_fe = np.array([1, 2, 3, 3.99, 4.99, 6, 7, 8])
X_pb = np.array([0.48, 0.96, 1.44, 1.96, 2.48, 2.96, 3.49, 3.95, 4.40, 4.84])

plt.errorbar(X_pb, Y_pb, xerr=xerr, yerr=yerr_pb,fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.errorbar(X_al, Y_al, xerr=xerr, yerr=yerr_al,fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.errorbar(X_fe, Y_fe, xerr=xerr, yerr=yerr_fe,fmt='none', marker='o', markersize=4, linestyle='none', ecolor='k', elinewidth=0.8, capsize=3, capthick=1)
plt.grid()
plt.legend()
plt.show()

print(lr_pb.intercept_, lr_pb.coef_, "Plumbum")
print(lr_al.intercept_, lr_al.coef_, "Aluminium")
print(lr_fe.intercept_, lr_fe.coef_, "Ferrum")




