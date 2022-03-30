'''
Numpy solution of a partial differential equation for the problem of elasticity of deflection of a beam with a fixed end under its own gravity:

-div(sigma(u)) = f

'''

import numpy as np
import scipy.linalg as spl

# Scaled variables
L = 1; W = 0.2
mu = 1
rho = 1
delta = W/L
gamma = 0.4*delta**2
beta = 1.25
lambda_ = beta
g = gamma
x_shape = 11
y_shape = 3 
z_shape = 3
delta_x = L/(x_shape-1)
delta_y = W/(y_shape-1)
delta_z = W/(z_shape-1)
f  = np.array((0, 0, -rho*g))
ksi = 0
global_epsilon = 1e-2
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
Dy = np.array([[0, 0, 0, 0, 0, 0],
               [0, -1, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0],
               [-1, 0, 0, 1, 0, 0],
               [0, 0, -1, 0, 0, 1],
               [0, 0, 0, 0, 0, 0]])/delta_y
Dz = np.array([[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, -1, 0, 0, 1],
               [0, 0, 0, 0, 0, 0],
               [0, -1, 0, 0, 1, 0],
               [-1, 0, 0, 1, 0, 0]])/delta_z
D = np.block([Dx+Dy+Dz, np.zeros((6, 3*(x_shape*y_shape*z_shape - 2)))])
for i in range(1, x_shape*y_shape*z_shape):
    kx, ky, kz = i%x_shape, i%y_shape, i%z_shape
    if kx == 0:
        D_x = np.block([np.zeros((6, 3*(i-1) + 3)), Dx, np.zeros((6, 3*(x_shape*y_shape*z_shape - (i-1) - 3)))])
    else:
        D_x = np.block([np.zeros((6, 3*(i-1))), Dx, np.zeros((6, 3*(x_shape*y_shape*z_shape - (i-1) - 2)))])
    if ky == 0:
        D_y = np.block([np.zeros((6, 3*(i-1) + 3)), Dy, np.zeros((6, 3*(x_shape*y_shape*z_shape - (i-1) - 3)))])
    else:
        D_y = np.block([np.zeros((6, 3*(i-1))), Dy, np.zeros((6, 3*(x_shape*y_shape*z_shape - (i-1) - 2)))])
    if kz == 0:
        D_z = np.block([np.zeros((6, 3*(i-1) + 3)), Dz, np.zeros((6, 3*(x_shape*y_shape*z_shape - (i-1) - 3)))])
    else:
        D_z = np.block([np.zeros((6, 3*(i-1))), Dz, np.zeros((6, 3*(x_shape*y_shape*z_shape - (i-1) - 2)))])
    D = np.block([[D],
                  [D_x+D_y+D_z]])
f_ = np.array(f)
for i in range(x_shape*y_shape*z_shape - 1):
    f = np.block([f_, f])
   
C = 2*np.dot(f.T, D.T)
C = np.dot(C,E)
C = np.dot(C,D) #2*f^T * D^T * E * D #
print(np.min(E), np.max(E))

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

I = np.dot(K.T, K) #K^T * K

print('V: ', B)
    
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
    return np.dot(sigma(u).T, A) + C + 2*ksi*np.dot(u.T, I)

def cost(u):
    sig = sigma(u)
    return F + np.dot(np.dot(sig.T, U) + V, sig) + ksi*np.dot(np.dot(u.T,I), u)

'''

Implementing gradient descent:

'''

def gradient_descent(u):
    descent_step = step
    grad = gradient(u)
    value = cost(u)
    grad = grad/np.linalg.norm(grad)
    print(value)
    while abs(value) > global_epsilon:
        descent_step *= 0.99
        u = u - descent_step*grad
        grad = gradient(u)
        grad = grad/np.linalg.norm(grad)
        value = cost(u)
        print(value, np.dot(u.T,u))

    return u
    
    
u = np.zeros(3*x_shape*y_shape*z_shape)
u = gradient_descent(u)
ix = np.arange(0,x_shape*y_shape*z_shape - 2,3)
iy = np.arange(1,x_shape*y_shape*z_shape - 1,3)
iz = np.arange(2,x_shape*y_shape*z_shape,3)
ux = u[ix]
uy = u[iy]
uz = u[iz]
magnitude_u = np.sqrt(ux**2 + uy**2 + uz**2)
print(np.min(magnitude_u), np.max(magnitude_u))
print(magnitude_u)
    
    
    
    
    
    
    
    
    
    
    
    
    
    

