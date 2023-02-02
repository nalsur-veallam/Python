import tt
from tt.amen import amen_solve
import numpy as np
import time
import pylab as plt


def operator(px, py, dx, dy): # Partial second derivative of a scalar field with respect to y
    
    eye_x = np.eye(2**px)
    eye_y = np.eye(2**py)
    
    deriv_y = np.zeros((2**py, 2**py))
    i,j = np.indices(deriv_y.shape)
    deriv_y[i==j-1] = 1
    deriv_y[i==j+1] = 1
    deriv_y[i==j] = -2
    
    deriv_x = np.zeros((2**px, 2**px))
    i,j = np.indices(deriv_x.shape)
    deriv_x[i==j-1] = 1/2
    deriv_x[i==j+1] = -1/2
    
    for_x = deriv_x@eye_x
    for_ttx = for_x.reshape([2,2] * px, order='F')
    der_x = 1/dx*tt.matrix(for_ttx)
    
    for_y = eye_y@deriv_y
    for_tty = for_y.reshape([2,2] * py, order='F')
    der_y = 1/(dy)**2*tt.matrix(for_tty)
    
    operator = tt.kron(der_x, der_y)
    
    return tt.matrix(operator)

def deriv_along_x(px, py, dx): # Partial derivative of a scalar field with respect to x
    
    deriv = np.zeros((2**px, 2**px))
    i,j = np.indices(deriv.shape)
    deriv[i==j-1] = 1/2
    deriv[i==j+1] = -1/2
    
    for_tt = deriv.reshape([2,2] * px, order='F')
    
    deriv_x = 1/dx*tt.matrix(for_tt)
    
    eye_y = tt.eye(2, py)
    
    delta_x = tt.kron(deriv_x, eye_y)
    
    return tt.matrix(delta_x)

def matrix(px, py, dx, dy):
    deriv_x = deriv_along_x(px, py, dx)
    op = operator(px, py, dx, dy)
    
    A = deriv_x + op
    return A

def vector(px, py):
    return tt.ones(2, px+py)

px = 6
py = 6

dx = 1/2**px
dy = 1/2**py
t1 = time.time()

A = matrix(px, py, dx, dy)
b = vector(px, py)

y = amen_solve(A, b, b, 1e-14, nswp=30)
t2 = time.time()
print('error:', (tt.matvec(A, y) - b).norm() / b.norm())
print('time:', (t2-t1))

points = y.full().reshape([2**px, 2**py], order='F')
X, Y = 1/2**px*np.mgrid[:2**px, :2**py]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, points, color='black')
fig.savefig('fig.pdf')
