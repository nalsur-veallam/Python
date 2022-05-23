import numpy as np
import tt
import time
from tt.amen import amen_solve

def initial_cond(T0, dx, dt):
    return T0*tt.ones(2, 3*dx+dt)

def vector(dx, dt, tau, I0, r02, k_sc, k_abs):
    nx = 2 ** dx # number of points in space
    nt = 2 ** dt # number of points in time
    
    bx = 1 # [0, b] - interval
    hx = bx / (nx - 1) # step 
    bt = 1 # [0, b] - interval
    ht = bt / (nt - 1) # step 
    
    x = hx * tt.xfun(2, dx) # coordinates generation
    ex = tt.ones(2, dx)
    t = ht * tt.xfun(2, dt) # coordinates generation
    et = tt.ones(2, dt)

    X = tt.mkron(x, ex, ex, et)
    Y = tt.mkron(ex, x, ex, et)
    Z = tt.mkron(ex, ex, x, et)
    T = tt.mkron(ex, ex, ex, t)
    
    Qs = tt.multifuncrs([X, Y, Z, T], lambda arg: I0 * (arg[:, 3]/tau *np.exp(-arg[:, 3]/tau)) * 
                        (np.exp( -(arg[:,1]**2 - arg[:,2]**2) / r02*np.exp(k_sc*arg[:,0]) ) * 
                         np.exp(-(k_sc + k_abs) * arg[:, 0]))  , 1e-6, verb = True)
    
    Qs = Qs.round(1e-6)
    
    return Qs

def matrix(dt, dx, rho, Cv, k_t):
    Idx = tt.eye(2, 3*dx) # identity tensor
    Idt = tt.eye(2, dt)
    
    delta = tt.qlaplace_dd([dx, dx, dx]) # laplasian
    
    support =  tt.delta(2, dt, center = 1) # first time derivative
    deriv = tt.Toeplitz(support,kind='L') - tt.Toeplitz(support,kind='L').T
    deriv = deriv.round(1e-6)
    
    return rho * Cv * tt.kron(Idx, deriv) - k_t * tt.kron(delta, Idt)

#consts
I0 = 1
rho = 1
tau = 1
r02 = 1
k_sc = 1
k_abs = 1
k_t = 1
Cv = 1
T0 = 1

#tensor dim
dx = 8
dt = 6

#initialisation'
t1 = time.time()
A = matrix(dt, dx, rho, Cv, k_t)
Qs = vector(dx, dt, tau, I0, r02, k_sc, k_abs)
t0 = initial_cond(T0, dx, dt)

y = amen_solve(A, Qs, Qs, 1e-6)
t2 = time.time()
print('error:', (tt.matvec(A, y) - Qs).norm() / Qs.norm())
print('time:', (t2-t1))
    
    
