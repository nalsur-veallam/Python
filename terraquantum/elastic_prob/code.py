"""
Numpy and skipy solution of a partial differential equation for the problem of elasticity of deflection of a beam with a fixed end under its own gravity:

-div(sigma(u)) = f

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Scaled variables
L = 1; W = 0.2
mu = 1
rho = 1
delta = W/L
gamma = 0.4*delta**2
beta = 1.25
lambda_ = beta
g = gamma
niter = 1E7
x_shape = 9
y_shape = 3 
z_shape = 3
f  = np.array((0, 0, -rho*g))

def divergence(u):
    """
    Computes the divergence of the vector field u, corresponding to dFx/dx + dFy/dy + ...
    :param f: List of ndarrays, where every item of the list is one dimension of the vector field
    :return: Single ndarray of the same shape as each of the items in f, which corresponds to a scalar field
    """
    num_dims = len(u)
    return np.ufunc.reduce(np.add, [np.gradient(u[num_dims - i - 1], axis=i) for i in range(num_dims)])

def laplacian(u):
    """
    Calculates the value of the Laplace operator on the grid.
    u - 3d function values in an n-dimensional grid.
    """
    ux, uy, uz = u[0], u[1], u[2]
    resultx, resulty, resultz = np.zeros_like(ux), np.zeros_like(uy), np.zeros_like(uz)
    gx, gy, gz = np.gradient(ux, edge_order=2), np.gradient(uy, edge_order=2), np.gradient(uz, edge_order=2)
    for i, [g_ix, g_iy, g_iz] in enumerate([gx, gy, gz]):
        gg_ix = np.gradient(g_ix, edge_order=2)
        gg_iy = np.gradient(g_iy, edge_order=2)
        gg_iz = np.gradient(g_iz, edge_order=2)
        resultx += gg_ix[i]
        resulty += gg_iy[i]
        resultz += gg_iz[i]
    return np.array([resultx, resulty, resultz])

def gradient(u):
    """
    Calculates a gradient along three axes and returns a 4-dimensional array.
    """
    gx = np.gradient(u, axis = 0)
    gy = np.gradient(u, axis = 1)
    gz = np.gradient(u, axis = 2)
    return np.array([gx, gy, gz])

def sigma(u):
    """
    Computes a left part of the elasticity equation : div(sigma(u))
    """
    return mu*laplacian(u) + (lambda_ + mu)*gradient(divergence(u))

def loss(u, x_shape, y_shape, z_shape):
    """
    Computes the loss function, which we use to find the vector field.
    
    ||div(sigma(u)) + f||**2 -> min
    
    Please note that the input of the function is a numpai array, taking into account the fact that zeros will be added to it on the left to take into account the boundary conditions.
    """
    u = np.array(np.split(np.array(np.split(np.array(np.split(np.array(np.split(u, z_shape)), y_shape, axis = 1)), x_shape, axis = 2)), 3, axis = 3))
    u = u.reshape(3, x_shape, y_shape, z_shape)
    u = np.concatenate((np.zeros((3, 1, np.shape(u)[2], np.shape(u)[3])), u), axis=1)
    sig = sigma(u)
    loss = np.sum(np.sqrt((sig[0] + f[0])**2 + (sig[1] + f[1])**2 + (sig[2] + f[2])**2))
    return loss
    
def minim(u, x_shape, y_shape, z_shape):
    return minimize(fun = lambda x: loss(x, x_shape, y_shape, z_shape), x0 = u, method = 'Nelder-Mead', options={'maxiter': niter})
    
U = np.zeros(3*x_shape*y_shape*z_shape)
min_u = minim(U, x_shape, y_shape, z_shape)
u = np.array(np.split(np.array(np.split(np.array(np.split(np.array(np.split(min_u.x, z_shape)), y_shape, axis = 1)), x_shape, axis = 2)), 3, axis = 3))
u = u.reshape(3, x_shape, y_shape, z_shape)
u = np.concatenate((np.zeros((3, 1, np.shape(u)[2], np.shape(u)[3])), u), axis=1)
magnitude_u = np.sqrt((u[0])**2 + (u[1])**2 + (u[2])**2)
print(min_u)
print('Magnitude: ', magnitude_u)
print('min/max: ', np.min(magnitude_u), np.max(magnitude_u))
    
    
    
    
    
    
    
    
    
    
