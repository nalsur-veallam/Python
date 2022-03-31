'''
Numpy solution of a partial differential equation for the problem of elasticity of deflection of a beam with a fixed end under its own gravity:

-div(sigma(u)) = f

'''

import numpy as np
import scipy.linalg as spl
import matplotlib.pyplot as plt

# Scaled variables
L = 1; W = 0.2
mu = 1
rho = 1
delta = W/L
gamma = 0.4*delta**2
beta = 1.25
lambda_ = beta
g = gamma
x_shape = 10
y_shape = 4 
z_shape = 4
delta_x = L/(x_shape-1)
delta_y = W/(y_shape-1)
delta_z = W/(z_shape-1)
f  = np.array((0, 0, -rho*g))
ksi = 0
global_epsilon = 59
step = 1e-3

'''
-D^T sigma = f
sigma = E*epsilon
epsilon = D*u

Here all capital letters are matrices, and lowercase letters are vectors. All operations are the usual matrix multiplication. Next, we will do gradient descent on the metric J:

J = || D^T sigma + f ||

dJ/du = 2(f^T * D^T + sigma^T * D * D^T) * E * D

Next, we collect large matrices for calculations. The free term in the gradient (2*f^T * D^T * E * D) will be called C; 2*D * D^T * E * D will be called A; Then:

dJ/du = sigma^T * A + C

'''

E_ = np.array([[lambda_ + 2*mu, lambda_, lambda_, 0, 0, 0],
               [lambda_, lambda_ + 2*mu, lambda_, 0, 0, 0],
               [lambda_, lambda_, lambda_ + 2*mu, 0, 0, 0],
               [0, 0, 0, mu, 0, 0],
               [0, 0, 0, 0, mu, 0],
               [0, 0, 0, 0, 0, mu]])
E = spl.block_diag(E_, E_)
for i in range(x_shape*y_shape*z_shape - 2):
    E = spl.block_diag(E, E_)

Dx = np.array([[-1, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, -1, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, -1, 0, 0, 1]])/delta_x
Dy0 = np.array([[0, 0, 0],
               [0, -1, 0],
               [0, 0, 0],
               [-1, 0, 0],
               [0, 0, -1],
               [0, 0, 0]])/delta_y
Dy1 = np.array([[0, 0, 0],
               [0, 1, 0],
               [0, 0, 0],
               [1, 0, 0],
               [0, 0, 1],
               [0, 0, 0]])/delta_y
Dy = np.block([Dy0, np.zeros((6, 3*(x_shape-1))), Dy1])
Dz0 = np.array([[0, 0, 0],
               [0, 0, 0],
               [0, 0, -1],
               [0, 0, 0],
               [0, -1, 0],
               [-1, 0, 0]])/delta_z
Dz1 = np.array([[0, 0, 0],
               [0, 0, 0],
               [0, 0, 1],
               [0, 0, 0],
               [0, 1, 0],
               [1, 0, 0]])/delta_z
Dz = np.block([Dz0, np.zeros((6, 3*(x_shape*y_shape-1))), Dz1])
D = np.block([Dx, np.zeros((6, 3*(x_shape*y_shape*z_shape - 2)))]) + np.block([Dy, np.zeros((6, 3*(x_shape*(y_shape*z_shape-1) - 1)))]) + np.block([Dz, np.zeros((6, 3*(x_shape*y_shape*(z_shape-1) - 1)))])
for i in range(1, x_shape*y_shape*z_shape):
    kx, ky, kz = i%x_shape, i%(x_shape*y_shape), i%(x_shape*y_shape*z_shape)
    if kx == 0:
        D_x = np.block([np.zeros((6, 3*(i-1) + 3)), Dx, np.zeros((6, 3*(x_shape*y_shape*z_shape - (i-1) - 3)))])
    else:
        D_x = np.block([np.zeros((6, 3*(i-1))), Dx, np.zeros((6, 3*(x_shape*y_shape*z_shape - (i-1) - 2)))])
    if ky < x_shape:
        D_y = np.block([np.zeros((6, 3*i)), Dy, np.zeros((6, 3*(x_shape*y_shape*z_shape - i - 1 - x_shape)))])
    else:
        D_y = np.block([np.zeros((6, 3*(i - x_shape))), Dy, np.zeros((6, 3*(x_shape*y_shape*z_shape - (i-x_shape) - 1 - x_shape)))])
    if kz < x_shape*y_shape:
        D_z = np.block([np.zeros((6, 3*i)), Dz, np.zeros((6, 3*(x_shape*y_shape*z_shape - i - 1 - x_shape*y_shape)))])
    else:
        D_z = np.block([np.zeros((6, 3*(i-x_shape*y_shape))), Dz, np.zeros((6, 3*(x_shape*y_shape*z_shape - (i-x_shape*y_shape) - 1 - x_shape*y_shape)))])
    D = np.block([[D],
                  [D_x+D_y+D_z]])
    
