import pylab as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def obr(x):
    return np.reshape(x, np.size(x))

x= np.array([975, 1100,1200, 1300, 1400,1500,1600,1700,1800,1900.0])

y= np.array([1.09,1.48,1.94,2.35,3.07,3.84,4.96,6.74,8.53,10.05])


eps = np.array([0.105, 0.119, 0.133, 0.144, 0.164, 0.179, 0.195, 0.209, 0.223, 0.236])


x = x
y = y*eps
x = x.reshape((-1, 1))
y = y.reshape((-1, 1))


x=np.log(x)
y=np.log(y)

k = 1

X = x**([i for i in range(k+1)])

lin_reg = LinearRegression(fit_intercept=False)
lin_reg.fit(X, y)

y_predicted = lin_reg.predict(x**([i for i in range(k+1)]))

x=obr(x)
y=obr(y)
y_predicted=obr(y_predicted)


fig, ax= plt.subplots()
plt.grid(True)

ax.plot(x,y_predicted, color='red', lw=2.5)
ax.scatter(x,y)
plt.xlabel('ln(T)', fontsize=20)
plt.ylabel('ln(W)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.grid()
plt.show()
print(lin_reg.coef_)
print(y_predicted)