n = f*(1 - x_shape)*y_shape*z_shape
f_ = np.array(n)
for i in range(x_shape*y_shape*z_shape - 1):
    if (i+1)%x_shape == 0:
        f_ = np.block([f_, n])
    else:
        f_ = np.block([f_, f])
f = f_
   
C = 2*np.dot(f.T, D.T)
C = np.dot(C,E)
C = np.dot(C,D) #2*f^T * D^T * E * D #

A = 2*np.dot(D, D.T)
A = np.dot(A, E)
A = np.dot(A, D) #2*D * D^T * E * D

B = np.dot(E,D) #E * D

U = np.dot(D, D.T) #D * D^T

F = np.dot(f.T, f) #f^T * f

V = 2*np.dot(f.T, D.T) #2*f^T * D^T #

K = np.zeros((3*x_shape*y_shape*z_shape, 3*x_shape*y_shape*z_shape))
for i in range(x_shape*y_shape*z_shape):
    if i%x_shape == 0:
        K[3*i][3*i] = 1
        K[3*i+1][3*i+1] = 1
        K[3*i+2][3*i+2] = 1
        
K_ = np.eye(3*x_shape*y_shape*z_shape)
for i in range(x_shape*y_shape*z_shape):
    if i%x_shape == 0:
        K_[3*i][3*i] = 0
        K_[3*i+1][3*i+1] = 0
        K_[3*i+2][3*i+2] = 0

I = np.dot(K.T, K) #K^T * K
    
'''

Now all matrices are precalculated and initialized, let's write a function that calculates sigma (E * D will be called B):

sigma = E*D*u = B*u

'''

def sigma(u):
    return np.dot(B,u)

'''
Let's write a function for calculating the gradient and J, taking into account the fact that the conditions on the boundary should be u = 0:

J' = J + ksi*|| K * u ||^2

Then:

dJ/du = sigma^T * A + C + 2ksi*u^T * K^T * K

K^T * K will be called I; D * D^T will be called U;  f^T * f will be called F; 2*f^T * D^T will be called V;

'''
    
def gradient(u):
    return np.dot(sigma(u).T, A) + C# + 2*ksi*np.dot(u.T, I)

def cost(u):
    sig = sigma(u)
    return F + np.dot(np.dot(sig.T, U) + V, sig)# + ksi*np.dot(np.dot(u.T,I), u)

'''

Implementing gradient descent:

'''

def gradient_descent(u):
    descent_step = step
    grad = gradient(u)
    value = cost(u)
    grad = grad/np.linalg.norm(grad)
    print(value)
    i = 0
    while abs(value) > global_epsilon:
        i+= 1
        descent_step = step/np.log(i+1)
        u = np.dot(K_,u - descent_step*grad)
        grad = gradient(u)
        grad = grad/np.linalg.norm(grad)
        value = cost(u)
        print(value)

    return u
    
    
u = np.zeros(3*x_shape*y_shape*z_shape)
u = gradient_descent(u)
ix = np.arange(0,3*x_shape*y_shape*z_shape - 2,3)
iy = np.arange(1,3*x_shape*y_shape*z_shape - 1,3)
iz = np.arange(2,3*x_shape*y_shape*z_shape,3)
ux = u[ix]
uy = u[iy]
uz = u[iz]
magnitude_u = np.sqrt(ux**2 + uy**2 + uz**2)
print('min/max: ', np.min(magnitude_u), np.max(magnitude_u))
print('magnitude_u: ',magnitude_u)
print('u_z: ', uz)

    

    
    
    
    
    
    
    
    
    
    

